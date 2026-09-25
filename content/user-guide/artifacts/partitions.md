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

> [!WARNING] Partition keys are fixed per artifact name
> The first partitioned version of `raw_events` fixes its keys to `date` and `region`. A later version published with different keys does not change them, and neither does adding partitions to an artifact that was declared without any. To use different keys, publish under a new artifact name. See [Partition keys are fixed](#partition-keys-are-fixed).

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

Publishing from a script or the CLI takes the same partition values. Use it to backfill partitions from data you already have:

{{< tabs "publish-partition" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

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

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte create artifact raw_events --from-file backfill/2026-07-31-us.parquet \
    --partition date=2026-07-31 --partition region=us
```

An ISO date (`2026-07-31`) is a daily partition, an ISO hour (`2026-07-31T09`) an hourly one, and anything else a string partition. Weekly and monthly partitions need the Python API. `--partition` on `flyte create artifact` is newer than the rest of this page; if `flyte create artifact --help` doesn't list it, upgrade flyte.

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Partition keys are fixed

An artifact name has one set of partition keys. They are fixed once, by whichever comes first:

* The first version published **with** partitions. A version published without partitions never fixes the keys.
* A declaration with `Artifact.declare`. See [Fixing the keys up front](#fixing-the-keys-up-front).

After that, no later version changes them. For `raw_events`, fixed to `date` and `region`:

| You publish | Result |
|---|---|
| A version with an extra key, such as `channel` | The keys stay `date` and `region` |
| A version without one of the keys, such as `date` alone | The keys stay `date` and `region` |
| A version without partitions | The keys stay `date` and `region` |

The same holds for an artifact declared with no partitions: a version published with partitions leaves it unpartitioned.

There is one case where adding partitions does change an artifact: its earlier versions have no partitions, and it was never declared. Then the first partitioned version fixes the keys, and the earlier versions no longer match them. To prevent this, declare the artifact with no partitions.

A version whose keys differ from the artifact's is not rejected. It is published after the task that made it has finished, so the registry stores it as published instead of failing the run. Compare its `partitions` with `Artifact.get_schema(name)` to find it.

### Changing an artifact's keys

To use different keys, publish under a new artifact name. Publishing versions with the new keys does not change the old name, and declaring different keys fails.

Deleting versions does not reliably reset the keys either. Declared keys stay after every version is deleted. Keys fixed by a first version are dropped only when the last version is deleted.

## Fixing the keys up front

When several teams or jobs write the same artifact, declare the keys before anyone publishes, so the first writer can't fix the wrong ones by accident:

```python
Artifact.declare("raw_events", {"date": date, "region": str})
Artifact.declare("raw_events_hourly", {"hour": datetime, "region": str})
Artifact.declare("monthly_report", {"date": "month"})
```

A key maps to `date` (or `"day"`) for daily, `datetime` (or `"hour"`) for hourly, `"week"` or `"month"` for the coarser time partitions, and `str` for a string partition. Declaring again with the same keys is a no-op. Declaring different keys fails, because changing an artifact's keys means using a new name.

An artifact that is read by version, not by partition, can be declared with no keys. Then a version published with partitions by mistake can't make it partitioned:

```python
Artifact.declare("tracking_data", {})
```

`Artifact.get_schema(name)` returns the keys an artifact has, and whether they were declared or fixed by the first version.
