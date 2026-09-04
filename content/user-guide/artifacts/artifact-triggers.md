---
title: Trigger on new versions
description: Run a task automatically whenever a new version of an artifact lands, using `flyte.OnArtifact`. It fires no matter who published the version.
icon: lightning-charge
weight: 4
variants: -flyte +union
---

# Trigger on new versions

An artifact trigger runs a task automatically whenever a new version of a named artifact lands. Use it to validate every new model, retrain when a dataset is refreshed, or kick off batch inference when fresh data arrives.

A trigger is a `flyte.Trigger` whose `automation` is `flyte.OnArtifact`. The `flyte.TriggeredArtifact` sentinel marks which task input receives the new version:

```python
import flyte
from flyte.io import File

env = flyte.TaskEnvironment(name="validation")

retrain = flyte.Trigger(
    name="retrain-on-new-model",
    automation=flyte.OnArtifact(name="customer_model"),
    inputs={"model": flyte.TriggeredArtifact, "threshold": 0.5},
    description="Validate every new customer_model version",
)


@env.task(triggers=(retrain,))
async def validate(model: File, threshold: float = 0.5) -> str:
    ...
```

Deploy the environment to register the trigger:

```bash
flyte deploy validation.py env
```

From then on, every new version of `customer_model` in the task's project and domain starts a run of `validate`, with the new version bound to the `model` input. The task body sees an ordinary `File` or `Dir` and needs no artifact-specific code.

## What counts as a new version

The trigger fires no matter how the version was published: a task output wrapped with `flyte.artifacts.new()`, an upload through `flyte.remote.Artifact.create()` or `flyte create artifact`, or a Hugging Face prefetch. This makes triggers a clean handoff point between external processes and your pipelines: a partner drops a dataset, publishes it as an artifact, and your processing task starts on its own.

By default any new version fires the trigger. Pass `version=` to `flyte.OnArtifact` to fire only when that exact version is published.

## Rules

* At most one input can be `flyte.TriggeredArtifact`.
* `flyte.TriggeredArtifact` requires the automation to be `flyte.OnArtifact`.
* `flyte.TriggerTime` cannot be combined with `flyte.OnArtifact`; it is for schedule triggers.

All other inputs must have values in the trigger definition or defaults on the task, the same as [schedule triggers](../tasks/task-configuration/triggers).

## Firing an artifact trigger by hand

> [!NOTE]
> Firing a trigger from Python requires flyte 2.7.1 or later.

An artifact trigger can also be fired on demand, from the UI or by passing it to `flyte.run()` in Python. See [Firing a trigger on demand](../tasks/task-configuration/triggers#firing-a-trigger-on-demand).

No new version is being published in that case, so nothing fills the `flyte.TriggeredArtifact` input. Pass it yourself as a keyword override:

```python
trigger = flyte.remote.Trigger.get(name="retrain-on-new-model", task_name="validation.validate")
model = flyte.remote.Artifact.get(name="customer_model")
run = flyte.run(trigger, model=model)
```
