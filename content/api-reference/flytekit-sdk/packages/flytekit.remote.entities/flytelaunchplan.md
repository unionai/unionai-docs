---
title: FlyteLaunchPlan
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteLaunchPlan

**Package:** `flytekit.remote.entities`

A class encapsulating a remote Flyte launch plan.


```python
class FlyteLaunchPlan(
    id,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `annotations` | `None` | The annotations to execute the workflow with :rtype: flytekit.models.common.Annotations |
| `auth_role` | `None` | The authorization method with which to execute the workflow. :rtype: flytekit.models.common.AuthRole |
| `concurrency_policy` | `None` | Concurrency settings for the launch plan. :rtype: flytekit.models.concurrency.ConcurrencyPolicy |
| `default_inputs` | `None` | Input values to be passed for the execution :rtype: flytekit.models.interface.ParameterMap |
| `entity_metadata` | `None` | :rtype: LaunchPlanMetadata |
| `entity_type_text` | `None` |  |
| `fixed_inputs` | `None` | Fixed, non-overridable inputs for the Launch Plan :rtype: flytekit.models.literals.LiteralMap |
| `flyte_workflow` | `None` |  |
| `id` | `None` |  |
| `interface` | `None` | The interface is not technically part of the admin.LaunchPlanSpec in the IDL, however the workflow ID is, and from the workflow ID, fetch will fill in the interface. This is nice because then you can __call__ the= object and get a node. |
| `is_empty` | `None` |  |
| `is_scheduled` | `None` |  |
| `labels` | `None` | The labels to execute the workflow with :rtype: flytekit.models.common.Labels |
| `max_parallelism` | `None` |  |
| `name` | `None` |  |
| `overwrite_cache` | `None` |  |
| `python_interface` | `None` |  |
| `raw_output_data_config` | `None` | Where to store offloaded data like Blobs and Schemas :rtype: flytekit.models.common.RawOutputDataConfig |
| `resource_type` | `None` |  |
| `security_context` | `None` |  |
| `workflow_id` | `None` | Unique identifier for the workflow in question :rtype: flytekit.models.core.identifier.Identifier |

## Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`execute()`](#execute) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### compile()

```python
def compile(
    ctx: FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` |  | |

### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
### promote_from_model()

```python
def promote_from_model(
    id: id_models.Identifier,
    model: _launch_plan_models.LaunchPlanSpec,
) -> FlyteLaunchPlan
```
| Parameter | Type | Description |
|-|-|-|
| `id` | `id_models.Identifier` | |
| `model` | `_launch_plan_models.LaunchPlanSpec` | |

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
:rtype: flyteidl.admin.launch_plan_pb2.LaunchPlanSpec


