---
title: RuntimeSystemError
version: 2.0.0b46
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RuntimeSystemError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails because of a system error. This could be a bug in the
Union system or a bug in the user's code.


```python
class RuntimeSystemError(
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

