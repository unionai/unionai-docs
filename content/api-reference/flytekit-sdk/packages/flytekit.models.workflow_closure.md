---
title: flytekit.models.workflow_closure
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: WorkflowClosure
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.workflow_closure_pb2.WorkflowClosure


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `tasks` |  | {{< multiline >}}:rtype: list[flytekit.models.task.TaskTemplate]
{{< /multiline >}} |
| `workflow` |  | {{< multiline >}}:rtype: flytekit.models.core.workflow.WorkflowTemplate
{{< /multiline >}} |

