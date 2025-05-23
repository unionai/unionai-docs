---
title: union.map
version: 0.1.171.dev4+g052020f1.d20250404
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



| Parameter | Type |
|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')]` |
| `bound_inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` |
| `concurrency` | `typing.Optional[int]` |
| `min_successes` | `typing.Optional[int]` |
| `min_success_ratio` | `float` |
| `kwargs` | ``**kwargs`` |

