---
title: CronSchedule
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CronSchedule

**Package:** `flytekit.core.schedule`

Use this when you have a launch plan that you want to run on a cron expression.
This uses standard [`cron format`](https://docs.flyte.org/en/latest/concepts/schedules.html#cron-expression-table)
in case where you are using default native scheduler using the schedule attribute.

```

    CronSchedule(
        schedule="*/1 * * * *",  # Following schedule runs every min
    )
```

See the :std:ref:`User Guide <cookbook:cron schedules>` for further examples.


```python
class CronSchedule(
    cron_expression: typing.Optional[str],
    schedule: typing.Optional[str],
    offset: typing.Optional[str],
    kickoff_time_input_arg: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `cron_expression` | `typing.Optional[str]` | |
| `schedule` | `typing.Optional[str]` | |
| `offset` | `typing.Optional[str]` | |
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

