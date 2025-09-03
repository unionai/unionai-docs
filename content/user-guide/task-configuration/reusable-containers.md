---
title: Reusable containers
weight: 180
variants: +flyte +serverless +byoc +selfmanaged
---

# Reusable containers

By default, each task execution in Flyte and Union runs in a fresh container instance that is created just for that execution and then discarded.
Container reuse is an optimization feature that allows the same container to be reused across multiple executions and tasks.
This approach reduces start up overhead and improves resource efficiency, making it especially beneficial for frequent, short-duration tasks.

{{< variant flyte >}}
{{< markdown >}}

> [!NOTE]
> The reusable container feature is only available when running your Flyte code on a Union backend.
> See [one of the Union.ai product variants of this page]({{< docs_home byoc v2 >}}/user-guide/reusable-containers) for details.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

## How It Works

With reusable containers, the system maintains a pool of persistent containers that can handle multiple task executions.
When you configure a `TaskEnvironment` with a `ReusePolicy`, the system does the following:

1. Creates a pool of persistent containers.
2. Routes task executions to available container instances.
3. Manages container lifecycle with configurable timeouts.
4. Supports concurrent task execution within containers (for async tasks).
5. For Python tasks, the Python execution environment is preserved across task executions.
   This allows you to maintain state through global variables from one execution to the next.

## Basic Usage

> [!NOTE]
> The reusable containers feature currently requires a dedicated runtime library
> ([`unionai-reuse`](https://pypi.org/project/unionai-reuse/)) to be installed in the task image used by the reusable task.
> You can add this library to your task image using the `flyte.Image.with_pip_packages` method, as shown below.
> This library only needs to be added to the task image.
> It does not need to be installed in your local development environment.

Enable container reuse by adding a `ReusePolicy` to your `TaskEnvironment`:

```python
import flyte

# Currently required to enable resuable containers
reusable_image = flyte.Image.from_debian_base().with_pip_packages("unionai-reuse>=0.1.3")

env = flyte.TaskEnvironment(
    name="reusable-env",
    resources=flyte.Resources(memory="1Gi", cpu="500m"),
    reusable=flyte.ReusePolicy(
        replicas=2,                    # Create 2 container instances
        concurrency=1,                 # Process 1 task per container at a time
        idle_ttl=300,                  # Individual containers shut down after 5 minutes of inactivity
        scaledown_ttl=1800             # Entire environment shuts down after 30 minutes of no tasks
    ),
    image=reusable_image  # Use the container image augmented with the unionai-reuse library.
)

@env.task
async def compute_task(x: int) -> int:
    return x * x

@env.task
async def main() -> list[int]:
    # These tasks will reuse containers from the pool
    results = []
    for i in range(10):
        result = await compute_task(i)
        results.append(result)
    return results
```

## `ReusePolicy` parameters

The `ReusePolicy` class controls how containers are managed in a reusable environment:

```python
flyte.ReusePolicy(
    replicas: typing.Union[int, typing.Tuple[int, int]],
    idle_ttl: typing.Union[int, datetime.timedelta],
    concurrency: int,
    scaledown_ttl: typing.Union[int, datetime.timedelta],
)
```

### `replicas`: Container pool size

Controls the number of container instances in the reusable pool:

- **Fixed size**: `replicas=3` creates exactly 3 container instances.
- **Auto-scaling**: `replicas=(2, 5)` scales from 2 to 5 containers based on demand.
- **Resource impact**: Each replica consumes the full resources defined in `TaskEnvironment.resources`.

```python
# Fixed pool size
reuse_policy = flyte.ReusePolicy(replicas=3, idle_ttl=300, concurrency=1)

# Auto-scaling pool
reuse_policy = flyte.ReusePolicy(replicas=(1, 10), idle_ttl=300, concurrency=1)
```

### `concurrency`: Tasks per container

Controls how many tasks can execute simultaneously within a single container:

- **Default**: `concurrency=1` (one task per container at a time).
- **Higher concurrency**: `concurrency=5` allows 5 tasks to run simultaneously in each container.
- **Total capacity**: `replicas × concurrency` = maximum concurrent tasks across the entire pool.

```python
# Sequential processing (default)
sequential_policy = flyte.ReusePolicy(
    replicas=2,
    concurrency=1,  # One task per container
    idle_ttl=300
)

# Concurrent processing
concurrent_policy = flyte.ReusePolicy(
    replicas=2,
    concurrency=5,  # 5 tasks per container = 10 total concurrent tasks
    idle_ttl=300
)
```

### `idle_ttl` vs `scaledown_ttl`: Container lifecycle

These parameters work together to manage container lifecycle at different levels:

#### `idle_ttl`: Individual container timeout

- **Scope**: Controls individual container instances.
- **Behavior**: When a container finishes a task and becomes idle, it will be terminated after `idle_ttl` expires.
- **Purpose**: Prevents resource waste from idle containers.
- **Typical values**: 5-30 minutes for most workloads.

#### `scaledown_ttl`: Environment timeout

- **Scope**: Controls the entire reusable environment infrastructure.
- **Behavior**: When there are no active or queued tasks, the entire environment scales down after `scaledown_ttl` expires.
- **Purpose**: Manages the lifecycle of the entire container pool.
- **Typical values**: 1-2 hours, or `None` for always-on environments

```python
from datetime import timedelta

lifecycle_policy = flyte.ReusePolicy(
    replicas=3,
    concurrency=2,
    idle_ttl=timedelta(minutes=10),    # Individual containers shut down after 10 minutes of inactivity
    scaledown_ttl=timedelta(hours=2)   # Entire environment shuts down after 2 hours of no tasks
)
```

## Understanding parameter relationships

The four `ReusePolicy` parameters work together to control different aspects of container management:

```python
reuse_policy = flyte.ReusePolicy(
    replicas=4,           # Infrastructure: How many containers?
    concurrency=3,        # Throughput: How many tasks per container?
    idle_ttl=600,         # Individual: When do idle containers shut down?
    scaledown_ttl=3600    # Environment: When does the whole pool shut down?
)
# Total capacity: 4 × 3 = 12 concurrent tasks
# Individual containers shut down after 10 minutes of inactivity
# Entire environment shuts down after 1 hour of no tasks
```

### Key relationships

- **Total throughput** = `replicas × concurrency`
- **Resource usage** = `replicas × TaskEnvironment.resources`
- **Cost efficiency**: Higher `concurrency` reduces container overhead, more `replicas` provides better isolation
- **Lifecycle management**: `idle_ttl` manages individual containers, `scaledown_ttl` manages the environment

## Example

A good use case for re-usable containers is machine learning inference. The overhead of loading a large model can be significant, so re-using containers for multiple inference requests can improve efficiency.

In this example we mock the model loading and prediction process. The full source code can be found on [GitHUb](https://github.com/unionai/unionai-examples/blob/main/user-guide-v2/task-configuration/reusable-containers/reuse.py).


First, import the needed modules:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse.py" fragment=import lang=python >}}

Next, mock-up the model loading and prediction process:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse.py" fragment=mock lang=python >}}

Now, we set up the reusable task environment. Note that, currently, the image used for a reusable environment requires an extra package to be installed:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse.py" fragment=env lang=python >}}

We define the `do_predict` task that loads the model and performs predictions using that model.

The key aspect of this task is that the model is loaded once per container and reused for all subsequent predictions, thus minimizes the overhead.

This is achieved through the use of a global variable to store the model and a lock to ensure that the model is only loaded once.

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse.py" fragment=do_predict lang=python >}}

The `main` task ofthe workflow drives the prediction loop with a set of test data:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse.py" fragment=main lang=python >}}

Finally, we deploy and run the workflow programmatically, so all you have to do is execute `python reuse.py` to see it in action:

{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse.py" fragment=run lang=python >}}

<!--
{{< /markdown >}}
{{< /variant >}}
-->