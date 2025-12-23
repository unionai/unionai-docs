---
title: FixedRate
version: 2.0.0b40
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FixedRate

**Package:** `flyte`

This class defines a FixedRate automation that can be associated with a Trigger in Flyte.
Example usage:
```python
from flyte.trigger import Trigger, FixedRate
my_trigger = Trigger(
    name="my_fixed_rate_trigger",
    automation=FixedRate(60),  # Runs every hour
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
| `interval_minutes` | `int` | |
| `start_time` | `datetime \| None` | |

