---
title: PrimaryContainerNotFoundError
version: 2.0.0b55
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PrimaryContainerNotFoundError

**Package:** `flyte.errors`

This error is raised when the primary container is not found.


```python
class PrimaryContainerNotFoundError(
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

