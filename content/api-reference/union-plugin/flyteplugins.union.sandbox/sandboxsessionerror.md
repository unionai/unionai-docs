---
title: SandboxSessionError
description: "A sandbox session could not be started, or ended before it was ready."
icon: exclamation-triangle
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# SandboxSessionError

**Package:** `flyteplugins.union.sandbox`

A sandbox session could not be started, or ended before it was ready.
A ``flyte.errors`` *user* error: the task that started the session fails
as its own, and isn't retried as a system failure would be.


## Parameters

```python
class SandboxSessionError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

