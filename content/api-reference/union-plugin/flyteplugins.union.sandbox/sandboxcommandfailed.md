---
title: SandboxCommandFailed
description: "A command run with ``sb.run(...)`` exited with a nonzero code (``check`` is on by default)."
icon: exclamation-triangle
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# SandboxCommandFailed

**Package:** `flyteplugins.union.sandbox`

A command run with ``sb.run(...)`` exited with a nonzero code (``check``
is on by default). ``.result`` is its `CommandResult`:
the exit code, stdout and stderr. A ``flyte.errors`` *user* error.


## Parameters

```python
class SandboxCommandFailed(
    message: str,
    result: object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `result` | `object` | |

