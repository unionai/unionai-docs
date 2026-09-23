---
title: Materialize and backfill
description: Deploy a factory, then build one partition or a whole range, preview the plan, rebuild after a code change, and resume a failed backfill.
icon: play-circle
weight: 2
variants: -flyte +union
---

# Materialize and backfill

Once a factory is [declared](./declare-a-factory), there is one verb for running it: **materialize**. You name an artifact and a partition or a range, and the factory builds whatever is needed to produce it.

## Deploy

Deploy the tasks, then the factory:

{{< tabs "deploy" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
import flyte

flyte.init_from_config()

flyte.deploy(env)       # the tasks
analytics.deploy()      # the factory
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte deploy analytics.py env
flyte factory deploy analytics.py
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

`flyte factory deploy` checks every build against its deployed task, including argument names, required parameters, partition mappings, and the number of outputs. It checks every source against the registry, then registers the factory as a task of type `factory`. Mistakes fail here, with a message per build, instead of halfway through a backfill. Add `--dry-run` (or `analytics.deploy(dryrun=True)`) to validate without registering.

## One partition

{{< tabs "one-partition" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
run = analytics.materialize(daily_report, date="2026-08-02")
run.wait()
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte factory materialize analytics daily_report --partition date=2026-08-02 --wait
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

The factory walks back from `daily_report[2026-08-02]`. That partition needs `features` for three days, each of which needs `events` for every region, each of which needs `raw_events`. The whole materialization is one run, and each partition built along the way is a child action you can open in the UI.

In Python, `materialize` returns an ordinary `flyte.remote.Run`.

## A range: backfill

A backfill is the same command over a range:

{{< tabs "range" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
run = analytics.materialize(daily_report, date="2026-08-01..2026-08-31")
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte factory materialize analytics daily_report --partition date=2026-08-01..2026-08-31
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

`a..b` is an inclusive range, expanded at the partition's granularity, and `a,b` lists values. The range crosses with the other keys, so this builds `events` for every region on every day that a report needs. Partitions build in parallel. Ordering follows the graph, not the calendar: the report for August 31 waits only on its own three-day window.

* **Rerunning resumes.** Run the same command again. Everything already built is a cache hit, so only the failed partitions and what depends on them run. There is no separate backfill object or resume command.
* **Failures are partial.** Partitions that succeeded are published and usable. A failed partition blocks only what depends on it, and the run fails naming them.
* **A missing source blocks only its dependents.** If `raw_events` has no version for one day, the rest of the range still builds.

## Preview the plan

{{< tabs "plan" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
run = analytics.materialize(daily_report, date="2026-08-01..2026-08-31", plan_only=True)
run.wait()
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte factory plan analytics daily_report --partition date=2026-08-01..2026-08-31
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

`plan` is short for `materialize --plan --wait`. It launches nothing and prints, per artifact, how many partitions are in each state:

| State | Meaning |
|---|---|
| `source` | A source partition found in the registry |
| `missing` | A source partition that doesn't exist, or a build partition with no published version yet |
| `existing` | A published version exists. The cache decides at run time whether it is reused |
| `reused` | During a run: a cache hit, nothing rebuilt |
| `built` | During a run: the task ran and a new version was published |
| `failed` / `blocked` | The task failed, or something upstream of it did |

## Freshness is the task cache

A partition is fresh if calling its task with the same inputs is a cache hit. That means the same task version, the same upstream artifact versions, the same partition values, and the same constants. So there's nothing to configure:

* **A code change** to `clean` changes its cache version, so `events` and everything downstream rebuild.
* **A new upstream version**, such as a corrected `raw_events` for one day, changes the inputs for that day only.
* **A task without caching** rebuilds every time. Use `cache="auto"` on factory tasks.

To force work anyway:

{{< tabs "rebuild" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
# Treat every partition of one build as stale.
analytics.materialize(daily_report, date="2026-08-01..2026-08-31", rebuild=["events"])

# Ignore the cache everywhere.
analytics.materialize(daily_report, date="2026-08-01..2026-08-31", rebuild_all=True)
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
# Treat every partition of one build as stale.
flyte factory materialize analytics daily_report --partition date=2026-08-01..2026-08-31 --rebuild events

# Ignore the cache everywhere.
flyte factory materialize analytics daily_report --partition date=2026-08-01..2026-08-31 --rebuild-all
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

`--rebuild` names a build by an artifact it makes, since the same task can back several builds. A task name also works.

## Other options

| Python | CLI | Effect |
|---|---|---|
| `params={"events": {"min_quality": 20}}` | `--param events.min_quality=20` | Override a build's constant for this materialization only |
| `concurrency=50` | `--concurrency 50` | Limit how many partitions build at once |
| `queue="gpu"` | `--queue gpu` | Run the materialization and every build on this queue |
| `downstream=True` | `--downstream` | Also refresh downstream partitions that become stale |
| `run.wait()` | `--wait` | Wait for the run to finish. The CLI also prints the plan with results |

## What gets published

Every artifact built during a materialization is published as a version with its partition values, not only the target you asked for. Each version's source is the action that ran the task, so [lineage](../artifacts/lineage) points at the work that made it. From there the results behave like any other artifact: [retrieve them](../artifacts/retrieving-artifacts) by partition, [trigger on them](../triggers/partition-triggers), or mount them in an [app](../artifacts/artifacts-in-apps).

## Inspect factories

{{< tabs "inspect" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
print(analytics.graph())       # the definition, as Mermaid
print(analytics.validate())    # structural problems, if any
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte factory get                      # factories in this project and domain
flyte factory get analytics --graph    # one factory's definition, as Mermaid
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}
