---
title: union.map
version: 0.1.201
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union.map

## Directory

### Methods

| Method | Description |
|-|-|
| [`map()`](#map) | Use to map over tasks, actors, launch plans, reference tasks and launch plans, and remote tasks and. |


## Methods

#### map()

```python
def map(
    target: typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')],
    bound_inputs: typing.Optional[typing.Dict[str, typing.Any]],
    concurrency: typing.Optional[int],
    min_successes: typing.Optional[int],
    min_success_ratio: float,
    kwargs,
)
```
Use to map over tasks, actors, launch plans, reference tasks and launch plans, and remote tasks and
launch plans.



| Parameter | Type | Description |
|-|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')]` | The Flyte entity of which will be mapped over |
| `bound_inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | Inputs that are bound to the array node and will not be mapped over |
| `concurrency` | `typing.Optional[int]` | If specified, this limits the number of mapped tasks than can run in parallel to the given batch size. If the size of the input exceeds the concurrency value, then multiple batches will be run serially until all inputs are processed. If set to 0, this means unbounded concurrency. If left unspecified, this means the array node will inherit parallelism from the workflow |
| `min_successes` | `typing.Optional[int]` | The minimum number of successful executions |
| `min_success_ratio` | `float` | The minimum ratio of successful executions |
| `kwargs` | `**kwargs` | |

