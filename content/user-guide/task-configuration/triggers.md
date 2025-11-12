---
title: Triggers
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

# Triggers

Triggers allow you to automate and parameterize an execution by scheduling its kick-off time and providing overrides for its task inputs.

Currently, we support only **schedule triggers**. This type of trigger runs a task based on a Cron expression or a fixed-rate schedule.

Support is coming for other trigger types, such as:

* Webhook triggers: Hit an API endpoint to run your task.
* Artifact triggers: Run a task when a specific artifact is produced.

## Triggers are set in the task decorator

A trigger is created by setting the `triggers` parameter in the task decorator to a `flyte.Trigger` object or a list of such objects (triggers are not settable at the `TaskEnvironment` definition or `task.override` levels).

Here is a simple example:

```python
import flyte
from datetime import datetime

env = flyte.TaskEnvironment(name="my_task_env")

@env.task(triggers=flyte.Trigger.hourly())  # Every hour
def example_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Task executed at {trigger_time.isoformat()} with x={x}"
```

Here we use a predefined hourly trigger to run the `example_task` every hour.
Other predefined triggers can be used similarly (see [Predefined schedule triggers](#predefined-schedule-triggers) below).

However, if you want full control over the trigger behavior, you can define a trigger using the `flyte.Trigger` class directly.

## Multiple triggers per task

You can attach multiple triggers to a single task by providing a list of triggers. This allows you to run the same task on different schedules or with different configurations:

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

You can mix and match any combination of trigger types - predefined triggers and custom `flyte.Trigger` instances with `flyte.Cron`, and `flyte.FixedRate` automations (see below for explanations of these concepts).

## `flyte.Trigger`

The `Trigger` class allows you to define custom triggers with full control over scheduling and execution behavior. It has the following signature:

```python
flyte.Trigger(
    name,
    automation,
    description="",
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

```python
comprehensive_trigger = flyte.Trigger(
    name="monthly_financial_report",
    automation=flyte.Cron("0 6 1 * *", timezone="America/New_York"),
    description="Monthly financial report generation for executive team",
    auto_activate=True,
    inputs={
        "report_date": flyte.TriggerTime,
        "report_type": "executive_summary",
        "include_forecasts": True
    },
    env_vars={
        "REPORT_OUTPUT_FORMAT": "PDF",
        "EMAIL_NOTIFICATIONS": "true"
    },
    interruptible=False,  # Critical report, use dedicated resources
    overwrite_cache=True,  # Always fresh data
    queue="financial-reports",
    labels={
        "team": "finance",
        "criticality": "high",
        "automation": "scheduled"
    },
    annotations={
        "compliance.company.com/sox-required": "true",
        "backup.company.com/retain-days": "2555"  # 7 years
    }
)
```

## `flyte.FixedRate`

You can define a fixed-rate schedule trigger by setting the `automation` parameter to an instance of `flyte.FixedRate`.

The `flyte.FixedRate` has the following signature:

```python
flyte.FixedRate(
    interval_minutes,
    start_time=None
)
```

### Parameters

**`interval_minutes: int`** (required)
The interval between trigger executions in minutes.

**`start_time: datetime | None`**
When to start the fixed rate schedule. If not specified, starts when the trigger is deployed and activated.

### Examples

```python
# Every 90 minutes, starting when deployed
every_90_min = flyte.Trigger(
    "data_processing",
    flyte.FixedRate(interval_minutes=90)
)

# Every 6 hours (360 minutes), starting at a specific time
from datetime import datetime
specific_start = flyte.Trigger(
    "batch_job",
    flyte.FixedRate(
        interval_minutes=360,  # 6 hours
        start_time=datetime(2025, 12, 1, 9, 0, 0)  # Start Dec 1st at 9 AM
    )
)
```

## `flyte.Cron`

You can define a Cron-based schedule trigger by setting the `automation` parameter to an instance of `flyte.Cron`.

The `flyte.Cron` has the following signature:

```python
flyte.Cron(
    cron_expression,
    timezone=None
)
```

### Parameters

**`cron_expression: str`** (required)
The cron expression defining when the trigger should fire. Uses standard Unix cron format with five fields: minute, hour, day of month, month, and day of week.

**`timezone: str | None`**
The timezone for the cron expression. If not specified, defaults to UTC. Use standard timezone names like "America/New_York" or "Europe/London".

### Examples

```python
# Every day at 6 AM UTC
daily_trigger = flyte.Trigger(
    "daily_report",
    flyte.Cron("0 6 * * *")
)

# Every weekday at 9:30 AM Eastern Time
weekday_trigger = flyte.Trigger(
    "business_hours_task",
    flyte.Cron("30 9 * * 1-5", timezone="America/New_York")
)

# Every first day of the month at midnight Pacific Time
monthly_trigger = flyte.Trigger(
    "monthly_cleanup",
    flyte.Cron("0 0 1 * *", timezone="America/Los_Angeles")
)

# Every 15 minutes during business hours (9 AM to 5 PM, Mon-Fri)
frequent_trigger = flyte.Trigger(
    "monitoring_task",
    flyte.Cron("*/15 9-17 * * 1-5", timezone="UTC")
)
```

### Cron Expressions

Here are some common cron expressions you can use:

| Expression | Description |
|------------|-------------|
| `0 0 * * *` | Every day at midnight |
| `0 9 * * 1-5` | Every weekday at 9 AM |
| `30 14 * * 6` | Every Saturday at 2:30 PM |
| `0 0 1 * *` | First day of every month at midnight |
| `0 0 25 * *` | 25th day of every month at midnight |
| `0 0 * * 0` | Every Sunday at midnight |
| `*/10 * * * *` | Every 10 minutes |
| `0 */2 * * *` | Every 2 hours |

For a full guide on Cron syntax, refer to [Crontab Guru](https://crontab.guru/).

## The `inputs` parameter

The `inputs` parameter allows you to provide default values for your task's parameters when the trigger fires. This is essential for parameterizing your automated executions and passing trigger-specific data to your tasks.

### Basic Usage

```python
trigger_with_inputs = flyte.Trigger(
    "data_processing",
    flyte.Cron("0 6 * * *"),  # Daily at 6 AM
    inputs={
        "batch_size": 1000,
        "environment": "production",
        "debug_mode": False
    }
)

@env.task(triggers=trigger_with_inputs)
def process_data(batch_size: int, environment: str, debug_mode: bool = True) -> str:
    return f"Processing {batch_size} items in {environment} mode"
```

### Using `flyte.TriggerTime`

The special `flyte.TriggerTime` value injects the trigger execution timestamp into your task:

```python
timestamp_trigger = flyte.Trigger(
    "daily_report",
    flyte.Cron("0 0 * * *"),  # Daily at midnight
    inputs={
        "report_date": flyte.TriggerTime,  # Receives trigger execution time
        "report_type": "daily_summary"
    }
)

@env.task(triggers=timestamp_trigger)
def generate_report(report_date: datetime, report_type: str) -> str:
    return f"Generated {report_type} for {report_date.strftime('%Y-%m-%d')}"
```

### Required vs Optional Parameters

> [!IMPORTANT]
> If your task has parameters without default values, you **must** provide values for them in the trigger inputs, otherwise the trigger will fail to execute.

```python
# ❌ This will fail - missing required parameter 'data_source'
@env.task(triggers=flyte.Trigger("bad_trigger", flyte.Cron("0 0 * * *")))
def process_data(data_source: str, batch_size: int = 100) -> str:
    return f"Processing from {data_source}"

# ✅ This works - all required parameters provided
good_trigger = flyte.Trigger(
    "good_trigger",
    flyte.Cron("0 0 * * *"),
    inputs={
        "data_source": "prod_database",  # Required parameter
        "batch_size": 500  # Override default
    }
)

@env.task(triggers=good_trigger)
def process_data(data_source: str, batch_size: int = 100) -> str:
    return f"Processing from {data_source} with batch size {batch_size}"
```

### Complex input types

You can pass various data types through trigger inputs:

```python
complex_trigger = flyte.Trigger(
    "ml_training",
    flyte.Cron("0 2 * * 1"),  # Weekly on Monday at 2 AM
    inputs={
        "model_config": {
            "learning_rate": 0.01,
            "batch_size": 32,
            "epochs": 100
        },
        "feature_columns": ["age", "income", "location"],
        "validation_split": 0.2,
        "training_date": flyte.TriggerTime
    }
)

@env.task(triggers=complex_trigger)
def train_model(
    model_config: dict,
    feature_columns: list[str],
    validation_split: float,
    training_date: datetime
) -> str:
    return f"Training model with {len(feature_columns)} features on {training_date}"
```

## Predefined schedule triggers

For common scheduling needs, Flyte provides predefined trigger methods that create Cron-based schedules without requiring you to specify cron expressions manually. These are convenient shortcuts for frequently used scheduling patterns.

### Available Predefined Triggers

```python
minutely_trigger = flyte.Trigger.minutely()    # Every minute
hourly_trigger = flyte.Trigger.hourly()        # Every hour
daily_trigger = flyte.Trigger.daily()          # Every day at midnight
weekly_trigger = flyte.Trigger.weekly()        # Every week (Sundays at midnight)
monthly_trigger = flyte.Trigger.monthly()      # Every month (1st day at midnight)
```

### Predefined Trigger Parameters

All predefined trigger methods (`minutely()`, `hourly()`, `daily()`, `weekly()`, `monthly()`) accept the same comprehensive set of parameters:

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

### Usage Examples

Each predefined trigger generates a unique name automatically and can be used directly in task decorators:

```python
# Simple usage with predefined triggers
@env.task(triggers=flyte.Trigger.hourly())
def hourly_data_sync(trigger_time: datetime) -> str:
    return f"Hourly sync completed at {trigger_time}"

@env.task(triggers=flyte.Trigger.daily())
def daily_backup(trigger_time: datetime) -> str:
    return f"Daily backup completed at {trigger_time}"

@env.task(triggers=flyte.Trigger.weekly())
def weekly_report(trigger_time: datetime) -> str:
    return f"Weekly report generated at {trigger_time}"
```

### Customizing predefined triggers

You can customize any predefined trigger by providing additional parameters:

```python
# Customize trigger name and description
monitoring_trigger = flyte.Trigger.minutely(
    name="health_monitor",
    description="Monitors system health every minute",
    queue="monitoring",
    labels={"team": "devops", "priority": "high"}
)

@env.task(triggers=monitoring_trigger)
def health_check(trigger_time: datetime) -> str:
    return f"Health check at {trigger_time}"

# Custom trigger time parameter name
processing_trigger = flyte.Trigger.daily(
    trigger_time_input_key="batch_date",  # Custom parameter name
    name="daily_batch_processing",
    inputs={
        "environment": "production",
        "max_records": 10000
    },
    env_vars={"PROCESSING_MODE": "batch"},
    overwrite_cache=True
)

@env.task(triggers=processing_trigger)
def process_daily_batch(batch_date: datetime, environment: str, max_records: int) -> str:
    return f"Processed {max_records} records for {batch_date.date()} in {environment}"
```

### Using `flyte.TriggerTime` with predefined triggers

All predefined triggers automatically include `flyte.TriggerTime` in their inputs, making trigger execution timestamps available to your tasks. You can access this in two ways:

#### Method 1: Default parameter value (recommended)

```python
@env.task(triggers=flyte.Trigger.hourly())
def hourly_processor(trigger_time: datetime = flyte.TriggerTime) -> str:
    return f"Hourly processing started at {trigger_time.isoformat()}"
```

#### Method 2: Custom parameter name

Use the `trigger_time_input_key` parameter to customize the parameter name:

```python
processing_trigger = flyte.Trigger.daily(
    trigger_time_input_key="execution_date",
    inputs={"environment": "production"}
)

@env.task(triggers=processing_trigger)
def daily_processor(execution_date: datetime, environment: str) -> str:
    return f"Daily processing in {environment} at {execution_date}"
```

### Advanced usage patterns

#### Time zone considerations

The `flyte.TriggerTime` value is always in UTC. For timezone-aware logic, convert as needed:

```python
@env.task(triggers=flyte.Trigger.daily())
def timezone_aware_task(utc_trigger_time: datetime = flyte.TriggerTime) -> str:
    from datetime import timezone
    local_time = utc_trigger_time.replace(tzinfo=timezone.utc).astimezone()
    return f"Daily task fired at {utc_trigger_time} UTC ({local_time} local)"
```

### Equivalent cron definitions

For reference, here's what each predefined trigger is equivalent to:

```python
# These are functionally identical:
flyte.Trigger.minutely()  ≡  flyte.Trigger("minutely", flyte.Cron("* * * * *"))
flyte.Trigger.hourly()    ≡  flyte.Trigger("hourly", flyte.Cron("0 * * * *"))
flyte.Trigger.daily()     ≡  flyte.Trigger("daily", flyte.Cron("0 0 * * *"))
flyte.Trigger.weekly()    ≡  flyte.Trigger("weekly", flyte.Cron("0 0 * * 0"))
flyte.Trigger.monthly()   ≡  flyte.Trigger("monthly", flyte.Cron("0 0 1 * *"))
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

When you deploy a task definition like those above, the corresponding triggers will be active immediately after deploy and will create runs as soon as the next scheduled time comes.
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

* `0 0 * * *` it will run next day at 0:00

* `*/15 14 * * 1-5` it will run every 15th minute past hour 14 on every day-of-week from
  Monday through Friday.
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
