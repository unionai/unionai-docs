---
title: flytekit.core.array_node
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.array_node

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrayNode`](../flytekit.core.array_node/arraynode) |  |

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
)
```
ArrayNode implementation that maps over tasks and other Flyte entities



| Parameter | Type | Description |
|-|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.task.ReferenceTask, ForwardRef('FlyteLaunchPlan')]` | The target Flyte entity to map over |
| `concurrency` | `typing.Optional[int]` | If specified, this limits the number of mapped tasks than can run in parallel to the given batch size. If the size of the input exceeds the concurrency value, then multiple batches will be run serially until all inputs are processed. If set to 0, this means unbounded concurrency. If left unspecified, this means the array node will inherit parallelism from the workflow |
| `min_success_ratio` | `typing.Optional[float]` | The minimum ratio of successful executions :return: A callable function that takes in keyword arguments and returns a Promise created by flyte_entity_call_handler |
| `min_successes` | `typing.Optional[int]` | The minimum number of successful executions. If set, this takes precedence over min_success_ratio |

