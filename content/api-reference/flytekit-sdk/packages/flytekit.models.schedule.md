---
title: flytekit.models.schedule
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.schedule

## Directory

### Classes

| Class | Description |
|-|-|
| [`Schedule`](.././flytekit.models.schedule#flytekitmodelsscheduleschedule) | None. |

## flytekit.models.schedule.Schedule

```python
def Schedule(
    kickoff_time_input_arg,
    cron_expression,
    rate,
    cron_schedule,
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| cron_expression |  |  |
| cron_schedule |  |  |
| is_empty |  |  |
| kickoff_time_input_arg |  |  |
| rate |  |  |
| schedule_expression |  |  |

