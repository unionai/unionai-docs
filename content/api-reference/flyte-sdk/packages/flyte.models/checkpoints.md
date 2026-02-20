---
title: Checkpoints
version: 2.0.0b58
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Checkpoints

**Package:** `flyte.models`

A class representing the checkpoints for a task. This is used to store the checkpoints for the task execution.



```python
class Checkpoints(
    prev_checkpoint_path: str | None,
    checkpoint_path: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `prev_checkpoint_path` | `str \| None` | |
| `checkpoint_path` | `str \| None` | |

