---
title: SQLite3TaskExecutor
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SQLite3TaskExecutor

**Package:** `flytekit.extras.sqlite3.task`

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
  {{< py_class_ref flytekit.extras.sqlite3.task.SQLite3Task >}} task.
* Task resolvers, because task resolvers are instances of {{< py_class_ref flytekit.core.python_auto_container.TaskResolverMixin >}}
  classes, not the classes themselves, which means we need to look on the left hand side of them to see how to
  find them at task execution time.


```python
class SQLite3TaskExecutor(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

## Methods

| Method | Description |
|-|-|
| [`execute_from_model()`](#execute_from_model) | This function must be overridden and is where all the business logic for running a task should live. |
| [`find_lhs()`](#find_lhs) |  |


### execute_from_model()

```python
def execute_from_model(
    tt: flytekit.models.task.TaskTemplate,
    kwargs,
) -> typing.Any
```
This function must be overridden and is where all the business logic for running a task should live. Keep in
mind that you're only working with the ``TaskTemplate``. You won't have access to any information in the task
that wasn't serialized into the template.



| Parameter | Type | Description |
|-|-|-|
| `tt` | `flytekit.models.task.TaskTemplate` | This is the template, the serialized form of the task. |
| `kwargs` | `**kwargs` | These are the Python native input values to the task. :return: Python native output values from the task. |

### find_lhs()

```python
def find_lhs()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` |  |  |
| `lhs` |  |  |
| `location` |  |  |

