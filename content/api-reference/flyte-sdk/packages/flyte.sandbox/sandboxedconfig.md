---
title: SandboxedConfig
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# SandboxedConfig

**Package:** `flyte.sandbox`

Configuration for a sandboxed task executed via Monty.


## Parameters

```python
class SandboxedConfig(
    max_memory: int,
    max_stack_depth: int,
    timeout_ms: int,
    type_check: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_memory` | `int` | |
| `max_stack_depth` | `int` | |
| `timeout_ms` | `int` | |
| `type_check` | `bool` | |

