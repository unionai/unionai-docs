---
title: ActionPhase
version: 2.0.11
variants: +flyte +union
layout: py_api
---

# ActionPhase

**Package:** `flyte.models`

Represents the execution phase of a Flyte action (run).

Actions progress through different phases during their lifecycle:
- Queued: Action is waiting to be scheduled
- Waiting for resources: Action is waiting for compute resources
- Initializing: Action is being initialized
- Running: Action is currently executing
- Succeeded: Action completed successfully
- Failed: Action failed during execution
- Aborted: Action was manually aborted
- Timed out: Action exceeded its timeout limit

This enum can be used for filtering runs and checking execution status.



## Parameters

```python
class ActionPhase(
    args,
    kwds,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwds` |  | |

