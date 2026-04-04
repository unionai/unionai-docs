---
title: flytekit.models.event
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.models.event

## Directory

### Classes

| Class | Description |
|-|-|
| [`TaskExecutionMetadata`](.././flytekit.models.event#flytekitmodelseventtaskexecutionmetadata) |  |

## flytekit.models.event.TaskExecutionMetadata

### Parameters

```python
class TaskExecutionMetadata(
    external_resources,
)
```
| Parameter | Type | Description |
|-|-|-|
| `external_resources` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `external_resources` | `None` |  |
| `is_empty` | `None` |  |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** TaskExecutionMetadata

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
**Returns:** flyteidl.event.TaskExecutionMetadata

