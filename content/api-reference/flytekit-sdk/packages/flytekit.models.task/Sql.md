---
title: Sql
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Sql

**Package:** `flytekit.models.task`

```python
class Sql(
    statement: str,
    dialect: int,
)
```
This defines a kubernetes pod target. It will build the pod target during task execution


| Parameter | Type | Description |
|-|-|-|
| `statement` | `str` | |
| `dialect` | `int` | |

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
    pb2_object: flyteidl.core.tasks_pb2.Sql,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.Sql` | |

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
## Properties

| Property | Type | Description |
|-|-|-|
| `dialect` |  |  |
| `is_empty` |  |  |
| `statement` |  |  |

