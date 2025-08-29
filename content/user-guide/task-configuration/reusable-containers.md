---
title: Reusable containers
weight: 180
variants: +flyte +serverless +byoc +selfmanaged
---

# Reusable containers

By default, each task execution in Flyte and Union runs in a fresh container instance that is created just for that execution and then discarded.
Container reuse is an optimization feature that allows the same container to be reused across multiple executions and tasks.
This approach reduces startup overhead and improves resource efficiency, making it especially beneficial for frequent, short-duration tasks.

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

## Basic Usage

Enable container reuse by adding a `ReusePolicy` to your `TaskEnvironment`:

> [!NOTE]
> The reusable containers feature currently requires a dedicated runtime library
> ([`unionai-reuse`](https://pypi.org/project/unionai-reuse/)) to be installed in the task image used by the reusable task.
> You can add this library to your task image using the `flyte.Image.with_pip_packages` method, as shown below.
> This library only needs to be added to the task image.
> It does not need to be installed in your local development environment.

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

## Examples

### Machine learning inference

Ideal for ML workloads where model loading is expensive:

```python
ml_env = flyte.TaskEnvironment(
    name="ml-inference",
    resources=flyte.Resources(memory="4Gi", cpu="2", gpu="1"),
    reusable=flyte.ReusePolicy(
        replicas=2,                    # 2 GPU containers (expensive resources)
        concurrency=5,                 # 5 concurrent predictions per container (GPU can handle multiple)
        idle_ttl=1800,                 # 30 minutes (longer due to expensive model loading)
        scaledown_ttl=3600             # 1 hour environment timeout
    )
)

# Model loaded once per container
model = None

@ml_env.task
async def predict(data: list[float]) -> float:
    global model
    if model is None:
        model = load_expensive_model()  # Only happens once per container
    return model.predict(data)
```

### Batch processing

Efficient for processing many small items with high concurrency:

```python
batch_env = flyte.TaskEnvironment(
    name="batch-processor",
    resources=flyte.Resources(memory="2Gi", cpu="1"),
    reusable=flyte.ReusePolicy(
        replicas=3,                    # 3 container instances
        concurrency=8,                 # 8 concurrent tasks per container (24 total capacity)
        idle_ttl=300,                  # 5 minutes individual timeout
        scaledown_ttl=1800             # 30 minutes environment timeout
    )
)

@batch_env.task
async def process_item(item: dict) -> dict:
    return {"processed": item["data"], "result": transform(item)}

@flyte.workflow
async def batch_workflow(items: list[dict]) -> list[dict]:
    results = await flyte.map_task(process_item)(item=items)
    return results
```

{{< /markdown >}}
{{< /variant >}}