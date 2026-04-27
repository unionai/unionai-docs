---
title: Triggers
weight: 9
variants: +flyte +union
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

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="hourly" lang="python" >}}

Here we use a predefined schedule trigger to run the `hourly_task` every hour.
Other predefined triggers can be used similarly (see [Predefined schedule triggers](#predefined-schedule-triggers) below).

If you want full control over the trigger behavior, you can define a trigger using the `flyte.Trigger` class directly.

## `flyte.Trigger`

For complete parameter documentation, see the [`Trigger`](../../api-reference/flyte-sdk/packages/flyte/trigger), [`Cron`](../../api-reference/flyte-sdk/packages/flyte/cron), and [`FixedRate`](../../api-reference/flyte-sdk/packages/flyte/fixedrate) API references.

The `Trigger` class allows you to define custom triggers with full control over scheduling and execution behavior. It has the following signature:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="dummy-trigger" lang="python">}}

Here's a comprehensive example showing all parameters:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="comprehensive-trigger" lang="python">}}

## The `automation` parameter with `flyte.FixedRate`

You can define a fixed-rate schedule trigger by setting the `automation` parameter of the `flyte.Trigger` to an instance of `flyte.FixedRate`.

The `flyte.FixedRate` has the following signature:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="dummy-fixed-rate" lang="python">}}

### Examples

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-examples" lang="python">}}

## The `automation` parameter with `flyte.Cron`

You can define a Cron-based schedule trigger by setting the `automation` parameter to an instance of `flyte.Cron`.

The `flyte.Cron` has the following signature:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="dummy-cron" lang="python">}}

### Examples

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="cron-examples" lang="python">}}

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

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="inputs-basic-usage" lang="python">}}

### Using `flyte.TriggerTime`

The special `flyte.TriggerTime` value is used in the `inputs` to indicate the task parameter into which Flyte will inject the trigger execution timestamp:

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

## Predefined schedule triggers

For common scheduling needs, Flyte provides predefined trigger methods that create Cron-based schedules without requiring you to specify cron expressions manually.
These are convenient shortcuts for frequently used scheduling patterns.

### Available Predefined Triggers

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

All predefined trigger methods accept the same parameters as `flyte.Trigger`, plus a `trigger_time_input_key`. For the full parameter list, see the [`Trigger` API reference](../../api-reference/flyte-sdk/packages/flyte/trigger).

### Trigger time in predefined triggers

By default, predefined triggers will pass the execution time to the parameter `trigger_time` of type `datetime`,if that parameter exists on the task.
If no such parameter exists, the task will still be executed without error.

Optionally, you can customize the parameter name that receives the trigger execution timestamp by setting the `trigger_time_input_key` parameter (in this case the absence of this custom parameter on the task will raise an error at trigger deployment time):

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="trigger-time-input-key" lang="python">}}

## Multiple triggers per task

You can attach multiple triggers to a single task by providing a list of triggers. This allows you to run the same task on different schedules or with different configurations:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="multiple-triggers" lang="python">}}

You can mix and match trigger types, combining predefined triggers with those that use `flyte.Cron`, and `flyte.FixedRate` automations (see below for explanations of these concepts).

## Notifications

You can attach notifications to a trigger using the `notifications` parameter of `flyte.Trigger`.
Notifications fire when a triggered run reaches a terminal execution phase.

```python
import flyte
from flyte import notify
from flyte.models import ActionPhase

env = flyte.TaskEnvironment(name="my_task_env")

trigger_with_notifications = flyte.Trigger(
    name="daily_report",
    automation=flyte.Cron("0 9 * * 1-5"),
    notifications=(
        notify.Slack(
            on_phase=ActionPhase.FAILED,
            webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
            message="Run {{.Run.Name}} failed with: {{.Error}}",
        ),
        notify.Email(
            on_phase=ActionPhase.SUCCEEDED,
            recipients=["oncall@example.com"],
            subject="Run {{.Run.Name}} succeeded",
            body="Run: {{.Run.Name}}",
        ),
    ),
)

@env.task(triggers=trigger_with_notifications)
def process_data(date: str) -> str:
    return f"Processed {date}"
```

### Execution phases

The `on_phase` parameter accepts a single phase or a tuple of terminal phases from `flyte.models.ActionPhase`:

| Phase | Description                |
|-------|----------------------------|
| `ActionPhase.SUCCEEDED` | Run completed successfully |
| `ActionPhase.FAILED` | Run failed with an error  |
| `ActionPhase.TIMED_OUT` | Run exceeded its timeout  |
| `ActionPhase.ABORTED` | Run was manually aborted  |

To notify on multiple phases with the same notification:

```python
notify.Email(
    on_phase=(ActionPhase.FAILED, ActionPhase.ABORTED),
    recipients=["oncall@example.com"],
    subject="Alert: Run completed with phase {{.Phase}}",
    body="Run: {{.Run.Name}}\nError: {{.Error}}",
)
```

### Template variables

All message fields support template variables that are substituted at delivery time:

| Variable           | Description                                            |
|--------------------|--------------------------------------------------------|
| `{{.Run.Project}}` | Project name                                           |
| `{{.Run.Domain}}`  | Domain name                                            |
| `{{.Run.Name}}`    | Run ID                                                 |
| `{{.Phase}}`       | Execution phase                                        |
| `{{.Error}}`       | Error message when failed or abort reason whan aborted |


### Slack notifications

`notify.Slack` sends a message to a Slack channel via an [incoming webhook](https://api.slack.com/messaging/webhooks).

**Simple message:**

```python
notify.Slack(
    on_phase=ActionPhase.FAILED,
    webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
    message="Run {{.Run.Name}} failed in {{.Run.Project}}/{{.Run.Domain}}: {{.Error}}",
)
```

**Rich formatting with [Block Kit](https://api.slack.com/block-kit):**

Use `blocks` instead of `message` for structured layouts. When `blocks` is provided, `message` is ignored.

```python
notify.Slack(
    on_phase=ActionPhase.SUCCEEDED,
    webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
    blocks=[
        {
            "type": "header",
            "text": {"type": "plain_text", "text": "Task Succeeded"},
        },
        {
            "type": "section",
            "fields": [
                {"type": "mrkdwn", "text": "*Run:*\n{{.Run.Name}}"},
                {"type": "mrkdwn", "text": "*Phase:*\n{{.Phase}}"},
            ],
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {"type": "mrkdwn", "text": "{{.Run.Project}}/{{.Run.Domain}}"},
            ],
        },
    ],
)
```

### Email notifications

`notify.Email` sends an email notification. You can provide a plain-text `body`, an `html_body`, or both (the email is sent as multipart when both are present).

```python
notify.Email(
    on_phase=ActionPhase.FAILED,
    recipients=["oncall@example.com"],
    cc=["team-lead@example.com"],
    subject="ALERT: Run {{.Run.Name}} failed",
    body="Run: {{.Run.Name}}\nError: {{.Error}}",
    html_body="<b>Error:</b> {{.Error}}<br>",
)
```

### Microsoft Teams notifications

`notify.Teams` sends a message to a Teams channel via an incoming webhook. Use `card` for [Adaptive Card](https://adaptivecards.io/designer/) formatting; when `card` is set, `title` and `message` are ignored.

```python
notify.Teams(
    on_phase=ActionPhase.FAILED,
    webhook_url="https://outlook.office.com/webhook/YOUR_WEBHOOK_URL",
    title="Task Failed",
    message="Run {{.Run.Name}} failed: {{.Error}}\n",
)
```

### Custom webhook notifications

`notify.Webhook` sends an HTTP request to any endpoint. All string values in `headers` and `body` support template variables.

```python
notify.Webhook(
    on_phase=ActionPhase.SUCCEEDED,
    url="https://api.example.com/events",
    method="POST",
    headers={"Authorization": "Bearer my-token"},
    body={
        "event": "task_succeeded",
        "run": "{{.Run.Name}}",
    },
)
```


## Deploying a task with triggers

We recommend that you define your triggers in code together with your tasks and deploy them together.

The Union UI displays:

* `Owner` - who last deployed the trigger.

* `Last updated` - who last activated or deactivated the trigger and when. Note: If you deploy a trigger with `auto_activate=True`(default), this will match the `Owner`.

* `Last Run` - when was the last run created by this trigger.

For development and debugging purposes, you can adjust and deploy individual triggers from the UI.

To deploy a task with its triggers, you can either use Flyte CLI:

```bash
flyte deploy -p <project> -d <domain> <file_with_tasks_and_triggers.py> env
```

Or in Python:

```python
flyte.deploy(env)
```

Upon deploy, all triggers that are associated with a given task `T` will be automatically switched to apply to the latest version of that task. Triggers on task `T` which are defined elsewhere (i.e. in the UI) will be deleted unless they have been referenced in the task definition of `T`

<!-- TODO
Add link to workflow deployment docs when available.
-->

## Activating and deactivating triggers

By default, triggers are automatically activated upon deployment (`auto_activate=True`).
Alternatively, you can set `auto_activate=False` to deploy inactive triggers.
An inactive trigger will not create runs until activated.

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="auto-activate-false" lang="python">}}

This trigger won't create runs until it is explicitly activated.
You can activate a trigger via the Flyte CLI:

```bash
flyte update trigger custom_cron my_task_env.custom_task --activate --project <project> --domain <domain>
```

If you want to stop your trigger from creating new runs, you can deactivate it:

```bash
flyte update trigger custom_cron my_task_env.custom_task --deactivate --project <project> --domain <domain>
```

You can also view and manage your deployed triggers in the Union UI.

## Trigger run timing

The timing of the first run created by a trigger depends on the type of trigger used (Cron-based or Fixed-rate) and whether the trigger is active upon deployment.

### Cron-based triggers

For Cron-based triggers, the first run will be created at the next scheduled time according to the cron expression after trigger activation and similarly thereafter.

* `0 0 * * *` If deployed at 17:00 today, the trigger will first fire 7 hours later (0:00 of the following day) and then every day at 0:00 thereafter.

* `*/15 14 * * 1-5` if today is Tuesday at 17:00, the trigger will fire the next day (Wednesday) at 14:00, 14:15, 14:30, and 14:45 and then the same for every subsequent weekday thereafter.

### Fixed-rate triggers without `start_time`

If no `start_time` is specified, then the first run will be created after the specified interval from the time of activation. No run will be created immediately upon activation, but the activation time will be used as the reference point for future runs.

#### No `start_time`, auto_activate: True

Let's say you define a fixed rate trigger with automatic activation like this:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="no-start-time-auto-activate-true" lang="python">}}

In this case, the first run will occur 60 minutes after the successful deployment of the trigger.
So, if you deployed this trigger at 13:15, the first run will occur at 14:15 and so on thereafter.

#### No `start_time`, auto_activate: False

On the other hand, let's say you define a fixed rate trigger without automatic activation like this:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="no-start-time-auto-activate-false" lang="python">}}

Then you activate it after about 3 hours. In this case the first run will kick off 60 minutes after trigger activation.
If you deployed the trigger at 13:15 and activated it at 16:07, the first run will occur at 17:07.

### Fixed-rate triggers with `start_time`

If a `start_time` is specified, the timing of the first run depends on whether the trigger is active at `start_time` or not.

#### Fixed-rate with `start_time` while active

If a `start_time` is specified, and the trigger is active at `start_time` then the first run will occur at `start_time` and then at the specified interval thereafter.
For example:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-with-start-time-while-active" lang="python">}}

If you deploy this trigger on October 24th, 2025, the trigger will wait until October 26th 10:00am and will create the first run at exactly 10:00am.

#### Fixed-rate with `start_time` while inactive

If a start time is specified, but the trigger is activated after `start_time`, then the first run will be created when the next time point occurs that aligns with the recurring trigger interval using `start_time` as the initial reference point.
For example:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="fixed-rate-with-start-time-while-inactive" lang="python">}}

If activated later than the `start_time`, say on October 28th 12:35pm for example, the first run will be created at October 28th at 1:00pm.

## Deleting triggers

If you decide that you don't need a trigger anymore, you can remove the trigger from the task definition and deploy the task again.

Alternatively, you can use Flyte CLI:

```bash
flyte delete trigger custom_cron my_task_env.custom_task --project <project> --domain <domain>
```

## Schedule time zones

### Setting time zone for a Cron schedule

Cron expressions are by default in UTC, but it's possible to specify custom time zones like so:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="timezone" lang="python">}}

The above two schedules will fire 1 minute apart, at 9 AM PT and 12:01 PM ET respectively.

### `flyte.TriggerTime` is always in UTC

The `flyte.TriggerTime` value is always in UTC. For timezone-aware logic, convert as needed:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="trigger-time-utc" lang="python">}}

### Daylight Savings Time behavior

When Daylight Savings Time (DST) begins and ends, it can impact when the scheduled execution begins.

On the day DST begins, time jumps from 2:00AM to 3:00AM, which means the time of 2:30AM won't exist. In this case, the trigger will not fire until the next 2:30AM, which is the next day.

On the day DST ends, the hour from 1:00AM to 2:00AM repeats, which means the time of 1:30AM will exist twice. If the schedule above was instead set for 1:30AM, it would only run once, on the first occurrence of 1:30AM.
