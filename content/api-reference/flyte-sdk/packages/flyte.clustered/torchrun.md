---
title: TorchRun
version: 2.5.2
variants: +flyte +union
layout: py_api
---

# TorchRun

**Package:** `flyte.clustered`

TorchRun launcher configuration for a ClusteredTaskEnvironment.



## Parameters

```python
class TorchRun(
    rdzv_backend: Literal['static', 'c10d'],
    max_restarts: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `rdzv_backend` | `Literal['static', 'c10d']` | Rendezvous backend. "static" (default) relies on JobSet-level restarts; "c10d" enables in-job elastic recovery via a TCPStore on rank-0. |
| `max_restarts` | `int` | In-pod torchrun restarts before the pod itself fails. Distinct from JobSet-level max_restarts on ClusterFailurePolicy. |

