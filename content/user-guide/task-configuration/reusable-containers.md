---
title: Reusable containers
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Reusable containers

By default, each task execution in Flyte and Union runs in a fresh container instance that is created just for that execution and then discarded.
With reusable containers, the same container can be reused across multiple executions and tasks.
This approach reduces start up overhead and improves resource efficiency.

{{< variant flyte >}}
{{< markdown >}}

> [!NOTE]
> The reusable container feature is only available when running your Flyte code on a Union backend.
> See [one of the Union.ai product variants of this page]({{< docs_home byoc v2 >}}/user-guide/reusable-containers) for details.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

> [!NOTE]
> The reusable container feature is only available when running your Flyte code on a Union backend.

## How It Works

With reusable containers, the system maintains a pool of persistent containers that can handle multiple task executions.
When you configure a `TaskEnvironment` with a `ReusePolicy`, the system does the following:

1. Creates a pool of persistent containers.
2. Routes task executions to available container instances.
3. Manages container lifecycle with configurable timeouts.
4. Supports concurrent task execution within containers (for async tasks).
5. Preserves the Python execution environment across task executions, allowing you to maintain state through global variables.

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
        replicas=2,                           # Create 2 container instances
        concurrency=1,                        # Process 1 task per container at a time
        scaledown_ttl=timedelta(minutes=10),  # Individual containers shut down after 5 minutes of inactivity
        idle_ttl=timedelta(hours=1)           # Entire environment shuts down after 30 minutes of no tasks
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
    concurrency: int,
    scaledown_ttl: typing.Union[int, datetime.timedelta],
    idle_ttl: typing.Union[int, datetime.timedelta]
)
```

### `replicas`: Container pool size

Controls the number of container instances in the reusable pool:

- **Fixed size**: `replicas=3` Creates exactly 3 container instances. These 3 replicas will be shutdown after `idle_ttl` expires.
- **Auto-scaling**: `replicas=(2, 5)` Starts with 2 containers and can scale up to 5 based on demand.
  - If the task is running on 2 replicas and demand drops to zero then these 2 containers will be shutdown after `idle_ttl` expires.
  - If the task is running on 2 replicas and demand increases, new containers will be created up to the maximum of 5.
  - If the task is running on 5 replicas and demand drops, container 5 will be shutdown after `scaledown_ttl` expires.
  - If demand drops again, container 4 will be also shutdown after another period of `scaledown_ttl` expires.
- **Resource impact**: Each replica consumes the full resources defined in `TaskEnvironment.resources`.

```python
# Fixed pool size
reuse_policy = flyte.ReusePolicy(
    replicas=3,
    concurrency=1,
    scaledown_ttl=timedelta(minutes=10),
    idle_ttl=timedelta(hours=1)
)

# Auto-scaling pool
reuse_policy = flyte.ReusePolicy(
    replicas=(1, 10),
    concurrency=1,
    scaledown_ttl=timedelta(minutes=10),
    idle_ttl=timedelta(hours=1)
)
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
    scaledown_ttl=timedelta(minutes=10),
    idle_ttl=timedelta(hours=1)
)

# Concurrent processing
concurrent_policy = flyte.ReusePolicy(
    replicas=2,
    concurrency=5,  # 5 tasks per container = 10 total concurrent tasks
    scaledown_ttl=timedelta(minutes=10),
    idle_ttl=timedelta(hours=1)
)
```

### `idle_ttl` vs `scaledown_ttl`: Container lifecycle

These parameters work together to manage container lifecycle at different levels:

#### `idle_ttl`: Environment timeout

- **Scope**: Controls the entire reusable environment infrastructure.
- **Behavior**: When there are no active or queued tasks, the entire environment scales down after `idle_ttl` expires.
- **Purpose**: Manages the lifecycle of the entire container pool.
- **Typical values**: 1-2 hours, or `None` for always-on environments

#### `scaledown_ttl`: Individual container timeout

- **Scope**: Controls individual container instances.
- **Behavior**: When a container finishes a task and becomes inactive, it will be terminated after `scaledown_ttl` expires.
- **Purpose**: Prevents resource waste from inactive containers.
- **Typical values**: 5-30 minutes for most workloads.


```python
from datetime import timedelta

lifecycle_policy = flyte.ReusePolicy(
    replicas=3,
    concurrency=2,
    scaledown_ttl=timedelta(minutes=10),  # Individual containers shut down after 10 minutes of inactivity
    idle_ttl=timedelta(hours=1)         # Entire environment shuts down after 1 hour of no tasks
)
```

## Understanding parameter relationships

The four `ReusePolicy` parameters work together to control different aspects of container management:

```python
reuse_policy = flyte.ReusePolicy(
    replicas=4,                           # Infrastructure: How many containers?
    concurrency=3,                        # Throughput: How many tasks per container?
    scaledown_ttl=timedelta(minutes=10),  # Individual: When do idle containers shut down?
    idle_ttl=timedelta(hours=1)           # Environment: When does the whole pool shut down?
)
# Total capacity: 4 × 3 = 12 concurrent tasks
# Individual containers shut down after 10 minutes of inactivity
# Entire environment shuts down after 1 hour of no tasks
```

### Key relationships

- **Total throughput** = `replicas × concurrency`
- **Resource usage** = `replicas × TaskEnvironment.resources`
- **Cost efficiency**: Higher `concurrency` reduces container overhead, more `replicas` provides better isolation
- **Lifecycle management**:  `scaledown_ttl` manages individual containers, `idle_ttl` manages the environment


## Simple example

Here is a simple, but complete, example of reuse with concurrency

First, import the needed modules, set upf logging:

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-concurrency.py" fragment=import lang=python >}}
{{< markdown >}}

Next, we set up the reusable task environment. Note that, currently, the image used for a reusable environment requires an extra package to be installed:

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-concurrency.py" fragment=env lang=python >}}
{{< markdown >}}

Now, we define the `reuse_concurrency` task (the main driver task of the workflow) and the `noop` task that will be executed multiple times reusing the same containers:

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-concurrency.py" fragment=tasks lang=python >}}
{{< markdown >}}

Finally, we deploy and run the workflow programmatically, so all you have to do is execute `python reuse_concurrency.py` to see it in action:

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-concurrency.py" fragment=run lang=python >}}

{{< /variant >}}

<!--
## Machine learning example

A good use case for re-usable containers is machine learning inference. The overhead of loading a large model can be significant, so re-using containers for multiple inference requests can improve efficiency.

In this example we mock the model loading and prediction process. The full source code can be found on [GitHUb](https://github.com/unionai/unionai-examples/blob/main/user-guide-v2/task-configuration/reusable-containers/reuse.py).

First, import the needed modules:

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-ml.py" fragment=import lang=python >}}
{{< markdown >}}

Next, mock-up the model loading and prediction process:

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-ml.py" fragment=mock lang=python >}}
{{< markdown >}}

Now, we set up the reusable task environment. Note that, currently, the image used for a reusable environment requires an extra package to be installed:

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-ml.py" fragment=env lang=python >}}
{{< markdown >}}

We define the `do_predict` task that loads the model and performs predictions using that model.

The key aspect of this task is that the model is loaded once per container and reused for all subsequent predictions, thus minimizes the overhead.

This is achieved through the use of a global variable to store the model and a lock to ensure that the model is only loaded once.

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-ml.py" fragment=do_predict lang=python >}}
{{< markdown >}}

The `main` task ofthe workflow drives the prediction loop with a set of test data:

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-ml.py" fragment=main lang=python >}}
{{< markdown >}}

Finally, we deploy and run the workflow programmatically, so all you have to do is execute `python reuse-ml.py` to see it in action:

{{< /markdown >}}
{{< code file="/external/unionai-examples/user-guide-v2/task-configuration/reusable-containers/reuse-ml.py" fragment=run lang=python >}}

{{< /variant >}}
-->