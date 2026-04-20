---
title: DeploymentError
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# DeploymentError

**Package:** `flyte.errors`

This error is raised when the deployment of a task fails, or some preconditions for deployment are not met.


## Parameters

```python
class DeploymentError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

