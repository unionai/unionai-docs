---
title: FixedRate
version: 2.0.0b59
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FixedRate

**Package:** `flyte`

This class defines a FixedRate automation that can be associated with a Trigger in Flyte.

Example usage:
```python
my_trigger = flyte.Trigger(
    name="my_fixed_rate_trigger",
    automation=flyte.FixedRate(60),  # Runs every hour
    description="A trigger that runs every hour",
)
```



```python
class FixedRate(
    interval_minutes: int,
    start_time: datetime | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `interval_minutes` | `int` | Interval to schedule the trigger in minutes. |
| `start_time` | `datetime \| None` | Start time of the trigger. This will enable starting a trigger with fixed rate as of this time. |

