---
title: Streaming map-reduce
weight: 19
variants: +flyte +union
---

# Streaming map-reduce

When you [fan out](./fanout) with [`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather), you wait for **every** task to finish before doing anything with the results.
For a map-reduce workload that is wasteful: the reduce step sits idle until the slowest mapper returns.

A better pattern is to process results **as they complete** — accumulating them into batches and kicking off reduce operations incrementally, while the remaining map tasks are still running.
This is a *gradual* (or *streaming*) map-reduce, and it is built on the standard-library [`asyncio.as_completed`](https://docs.python.org/3/library/asyncio-task.html#asyncio.as_completed) function.

## When to use it

Reach for streaming map-reduce when:

- Map tasks have **uneven durations**, so waiting for the slowest one wastes time the faster ones could spend reducing.
- You are processing a **large number of items** and want to reduce in batches rather than holding every intermediate result in memory at once.
- The reduce step is **associative** — batch results can themselves be reduced into a final result (counts, sums, aggregations, embeddings, inference outputs).

If you simply need all results before a single reduce, plain `asyncio.gather` (see [Fanout](./fanout)) is simpler.
If your goal is to *cap* how many map tasks run at once, see [Controlling parallel execution](./controlling-parallelism); the two patterns compose.

## Example

We define an environment and two tasks: one that maps over a single item, and one that reduces a batch of results.

```python
import asyncio
import random

import flyte

env = flyte.TaskEnvironment(
    name="streaming_map_reduce",
    resources=flyte.Resources(cpu="1"),
)


@env.task
async def process_item(item: str) -> str:
    print(f"Processing {item}", flush=True)
    # Simulate varying processing times so results finish out of order.
    await asyncio.sleep(random.uniform(1, 5))
    return f"processed_{item}"


@env.task
async def reduce_batch(items: list[str]) -> str:
    print(f"Reducing batch of {len(items)} items")
    return f"reduced_batch_of_{len(items)}_items"
```

{{< variant union >}}
{{< markdown >}}
#### Speed up the map step with reusable containers

The map step fans out many short `process_item` actions, each of which would otherwise pay container-startup cost. On {{< key product_name >}} you can make them reuse warm workers instead by giving the environment a [reusable container](../task-configuration/reusable-containers):

```python
reusable_image = flyte.Image.from_debian_base(name="streaming").with_pip_packages("unionai-reuse>=0.1.10")

env = flyte.TaskEnvironment(
    name="streaming_map_reduce",
    resources=flyte.Resources(cpu="1"),
    reusable=flyte.ReusePolicy(replicas=20, idle_ttl=30),
    image=reusable_image,
)
```

Reusable containers require a {{< key product_name >}} backend, so this optimization is not available when running on an open-source Flyte backend.
{{< /markdown >}}
{{< /variant >}}

### The driver task

The driver fans out all the map tasks up front, then walks the results in completion order with `asyncio.as_completed`.
Each time a batch fills up, it launches a `reduce_batch` action **without blocking** — the loop keeps consuming newly completed map results while the reduce runs.

```python
@env.task
async def streaming_reduce_processing() -> str:
    input_items = [f"item_{i}" for i in range(100)]

    # Fan out: start every item task immediately.
    tasks = [asyncio.create_task(process_item(item)) for item in input_items]

    batch_size = 10
    accumulated_values: list[str] = []
    reducers: list[asyncio.Task] = []

    print(f"Started {len(tasks)} tasks, will reduce in batches of {batch_size}")

    # Consume results as each task finishes, rather than waiting for all of them.
    for task in asyncio.as_completed(tasks):
        result = await task
        accumulated_values.append(result)

        # Once a batch has accumulated, kick off a reduce without blocking the loop.
        if len(accumulated_values) >= batch_size:
            print(f"Triggering reduce for batch of {len(accumulated_values)}")
            reducer_task = asyncio.create_task(reduce_batch(accumulated_values.copy()))
            reducers.append(reducer_task)
            accumulated_values.clear()

    # Reduce any stragglers that did not fill a full batch.
    if accumulated_values:
        print(f"Handling final batch of {len(accumulated_values)} stragglers")
        reducers.append(asyncio.create_task(reduce_batch(accumulated_values)))

    # Wait for every batch reduce to finish.
    reduced_results = await asyncio.gather(*reducers)

    # Combine the batch results into a single final result.
    final_result = await reduce_batch(reduced_results)

    print(f"Completed {len(reducers)} reduce operations, final result: {final_result}")
    return final_result
```

### Running the example

```python
if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(streaming_reduce_processing)
    print(run.url)
```

## How it works

The key building blocks are all standard `asyncio`:

1. **`asyncio.create_task(process_item(item))`** schedules each map action. Because `process_item` is a Flyte task, each of these runs in its own container on the cluster — the fanout is real distributed parallelism, not single-machine concurrency (see [Fanout](./fanout) for how Flyte turns `asyncio` into distributed execution).
2. **`asyncio.as_completed(tasks)`** yields the task handles in the order they *finish*, not the order they were submitted. This is what lets the driver react to the fastest map results first.
3. **`asyncio.create_task(reduce_batch(...))`** launches each reduce as its own Flyte action and appends it to `reducers` without awaiting it, so map consumption and reduction overlap.
4. **`asyncio.gather(*reducers)`** joins all the in-flight batch reduces before the final combine step.

The result is a pipeline where reduce work begins as soon as the first batch of map results is ready, instead of after the last map task returns.

> [!NOTE]
> `as_completed` returns awaitables in completion order but gives you no control over *how many* map tasks run at once — it schedules all of them.
> To bound the map fanout as well, combine this pattern with an `asyncio.Semaphore` or `flyte.map(concurrency=...)` from [Controlling parallel execution](./controlling-parallelism).
