---
title: TrackedInstance
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TrackedInstance

**Package:** `flytekit.core.tracker`

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
  {{&lt; py_class_ref flytekit.extras.sqlite3.task.SQLite3Task &gt;}} task.
* Task resolvers, because task resolvers are instances of {{&lt; py_class_ref flytekit.core.python_auto_container.TaskResolverMixin &gt;}}
  classes, not the classes themselves, which means we need to look on the left hand side of them to see how to
  find them at task execution time.



```python
class TrackedInstance(
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
| [`find_lhs()`](#find_lhs) |  |


### find_lhs()

```python
def find_lhs()
```
