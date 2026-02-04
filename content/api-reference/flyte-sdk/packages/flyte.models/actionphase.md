---
title: ActionPhase
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
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

Example:
    &gt;&gt;&gt; from flyte.models import ActionPhase
    &gt;&gt;&gt; from flyte.remote import Run
    &gt;&gt;&gt;
    &gt;&gt;&gt; # Filter runs by phase
    &gt;&gt;&gt; runs = Run.listall(in_phase=(ActionPhase.SUCCEEDED, ActionPhase.FAILED))
    &gt;&gt;&gt;
    &gt;&gt;&gt; # Check if a run succeeded
    &gt;&gt;&gt; run = Run.get("my-run")
    &gt;&gt;&gt; if run.phase == ActionPhase.SUCCEEDED:
    ...     print("Success!")
    &gt;&gt;&gt;
    &gt;&gt;&gt; # Check if phase is terminal
    &gt;&gt;&gt; if run.phase.is_terminal:
    ...     print("Run completed")


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

