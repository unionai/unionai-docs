---
title: ImagePullBackOffError
version: 2.0.0b32.dev0+g54ab96db3.d20251127
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ImagePullBackOffError

**Package:** `flyte.errors`

This error is raised when the image cannot be pulled.


```python
class ImagePullBackOffError(
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

