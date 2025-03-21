---
title: flytekit.models.admin.workflow
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.admin.workflow

## Directory

### Classes

| Class | Description |
|-|-|
| [`Documentation`](.././flytekit.models.admin.workflow#flytekitmodelsadminworkflowdocumentation) | DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`Workflow`](.././flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflow) | None. |
| [`WorkflowClosure`](.././flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowclosure) | None. |
| [`WorkflowSpec`](.././flytekit.models.admin.workflow#flytekitmodelsadminworkflowworkflowspec) | None. |

## flytekit.models.admin.workflow.Documentation

DescriptionEntity contains detailed description for the task/workflow/launch plan.
Documentation could provide insight into the algorithms, business use case, etc.


```python
def Documentation(
    short_description: typing.Optional[str],
    long_description: typing.Optional[flytekit.models.documentation.Description],
    source_code: typing.Optional[flytekit.models.documentation.SourceCode],
):
```
| Parameter | Type |
|-|-|
| `short_description` | `typing.Optional[str]` |
| `long_description` | `typing.Optional[flytekit.models.documentation.Description]` |
| `source_code` | `typing.Optional[flytekit.models.documentation.SourceCode]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.description_entity_pb2.DescriptionEntity,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.DescriptionEntity` |

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

## flytekit.models.admin.workflow.Workflow

```python
def Workflow(
    id,
    closure,
):
```
| Parameter | Type |
|-|-|
| `id` |  |
| `closure` |  |

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
| closure |  |  |
| id |  |  |
| is_empty |  |  |

## flytekit.models.admin.workflow.WorkflowClosure

```python
def WorkflowClosure(
    compiled_workflow,
):
```
| Parameter | Type |
|-|-|
| `compiled_workflow` |  |

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
    p,
):
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
| compiled_workflow |  |  |
| is_empty |  |  |

## flytekit.models.admin.workflow.WorkflowSpec

```python
def WorkflowSpec(
    template: flytekit.models.core.workflow.WorkflowTemplate,
    sub_workflows: typing.List[flytekit.models.core.workflow.WorkflowTemplate],
    docs: typing.Optional[flytekit.models.documentation.Documentation],
):
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
| docs |  |  |
| is_empty |  |  |
| sub_workflows |  |  |
| template |  |  |

