---
title: ArrayNode
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ArrayNode

**Package:** `flytekit.core.array_node`

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
| Parameter | Type | Description |
|-|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.task.ReferenceTask, ForwardRef('FlyteLaunchPlan')]` | The target Flyte entity to map over |
| `bindings` | `typing.Optional[typing.List[flytekit.models.literals.Binding]]` | |
| `concurrency` | `typing.Optional[int]` | If specified, this limits the number of mapped tasks than can run in parallel to the given batch size. If the size of the input exceeds the concurrency value, then multiple batches will be run serially until all inputs are processed. If set to 0, this means unbounded concurrency. If left unspecified, this means the array node will inherit parallelism from the workflow |
| `min_successes` | `typing.Optional[int]` | The minimum number of successful executions. If set, this takes precedence over min_success_ratio |
| `min_success_ratio` | `typing.Optional[float]` | The minimum ratio of successful executions. |
| `metadata` | `typing.Optional[flytekit.models.core.workflow.NodeMetadata]` | The metadata for the underlying node |

## Methods

| Method | Description |
|-|-|
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


### construct_node_metadata()

```python
def construct_node_metadata()
```
### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
## Properties

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

