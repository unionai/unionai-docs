---
title: TraceDoesNotAllowNestedTasksError
version: 2.0.0b56
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TraceDoesNotAllowNestedTasksError

**Package:** `flyte.errors`

This error is raised when the user tries to use a task from within a trace. Tasks can be nested under tasks
not traces.



```python
class TraceDoesNotAllowNestedTasksError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

