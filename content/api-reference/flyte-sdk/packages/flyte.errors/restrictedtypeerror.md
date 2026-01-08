---
title: RestrictedTypeError
version: 2.0.0b46
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RestrictedTypeError

**Package:** `flyte.errors`

This error is raised when the user uses a restricted type, for example current a Tuple is not supported for one
 value.


```python
class RestrictedTypeError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

