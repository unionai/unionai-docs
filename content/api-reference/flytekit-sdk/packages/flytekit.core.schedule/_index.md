---
title: flytekit.core.schedule
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.schedule


These classes provide functionality related to schedules.

## Directory

### Classes

| Class | Description |
|-|-|
| [`CronSchedule`](../flytekit.core.schedule/cronschedule) | Use this when you have a launch plan that you want to run on a cron expression. |
| [`FixedRate`](../flytekit.core.schedule/fixedrate) | Use this class to schedule a fixed-rate interval for a launch plan. |
| [`OnSchedule`](../flytekit.core.schedule/onschedule) | Base class for protocol classes. |

### Protocols

| Protocol | Description |
|-|-|
| [`LaunchPlanTriggerBase`](../flytekit.core.schedule/launchplantriggerbase) | Base class for protocol classes. |

