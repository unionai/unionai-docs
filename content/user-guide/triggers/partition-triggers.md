---
title: Trigger on partitions
description: Fire an artifact trigger only for matching partitions with `flyte.OnArtifact`, and pass the partition values into the task with `flyte.TriggeredPartition`.
icon: grid-3x3
weight: 6
variants: -flyte +union
---

# Trigger on partitions

> [!NOTE]
> Requires flyte 2.10.0 or later.

An ingest job publishes `raw_events` once per day for each region, as a [partitioned artifact](../artifacts/partitions). The US team owns a cleaning pipeline that should run when a US partition lands, and not when an EU one does. It also needs to know which day just arrived without opening the file to find out.

A plain [artifact trigger](./artifact-triggers) fires on every new version. Scope it to a partition and bind the partition values to inputs:

```python
from datetime import datetime

import flyte
from flyte.io import File

env = flyte.TaskEnvironment(name="us_cleaning")

process_us = flyte.Trigger(
    name="process-new-us-partition",
    automation=flyte.OnArtifact(name="raw_events", region="us"),
    inputs={
        "events": flyte.TriggeredArtifact,
        "day": flyte.TriggeredPartition("date"),
        "region": flyte.TriggeredPartition("region"),
    },
    description="Process every new US partition of raw_events",
)


@env.task(triggers=(process_us,))
async def process_partition(events: File, day: datetime, region: str) -> str:
    async with events.open("rb") as fh:
        content = bytes(await fh.read()).decode()
    return f"processed {region} for {day:%Y-%m-%d}: {content}"
```

Deploy the environment to register the trigger:

```bash
flyte deploy us_cleaning.py env
```

From then on, a new `raw_events` version with `region="us"` starts a run of `process_partition`, with `events`, `day`, and `region` filled in. A version published for `region="eu"` is still registered, but it fires nothing.

## Narrowing which versions fire

Pass partition values to `flyte.OnArtifact`, either as keyword arguments or as a `partitions` mapping:

```python
flyte.OnArtifact("raw_events", region="us")
flyte.OnArtifact("raw_events", partitions={"region": "us", "source": "web"})
```

A version fires the trigger only if its partitions carry every key and value you list. Only string partitions can narrow a trigger, and the values must be strings. To act on a particular day, bind the time partition to an input and check it in the task.

## Binding partition values to inputs

`flyte.TriggeredPartition("key")` fills a task input with that partition's value from the version that fired the trigger. It works like `flyte.TriggeredArtifact`, which fills in the version itself, and `flyte.TriggerTime`, which fills in a schedule's fire time.

The input type depends on the partition:

| Partition | Input type |
|---|---|
| Time partition (for example `date` or `hour`) | `datetime`, the start of the partition in UTC. A daily partition arrives as midnight UTC |
| String partition (for example `region`) | `str` |

You can bind any number of partition keys, with or without `flyte.TriggeredArtifact`. `flyte.TriggeredPartition` requires the automation to be `flyte.OnArtifact`.

## Firing it by hand

When you [fire the trigger on demand](./artifact-triggers#firing-an-artifact-trigger-by-hand), no version is being published. Pass the artifact and the partition-bound inputs as keyword overrides:

```python
from datetime import date, datetime, timezone

import flyte
from flyte.remote import Artifact, Trigger

flyte.init_from_config()

trigger = Trigger.get(name="process-new-us-partition", task_name="us_cleaning.process_partition")
events = Artifact.get("raw_events", date=date(2026, 8, 2), region="us")
run = flyte.run(trigger, events=events, day=datetime(2026, 8, 2, tzinfo=timezone.utc), region="us")
```
