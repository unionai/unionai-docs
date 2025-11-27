---
title: Cron
version: 2.0.0b32.dev0+g54ab96db3.d20251127
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Cron

**Package:** `flyte`

This class defines a Cron automation that can be associated with a Trigger in Flyte.
Example usage:
```python
from flyte.trigger import Trigger, Cron
my_trigger = Trigger(
    name="my_cron_trigger",
    automation=Cron("0 * * * *"),  # Runs every hour
    description="A trigger that runs every hour",
)
```


```python
class Cron(
    expression: str,
    timezone: Timezone,
)
```
| Parameter | Type | Description |
|-|-|-|
| `expression` | `str` | |
| `timezone` | `Timezone` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `timezone_expression` | `None` |  |

