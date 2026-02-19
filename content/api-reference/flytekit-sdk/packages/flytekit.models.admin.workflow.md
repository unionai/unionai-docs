---
title: flytekit.models.admin.workflow
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.admin.workflow

## Directory

### Classes

| Class | Description |
|-|-|
| [`Workflow`](.././flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflow) |  |
| [`WorkflowClosure`](.././flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowclosure) |  |
| [`WorkflowSpec`](.././flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowspec) |  |

## flytekit.models.admin.workflow.Workflow

```python
class Workflow(
    id,
    closure,
    short_description,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `closure` |  | |
| `short_description` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | :rtype: WorkflowClosure |
| `id` | `None` | :rtype: flytekit.models.core.identifier.Identifier |
| `is_empty` | `None` |  |
| `short_description` | `None` | :rtype: str |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.admin.workflow_pb2.Workflow


## flytekit.models.admin.workflow.WorkflowClosure

```python
class WorkflowClosure(
    compiled_workflow,
)
```
| Parameter | Type | Description |
|-|-|-|
| `compiled_workflow` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `compiled_workflow` | `None` | :rtype: flytekit.models.core.compiler.CompiledWorkflowClosure |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin.workflow_pb2.WorkflowClosure


## flytekit.models.admin.workflow.WorkflowSpec

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

### Properties

| Property | Type | Description |
|-|-|-|
| `docs` | `None` | :rtype: Description entity for the workflow |
| `is_empty` | `None` |  |
| `sub_workflows` | `None` | :rtype: list[flytekit.models.core.workflow.WorkflowTemplate] |
| `template` | `None` | :rtype: flytekit.models.core.workflow.WorkflowTemplate |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | flyteidl.admin.workflow_pb2.WorkflowSpec :rtype: WorkflowSpec |

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
:rtype: flyteidl.admin.workflow_pb2.WorkflowSpec


