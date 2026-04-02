---
title: NotInTaskContextError
version: 2.1.2
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# NotInTaskContextError

**Package:** `flyte.errors`

This error is raised when the user tries to access the task context outside of a task.


## Parameters

```python
class NotInTaskContextError(
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

