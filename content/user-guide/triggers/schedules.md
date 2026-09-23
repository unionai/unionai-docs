---
title: Schedule triggers
description: Run a task on a cron expression or a fixed interval with `flyte.Cron`, `flyte.FixedRate`, or a predefined schedule.
icon: clock
weight: 2
variants: +flyte +union
---

# Schedule triggers

A sales report should land every day at 9 AM Pacific, and the task needs to know which day it is reporting on. A cron schedule fires the run, and `flyte.TriggerTime` passes the fire time into the task:

```python
from datetime import datetime

import flyte

env = flyte.TaskEnvironment(name="reports")

daily_report = flyte.Trigger(
    "daily-report",
    flyte.Cron("0 9 * * *", timezone="America/Los_Angeles"),
    inputs={"run_at": flyte.TriggerTime},
)


@env.task(triggers=daily_report)
async def sales_report(run_at: datetime) -> str:
    # run_at is in UTC
    ...
```

Three kinds of schedule are available: a cron expression (`flyte.Cron`), a fixed interval (`flyte.FixedRate`), and predefined shortcuts such as `flyte.Trigger.daily()`. For when the first run happens after you deploy, see [When scheduled runs start](./schedule-timing).

## Fixed-rate schedules with `flyte.FixedRate`

You can define a fixed-rate schedule trigger by setting the `automation` parameter of the `flyte.Trigger` to an instance of `flyte.FixedRate`.

The `flyte.FixedRate` has the following signature:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="dummy-fixed-rate" lang="python">}}

### Examples

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-examples" lang="python">}}

## Cron schedules with `flyte.Cron`

You can define a Cron-based schedule trigger by setting the `automation` parameter to an instance of `flyte.Cron`.

The `flyte.Cron` has the following signature:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="dummy-cron" lang="python">}}

### Examples

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="cron-examples" lang="python">}}

#### Cron expressions

Here are some common cron expressions you can use:

| Expression     | Description                          |
|----------------|--------------------------------------|
| `0 0 * * *`    | Every day at midnight                |
| `0 9 * * 1-5`  | Every weekday at 9 AM                |
| `30 14 * * 6`  | Every Saturday at 2:30 PM            |
| `0 0 1 * *`    | First day of every month at midnight |
| `0 0 25 * *`   | 25th day of every month at midnight  |
| `0 0 * * 0`    | Every Sunday at midnight             |
| `*/10 * * * *` | Every 10 minutes                     |
| `0 */2 * * *`  | Every 2 hours                        |

For a full guide on Cron syntax, refer to [Crontab Guru](https://crontab.guru/).

## Predefined schedule triggers

For common scheduling needs, Flyte provides predefined trigger methods that create Cron-based schedules without requiring you to specify cron expressions manually.
These are convenient shortcuts for frequently used scheduling patterns.

### Available predefined triggers

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="predefined-available" lang="python">}}

For reference, here's what each predefined trigger is equivalent to:

```python
# These are functionally identical:
flyte.Trigger.minutely() == flyte.Trigger("minutely", flyte.Cron("* * * * *"))
flyte.Trigger.hourly() == flyte.Trigger("hourly", flyte.Cron("0 * * * *"))
flyte.Trigger.daily() == flyte.Trigger("daily", flyte.Cron("0 0 * * *"))
flyte.Trigger.weekly() == flyte.Trigger("weekly", flyte.Cron("0 0 * * 0"))
flyte.Trigger.monthly() == flyte.Trigger("monthly", flyte.Cron("0 0 1 * *"))
```

All predefined trigger methods accept the same parameters as `flyte.Trigger`, plus a `trigger_time_input_key`. For the full parameter list, see the [`Trigger` API reference](../../api-reference/flyte-sdk/flyte/trigger).

### Trigger time in predefined triggers

By default, predefined triggers will pass the execution time to the parameter `trigger_time` of type `datetime`,if that parameter exists on the task.
If no such parameter exists, the task will still be executed without error.

Optionally, you can customize the parameter name that receives the trigger execution timestamp by setting the `trigger_time_input_key` parameter (in this case the absence of this custom parameter on the task will raise an error at trigger deployment time):

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="trigger-time-input-key" lang="python">}}

## Schedule time zones

### Setting time zone for a cron schedule

Cron expressions are by default in UTC, but it's possible to specify custom time zones like so:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="timezone" lang="python">}}

The above two schedules will fire 1 minute apart, at 9 AM PT and 12:01 PM ET respectively.

### `flyte.TriggerTime` is always in UTC

The `flyte.TriggerTime` value is always in UTC. For timezone-aware logic, convert as needed:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="trigger-time-utc" lang="python">}}

### Daylight savings time behavior

When Daylight Savings Time (DST) begins and ends, it can impact when the scheduled execution begins.

On the day DST begins, time jumps from 2:00AM to 3:00AM, which means the time of 2:30AM won't exist. In this case, the trigger will not fire until the next 2:30AM, which is the next day.

On the day DST ends, the hour from 1:00AM to 2:00AM repeats, which means the time of 1:30AM will exist twice. If the schedule above was instead set for 1:30AM, it would only run once, on the first occurrence of 1:30AM.
