---
title: BatchStats
version: 2.0.11
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# BatchStats

**Package:** `flyte.extras`

Monitoring statistics exposed by `DynamicBatcher.stats`.

    Attributes:
        total_submitted: Total records submitted via `submit`.
        total_completed: Total records whose futures have been resolved.
        total_batches: Number of batches dispatched.
        total_batch_cost: Sum of estimated cost across all batches.
        avg_batch_size: Running average records per batch.
        avg_batch_cost: Running average cost per batch.
        busy_time_s: Cumulative seconds spent inside `process_fn`.
        idle_time_s: Cumulative seconds the processing loop waited for
            a batch to be assembled.
    


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
| `total_submitted` | `int` | |
| `total_completed` | `int` | |
| `total_batches` | `int` | |
| `total_batch_cost` | `int` | |
| `avg_batch_size` | `float` | |
| `avg_batch_cost` | `float` | |
| `busy_time_s` | `float` | |
| `idle_time_s` | `float` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `utilization` | `None` | Fraction of wall-clock time spent processing (0.0-1.0). |

