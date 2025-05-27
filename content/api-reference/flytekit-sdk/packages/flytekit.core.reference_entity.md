---
title: flytekit.core.reference_entity
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.reference_entity

## Directory

### Classes

| Class | Description |
|-|-|
| [`LaunchPlanReference`](.././flytekit.core.reference_entity#flytekitcorereference_entitylaunchplanreference) | A reference object containing metadata that points to a remote launch plan. |
| [`Reference`](.././flytekit.core.reference_entity#flytekitcorereference_entityreference) |  |
| [`ReferenceEntity`](.././flytekit.core.reference_entity#flytekitcorereference_entityreferenceentity) |  |
| [`ReferenceSpec`](.././flytekit.core.reference_entity#flytekitcorereference_entityreferencespec) |  |
| [`ReferenceTemplate`](.././flytekit.core.reference_entity#flytekitcorereference_entityreferencetemplate) |  |
| [`TaskReference`](.././flytekit.core.reference_entity#flytekitcorereference_entitytaskreference) | A reference object containing metadata that points to a remote task. |
| [`WorkflowReference`](.././flytekit.core.reference_entity#flytekitcorereference_entityworkflowreference) | A reference object containing metadata that points to a remote workflow. |

## flytekit.core.reference_entity.LaunchPlanReference

A reference object containing metadata that points to a remote launch plan.


```python
class LaunchPlanReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

## flytekit.core.reference_entity.Reference

```python
class Reference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

## flytekit.core.reference_entity.ReferenceEntity

```python
class ReferenceEntity(
    reference: typing.Union[flytekit.core.reference_entity.WorkflowReference, flytekit.core.reference_entity.TaskReference, flytekit.core.reference_entity.LaunchPlanReference],
    inputs: typing.Dict[str, typing.Type],
    outputs: typing.Dict[str, typing.Type],
)
```
| Parameter | Type |
|-|-|
| `reference` | `typing.Union[flytekit.core.reference_entity.WorkflowReference, flytekit.core.reference_entity.TaskReference, flytekit.core.reference_entity.LaunchPlanReference]` |
| `inputs` | `typing.Dict[str, typing.Type]` |
| `outputs` | `typing.Dict[str, typing.Type]` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task. |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Please see the local_execute comments in the main task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### unwrap_literal_map_and_execute()

```python
def unwrap_literal_map_and_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Please see the implementation of the dispatch_execute function in the real task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `interface` |  |  |
| `name` |  |  |
| `python_interface` |  |  |
| `reference` |  |  |

## flytekit.core.reference_entity.ReferenceSpec

```python
class ReferenceSpec(
    template: flytekit.core.reference_entity.ReferenceTemplate,
)
```
| Parameter | Type |
|-|-|
| `template` | `flytekit.core.reference_entity.ReferenceTemplate` |

### Properties

| Property | Type | Description |
|-|-|-|
| `template` |  | {{< multiline >}}:rtype: ReferenceTemplate
{{< /multiline >}} |

## flytekit.core.reference_entity.ReferenceTemplate

```python
class ReferenceTemplate(
    id: flytekit.models.core.identifier.Identifier,
    resource_type: int,
)
```
A reference template encapsulates all the information necessary to use reference entities within other
workflows or dynamic tasks.



| Parameter | Type |
|-|-|
| `id` | `flytekit.models.core.identifier.Identifier` |
| `resource_type` | `int` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  | {{< multiline >}}User-specified information that uniquely identifies this reference.
:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `resource_type` |  | {{< multiline >}}The type of reference.
:rtype: flytekit.models.core.identifier.ResourceType
{{< /multiline >}} |

## flytekit.core.reference_entity.TaskReference

A reference object containing metadata that points to a remote task.


```python
class TaskReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

## flytekit.core.reference_entity.WorkflowReference

A reference object containing metadata that points to a remote workflow.


```python
class WorkflowReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

