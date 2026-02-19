---
title: WorkflowNode
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkflowNode

**Package:** `flytekit.models.core.workflow`

```python
class WorkflowNode(
    launchplan_ref,
    sub_workflow_ref,
)
```
Refers to a the workflow the node is to execute. One of the references must be supplied.



| Parameter | Type | Description |
|-|-|-|
| `launchplan_ref` |  | |
| `sub_workflow_ref` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `launchplan_ref` | `None` | [Optional] A globally unique identifier for the launch plan.  Should map to Admin.  :rtype: flytekit.models.core.identifier.Identifier |
| `reference` | `None` | :rtype: flytekit.models.core.identifier.Identifier |
| `sub_workflow_ref` | `None` | [Optional] Reference to a subworkflow, that should be defined with the compiler context.  :rtype: flytekit.models.core.identifier.Identifier |

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
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.core.workflow_pb2.WorkflowNode


