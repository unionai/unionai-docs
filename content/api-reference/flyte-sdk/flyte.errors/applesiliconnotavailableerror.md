---
title: AppleSiliconNotAvailableError
description: "Raised when `gpu=\"AppleSilicon\"` is requested anywhere but a devbox on an Apple Silicon Mac: another OS or architecture, a devbox started without `--apple-silicon`, or a remote cluster."
icon: exclamation-triangle
version: 2.12.1
variants: +flyte +union
layout: py_api
---

# AppleSiliconNotAvailableError

**Package:** `flyte.errors`

Raised when `gpu="AppleSilicon"` is requested anywhere but a devbox on an Apple Silicon Mac: another OS or
architecture, a devbox started without `--apple-silicon`, or a remote cluster.


## Parameters

```python
class AppleSiliconNotAvailableError(
    message: str,
    worker: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `worker` | `str \| None` | |

