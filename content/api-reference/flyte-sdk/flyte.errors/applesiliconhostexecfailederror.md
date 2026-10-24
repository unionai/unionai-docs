---
title: AppleSiliconHostExecFailedError
description: "Raised when an Apple Silicon workload could not run on the Mac: its environment could not be built (e.g. `uv` is missing, or a package has no macOS wheel), its entrypoint could not start, or the bridge refused it."
icon: exclamation-triangle
version: 2.12.1
variants: +flyte +union
layout: py_api
---

# AppleSiliconHostExecFailedError

**Package:** `flyte.errors`

Raised when an Apple Silicon workload could not run on the Mac: its environment could not be built (e.g. `uv` is
missing, or a package has no macOS wheel), its entrypoint could not start, or the bridge refused it.


## Parameters

```python
class AppleSiliconHostExecFailedError(
    message: str,
    worker: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `worker` | `str \| None` | |

