---
title: OOMError
version: 2.0.0b58
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OOMError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails because of an out-of-memory error.



```python
class OOMError(
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

