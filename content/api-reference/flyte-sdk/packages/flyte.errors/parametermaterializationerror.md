---
title: ParameterMaterializationError
version: 2.0.10
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# ParameterMaterializationError

**Package:** `flyte.errors`

This error is raised when the user tries to use a Parameter in an App, that has delayed Materialization,
but the materialization fails.



## Parameters

```python
class ParameterMaterializationError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

