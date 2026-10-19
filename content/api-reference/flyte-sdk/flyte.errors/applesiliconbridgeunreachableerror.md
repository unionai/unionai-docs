---
title: AppleSiliconBridgeUnreachableError
description: "Raised when a container cannot reach the devbox's host-side Apple Silicon bridge, or the bridge lost track of the workload's host process."
icon: exclamation-triangle
version: 2.12.0
variants: +flyte +union
layout: py_api
---

# AppleSiliconBridgeUnreachableError

**Package:** `flyte.errors`

Raised when a container cannot reach the devbox's host-side Apple Silicon bridge, or the bridge lost track of the
workload's host process.


## Parameters

```python
class AppleSiliconBridgeUnreachableError(
    message: str,
    worker: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `worker` | `str \| None` | |

