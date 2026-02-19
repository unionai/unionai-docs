---
title: SleepCondition
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SleepCondition

**Package:** `flytekit.models.core.workflow`

```python
class SleepCondition(
    duration: datetime.timedelta,
)
```
A sleep condition.


| Parameter | Type | Description |
|-|-|-|
| `duration` | `datetime.timedelta` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `duration` | `None` |  |
| `is_empty` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.workflow_pb2.SignalCondition,
) -> SleepCondition
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.workflow_pb2.SignalCondition` | |

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
