---
title: RuntimeDataValidationError
version: 2.0.9
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# RuntimeDataValidationError

**Package:** `flyte.errors`

This error is raised when the user tries to access a resource that does not exist or is invalid.



## Parameters

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

