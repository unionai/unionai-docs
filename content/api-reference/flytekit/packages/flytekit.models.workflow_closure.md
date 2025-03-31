---
title: flytekit.models.workflow_closure
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.workflow_closure

## Directory

### Classes

| Class | Description |
|-|-|
| [`WorkflowClosure`](.././flytekit.models.workflow_closure#flytekitmodelsworkflow_closureworkflowclosure) |  |

## flytekit.models.workflow_closure.WorkflowClosure

```python
class WorkflowClosure(
    workflow,
    tasks,
)
```
| Parameter | Type |
|-|-|
| `workflow` |  |
| `tasks` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowClosure
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
| `is_empty` |  |  |
| `tasks` |  |  |
| `workflow` |  |  |

