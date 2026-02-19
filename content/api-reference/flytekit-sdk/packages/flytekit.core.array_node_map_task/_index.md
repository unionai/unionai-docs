---
title: flytekit.core.array_node_map_task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.array_node_map_task

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrayNodeMapTask`](../flytekit.core.array_node_map_task/arraynodemaptask) |  |
| [`ArrayNodeMapTaskResolver`](../flytekit.core.array_node_map_task/arraynodemaptaskresolver) | Special resolver that is used for ArrayNodeMapTasks. |

### Methods

| Method | Description |
|-|-|
| [`array_node_map_task()`](#array_node_map_task) | Map task that uses the ``ArrayNode`` construct. |
| [`map_task()`](#map_task) | Wrapper that creates a map task utilizing either the existing ArrayNodeMapTask. |


### Variables

| Property | Type | Description |
|-|-|-|
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### array_node_map_task()

```python
def array_node_map_task(
    task_function: flytekit.core.python_function_task.PythonFunctionTask,
    concurrency: typing.Optional[int],
    min_success_ratio: float,
    kwargs,
)
```
Map task that uses the ``ArrayNode`` construct..

> [!IMPORTANT]

> This is an experimental drop-in replacement for `flytekit.map_task`.



| Parameter | Type | Description |
|-|-|-|
| `task_function` | `flytekit.core.python_function_task.PythonFunctionTask` | This argument is implicitly passed and represents the repeatable function |
| `concurrency` | `typing.Optional[int]` | If specified, this limits the number of mapped tasks than can run in parallel to the given batch size. If the size of the input exceeds the concurrency value, then multiple batches will be run serially until all inputs are processed. If set to 0, this means unbounded concurrency. If left unspecified, this means the array node will inherit parallelism from the workflow |
| `min_success_ratio` | `float` | If specified, this determines the minimum fraction of total jobs which can complete successfully before terminating this task and marking it successful. |
| `kwargs` | `**kwargs` | |

#### map_task()

```python
def map_task(
    target: typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')],
    concurrency: typing.Optional[int],
    min_successes: typing.Optional[int],
    min_success_ratio: float,
    kwargs,
)
```
Wrapper that creates a map task utilizing either the existing ArrayNodeMapTask
or the drop in replacement ArrayNode implementation



| Parameter | Type | Description |
|-|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')]` | The Flyte entity of which will be mapped over |
| `concurrency` | `typing.Optional[int]` | If specified, this limits the number of mapped tasks than can run in parallel to the given batch size. If the size of the input exceeds the concurrency value, then multiple batches will be run serially until all inputs are processed. If set to 0, this means unbounded concurrency. If left unspecified, this means the array node will inherit parallelism from the workflow |
| `min_successes` | `typing.Optional[int]` | The minimum number of successful executions |
| `min_success_ratio` | `float` | The minimum ratio of successful executions |
| `kwargs` | `**kwargs` | |

