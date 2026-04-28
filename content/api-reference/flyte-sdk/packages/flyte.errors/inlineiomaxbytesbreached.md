---
title: InlineIOMaxBytesBreached
version: 2.2.0
variants: +flyte +union
layout: py_api
---

# InlineIOMaxBytesBreached

**Package:** `flyte.errors`

This error is raised when the inline IO max bytes limit is breached.
This can be adjusted per task by setting max_inline_io_bytes in the task definition.


## Parameters

```python
class InlineIOMaxBytesBreached(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

