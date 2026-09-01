---
title: RuntimeUserError
description: "This error is raised when the underlying task execution fails because of an error in the user's code."
icon: exclamation-triangle
version: 2.6.13
variants: +flyte +union
layout: py_api
---

# RuntimeUserError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails because of an error in the user's code.


## Parameters

```python
class RuntimeUserError(
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

