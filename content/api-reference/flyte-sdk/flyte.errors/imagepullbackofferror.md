---
title: ImagePullBackOffError
version: 2.6.5
variants: +flyte +union
layout: py_api
---

# ImagePullBackOffError

**Package:** `flyte.errors`

This error is raised when the image cannot be pulled.


## Parameters

```python
class ImagePullBackOffError(
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

