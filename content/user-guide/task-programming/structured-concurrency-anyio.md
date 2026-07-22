---
title: Structured concurrency with anyio
weight: 19
variants: +flyte +union
---

# Structured concurrency with anyio

Flyte builds a task's dependency graph from what you `await`, not from any particular async library.
`asyncio` is the default and the one used throughout the [Fanout](./fanout), [Controlling parallel execution](./controlling-parallelism), and [Task dependencies and ordering](./task-dependencies) guides, but it is not the only option.
Any structured-concurrency runtime that drives coroutines works, and [`anyio`](https://anyio.readthedocs.io/) is a popular one.
Its **task groups** give you a top-level alternative to raw `asyncio.gather` / `asyncio.create_task`, with clearer lifetime and error-propagation semantics.

Use `anyio` when you want structured concurrency (a scope that owns the tasks it spawns, waits for all of them on exit, and cancels the siblings automatically if one fails) instead of tracking `asyncio.create_task` handles by hand.

## The task-group pattern

An `anyio` task group is an `async with` block. You spawn work into it with `start_soon`, and the block does not exit until every spawned task has finished. Because task groups don't return the spawned tasks' values directly, this example uses [`aioresult`](https://aioresult.readthedocs.io/)'s `ResultCapture` to collect each result.

We define a reusable environment and a simple per-item task. `anyio` and `aioresult` are ordinary pip dependencies, so we add them to the image:

```python
from dataclasses import dataclass

import aioresult
import anyio

import flyte

env = flyte.TaskEnvironment(
    name="anyio_batch",
    resources=flyte.Resources(cpu="1"),
    image=flyte.Image.from_debian_base(name="anyio").with_pip_packages("anyio", "aioresult"),
)


@dataclass
class InferenceRequest:
    feature_a: float
    feature_b: float


@env.task
async def predict_one(request: InferenceRequest) -> float:
    # A dummy linear model: 2 * feature_a + 3 * feature_b + bias(=1.0)
    return 2.0 * request.feature_a + 3.0 * request.feature_b + 1.0
```

The driver task fans out over the batch inside a task group:

```python
@env.task
async def predict_batch(requests: list[InferenceRequest]) -> list[float]:
    captured = []
    async with anyio.create_task_group() as tg:
        # Start each prediction; they run at the same time.
        for req in requests:
            captured.append(aioresult.ResultCapture.start_soon(tg, predict_one, req))
    # The `async with` block has exited, so every task has completed.
    return [c.result() for c in captured]
```

What happens here mirrors an `asyncio.gather` fanout, but with structured-concurrency guarantees:

1. **`start_soon` schedules each `predict_one`** into the group. As with `asyncio`, Flyte runs each action in its own container, so the batch executes in true parallel across the cluster. The runtime you use to express concurrency does not change how Flyte distributes the work.
2. **Leaving the `async with` block is the fan-in edge.** The group blocks until all spawned tasks finish, exactly as `await asyncio.gather(...)` would. `predict_batch` cannot return until every prediction is in.
3. **`ResultCapture` collects the return values**, which you read with `.result()` after the group closes.

> [!NOTE]
> Task groups give you cancellation for free: if any task in the group raises, `anyio` cancels the remaining siblings and propagates the error out of the `async with` block. You get the "cancel the rest on failure" behavior that requires manual `.cancel()` bookkeeping with `asyncio` (see [Abort and cancel actions](./abort-tasks#canceling-actions-programmatically)).

## When to use anyio

Reach for `anyio` when:

- You want **structured concurrency** (spawned work is scoped to a block, awaited on exit, and cancelled together on error) rather than manually pairing `asyncio.create_task` handles with `asyncio.gather`.
- Your code (or a library you depend on) already uses `anyio` or `trio`, and you want one consistent concurrency model.

Stay with `asyncio` when:

- You just need to fan out and collect results. `await asyncio.gather(...)` is simpler (see [Fanout](./fanout)).
- You need fine-grained, dependency-driven scheduling where different consumers await different producers (see [Task dependencies and ordering](./task-dependencies)).

Either way, the underlying model is the same: Flyte reads the dependency graph from your `await`s and turns concurrent coroutines into distributed parallel actions.
