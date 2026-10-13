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
def train_model(data: list[float]) -> dict:
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
def preprocess(data: list[int]) -> list[int]:
    return [x * 2 for x in data]

# This task overrides to non-interruptible (critical, should not be preempted)
@env.task(interruptible=False)
def save_results(results: dict) -> str:
    return "saved"
```

You can also override at invocation time. From an `async` parent, call a sync task with `.aio()`:

```python
@env.task
async def main(data: list[int]) -> str:
    processed = await preprocess.aio(data=data)
    # Run this specific invocation as non-interruptible
    return await save_results.override(interruptible=False).aio(results={"data": processed})
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
def train_model(data: list[float]) -> dict:
    return {"accuracy": 0.95}
```

> [!NOTE]
> Retries due to spot preemption do not count against the user-configured retry budget.
> System retries (for preemptions and other system-level failures) are tracked separately.

## Fall back to on-demand when spot capacity is unavailable

Preemption and unavailability are different failures. A preempted task is rescheduled for you.
A task whose spot pool has no capacity can sit in the **Queued** or **Waiting for resources**
phase until capacity appears.

Bound that wait with
[`max_queued_time`](./retries-and-timeouts#max_queued_time-fail-fast-when-capacity-isnt-available).
When it fires, the parent receives `flyte.errors.MaxQueuedTimeExceededError`. Catch it and re-run
the task on on-demand compute with `interruptible=False`:

```python
from datetime import timedelta

import flyte
import flyte.errors

env = flyte.TaskEnvironment(
    name="my_env",
    interruptible=True,
)


@env.task(timeout=flyte.Timeout(max_queued_time=timedelta(minutes=10)))
async def train_model(data: list[float]) -> dict:
    return {"accuracy": 0.95}


# The parent runs on-demand, so it can start and catch the timeout even with no spot capacity
@env.task(interruptible=False)
async def main(data: list[float]) -> dict:
    try:
        # Spot, abandoned if nothing is scheduled within 10 minutes
        return await train_model(data=data)
    except flyte.errors.MaxQueuedTimeExceededError:
        # On-demand, with no queue bound
        return await train_model.override(interruptible=False, timeout=flyte.Timeout())(data=data)
```

- **Run the parent on-demand.** A parent in the interruptible environment needs spot capacity
  too. With none available, it never starts and never reaches the fallback.
- **Clear the queue bound on the fallback.** `override()` keeps the task's `timeout` unless you
  pass a new one, so without `timeout=flyte.Timeout()` the on-demand attempt also fails after
  10 minutes in the queue. `timeout=0` does not clear it.
- **Account for retries.** `max_queued_time` applies to each attempt, so with `retries=3` the
  parent sees the error after about 40 minutes, not 10. See
  [Combining retries and timeouts](./retries-and-timeouts#combining-retries-and-timeouts).

See [Falling back when GPU capacity isn't available](../task-programming/error-handling#falling-back-when-gpu-capacity-isnt-available)
for the same pattern with scarce GPUs.

{{< variant union >}}
{{< markdown >}}
> [!NOTE]
> Looking for scheduling control: concurrency limits, depth, priority, or routing
> work to a specific cluster? See [Queues](./queues).
{{< /markdown >}}
{{< /variant >}}
