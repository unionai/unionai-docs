---
title: Slurm
weight: 1
variants: +flyte +union
---

# Slurm

The Slurm plugin lets you run Flyte tasks as jobs on an existing [Slurm](https://slurm.schedmd.com/) cluster — an on-premise HPC installation, a cloud GPU cluster, or one managed by an operator such as [Soperator](https://github.com/nebius/soperator). Jobs are submitted over SSH to a login node, so the cluster needs no Flyte components installed and no configuration changes, and the plugin assumes nothing about which cloud the cluster runs in or where the run's object storage lives. The connector handles submission, state polling, cancellation and log retrieval.

The plugin supports:

- Running Python tasks on Slurm with the same typed inputs and outputs they would have on Kubernetes
- Running existing `sbatch` scripts unchanged, including multi-node jobs
- Full `sbatch` scheduling options, either as first-class fields or passed through verbatim
- Containerized execution through Pyxis and Enroot
- Slurm state mapping, so a queued job is not billed as runtime and a preempted job is retried

## Installation

```bash
pip install flyteplugins-slurm
```

The connector must also be installed in the `flyteconnector` image of your data plane. See [Deployment](#deployment).

## Task types

The plugin provides two task types, served by one connector.

| Task type | What is submitted | Typed I/O | Caching | Multi-node |
| --------- | ----------------- | --------- | ------- | ---------- |
| `slurm` | The task's own container image and the Flyte entrypoint, via Pyxis | Yes | Yes | No |
| `slurm_script` | A user-supplied `sbatch` script, unchanged | No — phase, exit code and logs | No | Yes |

Prefer `slurm` for anything that can be containerized and runs as a single process. Reach for `slurm_script` when a script cannot be converted, or when you need gang-scheduled multi-node execution.

## Quick start

Create a `Slurm` configuration and pass it as `plugin_config` to a `TaskEnvironment`:

```python
import flyte
from flyte.io import File
from flyteplugins.slurm import Slurm

slurm_env = flyte.TaskEnvironment(
    name="train",
    plugin_config=Slurm(
        partition="main",
        nodes=1,
        gres="gpu:8",
        time_limit="4:00:00",
        # Credentials for the run's object storage, mounted from the cluster's
        # shared filesystem.
        # Credentials for the run's object storage, mounted rather than passed in `env`.
        container_mounts=["/home/flyte/.cloud:/etc/cloud:ro"],
        env={"AWS_SHARED_CREDENTIALS_FILE": "/etc/cloud/credentials"},
    ),
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-slurm"),
)


@slurm_env.task(cache="auto", retries=2)
async def train(steps: int = 1000) -> File:
    ...
```

Remove `plugin_config` and the same task runs as a Kubernetes pod with no other changes. That is also the quickest way to tell a Slurm problem apart from a task problem.

> [!WARNING] Do not set `resources` on a Slurm task environment
> The allocation is described by the `Slurm` configuration and granted by Slurm, not by Kubernetes. Setting `resources` here has no effect on the allocation.

## Running an existing sbatch script

`SlurmScriptTask` submits a script as-is. Scalar inputs are exported as `FLYTE_INPUT_<NAME>`:

```python
import flyte
from flyteplugins.slurm import Slurm, SlurmScriptTask

train = SlurmScriptTask(
    name="train",
    script=open("train.sbatch").read(),
    plugin_config=Slurm(partition="main", nodes=4, time_limit="8:00:00"),
    inputs={"epochs": int},
)

env = flyte.TaskEnvironment.from_task("legacy-train", train)
```

The script's own leading `#SBATCH` directives are hoisted above the generated `export` lines and the plugin's directives follow them, so non-conflicting options are kept and the plugin's win on a duplicate — `sbatch` applies options in order and takes the last. Both blocks must sit above any executable line, because `sbatch` stops reading directives there. A leading shebang in the script is dropped. Because the script drives `srun` itself, this is the task type to use for multi-node work.

> [!NOTE] Script tasks must belong to an environment
> A task has to be attached to a `TaskEnvironment` before it can be serialized. `flyte.TaskEnvironment.from_task` does that for a standalone task.

> [!NOTE] What a script can receive
> `str`, `int`, `float` and `bool` arrive as `FLYTE_INPUT_<NAME>`, and `File`/`Dir` as their URI for the script to fetch with its own tooling. Anything else fails the task at submission, because an environment variable cannot carry it — pass a URI as a `str` instead.

### Outputs from a script task

An arbitrary sbatch script cannot write Flyte's literal format, so a script task produces
only what it is told to produce. Declaring outputs is what makes a script's results usable
by a downstream task; without them the task returns nothing.

#### Declare what the script will write

```python
train = SlurmScriptTask(
    name="train",
    script=open("train.sbatch").read(),
    plugin_config=Slurm(partition="main"),
    inputs={"epochs": int},
    outputs={"model": File, "shards": Dir},
)
```

**Only `File` and `Dir` may be declared.** Anything else is rejected when the task is
defined, rather than failing at run time. A scalar would have to come from parsing stdout,
which is silently wrong for any script that logs, and a structured value has no
representation a shell script can write. A native `slurm` task has the full range — see
[Output types](#output-types) for the comparison.

> [!WARNING] A declared output the script never wrote fails the task
> Even on exit 0. The alternative is handing a downstream task a URI to nothing, which
> surfaces much later as an unexplained read error.

#### Write to the destination the script is given

Each declared output arrives as `FLYTE_OUTPUT_<NAME>`, upper-cased. By default that is an
ordinary local path, so writing the output is a `cp`:

```bash
python train.py --epochs "$FLYTE_INPUT_EPOCHS" --out ./model.pt
cp ./model.pt "$FLYTE_OUTPUT_MODEL"
```

Once the job succeeds, the connector confirms every destination exists and records it as the
declared `File` or `Dir`, ready for the next task to read.

#### Choose who uploads

That default has the connector move the bytes for you, which is why the script above needed
no credentials and no upload tool. `output_upload` switches it:

| | `"connector"` (default) | `"job"` |
| --- | --- | --- |
| `FLYTE_OUTPUT_<NAME>` holds | a local path | the object-storage URI |
| Who uploads | the connector, after the job | the script, during the job |
| The compute node needs | nothing | a client and credentials for the store |
| The bytes travel | node → connector → storage | node → storage |
| Size limit | 100 MB by default | none |

**`"connector"`** suits what most scripts emit — metrics, summaries, configs, small models.
The node needs no upload tool, no credentials and no endpoint configuration.

> [!WARNING] The connector refuses to move more than 100 MB
> Streaming would work, but every byte would take two hops instead of one, through a pod
> concurrently polling every other job it tracks, on its bandwidth rather than the cluster's.
> The task fails rather than quietly taking the slow path — and since the mode decides what
> the script is handed, it cannot be switched after the fact, so the job's work is lost.
> Declare `"job"` up front for an output that might be large.

That ceiling is `FLYTE_SLURM_CONNECTOR_UPLOAD_MAX_BYTES` on the connector deployment — a
byte count or a suffixed size (`500MB`, `2GB`, `512MiB`), or `0` for none. It belongs to
whoever sized that pod, since it is the pod's bandwidth and scratch space being spent on
behalf of every job it polls, rather than to the task that would be spending it.

**`"job"`** has no size limit, because the bytes go straight from the compute node to
storage:

```python
train = SlurmScriptTask(..., outputs={"model": File}, output_upload="job")
```

```bash
# S3, and S3-compatible stores (MinIO, R2, Nebius, Ceph) with --endpoint-url
aws s3 cp ./model.pt "$FLYTE_OUTPUT_MODEL"

# Anything rclone has a remote for, often already configured on HPC clusters
rclone copyto ./model.pt "$FLYTE_OUTPUT_MODEL"

# Google Cloud Storage
gcloud storage cp ./model.pt "$FLYTE_OUTPUT_MODEL"

# Azure Blob
azcopy copy ./model.pt "$FLYTE_OUTPUT_MODEL"

# A directory output: copy the tree
aws s3 cp --recursive ./checkpoints "$FLYTE_OUTPUT_CHECKPOINTS"
```

A script task runs on the bare node rather than in a container, so which of these exists is
the site's business, not your image's. `command -v aws rclone gcloud azcopy` on a login node
settles it. Credentials are mounted the same way a native task's are — see
[Object storage from inside the job](#object-storage-from-inside-the-job).

> [!NOTE] None of this applies to native `slurm` tasks
> A native task runs the Flyte entrypoint inside the job, which writes its outputs to object
> storage directly. The connector never carries them, so there is no mode to choose and no
> size limit.

## Configuration

### Scheduling

These fields map one-to-one onto `sbatch` options.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `partition` | `str` | Partition to submit to |
| `nodes` | `int` | Number of nodes to allocate |
| `ntasks` | `int` | Number of tasks (`--ntasks`) |
| `cpus_per_task` | `int` | CPUs per task |
| `gres` | `str` | Generic resources, for example `"gpu:8"`. Requires GRES configured on the cluster — see the warning below |
| `gpus_per_node` | `int` or `str` | GPUs per node, for example `8` or `"h100:8"` |
| `mem` | `str` | Memory per node, for example `"64G"` |
| `time_limit` | `str` | Wall-clock limit in Slurm format, for example `"4:00:00"` |
| `account` | `str` | Account to charge |
| `qos` | `str` | Quality of service |
| `reservation` | `str` | Reservation name |
| `constraint` | `str` | Node feature constraint |
| `sbatch_options` | `Dict[str, Any]` | Any other `sbatch` option, passed through verbatim. `True` renders a bare flag. Overrides the first-class fields on conflict |

### Container and execution

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `container_runtime` | `str` | How the image is launched: `"pyxis"` (default) or `"apptainer"`. See [Container runtimes](#container-runtimes) |
| `container_image` | `str` | Override the image given to the runtime, for example a pre-imported `.sqsh` or `.sif` path. Defaults to the task's image |
| `container_mounts` | `List[str]` | `--container-mounts` entries, for example `["/data:/data"]` |
| `container_workdir` | `str` | `--container-workdir` |
| `srun_args` | `List[str]` | Extra arguments inserted before the command on the `srun` line |
| `env` | `Dict[str, str]` | Environment variables exported into the job |
| `working_dir` | `str` | Directory for generated scripts and logs. Relative paths are under the SSH user's home. Defaults to `.flyte/jobs` |

> [!WARNING] `gres` and `gpus_per_node` require GRES on the cluster
> Generic resources are opt-in per cluster: the controller needs `GresTypes` set and each
> node needs its own `Gres` entry. On a cluster without them, any GPU request is rejected
> at submission and the task never starts:
>
> ```
> sbatch: error: Invalid generic resource (gres) specification.
> ```
>
> Check what a cluster actually offers before asking for it:
>
> ```bash
> sinfo -N -o "%N %G"        # per-node GRES; "(null)" means none configured
> ```

> [!WARNING] Never put secrets in `env`
> Values in `env` are written into the generated `sbatch` script in plain text, and that script stays on the cluster filesystem. Mount credentials from the cluster's shared filesystem and reference the path instead.

### Connection

Each of these may be set per task, or once for the whole cluster on the connector deployment.

| Parameter | Connector environment variable | Description |
| --------- | ------------------------------ | ----------- |
| `host` | `FLYTE_SLURM_HOST` | Login node hostname |
| `port` | `FLYTE_SLURM_PORT` | SSH port, default `22` |
| `username` | `FLYTE_SLURM_USERNAME` | SSH user that jobs are submitted as |
| `ssh_private_key` | `FLYTE_SLURM_SSH_PRIVATE_KEY` | Name of the Flyte secret holding the SSH private key |
| `known_hosts` | `FLYTE_SLURM_KNOWN_HOSTS` | Path to a `known_hosts` file on the connector, for host-key verification |
| — | `FLYTE_SLURM_WORKING_DIR` | Cluster-wide default for `working_dir` |
| — | `FLYTE_SLURM_CONNECTOR_UPLOAD_MAX_BYTES` | Largest script-task output the connector will move itself; default `100MB`, `0` for no limit |

Setting the connection once on the connector is usually what you want: tasks then carry only
scheduling options and stay portable.

> [!NOTE] The connector's environment wins over task configuration
> For the connection fields specifically. The SSH key belongs to the deployment and is shared
> by every task, so a task that could point it at a host of its own choosing would be handed
> that key. Task configuration still supplies these on a connector that sets none of them,
> which is how local execution works. `FLYTE_SLURM_WORKING_DIR` is the exception — it is only
> a default, and a task's `working_dir` overrides it.

## Container runtimes

A native `slurm` task runs your image on the compute node, which needs a container
runtime on the cluster. `container_runtime` selects it:

| | `pyxis` (default) | `apptainer` |
|---|---|---|
| How it launches | flags on `srun` | a command the job runs |
| Image reference | `ghcr.io#org/img:tag` | `docker://ghcr.io/org/img:tag` |
| Mounts | `--container-mounts` | `--bind` |
| Working directory | `--container-workdir` | `--pwd` |
| Local image | `.sqsh` path | `.sif` path |

```python
Slurm(partition="main", container_runtime="apptainer")
```

Pyxis is the default because it ships with NVIDIA-shaped GPU clusters; Apptainer is more
common at traditional HPC sites. Nothing else about the job changes — the directives,
exports and entrypoint are identical — so a task moves between clusters by changing this
one field. Check which the cluster has before you start:

```bash
scontrol show config | grep -i plugstack   # Pyxis: look for spank_pyxis.so
command -v apptainer                       # the alternative
```

A cluster with neither cannot run native tasks; use `slurm_script` and invoke whatever
the site provides from inside the script. An unknown value is rejected where the task is
defined, not at submission.

## Container images

Enroot addresses registries as `REGISTRY#IMAGE:TAG` rather than `REGISTRY/IMAGE:TAG`. The plugin rewrites references automatically and leaves Docker Hub shorthand and absolute paths untouched:

| Input | Submitted as |
| ----- | ------------ |
| `ghcr.io/myorg/train:v1` | `ghcr.io#myorg/train:v1` |
| `python:3.12-slim` | unchanged |
| `/jail/images/train.sqsh` | unchanged |

On clusters that pre-import images to a shared filesystem, point at the squashfs file directly and skip the registry pull:

```python
Slurm(container_image="/jail/images/train.sqsh", partition="main")
```

> [!WARNING] Compute nodes need their own registry credentials
> Task images are pulled by Enroot on the compute nodes. That is a different credential from the one your local Docker uses and from Kubernetes `imagePullSecrets`, and neither substitutes for it. For a private registry, provide a `~/.config/enroot/.credentials` entry for the submitting user:
>
> ```
> machine ghcr.io login <username> password <token>
> ```
>
> Without it Enroot authenticates anonymously and the import fails with `401 Unauthorized`.

## Object storage from inside the job

A `slurm` task runs the Flyte entrypoint inside the job, which reads inputs and writes outputs to the run's object storage. Compute nodes therefore need network access to that storage and credentials for it.

Which credentials depends on the store, not on the plugin — it works with anything Flyte's storage layer supports:

| Store | Variable the job needs |
| --- | --- |
| S3, and S3-compatible (MinIO, R2, Nebius, …) | `AWS_SHARED_CREDENTIALS_FILE`, or the usual `AWS_*` pair |
| Google Cloud Storage | `GOOGLE_APPLICATION_CREDENTIALS` |
| Azure Blob | `AZURE_STORAGE_*` |

Mount the credential file from the cluster's shared filesystem with `container_mounts` and
name its path in `env`. Never put the secret itself in `env`: it is rendered into the
generated sbatch script, which stays on the login node's filesystem.

Outputs land in exactly the same place they would for a Kubernetes pod task, which is what allows a Slurm task to hand results to a task running elsewhere:

```python
slurm_env = flyte.TaskEnvironment(
    name="train",
    plugin_config=Slurm(partition="main", gres="gpu:8"),
    image=image,
)

k8s_env = flyte.TaskEnvironment(name="pipeline", image=image, depends_on=[slurm_env])


@k8s_env.task
async def prepare(rows: int) -> Dir: ...

@slurm_env.task
async def train(dataset: Dir) -> File: ...

@k8s_env.task
async def evaluate(model: File) -> dict[str, str]: ...

@k8s_env.task
async def pipeline() -> dict[str, str]:
    return await evaluate(await train(await prepare(1000)))
```

> [!WARNING] Return `File` or `Dir`, not a cluster filesystem path
> Returning a path such as `"/data/model.pt"` as a `str` satisfies the type system and then fails when a task on another cluster opens it — the Slurm cluster's filesystem does not exist there. Return `flyte.io.File` or `flyte.io.Dir` so the contents are uploaded. Path references are valid only between tasks that share a filesystem.

For data read repeatedly, such as a training set read every epoch, stage it onto the Slurm cluster's shared filesystem once and pass a path within the cluster. Re-reading it from object storage on every epoch is the expensive mistake.

## Outputs and caching

The two task types differ sharply here, because only one of them runs Flyte's entrypoint.

### Output types

| | `slurm` | `slurm_script` |
| --- | --- | --- |
| Scalars — `int`, `float`, `str`, `bool`, `datetime`, `date`, `timedelta`, `None` | Yes | No |
| Containers — `list`, `dict`, `Union`, `Optional`, `Enum` | Yes | No |
| Structured — dataclass, Pydantic model, protobuf | Yes | No |
| Offloaded — `File`, `Dir`, `DataFrame` | Yes | `File` and `Dir`, declared |
| Anything else, via pickle | Yes | No |
| Several outputs as a `tuple` | Yes | Yes, all declared |

A native `slurm` task runs the same entrypoint a Kubernetes pod task does, so its outputs
go through the standard type engine with nothing added or removed by the plugin. Scalars,
containers and structured values are inlined into `outputs.pb`; `File`, `Dir` and
`DataFrame` contents are offloaded to the raw-data prefix, including when nested inside a
dataclass or a list.

A `slurm_script` task has no such entrypoint — an arbitrary sbatch script cannot write
Flyte's literal format — so it produces only what it is told to write, as described in
[Outputs from a script task](#outputs-from-a-script-task). A scalar output would mean
parsing stdout, which is silently wrong for any script that logs.

> [!NOTE] Artifacts are narrower than outputs
> Only `File`, `Dir` and `DataFrame` can be wrapped with `flyte.artifacts.new(...)`, and an
> artifact must be a top-level output rather than nested inside another value. That applies
> to every task type, not just these.

Two things that follow from the job doing its own I/O: the compute node needs credentials
for the run's object storage, and a large value belongs in a `File` or `Dir` rather than
returned directly, since inline inputs and outputs are capped by `max_inline_io_bytes`.

### Caching

Both task types cache, and both invalidate on a change to the code that produced the
result — but they compute that differently.

| | What the cache version is derived from |
| --- | --- |
| `slurm` | The task function's source, as for any Python task |
| `slurm_script` | The script body, plus the configuration that shapes execution |

`cache="auto"` normally hashes the task function. A script task has no function, so the
default policy would return the hash of the empty string — one constant shared by every
script task, meaning an edited script would keep hitting its old entry. The plugin
substitutes a version over the script instead, so editing the script invalidates the cache
as you would expect.

Connection details are deliberately excluded from that version: moving the cluster to a new
login node, or rotating the SSH secret, does not change what the job computes and should
not discard valid results. An explicit `Cache(behavior="override", ...)` is left untouched.

> [!NOTE] Caching a script task needs declared outputs to be useful
> A cache hit restores outputs and skips the job. With no outputs declared there is nothing
> to restore, so a hit simply skips the work — rarely what you want from a script whose
> value is its side effects.

## Job state mapping

Only the first token of the Slurm state is matched, so `CANCELLED by 1234` behaves like `CANCELLED`. An unrecognized state is logged and treated as running rather than failing the task.

| Slurm state | Flyte phase | Consequence |
| ----------- | ----------- | ----------- |
| `PENDING`, `CONFIGURING`, `REQUEUED`, `SUSPENDED` | `QUEUED` | Waiting for an allocation does not count as running |
| `RUNNING`, `COMPLETING` | `RUNNING` | — |
| `COMPLETED` | `SUCCEEDED` | Outputs are read from object storage as usual |
| `FAILED`, `NODE_FAIL`, `OUT_OF_MEMORY`, `TIMEOUT`, `DEADLINE`, `BOOT_FAIL` | `FAILED` | The message carries Slurm's reason and the tail of stderr |
| `PREEMPTED` | `RETRYABLE_FAILED` | Consumes a retry rather than failing the run — but only if the task sets `retries`, which defaults to 0 |
| `CANCELLED` | `ABORTED` | Aborting the Flyte run runs `scancel` |

State is polled with `squeue`, falling back to `sacct` for jobs that have already left the queue, so **accounting must be working for the submitting user** or finished jobs are reported as unknown.

## Inspecting a job

Every job leaves three files on the login node under `working_dir`, named `flyte-<task>-<8 hex>`:

```bash
ls -t ~/.flyte/jobs | head
cat  ~/.flyte/jobs/<job>.sbatch   # exactly what was submitted
tail ~/.flyte/jobs/<job>.err
```

The generated `.sbatch` file is a plain script. Reading it answers most questions outright, and re-running it by hand with `sbatch` separates a plugin problem from a cluster problem. Both log paths are also named in the task's phase message in the UI.

> [!NOTE] No Kubernetes Pod is created
> A Slurm task runs on a Slurm worker, not in a pod. An empty pod list for the action is expected; check `sacct` on the cluster instead.

## Deployment

### Connector image

Add `flyteplugins-slurm` to the `flyteconnector` image:

```dockerfile
FROM ghcr.io/flyteorg/flyte-connectors:<tag matching your data plane>
COPY dist/flyteplugins_slurm-*.whl /tmp/
RUN pip install --no-deps /tmp/flyteplugins_slurm-*.whl && pip install asyncssh
```

Push it to a registry the data plane can pull from.

### Data plane values

{{< variant union >}}
{{< markdown >}}

Create the secret holding the SSH key and the `known_hosts` file:

```bash
kubectl -n <namespace> create secret generic slurm-login \
  --from-file=ssh-privatekey=./slurm-connector \
  --from-file=known_hosts=./known_hosts
```

Then point the connector at your image and give it the connection:

```yaml
flyteconnector:
  # Also gates the connector-service block in the leaseworker's config, so the
  # leaseworker has no connector endpoint at all when this is false.
  enabled: true
  image:
    repository: <your-registry>/slurm-connector
    tag: <your-tag>
  additionalEnvs:
    - { name: FLYTE_SLURM_HOST, value: "<login-host>" }
    - { name: FLYTE_SLURM_USERNAME, value: "flyte" }
    - name: FLYTE_SLURM_SSH_PRIVATE_KEY
      valueFrom:
        secretKeyRef: { name: slurm-login, key: ssh-privatekey }
    - { name: FLYTE_SLURM_KNOWN_HOSTS, value: /etc/slurm-login/known_hosts }
  # These two take a map, not a list — see the warning below.
  additionalVolumeMounts:
    volumeMounts:
      - { name: slurm-login, mountPath: /etc/slurm-login, readOnly: true }
  additionalVolumes:
    volumes:
      - name: slurm-login
        secret:
          secretName: slurm-login
          items: [{ key: known_hosts, path: known_hosts }]
```

`FLYTE_SLURM_SSH_PRIVATE_KEY` holds the key's **contents**, so it comes from a
`secretKeyRef`; `FLYTE_SLURM_KNOWN_HOSTS` is a **path**, so its file is mounted.

> [!WARNING] `additionalVolumes` and `additionalVolumeMounts` take a map, not a list
> The chart splices these into the pod spec without a `volumes:` / `volumeMounts:` key of
> its own, so the value has to supply it. A bare list — which the chart's own `[]` default
> and its comments imply — renders invalid YAML and fails the upgrade:
>
> ```
> YAML parse error on dataplane/templates/flyteconnector/deployment.yaml:
> error converting YAML to JSON: yaml: did not find expected key
> ```
>
> `additionalEnvs` is unaffected: the template does scaffold `env:`, so it takes a plain
> list. Render before upgrading:
>
> ```bash
> helm template t <chart> -s templates/flyteconnector/deployment.yaml -f values-slurm.yaml
> ```
>
> On upgrade Helm also prints `warning: destination for
> dataplane.flyteconnector.additionalVolumeMounts is a table. Ignoring non-table value
> ([])`. That is expected: your map overrides the chart's `[]` default.

{{< /markdown >}}
{{< /variant >}}

Task types are discovered at runtime from the connector's metadata service, so there is no task-type routing to configure. Confirm the connector advertises them:

```bash
kubectl -n <namespace> logs deploy/flyteconnector | grep -A6 "Connector Metadata"
```

### Credentials

The SSH private key is a Flyte secret named by `ssh_private_key`, or is set cluster-wide as `FLYTE_SLURM_SSH_PRIVATE_KEY` on the `flyteconnector` deployment. Provide a `known_hosts` file for host-key verification; `skip_host_key_verification=True` exists for development only and logs a warning.

### Network

The connector must reach the login node on its SSH port. Restrict the login node's allowed source ranges to the connector's egress addresses, and verify from the pod that will actually connect rather than from your workstation:

```bash
kubectl -n <namespace> exec deploy/flyteconnector -- \
  python -c "import socket; s=socket.socket(); s.settimeout(10); \
             s.connect(('<login-host>', 22)); print(s.recv(64))"
```

The connector keeps one SSH connection per cluster, reused across calls and re-established if it drops, so tracking many jobs costs one login-node session rather than one per job. It does still issue one `squeue` per job per poll, because a connector's `get` is called once per resource.

Each job also leaves a `.sbatch`, `.out` and `.err` file in `working_dir`, and nothing removes them — they are the first thing to read when a job fails. On a busy cluster they accumulate in the submitting user's home, so prune them on whatever schedule suits the site.

## Known gaps

What the plugin does not do today, and what to do instead.

### Execution

- **No multi-node gang execution for `slurm` tasks.** The native task pins
  `srun --nodes=1 --ntasks=1`, so the Flyte entrypoint runs exactly once even when the
  allocation spans several nodes. Without that pin, `nodes=2` would start one entrypoint
  per node, each writing the same output prefix. Distributed work belongs in a
  `slurm_script` task, which drives `srun` or `mpirun` itself. A launcher for native
  tasks is not implemented.
- **Only Pyxis and Apptainer are supported as container runtimes.** Anything else needs a
  new branch in the plugin's container invocation. A cluster with neither cannot run
  native tasks at all; use `slurm_script` and invoke whatever the site provides.
- **`resources` is refused on a Slurm task environment.** The allocation comes from the
  `Slurm` config, so setting `resources` raises rather than being silently ignored. Use
  `cpus_per_task`, `mem`, `gres` or `gpus_per_node`.

### Data and I/O

- **A script task's outputs are `File` and `Dir` only.** It cannot return a scalar, a
  dataclass or a `DataFrame`, since an arbitrary script has no way to write Flyte's literal
  format — see [Outputs from a script task](#outputs-from-a-script-task). Undeclared
  results are invisible to Flyte, and coordinating through an agreed path leaves them
  untracked.
- **The connector will not move more than 100 MB on a job's behalf.** Raise
  `FLYTE_SLURM_CONNECTOR_UPLOAD_MAX_BYTES`, or have the job upload its own outputs with
  `output_upload="job"`. The refusal fires after the job has run, so its work is lost.
- **Script inputs are limited to scalars and URIs.** `str`, `int`, `float` and `bool`
  become `FLYTE_INPUT_<NAME>`; `File` and `Dir` become their URI. Anything else fails at
  submission, because an environment variable cannot carry it.
- **No clickable log links.** A job's stdout and stderr are files on the login node, not
  resources behind a URL, so their paths are named in the task's message instead. Live
  stdout is streamed through the connector.

### Operations

- **SSH transport only.** A `slurmrestd` transport can be added behind the plugin's
  transport protocol, but is not implemented. Many clusters already have the prerequisite
  (`AuthAltTypes=auth/jwt`) without running the daemon.
- **One identity.** Every job runs as the configured SSH user, so the cluster attributes
  all work to that account regardless of who launched the run.
- **Status is polled per job.** The connector keeps one SSH connection per cluster, but
  `get` is called once per resource, so it issues one `squeue` per job per poll.
  Coalescing would need a cache inside the connector.
- **Job files accumulate.** Each job leaves a `.sbatch`, `.out` and `.err` in
  `working_dir` and nothing removes them — they are the first thing to read when a job
  fails. Prune them on whatever schedule suits the site.
- **A cluster without accounting has a small blind spot.** When `sacct` is unavailable,
  a finished job is resolved through `scontrol`, which only keeps it for `MinJobAge`
  seconds. A job that finishes and ages out between two polls cannot be resolved at all.

> [!WARNING] Values in `env` are written to the cluster in plain text
> They are rendered into the generated `sbatch` script, which stays on the login node's
> filesystem. Mount credentials from the shared filesystem and reference the path in
> `env`; never put the secret itself there.
