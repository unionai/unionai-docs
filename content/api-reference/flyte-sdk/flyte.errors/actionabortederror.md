---
title: ActionAbortedError
description: "This error is raised when an action was aborted, externally."
icon: exclamation-triangle
version: 2.6.13
variants: +flyte +union
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

