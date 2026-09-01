---
title: SyncTaskCallInAsyncContextError
description: "This error is raised when a sync task is invoked in a blocking way (`task(...)`) from inside an async task."
icon: exclamation-triangle
version: 2.6.13
variants: +flyte +union
layout: py_api
---

# SyncTaskCallInAsyncContextError

**Package:** `flyte.errors`

This error is raised when a sync task is invoked in a blocking way (`task(...)`) from inside an async
task. That call would block the event loop that drives the parent task — the same loop the runtime uses
to watch the controller for failures — so a controller/informer outage would leave the process stuck
forever. Use `await task.aio(...)` instead.


## Parameters

```python
class SyncTaskCallInAsyncContextError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

