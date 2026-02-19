---
title: WorkflowClosure
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkflowClosure

**Package:** `flytekit.models.admin.workflow`

```python
class WorkflowClosure(
    compiled_workflow,
)
```
| Parameter | Type | Description |
|-|-|-|
| `compiled_workflow` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `compiled_workflow` | `None` | :rtype: flytekit.models.core.compiler.CompiledWorkflowClosure |
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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin.workflow_pb2.WorkflowClosure


