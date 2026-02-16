---
title: Triggers and dynamic workflows
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Triggers and dynamic workflows

## LaunchPlan to Trigger migration

{{< tabs "migration-triggers" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import workflow, LaunchPlan, CronSchedule, FixedRate
from datetime import timedelta

@workflow
def my_workflow(x: int) -> int:
    return process(x)

# Cron schedule
cron_lp = LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="hourly_run",
    default_inputs={"x": 10},
    schedule=CronSchedule(schedule="0 * * * *"),
)

# Fixed rate
rate_lp = LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="frequent_run",
    default_inputs={"x": 5},
    schedule=FixedRate(duration=timedelta(minutes=30)),
)
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

# Hourly trigger (convenience method)
@env.task(triggers=flyte.Trigger.hourly())
def hourly_task(x: int = 10) -> int:
    return process(x)

# Custom cron trigger
cron_trigger = flyte.Trigger(
    name="custom_cron",
    automation=flyte.Cron("0 * * * *"),
    inputs={"x": 10},
    auto_activate=True,
)

@env.task(triggers=cron_trigger)
def scheduled_task(x: int) -> int:
    return process(x)

# Fixed rate trigger
rate_trigger = flyte.Trigger(
    name="frequent",
    automation=flyte.FixedRate(timedelta(minutes=30)),
    inputs={"x": 5},
    auto_activate=True,
)

@env.task(triggers=rate_trigger)
def frequent_task(x: int) -> int:
    return process(x)
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Trigger options

```python
# Convenience methods
flyte.Trigger.hourly()           # Every hour
flyte.Trigger.hourly("my_time")  # Custom time parameter name
flyte.Trigger.minutely()         # Every minute

# Custom Trigger
flyte.Trigger(
    name="my_trigger",           # Required: trigger name
    automation=flyte.Cron(...),  # Cron or FixedRate
    inputs={"x": 10},            # Default inputs
    auto_activate=True,          # Activate on deploy
)

# Cron options
flyte.Cron(
    schedule="0 9 * * 1-5",      # 9 AM weekdays
    timezone="America/New_York", # Optional timezone
)

# FixedRate options
flyte.FixedRate(timedelta(hours=1))  # Every hour
```

## Deploying triggers

```bash
# Deploy environment (triggers deploy with it)
flyte deploy my_module.py my_env

# Triggers with auto_activate=True activate automatically
# Otherwise, activate manually via UI or API
```

For full details on triggers, see [Triggers](../../user-guide/task-configuration/triggers).

## Dynamic workflows

In Flyte 1, `@dynamic` was needed for tasks that generate variable numbers of subtask calls at runtime. In Flyte 2, all tasks can have dynamic behavior natively.

### @dynamic to regular tasks

{{< tabs "migration-dynamic" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import dynamic, task, workflow

@task
def get_tiles(n: int) -> list[int]:
    return list(range(n))

@task
def process_tile(tile: int) -> int:
    return tile * 2

@dynamic
def process_all_tiles(tiles: list[int]) -> list[int]:
    results = []
    for tile in tiles:
        results.append(process_tile(tile=tile))
    return results

@workflow
def main_workflow(n: int) -> list[int]:
    tiles = get_tiles(n=n)
    return process_all_tiles(tiles=tiles)
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2 Sync" >}}
{{< markdown >}}
```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def process_tile(tile: int) -> int:
    return tile * 2

@env.task
def process_all_tiles(tiles: list[int]) -> list[int]:
    results = []
    for tile in tiles:
        results.append(process_tile(tile))
    return results

@env.task
def main(n: int) -> list[int]:
    tiles = list(range(n))
    return process_all_tiles(tiles)
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2 Async" >}}
{{< markdown >}}
```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def process_tile(tile: int) -> int:
    return tile * 2

@env.task
async def process_all_tiles(tiles: list[int]) -> list[int]:
    results = []
    for tile in tiles:
        results.append(await process_tile(tile))
    return results

@env.task
async def main(n: int) -> list[int]:
    tiles = list(range(n))
    return await process_all_tiles(tiles)
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Conditional execution

{{< tabs "migration-conditional" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import conditional

@workflow
def conditional_wf(x: int) -> int:
    return (
        conditional("test")
        .if_(x > 0)
        .then(positive_task(x=x))
        .else_()
        .then(negative_task(x=x))
    )
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
@env.task
def main(x: int) -> int:
    if x > 0:
        return positive_task(x)
    else:
        return negative_task(x)
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Subworkflows to nested tasks

{{< tabs "migration-subworkflows" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
@workflow
def sub_workflow(x: int) -> int:
    a = step1(x)
    b = step2(a)
    return b

@workflow
def main_workflow(item: int) -> int:
    result = sub_workflow(x=item)
    return result
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
@env.task
def sub_task(x: int) -> int:
    a = step1(x)
    b = step2(a)
    return b

@env.task
def main(item: int) -> int:
    result = sub_task(item)
    return result
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}
