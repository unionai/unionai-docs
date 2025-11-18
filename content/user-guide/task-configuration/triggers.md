---
title: Triggers
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

# Triggers

Triggers allow you to automate and parameterize an execution by scheduling its start time and providing overrides for its task inputs.

Currently, only **schedule triggers** are supported.
This type of trigger runs a task based on a Cron expression or a fixed-rate schedule.

Support is coming for other trigger types, such as:

* Webhook triggers: Hit an API endpoint to run your task.
* Artifact triggers: Run a task when a specific artifact is produced.

## Triggers are set in the task decorator

A trigger is created by setting the `triggers` parameter in the task decorator to a `flyte.Trigger` object or a list of such objects (triggers are not settable at the `TaskEnvironment` definition or `task.override` levels).

Here is a simple example:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="simple" lang="python">}}

Here we use a predefined schedule trigger to run the `example_task` every minute.
Other predefined triggers can be used similarly (see [Predefined schedule triggers](#predefined-schedule-triggers) below).

If you want full control over the trigger behavior, you can define a trigger using the `flyte.Trigger` class directly.

## `flyte.Trigger`

The `Trigger` class allows you to define custom triggers with full control over scheduling and execution behavior. It has the following signature:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="dummy-trigger" lang="python">}}

### Core Parameters

**`name: str`** (required)
The unique identifier for the trigger within your project/domain.

**`automation: Union[Cron, FixedRate]`** (required)
Defines when the trigger fires. Use `flyte.Cron("expression")` for Cron-based scheduling or `flyte.FixedRate(interval_minutes, start_time=start_time)` for fixed intervals.

### Configuration Parameters

**`description: str = ""`**
Human-readable description of the trigger's purpose.

**`auto_activate: bool = True`**
Whether the trigger should be automatically activated when deployed. Set to `False` to deploy inactive triggers that require manual activation.

**`inputs: Dict[str, Any] | None = None`**
Default parameter values for the task when triggered. Use `flyte.TriggerTime` as a value to inject the trigger execution timestamp into that parameter.

### Runtime Override Parameters

**`env_vars: Dict[str, str] | None = None`**
Environment variables to set for triggered executions, overriding the task's default environment variables.

**`interruptible: bool | None = None`**
Whether triggered executions can be interrupted (useful for cost optimization with spot/preemptible instances). Overrides the task's interruptible setting.

**`overwrite_cache: bool = False`**
Whether to bypass/overwrite task cache for triggered executions, ensuring fresh computation.

**`queue: str | None = None`**
Specific execution queue for triggered runs, overriding the task's default queue.

### Metadata Parameters

**`labels: Mapping[str, str] | None = None`**
Key-value labels for organizing and filtering triggers (e.g., team, component, priority).

**`annotations: Mapping[str, str] | None = None`**
Additional metadata, often used by infrastructure tools for compliance, monitoring, or cost tracking.

Here's a comprehensive example showing all parameters:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="comprehensive-trigger" lang="python">}}

## The `automation` parameter with `flyte.FixedRate`

You can define a fixed-rate schedule trigger by setting the `automation` parameter of the `flyte.Trigger` to an instance of `flyte.FixedRate`.

The `flyte.FixedRate` has the following signature:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="dummy-fixed-rate" lang="python">}}

### Parameters

**`interval_minutes: int`** (required)
The interval between trigger executions in minutes.

**`start_time: datetime | None`**
When to start the fixed rate schedule. If not specified, starts when the trigger is deployed and activated.

### Examples

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-examples" lang="python">}}

## The `automation` parameter with `flyte.Cron`

You can define a Cron-based schedule trigger by setting the `automation` parameter to an instance of `flyte.Cron`.

The `flyte.Cron` has the following signature:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="dummy-cron" lang="python">}}

### Parameters

**`cron_expression: str`** (required)
The cron expression defining when the trigger should fire. Uses standard Unix cron format with five fields: minute, hour, day of month, month, and day of week.

**`timezone: str | None`**
The timezone for the cron expression. If not specified, it defaults to UTC. Uses standard timezone names like "America/New_York" or "Europe/London".

### Examples

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="cron-examples" lang="python">}}

#### Cron Expressions

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

## The `inputs` parameter

The `inputs` parameter allows you to provide default values for your task's parameters when the trigger fires.
This is essential for parameterizing your automated executions and passing trigger-specific data to your tasks.

### Basic Usage

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="inputs-basic-usage" lang="python">}}

### Using `flyte.TriggerTime`

The special `flyte.TriggerTime` value injects the trigger execution timestamp into your task:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="inputs-trigger-time" lang="python">}}

### Required vs optional parameters

> [!IMPORTANT]
> If your task has parameters without default values, you **must** provide values for them in the trigger inputs, otherwise the trigger will fail to execute.

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="inputs-required-optional" lang="python">}}

### Complex input types

You can pass various data types through trigger inputs:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="inputs-complex" lang="python">}}

## Predefined schedule triggers

For common scheduling needs, Flyte provides predefined trigger methods that create Cron-based schedules without requiring you to specify cron expressions manually.
These are convenient shortcuts for frequently used scheduling patterns.

### Available Predefined Triggers

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="predefined-available" lang="python">}}
```python
minutely_trigger = flyte.Trigger.minutely()    # Every minute
hourly_trigger = flyte.Trigger.hourly()        # Every hour
daily_trigger = flyte.Trigger.daily()          # Every day at midnight
weekly_trigger = flyte.Trigger.weekly()        # Every week (Sundays at midnight)
monthly_trigger = flyte.Trigger.monthly()      # Every month (1st day at midnight)
```

For reference, here's what each predefined trigger is equivalent to:

```python
# These are functionally identical:
# flyte.Trigger.minutely() == flyte.Trigger("minutely", flyte.Cron("* * * * *"))
# flyte.Trigger.hourly() == flyte.Trigger("hourly", flyte.Cron("0 * * * *"))
# flyte.Trigger.daily() == flyte.Trigger("daily", flyte.Cron("0 0 * * *"))
# flyte.Trigger.weekly() == flyte.Trigger("weekly", flyte.Cron("0 0 * * 0"))
# flyte.Trigger.monthly() == flyte.Trigger("monthly", flyte.Cron("0 0 1 * *"))
```

### Predefined Trigger Parameters

All predefined trigger methods (`minutely()`, `hourly()`, `daily()`, `weekly()`, `monthly()`) accept the same set of parameters:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="predefined-parameters" lang="python">}}
```python
flyte.Trigger.daily(
    trigger_time_input_key="trigger_time",
    name="daily",
    description="A trigger that runs daily at midnight",
    auto_activate=True,
    inputs=None,
    env_vars=None,
    interruptible=None,
    overwrite_cache=False,
    queue=None,
    labels=None,
    annotations=None
)
```

#### Core Parameters

**`trigger_time_input_key: str = "trigger_time"`**
The parameter name that will receive the `flyte.TriggerTime` value in your task. This allows you to customize which parameter gets the execution timestamp.

**`name: str`**
The unique identifier for the trigger. Defaults to the method name (`"daily"`, `"hourly"`, etc.).

**`description: str`**
Human-readable description of the trigger's purpose. Each method has a sensible default.

#### Configuration Parameters

**`auto_activate: bool = True`**
Whether the trigger should be automatically activated when deployed. Set to `False` to deploy inactive triggers that require manual activation.

**`inputs: Dict[str, Any] | None = None`**
Additional parameter values for your task when triggered. The `trigger_time_input_key` parameter is automatically included with `flyte.TriggerTime` as its value.

#### Runtime Override Parameters

**`env_vars: Dict[str, str] | None = None`**
Environment variables to set for triggered executions, overriding the task's default environment variables.

**`interruptible: bool | None = None`**
Whether triggered executions can be interrupted (useful for cost optimization with spot/preemptible instances). Overrides the task's interruptible setting.

**`overwrite_cache: bool = False`**
Whether to bypass/overwrite task cache for triggered executions, ensuring fresh computation.

**`queue: str | None = None`**
Specific execution queue for triggered runs, overriding the task's default queue.

#### Metadata Parameters

**`labels: Mapping[str, str] | None = None`**
Key-value labels for organizing and filtering triggers (e.g., team, component, priority).

**`annotations: Mapping[str, str] | None = None`**
Additional metadata, often used by infrastructure tools for compliance, monitoring, or cost tracking.

### Trigger time in predefined triggers

By default, predefined triggers assume the existence of the parameter called `trigger_time` (of type `datetime`) on the triggered task and pass the trigger execution timestamp to that parameter.
This differs from custom triggers where you need to explicitly set the `flyte.TriggerTime` in the `inputs` dictionary.

For predefined triggers, you can customize the parameter name that receives the trigger execution timestamp by setting the `trigger_time_input_key` parameter.

### Predefined trigger examples

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="predefined-examples" lang="python">}}
```python
# Simple predefined schedule trigger in task decorator
@env.task(triggers=flyte.Trigger.hourly())
def hourly_data_sync(trigger_time: datetime, x: int = 11) -> str:
    return f"Hourly sync completed at {trigger_time} with x={x}"

# Customized predefined schedule trigger
daily_batch_trigger = flyte.Trigger.daily(
    trigger_time_input_key="batch_date",   # Custom trigger time parameter name
    name="daily_batch_trigger",            # Custom trigger name
    inputs={                               # Custom task inputs
        "environment": "production",
        "max_records": 10000
    },
    env_vars={"PROCESSING_MODE": "batch"}, # Override environment variables
    overwrite_cache=True                   # Bypass cache for triggered runs
)

@env.task(triggers=daily_batch_trigger)
def process_batch(batch_date: datetime, environment: str, max_records: int) -> str:
    return f"Processed {max_records} records for {batch_date.date()} in {environment}"
```

## Multiple triggers per task

You can attach multiple triggers to a single task by providing a list of triggers. This allows you to run the same task on different schedules or with different configurations:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="multiple-triggers" lang="python">}}
```python
@env.task(triggers=[
    flyte.Trigger.hourly(),  # Predefined trigger
    flyte.Trigger.daily(),   # Another predefined trigger
    flyte.Trigger("custom", flyte.Cron("0 */6 * * *"))  # Custom trigger every 6 hours
])
def multi_trigger_task(trigger_time: datetime = flyte.TriggerTime) -> str:
    # Different logic based on execution timing
    if trigger_time.hour == 0:  # Daily run at midnight
        return f"Daily comprehensive processing at {trigger_time}"
    else:  # Hourly or custom runs
        return f"Regular processing at {trigger_time.strftime('%H:%M')}"
```

You can mix and match trigger types, combining predefined triggers with those that use `flyte.Cron`, and `flyte.FixedRate` automations (see below for explanations of these concepts).

## Deploying a task with triggers

We recommend that you define your triggers in code together with your tasks and deploy them together.

The Union UI displays:

* `Owner` - who last deployed the trigger.

* `Last updated` - who last activated or deactivated the trigger and when. Note: If you deploy a trigger with `auto_activate=True`(default), this will match the `Owner`.

* `Last Run` - when was the last run created by this trigger.

For development and debugging purposes, you can adjust and deploy individual triggers from the UI.

To deploy a task with its triggers, you can either use Flyte CLI:

```shell
flyte deploy -p <project> -d <domain> <file_with_tasks_and_triggers.py> env
```

Or in Python::

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="deploying" lang="python">}}
```python
env = flyte.TaskEnvironment(name="my_task_env")

@env.task(triggers=flyte.Trigger.hourly())  # Every hour
def example_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Task executed at {trigger_time.isoformat()} with x={x}"

if __name__ == "__main__":
    flyte.init_from_config()
    flyte.deploy(env)
```

Upon deploy, all triggers that are associated with the task will be automatically switched to the latest task version. Triggers which are defined elsewhere (i.e. in the UI) will be deleted unless they have been referenced in the task definition.

## Activating and deactivating triggers

By default, triggers are automatically activated upon deployment (`auto_activate=True`).
Alternatively, you can set `auto_activate=False` to deploy inactive triggers.
An inactive trigger will not create runs until activated.

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="auto-activate-false" lang="python">}}
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

## Trigger run timing

The timing of the first run created by a trigger depends on the type of trigger used (Cron-based or Fixed-rate) and whether the trigger is active upon deployment.

### Cron-based triggers

For Cron-based triggers, the first run will be created at the next scheduled time according to the cron expression after trigger activation and similarly thereafter.

* `0 0 * * *` If deployed at 17:00 today, the trigger will first fire 7 hours later (0:00 of the following day) and then every day at 0:00 thereafter.

* `*/15 14 * * 1-5` if today is Tuesday at 17:00, the trigger will fire the next day (Wednesday) at 14:00, 14:15, 14:30, and 14:45 and then the same for every subsequent weekday thereafter.

### Fixed-rate triggers

#### Fixed-rate without `start_time`

If no `start_time` is specified, then the first run will be created after the specified interval from the time of activation. No run will be created immediately upon activation, but the activation time will be used as the reference point for future runs.

##### Fixed-rate without `start_time` and with automatic activation

Let's say you define a fixed rate trigger with automatic activation like this:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-without-start-time-with-auto-activate" lang="python">}}
```python
my_trigger = flyte.Trigger("my_trigger", flyte.FixedRate(60))
```

In this case, the first run will occur 60 minutes after the successful deployment of the trigger.
So, if you deployed this trigger at 13:15, the first run will occur at 14:15 and so on thereafter

##### Fixed-rate without `start_time` and without automatic activation

On the other hand, let's say you define a fixed rate trigger without automatic activation like this:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-without-start-time-without-auto-activate" lang="python">}}
```python
my_trigger = flyte.Trigger("my_trigger", flyte.FixedRate(60), auto_activate=False)
```

Then you activate it after about 3 hours. In this case the first run will kick off 60 minutes after trigger activation.
If you deployed the trigger at 13:15 and activated it at 16:07, the first run will occur at 17:07.

#### Fixed-rate with `start_time`

##### Fixed-rate with `start_time` while active

If a `start_time` is specified, and the trigger is active at `start_time` then the first run will occur at `start_time` and then at the specified interval thereafter.
For example:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-with-start-time-while-active" lang="python">}}
```python
my_trigger = flyte.Trigger(
    "my_trigger",
    # Runs every 60 minutes starting from October 26th, 2025, 10:00am
    flyte.FixedRate(60, start_time=datetime(2025, 10, 26, 10, 0, 0)),
)
```
If you deploy this trigger on October 24th, 2025, the trigger will wait until October 26th 10:00am and will create the first run at exactly 10:00am.

##### Fixed-rate with `start_time` while inactive

If a start time is specified, but the trigger is activated after `start_time`, then the first run will be created when the next time point occurs that aligns with the recurring trigger interval using `start_time` as the initial reference point.
For example:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-with-start-time-while-inactive" lang="python">}}
```python
custom_rate_trigger = flyte.Trigger(
    "custom_rate",
    # Runs every 60 minutes starting from October 26th, 2025, 10:00am
    flyte.FixedRate(60, start_time=datetime(2025, 10, 26, 10, 0, 0)),
    auto_activate=False
)
```
If activated later than the `start_time`, say on October 28th 12:35pm for example, the first run will be created at October 28th at 1:00pm.

## Deleting triggers

If you decide that you don't need a trigger anymore, you can remove the trigger from the task definition and deploy the task again.

Alternatively, you can use Flyte CLI:

```shell
flyte delete trigger custom_cron my_task_env.custom_task --project <project> --domain <domain>
```

## Schedule time zones

### Setting time zone for a Cron schedule

Cron expressions are by default in UTC, but it's possible to specify custom time zones like so:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="timezone" lang="python">}}
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

### `flyte.TriggerTime` is always in UTC

The `flyte.TriggerTime` value is always in UTC. For timezone-aware logic, convert as needed:

{{< code file="user-guide/task-configuration/triggers/triggers.py" fragment="trigger-time-utc" lang="python">}}
```python
@env.task(triggers=flyte.Trigger.daily())
def timezone_aware_task(utc_trigger_time: datetime = flyte.TriggerTime) -> str:
    from datetime import timezone
    local_time = utc_trigger_time.replace(tzinfo=timezone.utc).astimezone()
    return f"Daily task fired at {utc_trigger_time} UTC ({local_time} local)"
```

### Daylight Savings Time behavior

When Daylight Savings Time (DST) begins and ends, it can impact when the scheduled execution begins.

On the day DST begins, time jumps from 2:00AM to 3:00AM, which means the time of 2:30AM won't exist. In this case, the trigger will not fire until the next 2:30AM, which is the next day.

On the day DST ends, the hour from 1:00AM to 2:00AM repeats, which means the time of 1:30AM will exist twice. If the schedule above was instead set for 1:30AM, it would only run once, on the first occurrence of 1:30AM.
