---
title: RuntimeDataValidationError
version: 2.0.0b44
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RuntimeDataValidationError

**Package:** `flyte.errors`

This error is raised when the user tries to access a resource that does not exist or is invalid.


```python
class RuntimeDataValidationError(
    var: str,
    e: Exception | str,
    task_name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `var` | `str` | |
| `e` | `Exception \| str` | |
| `task_name` | `str` | |

