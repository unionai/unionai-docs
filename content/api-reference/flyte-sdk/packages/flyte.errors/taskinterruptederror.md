---
title: TaskInterruptedError
version: 2.2.2
variants: +flyte +union
layout: py_api
---

# TaskInterruptedError

**Package:** `flyte.errors`

This error is raised when the underlying task execution is interrupted.


## Parameters

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

