---
title: OnlyAsyncIOSupportedError
version: 2.0.0b47
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OnlyAsyncIOSupportedError

**Package:** `flyte.errors`

This error is raised when the user tries to use sync IO in an async task.


```python
class OnlyAsyncIOSupportedError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

