---
title: Manual triggers and firing on demand
description: Save named launch configurations for a task with triggers that have no automation, and fire any trigger from the UI or Python.
icon: hand-index
weight: 4
variants: +flyte +union
---

# Manual triggers and firing on demand

Not every repeated run is on a schedule. An analyst re-runs a report with the same few input combinations whenever someone asks, and retypes them each time. A trigger with no automation saves each combination under a name, and anyone can fire it from the UI or from Python.

## Triggers without automation

> [!NOTE]
> Triggers without automation, and firing a trigger on demand from Python, require flyte 2.7.1 or later.

Leave `automation` unset and the trigger has nothing that fires it.
It becomes a saved launch configuration for the task: a name, a set of inputs, and optionally env vars, a queue, notifications and the other `flyte.Trigger` settings.
Nothing runs until someone fires it, from the UI or from Python (see [Firing a trigger on demand](#firing-a-trigger-on-demand)).

This is a convenient way to publish a handful of "blessed" ways to run a task without re-typing inputs each time.
Here, one task gets a quick sanity-check configuration and a full monthly one, each with its own inputs and notifications:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/manual.py" fragment="manual-triggers" lang="python" >}}

Trigger inputs override the task's own defaults for every run fired through the trigger.
Inputs the trigger does not mention keep the task default, so `quick-report` above still runs with `as_of=None`.

A manual trigger can sit next to scheduled ones on the same task. Only a schedule can bind `flyte.TriggerTime`, since a manual trigger has no fire time:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/manual.py" fragment="manual-alongside-scheduled" lang="python" >}}

Deploy the task as usual and all three triggers are registered:

```bash
flyte deploy manual.py env
flyte get trigger
```

You can also create a manual trigger for an already-deployed task from the CLI by omitting `--schedule`:

```bash
flyte create trigger manual_trigger_example.report_on_demand ad-hoc --description "Fire by hand"
```

## Firing a trigger on demand

> [!NOTE]
> Passing a trigger to `flyte.run()` requires flyte 2.7.1 or later.

Every deployed trigger can be fired on demand, whether or not it has an automation.
The run starts with the inputs, env vars, queue and notification rules the trigger was deployed with, and the platform records the trigger as the run's origin, exactly as it does for a scheduled fire.

### From the UI

Open the task in the UI, go to its **Triggers** tab, open the trigger you want, and select **Run**.

### From Python

Fetch the trigger with `flyte.remote.Trigger.get()` and pass it to `flyte.run()`, exactly like a task.
This needs a remote client, so call `flyte.init_from_config()` or `flyte.init()` first.

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/programmatic.py" fragment="run-trigger-as-deployed" lang="python" >}}

Keyword arguments override individual inputs. Anything left out keeps the value the trigger was deployed with, or the task default if the trigger never bound that input:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/programmatic.py" fragment="run-trigger-with-overrides" lang="python" >}}

Overrides are keyword-only. Positional arguments raise an error, because a trigger already binds a subset of the inputs and positional values would be ambiguous.
Passing an input name the task does not have also raises an error, listing the known inputs.

`flyte.with_runcontext()` layers run-level settings on top of the trigger's own. The trigger's env vars, queue and notifications are the floor; anything the run context sets wins over the trigger's value for that setting:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/programmatic.py" fragment="run-trigger-with-runcontext" lang="python" >}}

Triggers returned by `flyte.remote.Trigger.listall()` can be fired the same way. Their full definition is fetched when you run them:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/programmatic.py" fragment="run-every-trigger" lang="python" >}}

A scheduled trigger fired this way runs immediately, off its schedule. The platform stamps the run start time, and any input bound to `flyte.TriggerTime` is filled from it.
If you pass that input explicitly as a keyword override, your value is used instead.

The returned `flyte.remote.Run` is an ordinary run handle, so you can `wait()` on it and read its inputs and outputs:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/programmatic.py" fragment="main" lang="python" >}}

Running a trigger is remote-only. It is not supported in local mode or with `dry_run`.
