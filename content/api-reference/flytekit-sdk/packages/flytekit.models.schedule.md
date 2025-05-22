---
title: flytekit.models.schedule
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.schedule

## Directory

### Classes

| Class | Description |
|-|-|
| [`Schedule`](.././flytekit.models.schedule#flytekitmodelsscheduleschedule) |  |

## flytekit.models.schedule.Schedule

```python
class Schedule(
    kickoff_time_input_arg,
    cron_expression,
    rate,
    cron_schedule,
)
```
One of cron_expression or fixed rate must be specified.



| Parameter | Type |
|-|-|
| `kickoff_time_input_arg` |  |
| `cron_expression` |  |
| `rate` |  |
| `cron_schedule` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Schedule
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.schedule_pb2.Schedule


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

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

