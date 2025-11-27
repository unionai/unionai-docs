---
title: TaskInterruptedError
version: 2.0.0b34.dev10+g162555e05
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskInterruptedError

**Package:** `flyte.errors`

This error is raised when the underlying task execution is interrupted.


```python
class TaskInterruptedError(
    code: str,
    message: str,
    worker: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |
| `worker` | `str \| None` | |

