---
title: NotInTaskContextError
description: "This error is raised when the user tries to access the task context outside of a task."
icon: exclamation-triangle
version: 2.6.13
variants: +flyte +union
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
    worker: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |
| `worker` | `str \| None` | |

