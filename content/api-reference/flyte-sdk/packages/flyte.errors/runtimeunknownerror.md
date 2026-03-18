---
title: RuntimeUnknownError
version: 2.0.9
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# RuntimeUnknownError

**Package:** `flyte.errors`

This error is raised when the underlying task execution fails because of an unknown error.



## Parameters

```python
class RuntimeUnknownError(
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

