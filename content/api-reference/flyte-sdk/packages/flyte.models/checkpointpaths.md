---
title: CheckpointPaths
version: 2.1.7
variants: +flyte +union
layout: py_api
---

# CheckpointPaths

**Package:** `flyte.models`

Paths the platform provides for this task's checkpoint output and optional previous-attempt input.

This is distinct from `flyte.Checkpoint`, which performs download/upload of the checkpoint **blob**
for those paths (see `flyte.models.TaskContext.checkpoint`).


## Parameters

```python
class CheckpointPaths(
    prev_checkpoint_path: str | None,
    checkpoint_path: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `prev_checkpoint_path` | `str \| None` | |
| `checkpoint_path` | `str \| None` | |

