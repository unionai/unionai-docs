---
title: AppleSiliconError
description: "Base class for errors of the devbox-local Apple Silicon accelerator, requested with `flyte.Resources(gpu=\"AppleSilicon\")`."
icon: exclamation-triangle
version: 2.12.1
variants: +flyte +union
layout: py_api
---

# AppleSiliconError

**Package:** `flyte.errors`

Base class for errors of the devbox-local Apple Silicon accelerator, requested with
`flyte.Resources(gpu="AppleSilicon")`. Each subclass carries one of the named codes in
`APPLE_SILICON_ERRORS_BY_CODE`, so a workload that cannot get the Mac's Metal GPU fails with the reason rather than
falling back to the CPU. `recoverable` says whether retrying the workload can help.


## Parameters

```python
class AppleSiliconError(
    message: str,
    worker: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `worker` | `str \| None` | |

