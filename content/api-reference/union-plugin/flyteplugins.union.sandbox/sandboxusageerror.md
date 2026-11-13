---
title: SandboxUsageError
description: "A sandbox session was used in a way that can't work: started outside a task, with a flyte that has no sessions, or used after its ``async with`` block ended."
icon: exclamation-triangle
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# SandboxUsageError

**Package:** `flyteplugins.union.sandbox`

A sandbox session was used in a way that can't work: started outside a
task, with a flyte that has no sessions, or used after its ``async with``
block ended. A ``flyte.errors`` *user* error.


## Parameters

```python
class SandboxUsageError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

