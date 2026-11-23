---
title: ClusterFailurePolicy
description: "Failure and restart policy for the JobSet as a whole."
icon: braces
version: 2.13.2
variants: +flyte +union
layout: py_api
---

# ClusterFailurePolicy

**Package:** `flyte.clustered`

Failure and restart policy for the JobSet as a whole.



## Parameters

```python
class ClusterFailurePolicy(
    max_restarts: int = 0,
    restart_on_host_maintenance: bool = False,
    resume_after_preemption: bool = False,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_restarts` | `int` | Number of times the entire JobSet may be restarted in place before the attempt fails. These restarts do not use the task's `retries`; the failed attempt does. |
| `restart_on_host_maintenance` | `bool` | When True, node evictions (DisruptionTarget condition) trigger a free restart that does not consume the max_restarts budget. Free restarts still increment `flyte.ctx().restart_attempt`. |
| `resume_after_preemption` | `bool` | When True, a gang that Kueue preempts after it started keeps its attempt and JobSet and resumes when Kueue re-admits it, so preemptions do not use the task's `retries`. Other evictions still end the attempt. `max_runtime` keeps counting while the gang waits. Save checkpoints with `flyte.ctx().checkpoint` so the work resumes where it stopped. Needs a Flyte backend v2.0.54 or later; older ones ignore it. |

