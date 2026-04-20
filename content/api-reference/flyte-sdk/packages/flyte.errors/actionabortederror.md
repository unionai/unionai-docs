---
title: ActionAbortedError
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# ActionAbortedError

**Package:** `flyte.errors`

This error is raised when an action was aborted, externally. The parent action will raise this error.


## Parameters

```python
class ActionAbortedError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

