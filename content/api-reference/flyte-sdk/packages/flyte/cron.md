---
title: Cron
version: 2.2.1
variants: +flyte +union
layout: py_api
---

# Cron

**Package:** `flyte`

Cron-based automation schedule for use with `Trigger`.

Cron expressions use the standard five-field format:
`minute hour day-of-month month day-of-week`

Common patterns:

- `"0 * * * *"` — every hour (at minute 0)
- `"0 0 * * *"` — daily at midnight
- `"0 0 * * 1"` — weekly on Monday at midnight
- `"0 0 1 * *"` — monthly on the 1st at midnight
- `"*/5 * * * *"` — every 5 minutes

```python
my_trigger = flyte.Trigger(
    name="my_cron_trigger",
    automation=flyte.Cron("0 * * * *"),  # Runs every hour
    description="A trigger that runs every hour",
)
```



## Parameters

```python
class Cron(
    expression: str,
    timezone: Timezone,
)
```
| Parameter | Type | Description |
|-|-|-|
| `expression` | `str` | Cron expression string (e.g., `"0 * * * *"`). |
| `timezone` | `Timezone` | Timezone for the cron schedule (default `"UTC"`). One of the standard timezone values (e.g., `"US/Eastern"`, `"Europe/London"`). Note that DST transitions may cause skipped or duplicated runs. |

## Properties

| Property | Type | Description |
|-|-|-|
| `timezone_expression` | `str` |  |

