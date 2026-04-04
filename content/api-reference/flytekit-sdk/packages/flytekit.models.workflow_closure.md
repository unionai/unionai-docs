---
title: flytekit.models.workflow_closure
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.models.workflow_closure

## Directory

### Classes

| Class | Description |
|-|-|
| [`WorkflowClosure`](.././flytekit.models.workflow_closure#flytekitmodelsworkflow_closureworkflowclosure) |  |

## flytekit.models.workflow_closure.WorkflowClosure

### Parameters

```python
class WorkflowClosure(
    workflow,
    tasks,
)
```
| Parameter | Type | Description |
|-|-|-|
| `workflow` |  | |
| `tasks` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `tasks` | `None` |  |
| `workflow` | `None` |  |

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

**Returns:** WorkflowClosure

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
**Returns:** flyteidl.core.workflow_closure_pb2.WorkflowClosure

