---
title: flytekit.models.admin.workflow
version: 1.16.10
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


### Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: WorkflowClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `is_empty` |  |  |
| `short_description` |  | {{< multiline >}}:rtype: str
{{< /multiline >}} |

## flytekit.models.admin.workflow.WorkflowClosure

```python
class WorkflowClosure(
    compiled_workflow,
)
```
| Parameter | Type | Description |
|-|-|-|
| `compiled_workflow` |  | |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `compiled_workflow` |  | {{< multiline >}}:rtype: flytekit.models.core.compiler.CompiledWorkflowClosure
{{< /multiline >}} |
| `is_empty` |  |  |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `docs` |  | {{< multiline >}}:rtype: Description entity for the workflow
{{< /multiline >}} |
| `is_empty` |  |  |
| `sub_workflows` |  | {{< multiline >}}:rtype: list[flytekit.models.core.workflow.WorkflowTemplate]
{{< /multiline >}} |
| `template` |  | {{< multiline >}}:rtype: flytekit.models.core.workflow.WorkflowTemplate
{{< /multiline >}} |

