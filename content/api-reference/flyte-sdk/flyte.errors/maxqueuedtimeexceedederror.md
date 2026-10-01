---
title: MaxQueuedTimeExceededError
description: "This error is raised when a task waits longer than `flyte.Timeout.max_queued_time` before it starts running, e.g. because no node can satisfy its resource request."
icon: exclamation-triangle
version: 2.10.5
variants: +flyte +union
layout: py_api
---

# MaxQueuedTimeExceededError

**Package:** `flyte.errors`

This error is raised when a task waits longer than `flyte.Timeout.max_queued_time` before it
starts running, e.g. because no node can satisfy its resource request.


## Parameters

```python
class MaxQueuedTimeExceededError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

