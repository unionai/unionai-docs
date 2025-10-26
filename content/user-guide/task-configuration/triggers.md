---
title: Triggers
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

# Triggers

You can attach multiple triggers to a task if you need to run a task automatically in case of a certain event. 
Currently, we support:
* Schedule triggers - can run your tasks based on a cron expression or fixed rate.

In future, we will add support for:
* Webhook triggers - hit an API endpoint to run your task.
* Artifacts triggers - run a task when a certain artifact is produced.

## Schedule triggers

You can define a task with a trigger using Python SDK like so:

```python
import flyte
from datetime import datetime

env = flyte.TaskEnvironment(name="my_task_env")

@env.task(triggers=flyte.Trigger.hourly())  # Every hour
def example_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Task executed at {trigger_time.isoformat()} with x={x}"
```

It is possible to define triggers with custom cron expression or fixed rate interval:
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

> [!NOTE]
> Scheduler can pass execution time to your task, but you need to specify kick off time argument name in the inputs.
> In our case, it was called "start_time" so we passed `"start_time": flyte.TriggerTime` to trigger inputs.
> If your task has other arguments which doesn't have default values,
> you must provide values for those in the trigger inputs.

## Deploying a task with triggers

To deploy a task with its triggers, you can either use Flyte CLI:
```shell
flyte deploy -p <project> -d <domain> <file_with_tasks_and_triggers.py> env
```
either Python SDK:
```python
env = flyte.TaskEnvironment(name="my_task_env")

@env.task(triggers=flyte.Trigger.hourly())  # Every hour
def example_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Task executed at {trigger_time.isoformat()} with x={x}"

if __name__ == "__main__":
    flyte.init_from_config("<path_to_flyte_config.yaml>")
    flyte.deploy(env)
```
and then run it like a python script: `python3 <file.py>`

If this is not the first deployment of a task and there are already some previous versions of a task,
triggers will be automatically switched to the latest version. 
You don't need to manually remove or deactivate triggers for a previous task version if one had any!

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
You can do so by either changing `auto_activate` bool in the trigger definition and deploying again, 
either using Flyte CLI:

```shell
flyte update trigger custom_cron my_task_env.custom_task --activate --project <project> --domain <domain>
```

If you want to stop your trigger from creating new runs, you can deactivate it: 
```shell
flyte update trigger custom_cron my_task_env.custom_task --deactivate --project <project> --domain <domain>
```

You can also view your currently deployed triggers, their activity status and many other details in the Union UI console.

## Understanding trigger activation time

If you define an active trigger with a cron expression, you can immediately tell when it will run next time.
For example:
* `0 0 * * *` it will run next day at 0:00,
* `*/15 14 * * 1-5` it will run every 15th minute past hour 14 on every day-of-week from Monday through Friday.
For example, if today is Tuesday 17:35, it will run next day on Wednesday at 14:00.

If you define an active fixed rate trigger like so:
```python
custom_rate = flyte.Trigger("custom_rate",flyte.FixedRate(60)) 
```
First run will fire after 60 minutes after successful deploy of the trigger.
So if you deployed this trigger at 13:15, the first run will fire at 14:15 and so on.

If you define an inactive trigger:
```python
custom_rate = flyte.Trigger("custom_rate",flyte.FixedRate(60),auto_activate=False)
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
If now is a October 24th, 2025, trigger will wait for October 26th 10:00am and 
will create the first run at exactly 10:00am.

If you define an inactive fixed rate trigger:
```python
custom_rate_trigger = flyte.Trigger(
    "custom_rate",
    # Runs every 60 minutes starting from October 26th, 2025, 10th 10:00am
    flyte.FixedRate(60, start_time=datetime(2025, 10, 26, 10, 0, 0)),
    auto_activate=False
)
```
you can activate it later after October 26th 10:00am. 
For example, if activated on October 28th 12:35pm, 
the first run will be created at October 28th 1:00pm.
Scheduler will not create runs for times when trigger was not active and 
will use `start_time` as a reference point for calculating triggering times. 

## Deleting triggers

If you decide that you don't need a trigger anymore, you can remove the trigger from the task Python definition
and deploy the task again.
Or you can use Flyte CLI:

```shell
flyte delete trigger custom_cron my_task_env.custom_task --project <project> --domain <domain> 
```

If you need to re-create a previously deleted trigger, you can do so 

## Deploying triggers to production

We recommend that you define your triggers in code together with your tasks and deploy them together with tasks
as described in [Deploying a task with triggers](#deploying-a-task-with-triggers). 
Code is usually versioned in some some VCS(e.g. Git) and reviewed by other people.

In the Union UI console we display:
* `Owner` - who deployed the trigger last time 
* `Last updated` - who and when activated or deactivated the trigger last time. Note: If you deploy a trigger with `auto_activate=True`(default), this will match the `Owner`.
* `Last Run` - when was the last run created by this trigger.

For development and debugging purposes, you can adjust and deploy individual triggers from UI. 
This can be handy if you want to see the results quicker 
or if you don't want to re-deploy an entire task environment. 
