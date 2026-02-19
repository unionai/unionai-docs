---
title: ShimTaskExecutor
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ShimTaskExecutor

**Package:** `flytekit.core.shim_task`

```python
class ShimTaskExecutor(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` | `None` |  |
| `lhs` | `None` |  |
| `location` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`execute_from_model()`](#execute_from_model) | This function must be overridden and is where all the business logic for running a task should live. |
| [`find_lhs()`](#find_lhs) |  |


### execute_from_model()

```python
def execute_from_model(
    tt: _task_model.TaskTemplate,
    kwargs,
) -> Any
```
This function must be overridden and is where all the business logic for running a task should live. Keep in
mind that you're only working with the ``TaskTemplate``. You won't have access to any information in the task
that wasn't serialized into the template.



| Parameter | Type | Description |
|-|-|-|
| `tt` | `_task_model.TaskTemplate` | This is the template, the serialized form of the task. |
| `kwargs` | `**kwargs` | These are the Python native input values to the task. :return: Python native output values from the task. |

### find_lhs()

```python
def find_lhs()
```
