---
title: FixedRate
version: 2.0.11
variants: +flyte +union
layout: py_api
---

# FixedRate

**Package:** `flyte`

Fixed-rate (interval-based) automation schedule for use with `Trigger`.

Unlike `Cron`, which runs at specific clock times, `FixedRate` runs at a
consistent interval regardless of clock time.

```python
my_trigger = flyte.Trigger(
    name="my_fixed_rate_trigger",
    automation=flyte.FixedRate(60),  # Runs every 60 minutes
    description="A trigger that runs every hour",
)
```



## Parameters

```python
class FixedRate(
    interval_minutes: int,
    start_time: datetime | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `interval_minutes` | `int` | Interval between trigger activations, in minutes (e.g., `60` for hourly, `1440` for daily). |
| `start_time` | `datetime \| None` | Optional start time for the first trigger. Subsequent triggers follow the interval from this point. If not set, the first trigger occurs `interval_minutes` after deployment/activation. |

