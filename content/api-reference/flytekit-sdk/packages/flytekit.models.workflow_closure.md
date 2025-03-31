---
title: flytekit.models.workflow_closure
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.workflow_closure

## Directory

### Classes

| Class | Description |
|-|-|
| [`WorkflowClosure`](.././flytekit.models.workflow_closure#flytekitmodelsworkflow_closureworkflowclosure) | None. |

## flytekit.models.workflow_closure.WorkflowClosure

```python
def WorkflowClosure(
    workflow,
    tasks,
):
```
| Parameter | Type |
|-|-|
| `workflow` |  |
| `tasks` |  |

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
| is_empty |  |  |
| tasks |  |  |
| workflow |  |  |

