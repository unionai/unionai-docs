---
title: flytekit.models.schedule
version: 1.16.16
variants: +flyte +union
layout: py_api
---

# flytekit.models.schedule

## Directory

### Classes

| Class | Description |
|-|-|
| [`Schedule`](.././flytekit.models.schedule#flytekitmodelsscheduleschedule) |  |

## flytekit.models.schedule.Schedule

### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `cron_expression` | `None` |  |
| `cron_schedule` | `None` |  |
| `is_empty` | `None` |  |
| `kickoff_time_input_arg` | `None` |  |
| `rate` | `None` |  |
| `schedule_expression` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** Schedule

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.schedule_pb2.Schedule

