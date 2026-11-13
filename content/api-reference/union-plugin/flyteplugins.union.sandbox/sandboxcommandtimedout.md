---
title: SandboxCommandTimedOut
description: "A command ran past its ``timeout`` and was stopped."
icon: exclamation-triangle
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# SandboxCommandTimedOut

**Package:** `flyteplugins.union.sandbox`

A command ran past its ``timeout`` and was stopped. A kind of
`SandboxCommandFailed`.


## Parameters

```python
class SandboxCommandTimedOut(
    message: str,
    result: object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `result` | `object` | |

