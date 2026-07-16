---
title: Parallelism and fan-out
weight: 7
variants: +flyte +union
---

# Parallelism and fan-out

Flyte 1's `map_task` becomes `flyte.map`, and the idiomatic Flyte 2 approach to fan-out is Python `async`/`await` with `asyncio.gather`. See the [Asynchronous model](./async) guide for the concepts, and [Migration](./migration) for the overall approach.

## Fan-out: `map_task`

`map_task()` becomes `flyte.map()`, a near drop-in replacement. The one catch: `flyte.map` returns a generator, so wrap it in `list()`. For new code, the idiomatic approach is Python `async`/`await` with `asyncio.gather()`, which gives you finer control over concurrency and error handling.

{{< tabs "migration-map-task" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/map_task_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2 (flyte.map)" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/map_task_v2.py" fragment="sync" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2 (asyncio.gather)" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/map_task_v2.py" fragment="async" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

See the [Asynchronous model](./async) guide and [Parallelism and async](../../../api-reference/migration/parallelism-and-async) for the full story.

## Data backfills

Reprocessing a range of dates is a textbook `@dynamic` use case in Flyte 1, because the number of days is only known at runtime. In Flyte 2 it's a plain task that builds the date range and fans the days out with `asyncio.gather`.

{{< tabs "migration-backfill" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/data_backfill_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/data_backfill_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

For fine-grained concurrency control (semaphores, `as_completed`, error handling), see [Fanout](../../task-programming/fanout).

## Next

- [Data types and I/O](./data-io) — files, DataFrames, and dataclasses
- [ML workloads](./ml-workloads) — training, HPO, and batch inference
