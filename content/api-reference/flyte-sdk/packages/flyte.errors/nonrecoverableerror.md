---
title: NonRecoverableError
version: 2.0.7
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# NonRecoverableError

**Package:** `flyte.errors`

Raised when an error is encountered that is not recoverable. Retries are irrelevant.



```python
class NonRecoverableError(
    message: str,
    code: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `code` | `str` | |

