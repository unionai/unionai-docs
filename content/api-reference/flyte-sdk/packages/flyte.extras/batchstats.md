---
title: BatchStats
version: 2.1.2.dev2+g62f55b516
variants: +flyte +union
layout: py_api
---

# BatchStats

**Package:** `flyte.extras`

Monitoring statistics exposed by `DynamicBatcher.stats`.



## Parameters

```python
class BatchStats(
    total_submitted: int,
    total_completed: int,
    total_batches: int,
    total_batch_cost: int,
    avg_batch_size: float,
    avg_batch_cost: float,
    busy_time_s: float,
    idle_time_s: float,
)
```
| Parameter | Type | Description |
|-|-|-|
| `total_submitted` | `int` | Total records submitted via `submit`. |
| `total_completed` | `int` | Total records whose futures have been resolved. |
| `total_batches` | `int` | Number of batches dispatched. |
| `total_batch_cost` | `int` | Sum of estimated cost across all batches. |
| `avg_batch_size` | `float` | Running average records per batch. |
| `avg_batch_cost` | `float` | Running average cost per batch. |
| `busy_time_s` | `float` | Cumulative seconds spent inside `process_fn`. |
| `idle_time_s` | `float` | Cumulative seconds the processing loop waited for a batch to be assembled. |

## Properties

| Property | Type | Description |
|-|-|-|
| `utilization` | `None` | Fraction of wall-clock time spent processing (0.0-1.0). |

