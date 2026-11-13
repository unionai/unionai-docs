---
title: SandboxSessionEnded
description: "A call into a sandbox failed because its session has ended: its microVM was lost (e.g. its node restarted), it ran past its maximum duration, or it was aborted."
icon: exclamation-triangle
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# SandboxSessionEnded

**Package:** `flyteplugins.union.sandbox`

A call into a sandbox failed because its session has ended: its
microVM was lost (e.g. its node restarted), it ran past its maximum
duration, or it was aborted. The message says which. A kind of
`SandboxSessionError`.


## Parameters

```python
class SandboxSessionEnded(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

