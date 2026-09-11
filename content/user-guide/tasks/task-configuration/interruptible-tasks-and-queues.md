---
title: Interruptible tasks
description: Run tasks on discounted spot instances that can be reclaimed at any time.
icon: lightning
weight: 11
variants: +flyte +union
---

# Interruptible tasks

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

## Setting at different levels

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

## Behavior on preemption

When a spot instance is reclaimed, the running task is terminated and automatically
rescheduled. Preemptions are retried on a separate, platform-managed budget, so they do
**not** consume the task's configured [retries](./retries-and-timeouts) — you don't need to
set `retries` for an interruptible task to be resilient to preemption.

`retries` instead governs re-attempts after your own task code fails (for example, an
unhandled exception or a timeout), and behaves the same for interruptible and
non-interruptible tasks:

```python
@env.task(interruptible=True, retries=3)
def train_model(data: list) -> dict:
    return {"accuracy": 0.95}
```

> [!NOTE]
> Retries due to spot preemption do not count against the user-configured retry budget.
> System retries (for preemptions and other system-level failures) are tracked separately.

{{< variant union >}}
{{< markdown >}}
> [!NOTE]
> Looking for scheduling control: concurrency limits, depth, priority, or routing
> work to a specific cluster? See [Queues](./queues).
{{< /markdown >}}
{{< /variant >}}
