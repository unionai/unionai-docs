---
title: MemoryMeta
version: 2.5.2
variants: +flyte +union
layout: py_api
---

# MemoryMeta

**Package:** `flyte.ai.agents.memory`

Per-file metadata sidecar (sha256, actor, timestamp, …) for a memory entry.


## Parameters

```python
class MemoryMeta(
    path: str,
    sha256: str,
    updated_at: str,
    updated_by: str,
    reason: str,
    bytes: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `sha256` | `str` | |
| `updated_at` | `str` | |
| `updated_by` | `str` | |
| `reason` | `str` | |
| `bytes` | `int` | |

