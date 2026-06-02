---
title: Interruptible tasks
weight: 10
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
> This is independent from how the medium (spot vs. on-demand) is chosen for each user-budget attempt — see [Spot to on-demand fallback](#spot-to-on-demand-fallback) below.

### Spot to on-demand fallback

By default, the **final attempt** of an interruptible task runs on an on-demand instance rather than on spot.
This shields long-running or expensive workloads from getting stuck in a preemption loop — once you're on your last attempt, the platform stops gambling on spot capacity.

Two consequences worth knowing:

- A task with `interruptible=True` and no retries is effectively on-demand. Its single attempt is also its final attempt, so it never runs on spot.
- A task with `interruptible=True, retries=2` makes up to 3 attempts: attempts 1 and 2 run on spot, attempt 3 (if reached) runs on on-demand.

If you want spot pricing to apply to *every* attempt, you need to size `retries` so the workload realistically completes before the final attempt — there's no way to opt out of the on-demand fallback on the last attempt.

> [!NOTE]
> Looking for scheduling control — concurrency limits, depth, priority, or routing
> work to a specific cluster? See [Queues](./queues).
