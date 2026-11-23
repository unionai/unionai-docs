---
title: Configure a trigger
description: Define a `flyte.Trigger` on a task, bind its inputs, and attach several triggers to one task.
icon: sliders
weight: 1
variants: +flyte +union
---

# Configure a trigger

Say a `refresh_dashboard` task serves two teams. The US team wants it every morning over the last day of data, and finance wants a 30-day run on the first of each month. You don't need two copies of the task or a wrapper script. Attach two triggers, each with its own schedule and inputs:

```python
import flyte

env = flyte.TaskEnvironment(name="dashboards")

morning_us = flyte.Trigger(
    "morning-us",
    flyte.Cron("0 7 * * *", timezone="America/New_York"),
    inputs={"region": "us", "days": 1},
)

monthly_all = flyte.Trigger(
    "monthly-all",
    flyte.Cron("0 0 1 * *"),
    inputs={"region": "all", "days": 30},
)


@env.task(triggers=[morning_us, monthly_all])
async def refresh_dashboard(region: str, days: int = 7) -> str:
    ...
```

A trigger is a named, pre-bound way to run a task. It carries the inputs and run settings, and optionally an automation that fires it. This page covers how to define one. See [Schedule triggers](./schedules) for the schedule options.

## Triggers are set in the task decorator

A trigger is created by setting the `triggers` parameter in the task decorator to a `flyte.Trigger` object or a list of such objects (triggers are not settable at the `TaskEnvironment` definition or `task.override` levels).

Here is a simple example:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="hourly" lang="python" >}}

Here we use a predefined schedule trigger to run the `hourly_task` every hour.
Other predefined triggers can be used similarly (see [Predefined schedule triggers](./schedules#predefined-schedule-triggers)).

If you want full control over the trigger behavior, you can define a trigger using the `flyte.Trigger` class directly.

## `flyte.Trigger`

For complete parameter documentation, see the [`Trigger`](../../api-reference/flyte-sdk/flyte/trigger), [`Cron`](../../api-reference/flyte-sdk/flyte/cron), and [`FixedRate`](../../api-reference/flyte-sdk/flyte/fixedrate) API references.

The `Trigger` class allows you to define custom triggers with full control over scheduling and execution behavior. It has the following signature:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="dummy-trigger" lang="python">}}

{{< variant union >}}
{{< markdown >}}
Only `name` is required. The `automation` parameter decides what fires the trigger: `flyte.Cron` or `flyte.FixedRate` for a schedule, `flyte.OnArtifact` for a new artifact version, or `None` (the default) for a trigger that is only fired on demand.
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
Only `name` is required. The `automation` parameter decides what fires the trigger: `flyte.Cron` or `flyte.FixedRate` for a schedule, or `None` (the default) for a trigger that is only fired on demand.
{{< /markdown >}}
{{< /variant >}}

Everything else describes the run that the trigger creates.

Here's a comprehensive example showing all parameters:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="comprehensive-trigger" lang="python">}}

## The `inputs` parameter

The `inputs` parameter allows you to provide default values for your task's parameters when the trigger fires.
This is essential for parameterizing your automated executions and passing trigger-specific data to your tasks.

### Basic usage

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="inputs-basic-usage" lang="python">}}

### Using `flyte.TriggerTime`

The special `flyte.TriggerTime` value is used in the `inputs` to indicate the task parameter into which Flyte will inject the trigger execution timestamp.
It is only available on schedule triggers (`flyte.Cron` or `flyte.FixedRate`), since a trigger without a schedule has no fire time:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="inputs-trigger-time" lang="python">}}

### Required vs optional parameters

> [!IMPORTANT]
> If your task has parameters without default values, you **must** provide values for them in the trigger inputs, otherwise the trigger will fail to execute.

```python
# ❌ This will fail - missing required parameter 'data_source'
bad_trigger = flyte.Trigger(
    "bad_trigger",
    flyte.Cron("0 0 * * *")
    # Missing inputs for required parameter 'data_source'
)

@env.task(triggers=bad_trigger)
def bad_trigger_taska(data_source: str, batch_size: int = 100) -> str:
    return f"Processing from {data_source} with batch size {batch_size}"

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
def good_trigger_task(data_source: str, batch_size: int = 100) -> str:
    return f"Processing from {data_source} with batch size {batch_size}"
```

### Complex input types

You can pass various data types through trigger inputs:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="inputs-complex" lang="python">}}

## Multiple triggers per task

You can attach multiple triggers to a single task by providing a list of triggers. This allows you to run the same task on different schedules or with different configurations:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="multiple-triggers" lang="python">}}

You can mix and match trigger types, combining predefined triggers with those that use `flyte.Cron`, and `flyte.FixedRate` automations (see [Schedule triggers](./schedules)).
