---
title: SandboxedConfig
version: 2.0.9
variants: +flyte +byoc +selfmanaged
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

