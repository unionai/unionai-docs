---
title: Clustered task environment
weight: 8
variants: +flyte +union
---

# Clustered task environment

Most tasks run in a single container. A **clustered task environment** runs a *single task* across a
gang of pods at once — a group of workers that start together, discover each other, and run as one
distributed job. This is what you need for multi-node, multi-GPU workloads such as distributed model
training, where the work is too large for one machine and every worker must participate in the same
computation.

A `flyte.clustered.ClusteredTaskEnvironment` is a specialized `flyte.TaskEnvironment`: it takes all
the usual environment settings (image, resources, secrets, and so on) and adds a few fields that
describe the shape of the cluster. When you run a task defined on one, the backend launches a
Kubernetes [JobSet](https://jobset.sigs.k8s.io/) of identical pods and bootstraps
[`torchrun`](https://docs.pytorch.org/docs/stable/elastic/run.html) inside them, so your task body
runs once per worker process with the standard PyTorch distributed environment variables already set.

## When to use it

Reach for a clustered task environment when a single task needs many machines working together:

- **Distributed data-parallel training** (DDP) — replicate a model across workers and average
  gradients each step to train faster on more data.
- **Sharded training** (FSDP, tensor/pipeline parallelism) — shard a model that is too large to fit
  on one device across many devices.
- **Any multi-node PyTorch job** that expects a `torchrun` rendezvous (`RANK`, `WORLD_SIZE`,
  `MASTER_ADDR`, …) to already be set up.

If your workload is a large number of *independent* tasks rather than one tightly-coupled distributed
job, you do not need this — use ordinary tasks with [fanout](../task-programming/fanout) or, for
warm-container throughput, [reusable containers](./reusable-containers) instead.

## How it works

When you decorate a function with a clustered environment's `@env.task` and run it, the backend:

1. Creates a **JobSet** of `replicas` identical pods (one pod per node).
2. Starts `torchrun` in each pod with `nproc_per_node` worker processes, so the total number of
   workers (the "world size") is `replicas × nproc_per_node`.
3. Establishes the `torchrun` rendezvous across pods, populating `RANK`, `LOCAL_RANK`, `WORLD_SIZE`,
   `MASTER_ADDR`, and `MASTER_PORT` in every worker.
4. Runs your task body **once in every worker process**. Your code calls
   `torch.distributed.init_process_group()` to join the group, and the collective operations
   (all-reduce, all-gather, …) work across the whole gang.
5. Applies the `failure_policy` to decide whether to restart the JobSet on failure or node eviction,
   and returns the result from rank 0.

Because every worker runs the same task body, you branch on the rank when you need to (for example,
only rank 0 saves checkpoints or returns outputs).

## Basic usage

The example below trains a tiny model with PyTorch `DistributedDataParallel` across the cluster.
First, import `flyte` and the clustered environment types:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/clustered-task-environment/ddp_train.py" fragment="imports" lang="python" >}}

Define a `flyte.clustered.ClusteredTaskEnvironment`. The image is a normal pip-based image —
`flyte` itself provides the runtime entrypoint that sets up the `torchrun` rendezvous, so no extra
runtime library is required. The `replicas` and `nproc_per_node` fields describe the cluster shape:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/clustered-task-environment/ddp_train.py" fragment="env" lang="python" >}}

Write the task body as if it were a single `torchrun` worker: initialize the process group, run your
distributed training loop, and clean up. It executes in every worker across every pod:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/clustered-task-environment/ddp_train.py" fragment="task" lang="python" >}}

Finally, deploy and run the workflow programmatically:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/clustered-task-environment/ddp_train.py" fragment="run" lang="python" >}}

> [!NOTE]
> The example above defaults to CPU (the `gloo` backend) so you can smoke-test it without a GPU
> cluster. For real training, set `USE_GPU = True` to use the `nccl` backend and request GPUs via
> `flyte.Resources(gpu=...)`.

## Configuration parameters

A `flyte.clustered.ClusteredTaskEnvironment` inherits every field of a `flyte.TaskEnvironment` (`name`, `image`,
`resources`, `env_vars`, `secrets`, `pod_template`, `cache`, and so on) and adds the following
cluster-specific fields. For full type signatures and defaults, see `flyte.clustered.ClusteredTaskEnvironment`
(API reference).

| Parameter | Description |
|-----------|-------------|
| **`replicas`** | Number of pods (nodes) in the JobSet. Required, must be `>= 1`. |
| **`nproc_per_node`** | Worker processes per pod, passed to `torchrun --nproc-per-node`. Required, must be `>= 1`. When you request GPUs, it must be `<=` the GPU count per pod (typically one process per GPU). |
| **`runtime`** | Launcher configuration. Currently a `flyte.clustered.TorchRun` instance (the default). |
| **`interconnect`** | Network fabric between pods. Currently only `"tcp"` is supported. |
| **`failure_policy`** | JobSet-level restart policy — a `flyte.clustered.ClusterFailurePolicy` (see below). |
| **`ttl_seconds_after_finished`** | Optional seconds to retain the JobSet after it completes, for inspecting pods. Defaults to the backend's behavior. |

The world size — the total number of distributed workers — is `replicas × nproc_per_node`.

### `TorchRun`

`flyte.clustered.TorchRun` configures the `torchrun` launcher:

- **`rdzv_backend`** — the rendezvous backend. `"static"` (default) relies on JobSet-level restarts;
  `"c10d"` enables in-job elastic recovery via a TCP store on rank 0.
- **`max_restarts`** — in-pod `torchrun` restarts before the pod itself is considered failed. This
  is distinct from the JobSet-level `max_restarts` on the failure policy.

### `ClusterFailurePolicy`

`flyte.clustered.ClusterFailurePolicy` controls how the JobSet as a whole recovers from failure:

- **`max_restarts`** — how many times the entire JobSet may restart before Flyte surfaces a failure.
- **`restart_on_host_maintenance`** — when `True`, node evictions (for example, spot reclamation or
  host maintenance) trigger a free restart that does not consume the `max_restarts` budget.

## The distributed context

Inside a clustered task, `flyte.ctx()` exposes the worker's place in the cluster, so you rarely need
to read the raw environment variables yourself:

| Attribute | Meaning |
|-----------|---------|
| `ctx.rank` | Global rank of this worker across the whole world. |
| `ctx.world_size` | Total number of workers (`replicas × nproc_per_node`). |
| `ctx.local_rank` | Rank of this worker within its pod — use it to pin the local GPU. |
| `ctx.node_rank` | Rank of this pod among all pods. |
| `ctx.nnodes` | Number of pods (nodes). |
| `ctx.master_addr` | Address of the rendezvous master (rank 0). |

A common pattern is to bind each worker to its local GPU *before* initializing the process group so
the backend binds to the right device:

```python
ctx = flyte.ctx()
torch.cuda.set_device(ctx.local_rank or 0)
torch.distributed.init_process_group(backend="nccl")
```

## Checkpointing

Pod-local disk is wiped when a JobSet restarts, so long-running training must persist model state to
durable storage rather than the local filesystem. Use the task's checkpoint store, available at
`flyte.ctx().checkpoint`, and typically write from rank 0 only. The FSDP example below shows the full
pattern: gather a full state dict onto rank 0 and save it (for models small enough to gather), or
have every rank write its own shard (for models too large to gather).

{{< code file="/unionai-examples/v2/user-guide/task-configuration/clustered-task-environment/fsdp_train.py" lang="python" >}}

## Using higher-level frameworks

Frameworks with their own multi-process launchers — such as PyTorch Lightning — also ride the
`torchrun` contract. Let the clustered runtime start one process per rank and configure the framework
to **attach to the existing process group** rather than spawn its own. In Lightning, that means
`strategy="ddp"` (not a `*_spawn` strategy) with `devices` and `num_nodes` taken from the clustered
context:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/clustered-task-environment/lightning_mnist.py" lang="python" >}}

## Constraints

- **No reusable containers.** A clustered environment cannot set `reusable` — the gang is created
  fresh for each run. Setting it raises an error.
- **`nproc_per_node` must not exceed the GPU count.** When `resources.gpu` is set, `nproc_per_node`
  must be `<=` the number of GPUs per pod.
- **`torchrun` runtime only.** The `runtime` must currently be a `flyte.clustered.TorchRun`; other
  launchers are not yet supported.
- **TCP interconnect only.** `interconnect` currently supports only `"tcp"`.
