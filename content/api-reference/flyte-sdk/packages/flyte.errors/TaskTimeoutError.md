---
title: TaskTimeoutError
version: 2.0.0b32.dev0+g54ab96db3.d20251127
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskTimeoutError

**Package:** `flyte.errors`

This error is raised when the underlying task execution runs for longer than the specified timeout.


```python
class TaskTimeoutError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

