---
title: TaskTimeoutError
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# TaskTimeoutError

**Package:** `flyte.errors`

This error is raised when the underlying task execution runs for longer than the specified timeout.


## Parameters

```python
class TaskTimeoutError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

