---
title: BatchStats
description: "Monitoring statistics exposed by `DynamicBatcher.stats`."
icon: braces
version: 2.6.13
variants: +flyte +union
layout: py_api
---

# BatchStats

**Package:** `flyte.extras`

Monitoring statistics exposed by `DynamicBatcher.stats`.



## Parameters

```python
class BatchStats(
    total_submitted: int = 0,
    total_completed: int = 0,
    total_batches: int = 0,
    total_batch_cost: int = 0,
    avg_batch_size: float = 0.0,
    avg_batch_cost: float = 0.0,
    busy_time_s: float = 0.0,
    idle_time_s: float = 0.0,
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
| `utilization` | `float` | Fraction of wall-clock time spent processing (0.0-1.0). |

