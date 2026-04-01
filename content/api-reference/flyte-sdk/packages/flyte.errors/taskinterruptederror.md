---
title: TaskInterruptedError
version: 2.1.2.dev2+g62f55b516
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

