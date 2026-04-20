---
title: TraceDoesNotAllowNestedTasksError
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# TraceDoesNotAllowNestedTasksError

**Package:** `flyte.errors`

This error is raised when the user tries to use a task from within a trace. Tasks can be nested under tasks
not traces.


## Parameters

```python
class TraceDoesNotAllowNestedTasksError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

