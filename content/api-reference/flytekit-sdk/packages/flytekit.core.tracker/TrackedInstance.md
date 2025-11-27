---
title: TrackedInstance
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TrackedInstance

**Package:** `flytekit.core.tracker`

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
  {{< py_class_ref flytekit.extras.sqlite3.task.SQLite3Task >}} task.
* Task resolvers, because task resolvers are instances of {{< py_class_ref flytekit.core.python_auto_container.TaskResolverMixin >}}
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

## Methods

| Method | Description |
|-|-|
| [`find_lhs()`](#find_lhs) |  |


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

