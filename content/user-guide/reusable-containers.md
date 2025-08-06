---
title: Reusable containers
weight: 180
variants: -flyte +serverless +byoc +selfmanaged
---

# Reusable containers

Container reuse is an optimization feature that allows you to reuse containers across multiple task executions. This reduces container startup overhead and improves resource efficiency, especially for frequent, short-duration tasks.

## How It Works

By default, Flyte creates a new container for each task execution. Container reuse changes this by maintaining a pool of persistent containers that can handle multiple task executions. When you configure a `TaskEnvironment` with a `ReusePolicy`, Flyte:

1. Creates a pool of persistent containers
2. Routes task executions to available container instances
3. Manages container lifecycle with configurable timeouts
4. Supports concurrent task execution within containers (for async tasks)

## Basic Usage

Enable container reuse by adding a `ReusePolicy` to your `TaskEnvironment`:

```python
import flyte

env = flyte.TaskEnvironment(
    name="reusable-env",
    resources=flyte.Resources(memory="1Gi", cpu="500m"),
    reusable=flyte.ReusePolicy(
        replicas=2,        # Number of container instances
        idle_ttl=300       # 5 minutes idle timeout
    )
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

## Configuration

### `ReusePolicy` Parameters

- **`replicas`**: Number of container instances in the pool (e.g., `2` or `(2, 5)` for auto-scaling).
  **Note: Autoscaling is coming soon**.
- **`idle_ttl`**: How long containers stay alive without processing tasks (in seconds)

```python
reuse_policy = flyte.ReusePolicy(
    replicas=3,
    idle_ttl=600  # 10 minutes
)
```

## Common Use Cases

### Machine Learning Inference

Ideal for ML workloads where model loading is expensive:
<!-- TODO:
Referring to  the section in the code below

```
# Model loaded once per container
model = None
```
Ketan Umare
this should have an asyncio lock. Better to use alru_cache
-->

```python
ml_env = flyte.TaskEnvironment(
    name="ml-inference",
    resources=flyte.Resources(memory="4Gi", cpu="2", gpu="1"),
    reusable=flyte.ReusePolicy(replicas=2, idle_ttl=1800)  # 30 minutes
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

### Batch Processing

Efficient for processing many small items:

```python
batch_env = flyte.TaskEnvironment(
    name="batch-processor",
    reusable=flyte.ReusePolicy(
        replicas=4,
        idle_ttl=300
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

## Best Practices

### Task Design

Design tasks to be stateless and avoid global state modifications:

```python
# ✅ Good: Stateless task
@env.task
async def process_data(data: dict) -> dict:
    result = transform_data(data)  # No side effects
    return result

# ❌ Avoid: Tasks with global state
cache = {}  # Global state

@env.task
async def stateful_task(data: dict) -> dict:
    cache[data["id"]] = data  # State leaks between executions
    return data
```

### Resource Sizing

Size resources appropriately for your workload:

```python
# Right-sized for workload
env = flyte.TaskEnvironment(
    name="optimized",
    resources=flyte.Resources(memory="1Gi", cpu="500m"),
    reusable=flyte.ReusePolicy(
        replicas=3,      # Based on expected load
        idle_ttl=600    # Reasonable cleanup interval    )
)
```

## When to Use Container Reuse

**Ideal for:**
- Frequent, short-duration tasks
- Tasks with expensive initialization (model loading, database connections)
- Batch processing workloads
- Development and testing scenarios

**Avoid for:**
- Long-running tasks that occupy containers for extended periods
- Tasks that consume large amounts of memory without cleanup
- Tasks that modify global state or have persistent side effects
- Environments requiring strict resource isolation

Container reuse provides significant performance improvements for appropriate workloads while maintaining the reliability and observability of the Flyte execution environment.