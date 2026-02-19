---
title: TaskExecutionMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskExecutionMetadata

**Package:** `flytekit.models.event`

```python
class TaskExecutionMetadata(
    external_resources,
)
```
| Parameter | Type | Description |
|-|-|-|
| `external_resources` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `external_resources` | `None` | :rtype: google.protobuf.internal.containers.RepeatedCompositeFieldContainer |
| `is_empty` | `None` |  |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

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
:rtype: flyteidl.event.TaskExecutionMetadata


