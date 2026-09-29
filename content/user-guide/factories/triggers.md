---
title: Trigger a factory
description: Materialize automatically when a source gets a new version or on a schedule.
icon: lightning-charge
weight: 4
variants: -flyte +union
---

# Trigger a factory

> [!NOTE] Preview feature
> Factories are in preview. If you want changes or improvements, talk to the Union team.
>
> Triggers on factories require `flyteplugins-union` 0.15.0 or later.

A factory can materialize itself. A trigger starts a materialization when a source gets a new version, or on a schedule. Add triggers with `factory.on` and pass them to the factory:

```python
sensors = factory.Factory(
    "sensors",
    daily,
    triggers=[
        factory.on(readings),                        # each new version of the readings source
        factory.on(flyte.Cron("0 1 * * *"), daily),  # every night at 01:00
    ],
)
```

Each trigger starts an ordinary materialization, and a partition that is already up to date is a cache hit. The rest of this page covers the details: which partitions a source event or a schedule materializes, filters, lags and timezones, names, and limits.

## Declare triggers

`factory.on(event, *targets)` takes a source handle, a `flyte.Cron`, or a `flyte.FixedRate`, and optionally the artifacts to materialize. Every form, on one graph:

```python
import flyte
from flyteplugins.union import factory

readings = factory.source("readings", type=flyte.io.File, partitions={"date": factory.Daily, "site": str})
summary = factory.build("summary").using(summarize, readings=readings)
daily = factory.build("rollup").using(rollup, summaries=summary.all("site"))

sensors = factory.Factory(
    "sensors",
    daily,
    triggers=[
        factory.on(readings),
        factory.on(readings, summary, site="north", name="north-only"),
        factory.on(flyte.FixedRate(60), name="hourly"),
        factory.on(flyte.Cron("0 1 * * *"), daily, lag=factory.TimeRange(days=1), name="yesterday"),
    ],
)
```

`flyte factory deploy` registers the triggers with the factory. A triggered materialization is an ordinary run, listed on the factory's **Materializations** tab. Its **Triggers** tab lists the factory's triggers. When nothing has changed, every build is a cache hit, so a trigger that fires often costs little.

## When a source gets a new version

`factory.on(source)` fires when a new version of that source is published. It materializes the partition the new version belongs to:

* **The partition comes from the event.** When `readings[2026-09-28, north]` is published, `rollup` is materialized for 2026-09-28. On a key the source doesn't carry, the target is materialized for every value the registry knows.
* **Targets default to what the factory produces downstream of the source.** Name targets to narrow it, as `north-only` does with `summary`. A target doesn't have to be one of the artifacts listed in `Factory(...)`.
* **Filter by partition** with keyword arguments: `site="north"` fires only for versions whose `site` is `north`. Filters match string keys. `name` and `lag` are the function's own arguments, so a key with either name can't be filtered on.

Only a source can fire a trigger. To act on each new version of something the factory builds, add a build that reads it: materializing the new build builds what it reads first.

## On a schedule

`factory.on(flyte.Cron(...))` and `factory.on(flyte.FixedRate(...))` fire on a schedule, and targets default to everything the factory produces:

* **The partition is the fire time**, rounded down to the target's granularity. A daily target that fires at 14:00 builds that day.
* **`lag=` moves it back.** `yesterday` fires at 01:00 and builds the previous day, when that day's data is complete.
* **The day is named in the schedule's timezone.** `flyte.Cron("0 22 * * *", timezone="America/Los_Angeles")` builds that day in Los Angeles, not the next day in UTC.

A schedule that fires every hour on a factory whose inputs rarely change is a cheap way to keep it fresh: most runs are all cache hits and finish in seconds.

## Names and inputs

Each trigger has a name. It defaults to one derived from the event, such as `on-readings` or `every-60m`. Pass `name=` to choose one, using lowercase letters, digits, and `-`. A trigger with several targets registers one trigger per target, named `<name>-<target>`.

A factory with triggers gets a few extra inputs that the triggers fill in: `trigger`, `at`, and one `at_<key>` for each partition key a source event carries. You don't set them yourself. A factory without triggers keeps its original inputs.

## Limits

* A source must be in the factory's project and domain to fire a trigger.
* One source event starts one run per target. A trigger with many targets starts that many runs, and they share cache hits for what they have in common.
