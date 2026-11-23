---
title: Publish outputs of tasks you don't own
description: Register another task's outputs as artifacts from the caller with `flyte.artifacts.produces`, without changing the task.
icon: box-arrow-up-right
weight: 9
variants: -flyte +union
---

# Publish outputs of tasks you don't own

> [!NOTE]
> Requires flyte 2.10.0 or later.

Another team maintains a shared `clean` task. It returns a plain `File` and knows nothing about artifacts. Your pipeline calls it once per day and region, and you want each output registered as a partition of `clean_events`. You can't wrap its return value with `flyte.artifacts.new()`, because the task isn't yours to edit.

`flyte.artifacts.produces` lets the caller declare which outputs become artifacts:

```python
import asyncio
from datetime import date, timedelta

import flyte
import flyte.artifacts as artifacts
from flyte.io import File

env = flyte.TaskEnvironment(name="pipeline")


# Owned by another team. It returns a plain File.
@env.task
async def clean(day: date, region: str) -> File:
    ...


async def clean_one(day: date, region: str) -> File:
    with artifacts.produces(
        o0=artifacts.Metadata(name="clean_events", partitions={"date": day, "region": region})
    ):
        return await clean.override(produces_artifacts=True)(day=day, region=region)


@env.task
async def main(days: int = 2) -> None:
    start = date(2026, 8, 1)
    await asyncio.gather(
        *(clean_one(start + timedelta(days=d), r) for d in range(days) for r in ("us", "eu"))
    )
```

Each call publishes one `clean_events` version, partitioned by its own day and region. The result is the same as if `clean` had returned `artifacts.new(...)` itself: the version's source is the action that ran `clean`, and it shows up in [lineage](./lineage) and fires [artifact triggers](../triggers/artifact-triggers) like any other.

## How it works

* **Keyword names are output slots.** `o0` is the first output, `o1` the second, and so on. Outputs you don't name stay ordinary outputs.
* **The call needs `produces_artifacts=True`.** That flag is what lets the platform publish a task's outputs. Turn it on for this call with `.override(produces_artifacts=True)`. Without it, nothing is published.
* **Call one task per block.** The declaration applies to every task called inside the `with` block, so keep one call per block. Concurrent calls, as in `asyncio.gather` above, each keep their own declaration. It does not pass on to the actions that the called task spawns.
* **Publishing happens on success.** If the called task fails, nothing is published.
* **Outside a task, `produces` does nothing.**

## Publishing only some outputs

A task that returns several values publishes only the slots you declare. Here `train` returns a model and a training log, and only the model is registered:

```python
with artifacts.produces(o0=artifacts.Metadata(name="events_model", kind="model")):
    model, _log = await train.override(produces_artifacts=True)(features=features)
```

## When the task also wraps its output

If the called task already returns `artifacts.new(...)`, the caller's declaration wins for the name, version, partitions, and parents. The task's own description, card, and attrs fill in whatever the caller leaves empty. This lets you reuse a task that publishes under its own name, but file its output under yours.

## Remote task references

The same works for a task you only have a reference to, such as one deployed by another team. Fetch it, turn on publishing, and declare its outputs:

```python
ref = flyte.remote.Task.get("other_team.clean", auto_version="latest")
callee = await ref.override.aio(produces_artifacts=True)

with artifacts.produces(o0=artifacts.Metadata(name="clean_events", partitions={"date": day, "region": region})):
    await callee(day=day, region=region)
```
