---
title: flytekit.models.admin.workflow
version: 1.16.16
variants: +flyte +byoc +selfmanaged
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

### Parameters

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
| `closure` | `None` |  |
| `id` | `None` |  |
| `is_empty` | `None` |  |
| `short_description` | `None` |  |

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

**Returns:** Workflow

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
**Returns:** flyteidl.admin.workflow_pb2.Workflow

## flytekit.models.admin.workflow.WorkflowClosure

### Parameters

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
| `compiled_workflow` | `None` |  |
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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
**Returns:** flyteidl.admin.workflow_pb2.WorkflowClosure

## flytekit.models.admin.workflow.WorkflowSpec

### Parameters

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
| `docs` | `None` |  |
| `is_empty` | `None` |  |
| `sub_workflows` | `None` |  |
| `template` | `None` |  |

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
| `pb2_object` |  | flyteidl.admin.workflow_pb2.WorkflowSpec |

**Returns:** WorkflowSpec

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
**Returns:** flyteidl.admin.workflow_pb2.WorkflowSpec

