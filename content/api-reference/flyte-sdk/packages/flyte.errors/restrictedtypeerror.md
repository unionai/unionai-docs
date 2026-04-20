---
title: RestrictedTypeError
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# RestrictedTypeError

**Package:** `flyte.errors`

This error is raised when the user uses a restricted type, for example current a Tuple is not supported for one
 value.


## Parameters

```python
class RestrictedTypeError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

