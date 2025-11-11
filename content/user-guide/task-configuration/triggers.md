---
title: Triggers
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

# Triggers

Triggers allow you to automate (i.e. schedule) and parameterize (i.e. override inputs) for your executions.

Currently, we support:
* Schedule triggers - run tasks based on a cron expression or fixed rate schedule.

In the future, we will add support for:
* Webhook triggers - hit an API endpoint to run your task.
* Artifact triggers - run a task when a certain artifact is produced.

## Schedules

You can define a task with a trigger using the Python SDK like so:

```python
import flyte
from datetime import datetime

env = flyte.TaskEnvironment(name="my_task_env")

@env.task(triggers=flyte.Trigger.hourly())  # Every hour
def example_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Task executed at {trigger_time.isoformat()} with x={x}"
```

It is possible to define triggers with a custom cron expression or a fixed rate interval, and to specify inputs which will be used for triggered executions:
```python
custom_cron_trigger = flyte.Trigger(
    "custom_cron",
    flyte.Cron("0 0 * * *"),  # Runs every day
    inputs={"start_time": flyte.TriggerTime, "x": 1},
)

custom_rate_trigger = flyte.Trigger(
    "custom_rate",
    flyte.FixedRate(90),  # Runs every 90 minutes
    inputs={"start_time": flyte.TriggerTime, "x": 1},
)

# You can attach multiple triggers to the same task
@env.task(triggers=(custom_cron_trigger, custom_rate_trigger))
def custom_task(start_time: datetime, x: int) -> str:
    return f"Custom task executed at {start_time.isoformat()} with x={x}"
```


It's possible to pass the trigger invocation timestamp to the task.
In the above example, we specified `"start_time": flyte.TriggerTime` in the trigger inputs.
> [!NOTE]
> If your task has other arguments which don't have default values,
> you must provide values for those in the trigger inputs.

You can also override many other fields in the trigger definition that will be used
in the triggered task pod:
```python
custom_cron_trigger = flyte.Trigger(
    "custom_cron",
    flyte.Cron("0 0 * * *"),
    env_vars={"LOG_LEVEL": "DEBUG"},                # Environment variables
    labels={"app": "my-app"},                       # Custom pod labels
    annotations={"deployed_by": "john.foo@bar.com"},# Custom pod annotations
    interruptible=True,                             # Whether triggered task can be interrupted
    overwrite_cache=True,                           # Whether to recompute outputs for triggered task run and overwrite any existing cache.
    queue="prod-queue",                             # The specific cluster that this action should be executed on
)
```

## Deploying a task with triggers

To deploy a task with its triggers, you can either use Flyte CLI:

```shell
flyte deploy -p <project> -d <domain> <file_with_tasks_and_triggers.py> env
```

Or the Python SDK, by running the script below: `python3 <file.py>`

```python
env = flyte.TaskEnvironment(name="my_task_env")

@env.task(triggers=flyte.Trigger.hourly())  # Every hour
def example_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Task executed at {trigger_time.isoformat()} with x={x}"

if __name__ == "__main__":
    flyte.init_from_config("<path_to_flyte_config.yaml>")
    flyte.deploy(env)
```

Upon deploy, all triggers that are associated with the task will be automatically switched to the latest task version. Triggers which are defined elsewhere (i.e. in the UI) will be deleted unless they have been referenced in the task definition.

## Activating and deactivating triggers

When you deploy a task definition like those above, the corresponding triggers will be active immediately
after deploy and will create runs as soon as the next scheduled time comes.
It is possible to define triggers that are not immediately active:

```python
env = flyte.TaskEnvironment(name="my_task_env")

custom_cron_trigger = flyte.Trigger(
    "custom_cron",
    flyte.Cron("0 0 * * *"),
    auto_activate=False # Dont create runs yet
)

@env.task(triggers=custom_cron_trigger)
def custom_task() -> str:
    return "Hello, world!"
```

This trigger won't create runs until it is explicitly activated.
You can activate a trigger via the Flyte CLI:

```shell
flyte update trigger custom_cron my_task_env.custom_task --activate --project <project> --domain <domain>
```

If you want to stop your trigger from creating new runs, you can deactivate it:
```shell
flyte update trigger custom_cron my_task_env.custom_task --deactivate --project <project> --domain <domain>
```

You can also view and manage your deployed triggers in the Union UI.

## Understanding trigger activation time

If you define a trigger with a cron expression, you can tell when it will run in the future by looking at the cron expression.
For example:
* `0 0 * * *` it will run next day at 0:00,
* `*/15 14 * * 1-5` it will run every 15th minute past hour 14 on every day-of-week from Monday through Friday.
For example, if today is Tuesday 17:35, it will run next day on Wednesday at 14:00.

If you define a fixed rate trigger like so:
```python
custom_rate = flyte.Trigger("custom_rate", flyte.FixedRate(60))
```
The first run will fire 60 minutes after successful deploy of the trigger.
So if you deployed this trigger at 13:15, the first run will fire at 14:15 and so on.

If you define an inactive trigger:
```python
custom_rate = flyte.Trigger("custom_rate", flyte.FixedRate(60), auto_activate=False)
```
But activate after about 3 hours, the first run will fire after 60 minutes after trigger activation.
If you deployed this trigger at 13:15 and activated it at 16:07, the first run will fire at 17:07.

You can explicitly define the start time for a fixed rate trigger:
```python
custom_rate_trigger = flyte.Trigger(
    "custom_rate",
    # Runs every 60 minutes starting from October 26th, 2025, 10:00am
    flyte.FixedRate(60, start_time=datetime(2025, 10, 26, 10, 0, 0)),
)
```
If you deploy this trigger on October 24th, 2025, the trigger will wait until October 26th 10:00am and will create the first run at exactly 10:00am.

You can also define an inactive fixed rate trigger:
```python
custom_rate_trigger = flyte.Trigger(
    "custom_rate",
    # Runs every 60 minutes starting from October 26th, 2025, 10:00am
    flyte.FixedRate(60, start_time=datetime(2025, 10, 26, 10, 0, 0)),
    auto_activate=False
)
```
If activated later than the `start_time`, say on October 28th 12:35pm for example, the first run will be created at October 28th at 1:00pm.
The scheduler will not create runs for times when trigger was not active and will use `start_time` as a reference point for future triggered runs.

## Deleting triggers

If you decide that you don't need a trigger anymore, you can remove the trigger from the task definition and deploy the task again.

Alternatively, you can use Flyte CLI:

```shell
flyte delete trigger custom_cron my_task_env.custom_task --project <project> --domain <domain>
```

## Deploying triggers to production

We recommend that you define your triggers in code together with your tasks and deploy them together with tasks
as described in [Deploying a task with triggers](#deploying-a-task-with-triggers).

In the Union UI we display:
* `Owner` - who last deployed the trigger
* `Last updated` - who last activated or deactivated the trigger and when. Note: If you deploy a trigger with `auto_activate=True`(default), this will match the `Owner`.
* `Last Run` - when was the last run created by this trigger.

For development and debugging purposes, you can adjust and deploy individual triggers from the UI.

## Schedule time zones

### Setting time zone for a Cron schedule

Cron expressions are by default in UTC, but it's possible to specify custom time zones like so:

```python
sf_trigger = flyte.Trigger(
    "sf_tz",
    flyte.Cron(
        "0 9 * * *", timezone="America/Los_Angeles"
    ), # Every day at 9 AM PT
    inputs={"start_time": flyte.TriggerTime, "x": 1},
)

nyc_trigger = flyte.Trigger(
    "nyc_tz",
    flyte.Cron(
        "1 12 * * *", timezone="America/New_York"
    ), # Every day at 12:01 PM ET
    inputs={"start_time": flyte.TriggerTime, "x": 1},
)
```

The above two schedules will fire 1 minute apart, at 9 AM PT and 12:01 PM ET respectively.

### Daylight Savings Time behavior

Cron expressions are by default in UTC, but it's possible to specify a custom time zone like so:

```python
cron_eastern_time = flyte.Trigger(
    "eastern_time",
    CRON_TZ=America/New_York 30 2 * * *,
)
```
The above schedule will run every day at 2:30AM in US Eastern time (America/New_York).

When Daylight Savings Time (DST) begins and ends, it can impact when the scheduled execution begins.

### Spring Forward
On the day DST begins, time jumps from 2:00AM to 3:00AM, which means the time of 2:30AM won't exist. In this case, the trigger will not fire until the next 2:30AM, which is the next day.

### Fall Back
On the day DST ends, the hour from 1:00AM to 2:00AM repeats, which means the time of 1:30AM will exist twice. If the schedule above was instead set for 1:30AM, it would only run once, on the first occurrence of 1:30AM.
