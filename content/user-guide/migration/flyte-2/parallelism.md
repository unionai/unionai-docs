---
title: Parallelism and fan-out
weight: 8
variants: +flyte +union
---

# Parallelism and fan-out

Flyte 1's `map_task` becomes `flyte.map`, and the idiomatic Flyte 2 approach to fan-out is Python `async`/`await` with `asyncio.gather`. See the [Asynchronous model](./overview#asynchronous-model) guide for the concepts, and [Migration](./overview) for the overall approach.

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

See the [Asynchronous model](./overview#asynchronous-model) guide for the concepts behind async execution.

### Choosing `flyte.map` vs `asyncio.gather`

| Feature | `flyte.map` (sync) | `asyncio.gather` (async) |
|---|---|---|
| Syntax | `list(flyte.map(fn, items))` | `await asyncio.gather(*tasks)` |
| Concurrency limit | Built-in `concurrency=N` | Use `asyncio.Semaphore` |
| Streaming / as-completed | No | Yes, via `asyncio.as_completed()` |
| Error handling | `return_exceptions=True` | Check return type |

Use **`flyte.map`** for the smallest change from Flyte 1 `map_task`, or when you're stuck in synchronous code. Use **`asyncio.gather`** for new code where you want streaming results or fine-grained concurrency control.

### Concurrency control and error handling

`map_task`'s `concurrency` and `min_success_ratio` become an `asyncio.Semaphore` and `return_exceptions=True`:

```python
import asyncio

@env.task
async def main(items: list[int], max_concurrent: int = 5) -> list[str]:
    sem = asyncio.Semaphore(max_concurrent)

    async def process_with_limit(item: int) -> str:
        async with sem:
            return await process_item(item)

    tasks = [process_with_limit(i) for i in items]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    return [r for r in results if not isinstance(r, Exception)]
```

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

- [Data types and I/O](./data-io): files, DataFrames, and dataclasses
- [ML workloads](./ml-workloads): training, HPO, and batch inference
