---
title: OnSchedule
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OnSchedule

**Package:** `flytekit.core.schedule`

```python
class OnSchedule(
    schedule: typing.Union[flytekit.core.schedule.CronSchedule, flytekit.core.schedule.FixedRate],
)
```
| Parameter | Type | Description |
|-|-|-|
| `schedule` | `typing.Union[flytekit.core.schedule.CronSchedule, flytekit.core.schedule.FixedRate]` | |

## Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### to_flyte_idl()

```python
def to_flyte_idl()
```
