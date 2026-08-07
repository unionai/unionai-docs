---
title: SandboxedConfig
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# SandboxedConfig

**Package:** `flyte.sandbox`

Configuration for a sandboxed task executed via Monty.


## Parameters

```python
class SandboxedConfig(
    max_memory: int = 52428800,
    max_stack_depth: int = 256,
    timeout_ms: int = 30000,
    type_check: bool = True,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_memory` | `int` | |
| `max_stack_depth` | `int` | |
| `timeout_ms` | `int` | |
| `type_check` | `bool` | |

