---
title: AppleSiliconDaemonOOMError
description: "Raised when the host process of an Apple Silicon workload (its code, or its MLX daemon) is killed for running out of memory."
icon: exclamation-triangle
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# AppleSiliconDaemonOOMError

**Package:** `flyte.errors`

Raised when the host process of an Apple Silicon workload (its code, or its MLX daemon) is killed for running out
of memory.


## Parameters

```python
class AppleSiliconDaemonOOMError(
    message: str,
    worker: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `worker` | `str \| None` | |

