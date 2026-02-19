---
title: Schedule
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Schedule

**Package:** `flytekit.models.schedule`

```python
class Schedule(
    kickoff_time_input_arg,
    cron_expression,
    rate,
    cron_schedule,
)
```
One of cron_expression or fixed rate must be specified.



| Parameter | Type | Description |
|-|-|-|
| `kickoff_time_input_arg` |  | |
| `cron_expression` |  | |
| `rate` |  | |
| `cron_schedule` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `cron_expression` | `None` | :rtype: Text |
| `cron_schedule` | `None` | :rtype: Schedule.CronSchedule |
| `is_empty` | `None` |  |
| `kickoff_time_input_arg` | `None` |  |
| `rate` | `None` | :rtype: Schedule.FixedRate |
| `schedule_expression` | `None` |  |

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


