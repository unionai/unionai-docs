---
title: AppleSiliconModelNotFoundError
description: "Raised when the model an Apple Silicon workload asks the MLX daemon to serve cannot be found or loaded."
icon: exclamation-triangle
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# AppleSiliconModelNotFoundError

**Package:** `flyte.errors`

Raised when the model an Apple Silicon workload asks the MLX daemon to serve cannot be found or loaded.


## Parameters

```python
class AppleSiliconModelNotFoundError(
    message: str,
    worker: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `worker` | `str \| None` | |

