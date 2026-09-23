---
title: Declare a factory
description: Describe how each artifact is made with sources and builds, map partitions between them, and name the outputs of multi-output tasks.
icon: pencil-square
weight: 1
variants: -flyte +union
---

# Declare a factory

> [!NOTE] Preview feature
> Factories are in preview. If you want changes or improvements, talk to the Union team.

This page builds the analytics factory from the [overview](./_index): `raw_events` is cleaned per day and region, combined across regions into `features`, and rolled into a report over a trailing three-day window.

## The tasks

The tasks are ordinary. They take plain inputs, return plain outputs, and don't import the factory. Turn on caching, because the task cache is how a factory decides that a partition is still fresh:

```python
from datetime import datetime

import flyte
from flyte.io import File

env = flyte.TaskEnvironment(name="analytics_tasks")


@env.task(cache="auto")
async def clean(raw: File, date: datetime, region: str, min_quality: int = 30) -> File:
    ...


@env.task(cache="auto")
async def featurize(per_region: list[File], date: datetime) -> File:
    ...


@env.task(cache="auto")
async def report(week: list[File], date: datetime) -> File:
    ...
```

Deploy them as usual with `flyte deploy analytics.py env`. In practice they often live in other teams' repositories.

## The factory

```python
from flyte.remote import Task
from flyteplugins.union import factory

clean_task = Task.get("analytics_tasks.clean", auto_version="latest")
featurize_task = Task.get("analytics_tasks.featurize", auto_version="latest")
report_task = Task.get("analytics_tasks.report", auto_version="latest")

raw_events = factory.source("raw_events")

events = factory.build("events").using(clean_task, raw=raw_events, min_quality=30)
features = factory.build("features").using(featurize_task, per_region=events.all("region"))
daily_report = factory.build("daily_report").using(
    report_task, week=features.window(date=factory.TimeRange(days=3))
)

analytics = factory.Factory("analytics", daily_report, description="Daily analytics report")
```

Nothing runs here. `source` and `build` only declare.

* **`factory.source(name)`** is an artifact made outside the factory. Its type and partition keys come from the registry, so `raw_events` needs to have been [published with partitions](../artifacts/partitions) at least once, or declared with `Artifact.declare`. Pass `project=` and `domain=` to read a source from another project.
* **`factory.build(name).using(task, **args)`** is one task call and the artifact it makes. `build(...)` says what is made, and `.using(...)` takes the task and its arguments, like `functools.partial`.
* **Handles form the graph.** `.using(...)` returns a handle for the artifact it makes. Passing that handle into another build is what connects them. There is no separate step for adding edges.
* **`factory.Factory(name, *targets)`** includes every build reachable by walking back from the artifacts you list. You can materialize any artifact in it, not only the ones listed.

To check the definition without registering anything, validate it and print the graph as Mermaid:

{{< tabs "check-graph" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
print(analytics.validate())   # structural problems, if any
print(analytics.graph())
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte factory deploy analytics.py --dry-run
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Mapping partitions between artifacts

A build's partitions follow from its inputs. Each argument that reads an artifact says which partitions of it a single call receives:

| Written as | The task receives | Example |
|---|---|---|
| `events` | The same partition: one value | `events[2026-08-02, us]` for `events[2026-08-02, us]` |
| `events.all("region")` | Every value of `region` for the same other keys: a `list` | All regions of `events` for 2026-08-02. The output loses `region` |
| `features.window(date=factory.TimeRange(days=3))` | A trailing window ending at this partition: a `list` | `features` for 07-31, 08-01, and 08-02 |
| `events.select(region="us")` | One pinned value, other keys matched: one value | Only the US `events` for each date. The output loses `region` |

So `events` is partitioned by `date` and `region` like `raw_events`. `features` is partitioned by `date` alone, because it reads every region, and `daily_report` keeps `date`.

### Passing partition values to a task

A task parameter named like a partition key receives that key's value for the partition being built. That's why `clean` gets `date` and `region` without either being written in `.using(...)`. A time partition arrives as a `datetime`.

If the parameter has a different name, bind it with `factory.partition`:

```python
factory.build("events").using(clean_task, raw=raw_events, day=factory.partition("date"))
```

### A build that adds a partition

When a build reads no artifacts, or its output has a key that no input carries, state its partitions:

```python
raw_rows = factory.build("raw_rows", partitions={"date": factory.Daily}).using(
    pull_task, day=factory.partition("date"), source_url="https://example.com/rows"
)
```

Time keys use `factory.Hourly`, `factory.Daily`, `factory.Weekly`, or `factory.Monthly`. String keys use `str` or `int`.

## Tasks with several outputs

The names given to `build` line up with the task's return tuple, left to right. Use `"_"` for an output that is not an artifact:

```python
# split returns (File, File): both are artifacts, made by one call.
clean_rows, rejects = factory.build("clean_rows", "rejects").using(split_task, raw=raw_rows)

# train returns (log, model, metrics, debug): only the middle two are artifacts.
model, metrics = factory.build("_", "model", "metrics", "_").using(train_task, rows=clean_rows)
```

The list must be as long as the return tuple, so deploy fails rather than guessing which output you meant. Asking for one output of a build builds all of them. The same task can back several builds with different constants, because builds are identified by what they make.

## Build options

`factory.build(...)` also takes:

* `kind`: the artifact kind, such as `"model"`, or a mapping of artifact name to kind for a multi-output build.
* `runcontext`: settings for this build's task call. The supported keys are `queue`, `env_vars`, and `service_account`.
* `description`: shown with the artifact.

Next, [deploy and materialize it](./materialize).
