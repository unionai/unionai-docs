---
title: ModuleLoadError
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# ModuleLoadError

**Package:** `flyte.errors`

This error is raised when the module cannot be loaded, either because it does not exist or because of a
 syntax error.


## Parameters

```python
class ModuleLoadError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

