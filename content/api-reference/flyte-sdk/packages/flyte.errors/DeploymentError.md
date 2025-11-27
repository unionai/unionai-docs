---
title: DeploymentError
version: 2.0.0b34.dev10+g162555e05
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DeploymentError

**Package:** `flyte.errors`

This error is raised when the deployment of a task fails, or some preconditions for deployment are not met.


```python
class DeploymentError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

