---
title: NonRecoverableError
description: "Raised when an error is encountered that is not recoverable."
icon: exclamation-triangle
version: 2.6.13
variants: +flyte +union
layout: py_api
---

# NonRecoverableError

**Package:** `flyte.errors`

Raised when an error is encountered that is not recoverable. Retries are irrelevant.


## Parameters

```python
class NonRecoverableError(
    message: str,
    code: str = 'NonRecoverableError',
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `code` | `str` | |

