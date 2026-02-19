---
title: WorkflowSpec
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkflowSpec

**Package:** `flytekit.models.admin.workflow`

```python
class WorkflowSpec(
    template: flytekit.models.core.workflow.WorkflowTemplate,
    sub_workflows: typing.List[flytekit.models.core.workflow.WorkflowTemplate],
    docs: typing.Optional[flytekit.models.documentation.Documentation],
)
```
This object fully encapsulates the specification of a workflow


| Parameter | Type | Description |
|-|-|-|
| `template` | `flytekit.models.core.workflow.WorkflowTemplate` | |
| `sub_workflows` | `typing.List[flytekit.models.core.workflow.WorkflowTemplate]` | |
| `docs` | `typing.Optional[flytekit.models.documentation.Documentation]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `docs` | `None` | :rtype: Description entity for the workflow |
| `is_empty` | `None` |  |
| `sub_workflows` | `None` | :rtype: list[flytekit.models.core.workflow.WorkflowTemplate] |
| `template` | `None` | :rtype: flytekit.models.core.workflow.WorkflowTemplate |

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
| `pb2_object` |  | flyteidl.admin.workflow_pb2.WorkflowSpec :rtype: WorkflowSpec |

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
:rtype: flyteidl.admin.workflow_pb2.WorkflowSpec


