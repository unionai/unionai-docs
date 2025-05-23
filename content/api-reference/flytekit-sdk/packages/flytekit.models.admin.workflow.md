---
title: flytekit.models.admin.workflow
version: 0.1.dev2192+g7c539c3.d20250403
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
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `closure` |  |

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
) -> n: Workflow
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
:rtype: flyteidl.admin.workflow_pb2.Workflow


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: WorkflowClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.models.admin.workflow.WorkflowClosure

```python
class WorkflowClosure(
    compiled_workflow,
)
```
| Parameter | Type |
|-|-|
| `compiled_workflow` |  |

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
    p,
) -> e: WorkflowClosure
```
| Parameter | Type |
|-|-|
| `p` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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


| Parameter | Type |
|-|-|
| `template` | `flytekit.models.core.workflow.WorkflowTemplate` |
| `sub_workflows` | `typing.List[flytekit.models.core.workflow.WorkflowTemplate]` |
| `docs` | `typing.Optional[flytekit.models.documentation.Documentation]` |

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
) -> e: WorkflowSpec
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
:rtype: flyteidl.admin.workflow_pb2.WorkflowSpec


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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

