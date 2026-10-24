---
title: AppleSiliconDaemonStartFailedError
description: "Raised when the host-side MLX daemon serving an Apple Silicon workload in container mode fails to start."
icon: exclamation-triangle
version: 2.12.1
variants: +flyte +union
layout: py_api
---

# AppleSiliconDaemonStartFailedError

**Package:** `flyte.errors`

Raised when the host-side MLX daemon serving an Apple Silicon workload in container mode fails to start.


## Parameters

```python
class AppleSiliconDaemonStartFailedError(
    message: str,
    worker: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `worker` | `str \| None` | |

