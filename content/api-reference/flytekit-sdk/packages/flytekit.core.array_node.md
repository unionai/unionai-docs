---
title: flytekit.core.array_node
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.array_node

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrayNode`](.././flytekit.core.array_node#flytekitcorearray_nodearraynode) |  |

### Methods

| Method | Description |
|-|-|
| [`array_node()`](#array_node) | ArrayNode implementation that maps over tasks and other Flyte entities. |


### Variables

| Property | Type | Description |
|-|-|-|
| `ARRAY_NODE_SUBNODE_NAME` | `str` |  |
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### array_node()

```python
def array_node(
    target: typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.task.ReferenceTask, ForwardRef('FlyteLaunchPlan')],
    concurrency: typing.Optional[int],
    min_success_ratio: typing.Optional[float],
    min_successes: typing.Optional[int],
) -> n: A callable function that takes in keyword arguments and returns a Promise created by
```
ArrayNode implementation that maps over tasks and other Flyte entities



| Parameter | Type |
|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.task.ReferenceTask, ForwardRef('FlyteLaunchPlan')]` |
| `concurrency` | `typing.Optional[int]` |
| `min_success_ratio` | `typing.Optional[float]` |
| `min_successes` | `typing.Optional[int]` |

## flytekit.core.array_node.ArrayNode

```python
class ArrayNode(
    target: typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.task.ReferenceTask, ForwardRef('FlyteLaunchPlan')],
    bindings: typing.Optional[typing.List[flytekit.models.literals.Binding]],
    concurrency: typing.Optional[int],
    min_successes: typing.Optional[int],
    min_success_ratio: typing.Optional[float],
    metadata: typing.Optional[flytekit.models.core.workflow.NodeMetadata],
)
```
| Parameter | Type |
|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.task.ReferenceTask, ForwardRef('FlyteLaunchPlan')]` |
| `bindings` | `typing.Optional[typing.List[flytekit.models.literals.Binding]]` |
| `concurrency` | `typing.Optional[int]` |
| `min_successes` | `typing.Optional[int]` |
| `min_success_ratio` | `typing.Optional[float]` |
| `metadata` | `typing.Optional[flytekit.models.core.workflow.NodeMetadata]` |

### Methods

| Method | Description |
|-|-|
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise]
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `bindings` |  |  |
| `bound_inputs` |  |  |
| `concurrency` |  |  |
| `data_mode` |  |  |
| `execution_mode` |  |  |
| `flyte_entity` |  |  |
| `interface` |  |  |
| `is_original_sub_node_interface` |  |  |
| `min_success_ratio` |  |  |
| `min_successes` |  |  |
| `name` |  |  |
| `python_interface` |  |  |
| `upstream_nodes` |  |  |

