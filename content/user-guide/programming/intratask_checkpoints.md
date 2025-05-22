---
title: Intratask checkpoints
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Intratask checkpoints

A checkpoint in Flyte serves to recover a task from a previous failure by preserving the task's state before the failure
and resuming from the latest recorded state.

## Why intratask checkpoints?

The inherent design of Flyte, being a workflow engine, allows users to break down operations, programs or ideas
into smaller tasks within workflows. In the event of a task failure, the workflow doesn't need to rerun the
previously completed tasks. Instead, it can retry the specific task that encountered an issue.
Once the problematic task succeeds, it won't be rerun. Consequently, the natural boundaries between tasks act as implicit checkpoints.

However, there are scenarios where breaking a task into smaller tasks is either challenging or undesirable due to the associated overhead.
This is especially true when running a substantial computation in a tight loop.
In such cases, users may consider splitting each loop iteration into individual tasks using dynamic workflows.
Yet, the overhead of spawning new tasks, recording intermediate results, and reconstructing the state can incur additional expenses.

### Use case: Model training

An exemplary scenario illustrating the utility of intra-task checkpointing is during model training.
In situations where executing multiple epochs or iterations with the same dataset might be time-consuming,
setting task boundaries can incur a high bootstrap time and be costly.

Flyte addresses this challenge by providing a mechanism to checkpoint progress within a task execution,
saving it as a file or set of files. In the event of a failure, the checkpoint file can be re-read to
resume most of the state without rerunning the entire task.
This feature opens up possibilities to leverage alternate, more cost-effective compute systems,
such as [AWS spot instances](https://aws.amazon.com/ec2/spot/),
[GCP pre-emptible instances](https://cloud.google.com/compute/docs/instances/preemptible) and others.

These instances offer great performance at significantly lower price points compared to their on-demand or reserved counterparts.
This becomes feasible when tasks are constructed in a fault-tolerant manner.
For tasks running within a short duration, e.g., less than 10 minutes, the likelihood of failure is negligible,
and task-boundary-based recovery provides substantial fault tolerance for successful completion.

However, as the task execution time increases, the cost of re-running it also increases,
reducing the chances of successful completion. This is precisely where Flyte's intra-task checkpointing proves to be highly beneficial.

Here's an example illustrating how to develop tasks that leverage intra-task checkpointing.
It's important to note that Flyte currently offers the low-level API for checkpointing.
Future integrations aim to incorporate higher-level checkpointing APIs from popular training frameworks
like Keras, PyTorch, Scikit-learn, and big-data frameworks such as Spark and Flink, enhancing their fault-tolerance capabilities.

Create a file called `checkpoint.py`:

Import the required libraries:

```python
import {{< key kit_import >}}
from flytekit.exceptions.user import FlyteRecoverableException

RETRIES = 3
```

We define a task to iterate precisely `n_iterations`, checkpoint its state, and recover from simulated failures:

```python
# Define a task to iterate precisely `n_iterations`, checkpoint its state, and recover from simulated failures.
@{{< key kit_as >}}.task(retries=RETRIES)
def use_checkpoint(n_iterations: int) -> int:
    cp = {{< key kit_as >}}.current_context().checkpoint
    prev = cp.read()

    start = 0
    if prev:
        start = int(prev.decode())

    # Create a failure interval to simulate failures across 'n' iterations and then succeed after configured retries
    failure_interval = n_iterations // RETRIES
    index = 0
    for index in range(start, n_iterations):
        # Simulate a deterministic failure for demonstration. Showcasing how it eventually completes within the given retries
        if index > start and index % failure_interval == 0:
            raise FlyteRecoverableException(f"Failed at iteration {index}, failure_interval {failure_interval}.")
        # Save progress state. It is also entirely possible to save state every few intervals
        cp.write(f"{index + 1}".encode())
    return index
```

The checkpoint system offers additional APIs. The code can be found at
[checkpointer code](https://github.com/flyteorg/flytekit/blob/master/flytekit/core/checkpointer.py).

Create a workflow that invokes the task:
The task will automatically undergo retries in the event of a [FlyteRecoverableException](../../api-reference/flytekit-sdk/packages/flytekit.exceptions.base#flytekitexceptionsbaseflyterecoverableexception)

```python
@{{< key kit_as >}}.workflow
def checkpointing_example(n_iterations: int) -> int:
    return use_checkpoint(n_iterations=n_iterations)
```

The local checkpoint is not utilized here because retries are not supported:

```python
if __name__ == "__main__":
    try:
        checkpointing_example(n_iterations=10)
    except RuntimeError as e:  # noqa : F841
        # Since no retries are performed, an exception is expected when run locally
        pass
```

## Run the example on the Flyte cluster

To run the provided workflow on the Flyte cluster, use the following command:

```bash
pyflyte run --remote \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/69dbe4840031a85d79d9ded25f80397c6834752d/examples/advanced_composition/advanced_composition/checkpoint.py \
  checkpointing_example --n_iterations 10
```

{{< variant flyte >}}
{{< markdown >}}
```bash
pyflyte run --remote \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/69dbe4840031a85d79d9ded25f80397c6834752d/examples/advanced_composition/advanced_composition/checkpoint.py \
  checkpointing_example --n_iterations 10
```
{{< /markdown >}}
{{< /variant >}}

{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}
```bash
union run --remote checkpoint.py checkpointing_example --n_iterations 10
```
{{< /markdown >}}
{{< /variant >}}
