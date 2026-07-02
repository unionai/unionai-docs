---
title: ClusterFailurePolicy
version: 2.5.7
variants: +flyte +union
layout: py_api
---

# ClusterFailurePolicy

**Package:** `flyte.clustered`

Failure and restart policy for the JobSet as a whole.



## Parameters

```python
class ClusterFailurePolicy(
    max_restarts: int,
    restart_on_host_maintenance: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_restarts` | `int` | Number of times the entire JobSet may be restarted before Flyte surfaces a RetryableFailure. |
| `restart_on_host_maintenance` | `bool` | When True, node evictions (DisruptionTarget condition) trigger a free restart that does not consume the max_restarts budget. |

