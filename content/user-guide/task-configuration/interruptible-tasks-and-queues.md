---
title: Interruptible tasks and queues
weight: 10
variants: +flyte +byoc +selfmanaged
---

# Interruptible tasks and queues

## Interruptible tasks

Cloud providers offer discounted compute instances (AWS Spot Instances, GCP Preemptible VMs)
that can be reclaimed at any time. These instances are significantly cheaper than on-demand
instances but come with the risk of preemption.

Setting `interruptible=True` allows Flyte to schedule the task on these spot/preemptible instances
for cost savings:

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    interruptible=True,
)

@env.task
def train_model(data: list) -> dict:
    return {"accuracy": 0.95}
```

### Setting at different levels

`interruptible` can be set at the `TaskEnvironment` level, the `@env.task` decorator level,
and at the `task.override()` invocation level. The more specific level always takes precedence.

This lets you set a default at the environment level and override per-task:

```python
import flyte

# All tasks in this environment are interruptible by default
env = flyte.TaskEnvironment(
    name="my_env",
    interruptible=True,
)

# This task uses the environment default (interruptible)
@env.task
def preprocess(data: list) -> list:
    return [x * 2 for x in data]

# This task overrides to non-interruptible (critical, should not be preempted)
@env.task(interruptible=False)
def save_results(results: dict) -> str:
    return "saved"
```

You can also override at invocation time:

```python
@env.task
async def main(data: list) -> str:
    processed = preprocess(data=data)
    # Run this specific invocation as non-interruptible
    return save_results.override(interruptible=False)(results={"data": processed})
```

### Behavior on preemption

When a spot instance is reclaimed, the task is terminated and rescheduled.
Combine `interruptible=True` with [retries](./retries-and-timeouts) to handle preemptions gracefully:

```python
@env.task(interruptible=True, retries=3)
def train_model(data: list) -> dict:
    return {"accuracy": 0.95}
```

> [!NOTE]
> Retries due to spot preemption do not count against the user-configured retry budget.
> System retries (for preemptions and other system-level failures) are tracked separately.

## Queues

Queues are named routing labels that map tasks to specific resource pools or execution clusters
in your infrastructure.

Setting a queue directs the task to the corresponding compute partition:

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    queue="gpu-pool",
)

@env.task
def train_model(data: list) -> dict:
    return {"accuracy": 0.95}
```

### Setting at different levels

`queue` can be set at the `TaskEnvironment` level, the `@env.task` decorator level,
and at the `task.override()` invocation level. The more specific level takes precedence.

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    queue="default-pool",
)

# Uses environment-level queue ("default-pool")
@env.task
def preprocess(data: list) -> list:
    return [x * 2 for x in data]

# Overrides to a different queue
@env.task(queue="gpu-pool")
def train_model(data: list) -> dict:
    return {"accuracy": 0.95}
```

If no queue is specified at any level, the default queue is used.

> [!NOTE]
> Queues are configured as part of your {{< key product_name >}} deployment by your platform administrator.
> The available queue names depend on your infrastructure setup.
