---
title: Find and retrieve artifacts
description: Look up artifacts by name, version, partition, range, source run, kind, or attributes, from Python or the CLI, and pass them to runs.
icon: search
weight: 8
variants: -flyte +union
---

# Find and retrieve artifacts

Different consumers ask different questions of the registry. An evaluation job wants the latest model. A backfill wants the newest version of every August partition. A dashboard wants the list of regions that have data, and an auditor wants everything a given run produced. Each of these is one call on `flyte.remote.Artifact`, or one `flyte get artifact` command.

The recipes below go from simple to specific. The Python calls need a client, so call `flyte.init_from_config()` first. All of them accept `project=` and `domain=` and default to your config.

```python
from datetime import date, datetime

import flyte
from flyte.remote import Artifact

flyte.init_from_config()
```

## By name and version

{{< tabs "by-name" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
model = Artifact.get("trained-model")                  # latest version
model = Artifact.get("trained-model", version="v3")    # a pinned version
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte get artifact trained-model        # every version, newest first
flyte get artifact trained-model v3     # one version
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## One partition

For a [partitioned artifact](./partitions), pass one value per partition key to get the latest version of that partition:

{{< tabs "one-partition" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
events = Artifact.get("raw_events", date=date(2026, 8, 2), region="us")
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte get artifact raw_events --partition date=2026-08-02 --partition region=us
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

A `date` matches a daily partition, a `datetime` an hourly one, and a string that reads as an ISO date or timestamp is treated as a time value too. If a key name clashes with an argument of `get` (such as `name` or `version`), pass it in a `partitions={...}` mapping instead.

## A range of partitions

`listall` takes a `(start, end)` tuple on the time key, inclusive at both ends, and a list on a string key to match any of its values. Add `latest_per_partition=True` to get one version per partition instead of every version:

{{< tabs "range" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
august = list(
    Artifact.listall(
        "raw_events",
        date=(date(2026, 8, 1), date(2026, 8, 31)),
        region=["us", "eu"],
        latest_per_partition=True,
    )
)
for a in august:
    print(a.partitions, a.version)
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte get artifact raw_events --partition date=2026-08-01..2026-08-31 --partition region=us,eu --latest-per-partition
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

This is the query a backfill plans with: compare the partitions that came back against the days you expect, and fill the gaps.

## The values a partition key has

`partition_values` returns the distinct values of one key, sorted. Other keys narrow it:

```python
Artifact.partition_values("raw_events", "region")                      # ["eu", "us"]
Artifact.partition_values("raw_events", "date", region="us")           # [date(2026, 8, 1), ...]
```

Time keys come back as `date` values, or `datetime` for hourly partitions. `Artifact.get_schema(name)` tells you which keys an artifact has.

## By where it came from, or what it is

`listall` filters server-side on provenance and metadata. Combine as many as you need:

{{< tabs "provenance" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
Artifact.listall(source_run="my-run")                                  # everything a run produced
Artifact.listall(source_run="my-run", source_action="a0")              # one action of that run
Artifact.listall(source_external_ref="s3://partner-bucket/drop/2026-08-18.csv")
Artifact.listall(kind="model", attrs={"framework": ["torch", "jax"]})  # any listed value matches
Artifact.listall("trained-model", created_after=datetime(2026, 8, 1), limit=10)
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte get artifact --source-run my-run
flyte get artifact --kind model --attr framework=torch
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

`listall` returns an iterator, newest first.

## Browsing names

{{< tabs "browse-names" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
for group in Artifact.list_names(search="events"):
    print(group)
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte get artifact                    # every name, with its latest version and version count
flyte get artifact --search events
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Passing what you found to a run

An `Artifact` binds to a task input of the matching type. The task receives a plain `File`, `Dir`, or `DataFrame`:

```python
run = flyte.run(summarize, events=Artifact.get("raw_events", date=date(2026, 8, 2), region="eu"))
```

A task that takes a list accepts a list of artifacts. `listall` is an iterator, so materialize it first:

```python
august = list(Artifact.listall("raw_events", date=(date(2026, 8, 1), date(2026, 8, 31)), latest_per_partition=True))
run = flyte.run(monthly_rollup, days=august)
```

To load the data in a notebook or script instead, see [reading an artifact's value directly](./task-outputs#reading-an-artifacts-value-directly).

## Things to know

* `get` returns exactly one version. It rejects a range or a list (use `listall`) and a version combined with partition values, since a version already names one artifact.
* `latest_per_partition` needs an artifact name.
* A read by partition raises an error when that partition has no version yet.
