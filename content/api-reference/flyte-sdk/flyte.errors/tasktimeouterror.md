---
title: TaskTimeoutError
description: "This error is raised when a task exceeds one of its `flyte.Timeout` bounds."
icon: exclamation-triangle
version: 2.10.4
variants: +flyte +union
layout: py_api
---

# TaskTimeoutError

**Package:** `flyte.errors`

This error is raised when a task exceeds one of its `flyte.Timeout` bounds. The subclasses
below say which bound fired; this base class is raised when the server does not report it.


## Parameters

```python
class TaskTimeoutError(
    message: str,
    code: str = 'TaskTimeoutError',
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `code` | `str` | |

