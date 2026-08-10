---
title: From Slurm to Flyte
weight: 3
variants: +flyte +union
---

# From Slurm to Flyte

A guide to moving batch and ML workloads off a Slurm cluster onto Flyte 2.

The compute code mostly survives the move. The training loop, the preprocessing script, and the
eval harness come over unchanged. What changes is everything around them: where the environment
comes from, how a job gets its inputs, how one job triggers the next, and how you ask for capacity.

Three shifts account for most of the work:

- **`module load` and conda environments become container images.** You declare the environment
  once, in Python, instead of relying on what happens to be installed on the login node.
- **The shared filesystem becomes explicit inputs and outputs.** A script that assumes `/scratch`
  exists on every node needs to take its data as arguments instead.
- **`sbatch` chains become function calls.** Dependency flags, sentinel files, and the cron entries
  that glue them together become ordinary Python.

The rest of this guide maps Slurm constructs onto their Flyte equivalents.

> [!NOTE]
> The [`flyte-migrate-slurm` skill](../../api-reference/agent-plugins#migration-slurm--flyte-2)
> automates the mechanical part of this translation: `#SBATCH` directives become task environment
> configuration, job arrays become `flyte.map` or `asyncio.gather`, and dependency chains become
> plain Python. Treat its output as a first pass to review against this guide, not a finished port.

---

## The mapping at a glance

| Slurm | Flyte |
|---|---|
| `sbatch train.sh` | `flyte run train.py main` |
| `#SBATCH --gres=gpu:a100:8` | `flyte.Resources(gpu="A100:8")` |
| `#SBATCH --cpus-per-task=16 --mem=64G` | `flyte.Resources(cpu=16, memory="64Gi")` |
| `#SBATCH --time=04:00:00` | `@env.task(timeout=timedelta(hours=4))` |
| `#SBATCH --requeue` | `@env.task(retries=3)` |
| `#SBATCH --array=0-999` | `flyte.map(step, range(1000))` |
| `#SBATCH --nodes=4 --ntasks-per-node=8` | `ClusteredTaskEnvironment(replicas=4, nproc_per_node=8)` |
| `#SBATCH --dependency=afterok:$JOBID` | `await` the upstream task |
| `#SBATCH --begin=...`, cron on the login node | `@env.task(triggers=flyte.Trigger(...))` |
| `module load cuda && source venv/bin/activate` | `flyte.Image.from_debian_base().with_pip_packages(...)` |
| `$SLURM_PROCID`, `$SLURM_NNODES` | `flyte.ctx().rank`, `flyte.ctx().nnodes` |
| `squeue`, `sacct` | `flyte get run`, `flyte get logs`, the UI |
| `/scratch/$USER/data.parquet` | `flyte.io.File` passed between tasks |

---

## The job script becomes a task

A representative Slurm job:

```bash
#!/bin/bash
#SBATCH --job-name=train
#SBATCH --partition=gpu
#SBATCH --gres=gpu:a100:8
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=04:00:00
#SBATCH --requeue

module load cuda/12.1
source ~/venvs/train/bin/activate
srun python train.py --lr 3e-4
```

The same job in Flyte:

```python
from datetime import timedelta

import flyte

env = flyte.TaskEnvironment(
    name="training",
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages("torch"),
    resources=flyte.Resources(cpu=16, memory="64Gi", gpu="A100:8"),
)


@env.task(retries=3, timeout=timedelta(hours=4))
async def train(lr: float = 3e-4) -> flyte.io.File:
    ...
```

The `#SBATCH` block splits in two. Anything that describes the *environment* (image, resources)
belongs on the `flyte.TaskEnvironment`, which is shared by every task declared against it. Anything
that describes *this job* (retries, timeout, caching) belongs on the `@env.task` decorator. Both
can be overridden per invocation with `task.override(...)`, which has no Slurm equivalent: the same
task can run with 1 GPU in one call and 8 in the next.

The function signature also does more work than a job script's argv. `lr: float` and
`-> flyte.io.File` are the task's interface, and Flyte records the value of every input and output
of every run, so a checkpoint six months old can be traced back to the arguments that produced it.

Docs: [TaskEnvironment](../get-started/core-concepts/task-environment) &middot; [Resources](../tasks/task-configuration/resources) &middot; [Overrides](../tasks/task-configuration/overrides)

---

## `module load` becomes an image

This is usually the slowest part of a Slurm migration, and the one worth doing carefully. On a
Slurm cluster the environment is ambient: modules, a conda env on NFS, whatever the sysadmin
installed. In Flyte the environment is part of the task definition.

You do not need to write a Dockerfile. `flyte.Image` builds one for you from Python:

```python
image = (
    flyte.Image.from_debian_base(python_version=(3, 12))
    .with_apt_packages("git")
    .with_pip_packages("torch", "transformers", "datasets")
)
```

If you already keep your dependencies in a `pyproject.toml`, point at it directly with
`.with_uv_project("pyproject.toml")`. If your organization already publishes a blessed CUDA image,
pass it by reference instead and skip the build entirely:

```python
env = flyte.TaskEnvironment(
    name="training",
    image="registry.example.com/ml-platform/cuda-torch:2026.04.01",
)
```

Two practical notes for people coming from modules:

- **Different tasks can use different images.** There is no single cluster-wide Python environment
  to keep everyone happy. A preprocessing task on a slim CPU image and a training task on a CUDA
  image are part of the same run.
- **Images are content-hashed.** Rerunning with an unchanged spec reuses the previous build instead
  of rebuilding.

Where that build runs depends on your deployment.

{{< variant union >}}
{{< markdown >}}

Set `image.builder` to `remote` in your config file to build with Union's `ImageBuilder`, which runs
the build on the cluster and needs no Docker and no registry credentials on your machine. Set it to
`local` to build with Docker locally and push to a registry your cluster can pull from.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

Images are built locally and pushed to a registry your cluster can pull from, so `image.builder`
must be set to `local`, Docker must be running on your machine, and you must have run
`docker login` against that registry.

{{< /markdown >}}
{{< /variant >}}

Docs: [Container images](../tasks/task-configuration/container-images)

---

## Job arrays become fan-out

A Slurm job array indexes into work with `$SLURM_ARRAY_TASK_ID` and leaves collection of the
results to you, usually as files in a shared directory plus a script that reads them back.

```bash
#SBATCH --array=0-999%50
python process.py --shard $SLURM_ARRAY_TASK_ID
```

In Flyte the fan-out is a call, and the results come back as return values:

```python
@env.task
async def process(shard: int) -> int: ...


@env.task
async def main(n_shards: int = 1000) -> int:
    counts = flyte.map(process, range(n_shards), concurrency=50)
    return sum(c for c in counts if not isinstance(c, Exception))
```

`concurrency=50` is the equivalent of the `%50` throttle: at most 50 shards run at once, and the
rest wait. `flyte.map` yields results in input order and returns an exception object in place of a
result for shards that failed, so a partial failure does not cost you the whole array.

When the items are not uniform, or you want to fan out across different tasks, use `asyncio.gather`
instead:

```python
results = await asyncio.gather(*(process(s) for s in shards), return_exceptions=True)
```

Docs: [Mapping over inputs](../tasks/task-programming/map) &middot; [Fanout](../tasks/task-programming/fanout) &middot; [Controlling parallelism](../tasks/task-programming/controlling-parallelism)

---

## Job dependencies become ordinary Python

`--dependency=afterok:$JOBID` handles a linear chain. Anything past that (a fan-out that joins, a
branch on the result of an earlier step, a retry of just one stage) tends to become a driver bash
script, some sentinel files, and a wiki page describing the arrangement.

In Flyte, a pipeline is a task that calls other tasks. There is no workflow DSL and no graph to
compile:

```python
@env.task
async def main(ds: str) -> Report:
    raw = await ingest(ds)
    clean = await filter_rows(raw)
    shards = await asyncio.gather(*(tokenize(clean, i) for i in range(8)))
    model = await train(shards)
    return await evaluate(model)
```

Because the driver runs at execution time as normal Python, control flow is normal Python too.
Branching is `if`. Early exit is `return`. Failure handling is `try`/`except`/`finally`, and
specific failure modes are catchable by type:

```python
import flyte.errors


@env.task
async def main(ds: str) -> int:
    try:
        return await transform(ds)
    except flyte.errors.OOMError:
        return await transform.override(resources=flyte.Resources(memory="64Gi"))(ds)
```

Scheduled submission moves from a cron entry on the login node to a trigger on the task itself:

```python
@env.task(triggers=flyte.Trigger("nightly", flyte.Cron("0 2 * * *")))
async def nightly_eval() -> Report: ...
```

Docs: [Triggers](../tasks/task-configuration/triggers) &middot; [Error handling](../tasks/task-programming/error-handling)

---

## `--requeue` becomes retries, spot handling, and checkpoints

`--requeue` restarts the script from the top and leaves the rest to you. Flyte splits the problem
into pieces that can be configured separately.

**Retries** are declarative, and count only against failures your code is responsible for:

```python
@env.task(retries=3, timeout=timedelta(hours=4))
async def train(cfg: TrainConfig) -> flyte.io.File: ...
```

**Spot capacity** is a flag. `interruptible=True` schedules the task on spot or preemptible
instances. Preemptions are recorded as system failures rather than task failures, so they do not
consume the retry budget, and the last attempt falls back to on-demand so a task cannot loop
forever on reclaimed capacity.

**Checkpoints** make the retry cheap. `flyte.ctx().checkpoint` writes to object storage rather than
a shared filesystem, so the next attempt resumes on whatever node it lands on:

```python
@env.task(retries=5)
async def train(steps: int) -> flyte.io.File:
    ckpt = flyte.ctx().checkpoint
    start = 0
    if (prev := await ckpt.load()) is not None:
        start = load_state(prev)

    for step in range(start, steps):
        ...
        if step % 100 == 0:
            await ckpt.save(state_path)
```

Task-level [caching](../tasks/task-configuration/caching) covers the other half of the problem. A
cached task with unchanged inputs is skipped on re-execution, so rerunning a twelve-hour pipeline
after fixing step nine starts at step nine instead of step one.

Docs: [Retries and timeouts](../tasks/task-configuration/retries-and-timeouts) &middot; [Interruptible tasks](../tasks/task-configuration/interruptible-tasks-and-queues) &middot; [Intra-task checkpoints](../tasks/task-programming/intra-task-checkpoints)

---

## Multi-node jobs become clustered tasks

`--nodes=4 --ntasks-per-node=8` maps onto a `ClusteredTaskEnvironment`, which launches all replicas
together as a single Kubernetes JobSet with `torchrun` handling rendezvous:

```python
import flyte
from flyte.clustered import ClusteredTaskEnvironment, ClusterFailurePolicy, TorchRun

env = ClusteredTaskEnvironment(
    name="pretrain",
    image=image,
    resources=flyte.Resources(cpu=16, memory="64Gi", gpu="H100:8", shm="auto"),
    replicas=4,           # nodes
    nproc_per_node=8,     # processes per node, so world size is 32
    runtime=TorchRun(rdzv_backend="c10d"),
    failure_policy=ClusterFailurePolicy(max_restarts=2, restart_on_host_maintenance=True),
)


@env.task
async def pretrain(steps: int) -> flyte.io.File:
    import torch.distributed as dist

    dist.init_process_group(backend="nccl")
    ...
```

Training code that already runs under `srun` with torchrun needs no changes: `RANK`, `WORLD_SIZE`,
`MASTER_ADDR`, and `MASTER_PORT` are populated in each worker as usual. The same values are
available from `flyte.ctx()` (`rank`, `local_rank`, `node_rank`, `nnodes`, `world_size`,
`master_addr`) if you would rather read them from Python. Only rank 0 uploads the task's outputs.

`ClusterFailurePolicy` distinguishes between two things Slurm treats alike.
`restart_on_host_maintenance=True` restarts the job when the underlying node is preempted or drained
for maintenance, without spending the `max_restarts` budget you set aside for actual crashes.

> [!NOTE]
> Clustered tasks are new and currently target `torchrun` workloads. There is no MPI launcher yet,
> so `mpirun`-based applications stay on Slurm for now. For Ray, Spark, or Dask, use the
> corresponding integration, which brings up a per-task cluster and tears it down when the task
> finishes.

Docs: [Clustered task environments](../../api-reference/flyte-sdk/flyte.clustered/_index)

---

{{< variant union >}}
{{< markdown >}}

## Partitions and QOS become queues

A queue is a named scheduling lane bound to a cluster pool, which is the closest analogue to a
Slurm partition with a QOS attached. Targeting one is a single parameter, settable on the
environment, the task, the invocation, or a trigger:

```python
@env.task(queue="research-h100")
async def evaluate(model: flyte.io.File) -> EvalReport: ...


await train.override(queue="prod-high")(cfg)
```

| Slurm | Flyte |
|---|---|
| `--partition=gpu` | `queue="gpu"`, bound by an admin to a cluster pool |
| `--qos=high` | queue priority |
| `MaxJobsPerAccount` | run concurrency on the queue |
| `MaxSubmitJobs` | queue depth, which rejects past the limit rather than queueing forever |
| `squeue -p gpu` | `flyte get queue gpu --watch` |

Two differences from Slurm's accounting model will affect how you plan capacity. Queue priority
controls *ordering*, not preemption: a running low-priority task is not evicted when higher-priority
work arrives. And when a queue hits its depth limit, new submissions are rejected immediately with
`RESOURCE_EXHAUSTED` instead of sitting in `PENDING` for an unknown length of time. That rejection
is a back-pressure signal for the submitting process to slow down.

Docs: [Queues](../tasks/task-configuration/queues) &middot; [Managing queues](../cluster-workload-management/queues)

---

{{< /markdown >}}
{{< /variant >}}

## The shared filesystem becomes explicit data

This mapping has no one-line translation. Doing it properly is what buys you lineage, caching, and
reproducible reruns; working around it costs you all three.

On Slurm, your home directory and `/scratch` are visible from the login node and every compute node,
so a job reads and writes paths and the filesystem does the rest. There is no equivalent guarantee
in Flyte. Data moves because a task takes it as an argument or returns it.

For most cases, the change is mechanical. Values that fit in a return type (numbers, strings,
dataclasses, Pydantic models) travel as return values. Anything larger travels as `flyte.io.File`
or `flyte.io.Dir`, which are typed references to object storage:

```python
from flyte.io import Dir, File


@env.task
async def tokenize(raw: Dir) -> File:
    out = File.new_remote()
    async with out.open("wb") as f:
        ...
    return out


@env.task
async def train(tokens: File) -> File:
    local = await tokens.download()
    ...
```

A `File` passes between tasks the way an `int` does. The upload on write and the download on read
are handled for you, and the object supports streaming, so reading a range out of a 500 GB file does
not require pulling the whole thing to local disk first.

Workloads that genuinely need a filesystem view have an escape hatch. If you already run a parallel
filesystem such as FSx for Lustre or a shared NFS export, mount it into tasks with a
[pod template](../tasks/task-configuration/pod-templates). Pod templates give you the full
Kubernetes pod spec: volumes, node selectors, tolerations, service accounts, and sidecars.

{{< variant union >}}
{{< markdown >}}
[Volumes](../tasks/task-programming/volumes) are the other option, a durable, versioned filesystem
backed by object storage that tasks mount and read like a local directory, with copy-on-write forks
for parallel branches of work.

{{< /markdown >}}
{{< /variant >}}

Docs: [Files and directories](../tasks/task-programming/files-and-directories) &middot; [Pod templates](../tasks/task-configuration/pod-templates)

---

## Watching and debugging jobs

`squeue` and `sacct` map onto the CLI and the UI:

```bash
flyte get run                # recent runs and their phases
flyte get run <run-name>     # actions within a run
flyte get logs <run-name>    # streaming logs
```

Runs are also visible in the UI with per-task logs, GPU and memory utilization, and inputs and
outputs for every action.

{{< variant union >}}
{{< markdown >}}
`srun --pty bash` and `ssh node042` both have direct equivalents. You can
[SSH into a running task](../tasks/task-deployment/debug-runs#ssh-into-the-task-beta), currently in
beta, which is the closest match to an interactive Slurm session. A run launched with `--debug` (or
`debug=True` from the SDK) goes further and starts a browser-based VS Code session inside the task
pod, where you can set breakpoints and step through the code on the same hardware, against the same
data and dependencies the run uses. Any running action can also be opened from the UI with one click.

What differs is where you land. An interactive session on a Slurm node puts you on a shared machine
whose environment may not match the job; here you land inside the failing task's own container, with
the image and paths that task actually ran with.

Docs: [Debug a run](../tasks/task-deployment/debug-runs) &middot; [View logs](../tasks/task-deployment/view-logs)
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
Docs: [Interacting with runs](../tasks/task-deployment/interacting-with-runs) &middot; [View logs](../tasks/task-deployment/view-logs)
{{< /markdown >}}
{{< /variant >}}

---

{{< variant union >}}
{{< markdown >}}

## Cold start and warm pools

A Slurm allocation feels instant because the nodes are already yours and already running. In Flyte,
each task call gets a fresh pod by default, which means scheduling, an image pull, and interpreter
startup before your code runs. On a task that runs for hours, that overhead is noise. On a fan-out
of hundreds of short tasks against a heavy image, it dominates.

A reuse policy keeps a pool of warm containers alive across invocations:

```python
env = flyte.TaskEnvironment(
    name="rollouts",
    image=flyte.Image.from_debian_base().with_pip_packages("unionai-reuse", "vllm"),
    resources=flyte.Resources(gpu="L4:1"),
    reusable=flyte.ReusePolicy(replicas=(2, 10), concurrency=4, idle_ttl=300),
)
```

The pool autoscales between the given bounds and shuts down after `idle_ttl` seconds of inactivity.
Because each replica is a long-lived Python process, a model loaded once serves many subsequent
invocations, and scheduling a task onto a warm replica costs milliseconds rather than a pod startup.
The trade-off is the same one you would accept in any long-running server: in-memory state survives
between invocations on a replica, so global state deserves care.

Docs: [Reusable containers](../tasks/task-configuration/reusable-containers)

---

{{< /markdown >}}
{{< /variant >}}

## Staging the migration

Migrations tend to go badly when the first workload moved is the most expensive one. A sequence that
works:

1. **Start with pipeline-shaped work.** Data processing, evaluation, hyperparameter sweeps, batch
   inference. These gain the most from typed inputs and outputs, caching, and retries, and they are
   the workloads where the `sbatch` glue was worst. Nothing expensive is at risk while you settle
   the image and data-access questions.
2. **Move single-node training next.** By this point the image is validated and the data is coming
   in as arguments, so what you pick up is reproducible environments, spot with automatic fallback,
   checkpoint recovery, and run metadata.
3. **Move multi-node training last.** It is the most performance-sensitive workload in the stack,
   and by the time you get to it, everything underneath it has already been exercised.

Existing binaries do not have to be rewritten to come along. A
[container task](../tasks/task-programming/container-tasks) runs an arbitrary image with typed
inputs and outputs, whatever language the tool is written in, which covers the bioinformatics
binaries and vendor CLIs that tend to be wrapped in `srun` today.

For the inner loop, `flyte run --local` executes the same code in your local Python process with no
cluster involved, which is the closest thing to iterating on the login node before submitting.

Docs: [Running locally](../get-started/run-modes/running-locally) &middot; [Container tasks](../tasks/task-programming/container-tasks)

---

## Scheduler features that do not have an equivalent yet

Three things Slurm's scheduler does are not available today, and if your workload depends on them,
plan around them explicitly:

- **Gang admission.** A clustered task's replicas are launched together and `torchrun` waits for the
  full group before training starts, but scheduler-level all-or-nothing admission is in the works
  and will be supported soon.
- **Topology-aware placement.** There is currently no way to request workers on the same rack or
  switch. We plan to support this soon as well.
- **Preemption.** Nothing evicts running low-priority work to make room for high-priority work the
  way a Slurm QOS can. Priority affects the order work starts in, not what happens to work that has
  already started. Preemption is something we plan to prioritize in the near future, but let us know
  if it is a priority for you.

These are gaps in the Kubernetes batch ecosystem rather than anything specific to Flyte, and the
upstream work on JobSet, Dynamic Resource Allocation, and workload-aware scheduling is closing them.
