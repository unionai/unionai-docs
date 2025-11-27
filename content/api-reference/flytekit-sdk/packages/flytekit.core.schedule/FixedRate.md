---
title: FixedRate
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FixedRate

**Package:** `flytekit.core.schedule`

Use this class to schedule a fixed-rate interval for a launch plan.

```python
from datetime import timedelta

FixedRate(duration=timedelta(minutes=10))
```

See the :std:ref:`fixed rate intervals` chapter in the cookbook for additional usage examples.


```python
class FixedRate(
    duration: datetime.timedelta,
    kickoff_time_input_arg: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `duration` | `datetime.timedelta` | |
| `kickoff_time_input_arg` | `typing.Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.schedule_pb2.Schedule


## Properties

| Property | Type | Description |
|-|-|-|
| `cron_expression` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `cron_schedule` |  | {{< multiline >}}:rtype: Schedule.CronSchedule
{{< /multiline >}} |
| `is_empty` |  |  |
| `kickoff_time_input_arg` |  |  |
| `rate` |  | {{< multiline >}}:rtype: Schedule.FixedRate
{{< /multiline >}} |
| `schedule_expression` |  |  |

