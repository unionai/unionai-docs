---
title: Task dependencies and ordering
weight: 19
variants: +flyte +union
---

# Task dependencies and ordering

Flyte 1 built a workflow's DAG (directed acyclic graph) explicitly: you declared nodes and wired their edges with the `>>` operator or `create_node`.
Flyte 2 has no such API. Instead, **the dependency graph is inferred from the data you `await`**.
When you await one task's result and pass it into another, Flyte records the edge; tasks that share no data run independently.
This page shows how to express the ordering patterns you used to build by hand (sequencing, fan-out, fan-in, and fine-grained dependency-driven scheduling) using ordinary Python `asyncio`.

If you are coming from Flyte 1, read [Parallelism and fan-out](../migration/flyte-2/parallelism) first for the migration mapping.

## The dependency graph is implicit

There is nothing special to learn: a data dependency *is* the edge.

```python
import asyncio

import flyte

env = flyte.TaskEnvironment(name="pipeline")


@env.task
async def extract() -> str:
    return "raw"


@env.task
async def transform(data: str) -> str:
    return f"transformed({data})"


@env.task
async def load(data: str) -> str:
    return f"loaded({data})"


@env.task
async def main() -> str:
    raw = await extract()          # runs first
    clean = await transform(raw)   # waits for extract — it consumes `raw`
    return await load(clean)       # waits for transform — it consumes `clean`
```

Each `await` means "wait for this to finish before continuing," so a chain of `await`s that pass results downstream runs sequentially, exactly like a linear Flyte 1 workflow. You never declare the edges; passing `raw` into `transform` and `clean` into `load` *is* the DAG.

## Ordering without a data dependency

Sometimes you need task `B` to run after task `A` even though `B` does not consume `A`'s output. For example, `A` writes to a store that `B` reads out-of-band, or `A` must finish before you send a notification.

Because ordering comes from `await`, you force it simply by awaiting `A` before invoking `B`:

```python
@env.task
async def main() -> str:
    result = await transform(await extract())
    await notify()   # runs after transform completes, though it uses no upstream output
    return result
```

You do not need a special "run after" construct: a preceding `await` is the ordering primitive.

## Fan-out and fan-in

**Fan-out** launches independent tasks concurrently; **fan-in** collects their results into a single downstream task.
Use [`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) to await several tasks at once. Flyte runs each in its own container in parallel (see [Fanout](./fanout)):

```python
@env.task
async def combine(a: str, b: str, c: str) -> str:
    return f"{a} + {b} + {c}"


@env.task
async def main() -> str:
    # Fan-out: three tasks start together and run in parallel
    a, b, c = await asyncio.gather(extract(), extract(), extract())
    # Fan-in: one task depends on all three results
    return await combine(a, b, c)
```

The `await asyncio.gather(...)` establishes the fan-in edge: `combine` cannot start until all three upstream tasks have produced their results.

## Dependency-driven scheduling

The pattern that most often motivates "replicating DAG behavior" is **fine-grained scheduling**: a diamond or fork where each downstream task should start the moment *its own* upstreams finish, without waiting for unrelated slow tasks.

Consider three producers of different durations and four consumers with different dependencies:

- `needs_short` depends on `short` only
- `needs_medium` depends on `medium` only
- `needs_long` depends on `long` only
- `needs_all` depends on all three

A single `await asyncio.gather(short, medium, long)` before starting any consumer would make every consumer wait for the slowest producer. To let each consumer start as early as possible, start the producers as [`asyncio.create_task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task) handles, then wrap each consumer in a small helper coroutine that awaits only the handles it needs. Launch all the helpers together with `asyncio.gather`:

```python
@env.task
async def long_producer() -> str:
    await asyncio.sleep(10)
    return "long"


@env.task
async def medium_producer() -> str:
    await asyncio.sleep(3)
    return "medium"


@env.task
async def short_producer() -> str:
    await asyncio.sleep(1)
    return "short"


@env.task
async def needs_short(x: str) -> str:
    return f"needs_short({x})"


@env.task
async def needs_medium(x: str) -> str:
    return f"needs_medium({x})"


@env.task
async def needs_long(x: str) -> str:
    return f"needs_long({x})"


@env.task
async def needs_all(long: str, medium: str, short: str) -> str:
    return f"needs_all({long}, {medium}, {short})"


@env.task
async def main() -> str:
    # Start all producers concurrently and keep their handles
    long_task = asyncio.create_task(long_producer())
    medium_task = asyncio.create_task(medium_producer())
    short_task = asyncio.create_task(short_producer())

    # Each helper awaits only the producers it actually depends on,
    # so it starts as soon as those specific producers finish.
    async def run_needs_short() -> str:
        return await needs_short(await short_task)

    async def run_needs_medium() -> str:
        return await needs_medium(await medium_task)

    async def run_needs_long() -> str:
        return await needs_long(await long_task)

    async def run_needs_all() -> str:
        long_r, medium_r, short_r = await asyncio.gather(long_task, medium_task, short_task)
        return await needs_all(long_r, medium_r, short_r)

    # Launch every branch concurrently; each resolves on its own dependencies
    results = await asyncio.gather(
        run_needs_short(),   # starts after ~1s
        run_needs_medium(),  # starts after ~3s
        run_needs_long(),    # starts after ~10s
        run_needs_all(),     # starts after ~10s
    )
    return str(results)
```

`needs_short` starts about a second in, as soon as `short_producer` returns. It does not wait for the 10-second `long_producer`. Awaiting an `asyncio` task handle more than once is safe: the handle caches its result, so `long_task` can feed both `run_needs_long` and `run_needs_all` without re-running the producer.

> [!NOTE]
> Reach for helper coroutines that each `await` their specific handles, rather than a manual completion loop that inspects [`asyncio.as_completed`](https://docs.python.org/3/library/asyncio-task.html#asyncio.as_completed) and dispatches downstream tasks by hand. Hand-rolled dispatch loops are easy to get wrong: a mis-tracked "has this fired yet?" check can launch the same downstream task twice. Let the dependency edges fall out of `await` instead.

## When to reach for `as_completed`

Use [`asyncio.as_completed`](https://docs.python.org/3/library/asyncio-task.html#asyncio.as_completed) when you want to process results **in completion order** (for example, streaming each result into a running reduction as it lands) rather than to encode a fixed dependency graph:

```python
@env.task
async def main() -> list[str]:
    tasks = [asyncio.create_task(short_producer()) for _ in range(10)]
    processed = []
    for task in asyncio.as_completed(tasks):
        result = await task
        processed.append(result)  # handle each result the moment it arrives
    return processed
```

For a worked streaming/reduce example, see [Fanout](./fanout) and [Controlling parallel execution](./controlling-parallelism).

## Summary

- Flyte 2 has no explicit DAG-construction API; dependencies come from the data you `await`.
- Sequence tasks by awaiting them in order: a preceding `await` orders even tasks that share no data.
- Fan out with `asyncio.gather`; fan in by awaiting several results into one downstream task.
- For fine-grained scheduling, keep producer handles from `asyncio.create_task` and have each consumer await only the handles it depends on, so it starts as early as possible.
- Prefer letting `await` express the graph over hand-rolled completion-tracking loops.
