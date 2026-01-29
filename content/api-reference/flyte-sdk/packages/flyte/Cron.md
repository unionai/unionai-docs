---
title: Cron
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Cron

**Package:** `flyte`

This class defines a Cron automation that can be associated with a Trigger in Flyte.
Example usage:
```python
my_trigger = flyte.Trigger(
    name="my_cron_trigger",
    automation=flyte.Cron("0 * * * *"),  # Runs every hour
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
| `expression` | `str` | String cron expression to trigger - Example |
| `timezone` | `Timezone` | One of Timezone values. |

## Properties

| Property | Type | Description |
|-|-|-|
| `timezone_expression` | `None` |  |

