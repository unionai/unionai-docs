---
title: TraceDoesNotAllowNestedTasksError
version: 2.1.5
variants: +flyte +union
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

