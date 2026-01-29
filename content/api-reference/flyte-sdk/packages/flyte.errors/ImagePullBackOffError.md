---
title: ImagePullBackOffError
version: 2.0.0b52
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

