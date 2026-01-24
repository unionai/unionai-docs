---
title: ActionAbortedError
version: 2.0.0b49
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ActionAbortedError

**Package:** `flyte.errors`

This error is raised when an action was aborted, externally. The parent action will raise this error.


```python
class ActionAbortedError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

