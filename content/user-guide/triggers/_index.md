---
title: Triggers
description: Run tasks automatically on a schedule or in reaction to new data, or save named launch configurations to fire on demand.
icon: alarm
weight: 4
variants: +flyte +union
---

# Triggers

A trigger is a named, pre-bound way to run a task. It carries the inputs, env vars, queue, notifications, and other run settings that a run started through it should use.
A trigger can also carry an *automation* that fires it on its own, such as a schedule. A trigger with no automation is fired on demand only.

```python
import flyte
from datetime import datetime

env = flyte.TaskEnvironment(name="trigger_env")


@env.task(triggers=flyte.Trigger.hourly())
def hourly_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Hourly example executed at {trigger_time.isoformat()} with x={x}"
```

Deploy the task with `flyte deploy` and the trigger starts creating runs every hour.

{{< note >}}
In Flyte 1 these were configured with a `LaunchPlan` (the `flytekit.LaunchPlan` API) and `CronSchedule`. Flyte 2 replaces them with `flyte.Trigger` and `flyte.Cron`.
{{< /note >}}

## Types of automation

The `automation` argument of `flyte.Trigger` decides what fires it. Each kind can also bind a value into one of the task's inputs.

{{< variant union >}}
{{< markdown >}}

| Kind | Automation | Fires when | Binds into inputs | Details |
|---|---|---|---|---|
| Scheduled | `flyte.Cron("0 9 * * *", timezone=...)` | A cron expression matches | `flyte.TriggerTime` | [Schedule triggers](./schedules) |
| Scheduled | `flyte.FixedRate(60, start_time=...)` | Every N minutes | `flyte.TriggerTime` | [Schedule triggers](./schedules) |
| Scheduled | `flyte.Trigger.hourly()`, `daily()`, `weekly()`, `monthly()` | Predefined cron shortcuts | `flyte.TriggerTime` | [Predefined schedules](./schedules#predefined-schedule-triggers) |
| Reactive | `flyte.OnArtifact("model")` | Any new version of an artifact is published | `flyte.TriggeredArtifact` | [Trigger on new artifact versions](./artifact-triggers) |
| Reactive | `flyte.OnArtifact("model", version="v2")` | That exact version is published | `flyte.TriggeredArtifact` | [Trigger on new artifact versions](./artifact-triggers) |
| Reactive | `flyte.OnArtifact("raw_events", region="us")` | A new version lands in a matching partition | `flyte.TriggeredArtifact`, `flyte.TriggeredPartition` | [Trigger on partitions](./partition-triggers) |
| Manual | None | Only when fired from the UI or with `flyte.run(trigger)` | None | [Manual triggers](./manual-triggers) |

Every trigger, whatever its automation, can also be [fired on demand](./manual-triggers#firing-a-trigger-on-demand).

Support is coming for webhook triggers, which will hit an API endpoint to run your task.

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

| Kind | Automation | Fires when | Binds into inputs | Details |
|---|---|---|---|---|
| Scheduled | `flyte.Cron("0 9 * * *", timezone=...)` | A cron expression matches | `flyte.TriggerTime` | [Schedule triggers](./schedules) |
| Scheduled | `flyte.FixedRate(60, start_time=...)` | Every N minutes | `flyte.TriggerTime` | [Schedule triggers](./schedules) |
| Scheduled | `flyte.Trigger.hourly()`, `daily()`, `weekly()`, `monthly()` | Predefined cron shortcuts | `flyte.TriggerTime` | [Predefined schedules](./schedules#predefined-schedule-triggers) |
| Manual | None | Only when fired from the UI or with `flyte.run(trigger)` | None | [Manual triggers](./manual-triggers) |

Every trigger, whatever its automation, can also be [fired on demand](./manual-triggers#firing-a-trigger-on-demand).

Support is coming for other trigger types, such as:

* Webhook triggers: Hit an API endpoint to run your task.
* Artifact triggers: Run a task when a specific artifact is produced.

{{< /markdown >}}
{{< /variant >}}

## In this section

{{< grid >}}

{{< link-card target="configure-triggers" icon="sliders" title="Configure a trigger" >}}
Define a `flyte.Trigger` on a task, bind its inputs, and attach several triggers to one task.
{{< /link-card >}}

{{< link-card target="schedules" icon="clock" title="Schedule triggers" >}}
Run a task on a cron expression or a fixed interval with `flyte.Cron`, `flyte.FixedRate`, or a predefined schedule.
{{< /link-card >}}

{{< link-card target="schedule-timing" icon="hourglass-split" title="When scheduled runs start" >}}
When the first run of a cron or fixed-rate trigger happens, depending on activation and `start_time`.
{{< /link-card >}}

{{< link-card target="manual-triggers" icon="hand-index" title="Manual triggers and firing on demand" >}}
Save named launch configurations for a task with triggers that have no automation, and fire any trigger from the UI or Python.
{{< /link-card >}}

{{< variant union >}}
{{< link-card target="artifact-triggers" icon="lightning-charge" title="Trigger on new artifact versions" >}}
Run a task automatically whenever a new version of an artifact lands, using `flyte.OnArtifact`. It fires no matter who published the version.
{{< /link-card >}}

{{< link-card target="partition-triggers" icon="grid-3x3" title="Trigger on partitions" >}}
Fire an artifact trigger only for matching partitions with `flyte.OnArtifact`, and pass the partition values into the task with `flyte.TriggeredPartition`.
{{< /link-card >}}
{{< /variant >}}

{{< link-card target="trigger-notifications" icon="bell" title="Notifications" >}}
Send Slack, email, Teams, or webhook notifications when a run started by a trigger ends.
{{< /link-card >}}

{{< link-card target="manage-triggers" icon="toggles" title="Deploy and manage triggers" >}}
Deploy triggers with their task, activate or deactivate them, and delete them.
{{< /link-card >}}

{{< /grid >}}
