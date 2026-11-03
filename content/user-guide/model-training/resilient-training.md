---
title: Resilient training
description: Keep long training jobs from losing progress to preemption, node failures, out-of-memory errors, and scarce GPU capacity.
icon: shield-check
weight: 4
variants: +flyte +union
---

# Resilient training

The longer a training job runs, the more likely something under it fails: a spot node is reclaimed, a GPU falls off the bus, a batch runs out of memory, or the cluster has no free H100s. Flyte turns each of these into something your code handles, instead of a run you start over.

| Failure | What to use | What happens |
|---|---|---|
| The task's pod dies or is preempted | `retries` with `flyte.Checkpoint` | The next attempt loads the last checkpoint and continues from there |
| A node in a multi-node job fails | `ClusterFailurePolicy` | The whole group restarts in place and resumes from the checkpoint |
| The container runs out of memory | `flyte.errors.OOMError` with `override` | The driver retries the task with more memory |
| The GPU type you asked for isn't available | `max_queued_time` with `override` | The driver moves on to the next GPU type |
| A later stage fails | Recovery or caching | A new run reuses the stages that already succeeded |

## Resume from a checkpoint after a retry

`flyte.ctx().checkpoint` is a per-task store in your object store. It survives across a task's retries. Save to it as training progresses, and load from it at the start of the task:

{{< code file="/unionai-examples/v2/user-guide/task-programming/intra-task-checkpoints/pytorch_checkpoint.py" fragment="task" lang=python >}}

Save the optimizer state and the step or epoch along with the weights, so the resumed attempt continues the same schedule. To connect a framework's own checkpointing, such as the Hugging Face `Trainer` or Lightning's `ModelCheckpoint`, use a callback. See [Intra-task checkpoints](../tasks/task-programming/intra-task-checkpoints).

## Use spot capacity

Spot and preemptible GPUs cost a fraction of on-demand ones. With checkpoints in place, a preemption costs only the work since the last save. Set `interruptible=True` and give the task retries:

```python
train_env = flyte.TaskEnvironment(
    name="train",
    resources=flyte.Resources(gpu="A100:8"),
    interruptible=True,
)


@train_env.task(retries=5)
async def train(epochs: int) -> flyte.io.Dir: ...
```

Keep the driver and evaluation tasks on on-demand capacity with `interruptible=False`. See [Interruptible tasks](../tasks/task-configuration/interruptible-tasks-and-queues).

## Restart a multi-node job

When one pod of a clustered job fails, the other ranks can't continue. `ClusterFailurePolicy` restarts the whole group in place:

```python
from flyte.clustered import ClusterFailurePolicy, ClusteredTaskEnvironment, TorchRun

env = ClusteredTaskEnvironment(
    name="pretrain",
    resources=flyte.Resources(gpu="H100:8", shm="16Gi"),
    replicas=4,
    nproc_per_node=8,
    runtime=TorchRun(),
    failure_policy=ClusterFailurePolicy(max_restarts=2, restart_on_host_maintenance=True),
)
```

- `max_restarts` is the number of in-place restarts before the attempt fails. They don't count against the task's `retries`.
- `restart_on_host_maintenance=True` makes a restart caused by a node eviction free, so planned maintenance doesn't use up `max_restarts`.

Pod-local disk is wiped on a restart, so write checkpoints from rank 0 to `flyte.ctx().checkpoint`. See [Clustered task environment](../tasks/task-configuration/clustered-task-environment#checkpointing).

## Recover from out-of-memory errors

When a container runs out of host memory, the parent task receives `flyte.errors.OOMError` and can call the task again with more memory:

```python
@driver_env.task
async def main() -> flyte.io.Dir:
    for memory in ["64Gi", "128Gi", "256Gi"]:
        try:
            return await train.override(resources=flyte.Resources(gpu="A100:1", memory=memory))()
        except flyte.errors.OOMError:
            continue
    raise RuntimeError("Out of memory at every size")
```

Running out of GPU memory is different: the framework raises its own exception, such as `torch.cuda.OutOfMemoryError`. See [Error handling](../tasks/task-programming/error-handling#out-of-memory-on-the-gpu) to catch it and retry with a smaller batch, and [Falling back when GPU capacity isn't available](../tasks/task-programming/error-handling#falling-back-when-gpu-capacity-isnt-available) to move to another GPU type when the first one has no capacity.

## Reuse finished stages

A pipeline that fails at evaluation shouldn't retrain the model. Two features keep finished stages from running again:

- **Recovery** starts a new run from a failed one and reuses every action that succeeded. See [Recover a failed run](../tasks/task-deployment/recover-runs).
- **Caching** reuses a task's output in any later run with the same inputs and code. Set `cache="auto"` on data prep and training. See [Caching](../tasks/task-configuration/caching).

## Related

- [Retries and timeouts](../tasks/task-configuration/retries-and-timeouts)
- [Pretraining](./pretraining)
- [Post-training and fine-tuning](./post-training)
