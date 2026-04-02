---
title: NonRecoverableError
version: 2.1.3.dev1+ge23e739d5
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
    code: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `code` | `str` | |

