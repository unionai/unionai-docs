---
title: RuntimeUserError
version: 2.0.0b34
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RuntimeUserError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails because of an error in the user's code.


```python
class RuntimeUserError(
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

