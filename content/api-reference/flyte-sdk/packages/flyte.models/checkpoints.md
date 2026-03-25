---
title: Checkpoints
version: 2.0.11
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Checkpoints

**Package:** `flyte.models`

A class representing the checkpoints for a task. This is used to store the checkpoints for the task execution.


## Parameters

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

