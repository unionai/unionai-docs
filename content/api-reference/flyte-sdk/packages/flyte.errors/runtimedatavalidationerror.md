---
title: RuntimeDataValidationError
version: 2.1.2.dev2+g62f55b516
variants: +flyte +union
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

