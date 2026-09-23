---
title: Partitioned artifacts
description: Give each artifact version a day, hour, region, or other key with `partitions`, so you can address one slice of a dataset and list the slices you have.
icon: grid-3x3
weight: 7
variants: -flyte +union
---

# Partitioned artifacts

> [!NOTE]
> Requires flyte 2.10.0 or later.

An ingest job writes raw events every day for each region. If every run publishes a new version of one `raw_events` artifact, the versions pile up in a flat list. Finding "the US data for August 2" means reading descriptions, and a backfill has no way to ask which days already exist.

Partitions fix this. Each version records the day and region it holds, and those values are part of its identity:

```python
import asyncio
from datetime import date, timedelta

import flyte
import flyte.artifacts as artifacts
from flyte.io import File

env = flyte.TaskEnvironment(name="ingest")


@env.task(produces_artifacts=True)
async def ingest(day: date, region: str) -> File:
    file = await File.from_local(f"/data/{region}/{day}.parquet")
    return artifacts.new(
        file,
        artifacts.Metadata(name="raw_events", partitions={"date": day, "region": region}),
    )


@env.task
async def main(days: int = 3) -> None:
    start = date(2026, 8, 1)
    await asyncio.gather(
        *(ingest(start + timedelta(days=d), r) for d in range(days) for r in ("us", "eu"))
    )
```

One run of `main` fills six partitions. Now you can ask for exactly the slice you want:

```python
from flyte.remote import Artifact

us_aug_2 = Artifact.get("raw_events", date=date(2026, 8, 2), region="us")
```

See [Find and retrieve artifacts](./retrieving-artifacts) for ranges, listing partition values, and more. To run a task each time a partition lands, see [Trigger on partitions](../triggers/partition-triggers).

## Partition values

`Metadata.partitions` maps a partition key to a value. The Python type of the value decides what kind of partition it is:

| Value | Partition |
|---|---|
| `datetime.date` | Daily time partition |
| `datetime.datetime` | Hourly time partition, floored to the hour in UTC. A naive `datetime` is treated as UTC |
| `flyte.artifacts.TimePartition(value, "week")` or `"month"` | Weekly or monthly time partition. Use it for the coarser granularities, or to be explicit |
| Anything else | String partition, stored as `str(value)`. `7` becomes `"7"` |

A version can carry at most one time partition, plus any number of string partitions. A `None` value is rejected, since an unset partition is almost always a bug.

```python
# Hourly
artifacts.Metadata(name="raw_events_hourly", partitions={"hour": datetime(2026, 8, 1, 9, 30)})

# Monthly
artifacts.Metadata(
    name="monthly_report",
    partitions={"date": artifacts.TimePartition(date(2026, 8, 1), "month")},
)
```

## Republishing a partition

Publishing to a partition that already has a version adds a new version. It does not overwrite the old one. Reads by partition return the newest version, and older ones stay addressable by their version id. A rerun of a failed day is safe, and you can always see what the partition held before.

## Publishing from outside a task

`Artifact.create` takes the same `partitions` mapping. Use it to backfill partitions from data you already have:

```python
import flyte
from flyte.io import File
from flyte.remote import Artifact

flyte.init_from_config()

Artifact.create(
    File.from_local_sync("backfill/2026-07-31-us.parquet"),
    name="raw_events",
    partitions={"date": date(2026, 7, 31), "region": "us"},
)
```

## Fixing the keys up front

An artifact's partition keys are fixed by its first partitioned version. When several teams or jobs write the same artifact, declare the keys before anyone publishes, so the first writer can't fix the wrong ones by accident:

```python
Artifact.declare("raw_events", {"date": date, "region": str})
Artifact.declare("raw_events_hourly", {"hour": datetime, "region": str})
Artifact.declare("monthly_report", {"date": "month"})
```

A key maps to `date` (or `"day"`) for daily, `datetime` (or `"hour"`) for hourly, `"week"` or `"month"` for the coarser time partitions, and `str` for a string partition. Declaring again with the same keys is a no-op. Declaring different keys fails, because changing an artifact's keys means using a new name.

`Artifact.get_schema(name)` returns the keys an artifact has, whether they were declared or fixed by the first version.
