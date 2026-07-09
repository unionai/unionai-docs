---
title: Mapping over inputs
weight: 17
variants: +flyte +union
---

# Mapping over inputs

`flyte.map` applies a single task to every item of one or more input iterables, running the
invocations in parallel across the cluster and yielding their results **in input order**.
It is the structured way to [fan out](./fanout) uniform work: instead of assembling a list of
coroutines by hand and passing them to `asyncio.gather`, you hand `flyte.map` the task and the
inputs and it produces one action per item.

Use `flyte.map` when every item goes through the *same* task. For fanning out across *different*
tasks, or for full control over how invocations are assembled, use `asyncio.gather` — see
[Fanout](./fanout).

## Minimal example

From a **synchronous** task, iterate the results with a plain `for` loop:

```python
from typing import List

import flyte

env = flyte.TaskEnvironment(name="map-example")


@env.task
def process(x: int) -> str:
    return f"result-{x}"


@env.task
def main(n: int) -> List[str]:
    results: List[str] = []
    for r in flyte.map(process, range(n)):
        if isinstance(r, Exception):
            raise r
        results.append(r)
    return results


if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(main, 10)
    print(run.url)
```

Each item in `range(n)` becomes its own action, running in its own container, and the results come
back in the same order as the inputs.

## Mapping from an async task: `flyte.map.aio`

`flyte.map` returns a synchronous iterator. Inside an **async** task, use `flyte.map.aio`, which
returns an async iterator you consume with `async for`:

```python
@env.task
async def main(n: int) -> List[str]:
    results: List[str] = []
    async for r in flyte.map.aio(process, range(n)):
        if isinstance(r, Exception):
            raise r
        results.append(r)
    return results
```

`flyte.map.aio` works over both async and sync tasks, so you can call an existing synchronous task
in parallel from an async context without rewriting it — useful when migrating a Flyte 1.x
`map_task` or integrating legacy sync code.

## Signature and parameters

```python
flyte.map(
    func,               # the task (or functools.partial) to apply to each item
    *args,              # one or more iterables, zipped item-by-item into func's arguments
    group_name=None,    # optional name for the group of mapped actions (UI grouping)
    concurrency=0,      # max actions in flight at once; 0 means unbounded (all at once)
    return_exceptions=True,
)
```

- **`func`** — the task to map. It receives one item per invocation. To hold some arguments
  constant across the map, wrap it with `functools.partial` (see [Binding constant
  arguments](#binding-constant-arguments-with-functoolspartial)).
- **`*args`** — one or more input iterables. With multiple iterables they are **zipped**: the
  *i*-th invocation receives the *i*-th element of each, matching `func`'s positional parameters in
  order.
- **`group_name`** — groups the resulting actions under a single label in the UI (see
  [Grouping actions](./grouping-actions)).
- **`concurrency`** — the maximum number of actions in flight at any moment. `0` (the default)
  submits everything at once. A positive value bounds the fan-out with a worker pool, so memory
  stays proportional to `concurrency` rather than to the total number of items — see
  [Controlling parallel execution](./controlling-parallelism).
- **`return_exceptions`** — when `True` (the default), a failed invocation yields the raised
  exception as its result instead of aborting the whole map; check each result with
  `isinstance(r, Exception)`. When `False`, the first failure stops iteration and raises.

Results are always yielded **in the order of the inputs**, regardless of the order in which the
individual actions finish.

## Limiting concurrency

For rate-limited APIs, GPU quotas, or connection limits, cap how many actions run at once with the
`concurrency` parameter:

```python
async for r in flyte.map.aio(call_llm_api, prompts, concurrency=3):
    ...
```

Only three actions are in flight at a time; as each completes, the next input is submitted. For a
full comparison of `flyte.map(concurrency=N)` against `asyncio.Semaphore`, see
[Controlling parallel execution](./controlling-parallelism).

## Handling errors

By default (`return_exceptions=True`) the map runs to completion even if some invocations fail, and
each failure surfaces as an exception object in the results stream:

```python
@env.task
def maybe_fail(x: int) -> str:
    if x == 2:
        raise ValueError("bad input")
    return f"ok-{x}"


@env.task
def main(n: int) -> None:
    for r in flyte.map(maybe_fail, range(n)):
        if isinstance(r, Exception):
            print(f"error: {r}")
        else:
            print(r)
```

Set `return_exceptions=False` to fail fast instead: iteration raises on the first failed action.

## Binding constant arguments with `functools.partial`

Often you want to map over one argument while holding others constant. Bind the constants with
`functools.partial`, leaving exactly one parameter free — that's the one `flyte.map` varies:

```python
from functools import partial

import flyte

env = flyte.TaskEnvironment(name="map-partial")


@env.task
def score(compound_id: str, model_name: str, batch_id: str) -> str:
    return f"{compound_id}:{model_name}:{batch_id}"


@env.task
def main() -> None:
    compounds = [str(i) for i in range(3)]
    scorer = partial(score, model_name="v2", batch_id="run-42")
    # compound_id is the only parameter left unbound, so it is what map varies.
    results = list(flyte.map(scorer, compounds))
    print("\n".join(results))
```

`flyte.map` inserts each mapped value **positionally, right after the partial's bound positional
arguments**, and requires **exactly one** parameter to be left unbound. Above, `model_name` and
`batch_id` are bound as keywords, so the mapped value fills the first slot — `compound_id`. To vary a
*later* parameter, bind the ones before it positionally and the ones after it by keyword — for
example, `partial(score, "compound-1", batch_id="run-42")` maps `model_name`. `flyte.map` raises a
`TypeError` if more or fewer than one parameter is left unbound, or if the mapped positional slot is
also bound as a keyword.

{{< variant union >}}
{{< markdown >}}
## Mapping with reusable environments

`flyte.map` composes naturally with [reusable containers](../task-configuration/reusable-containers):
a warm pool of persistent containers that survive across invocations,
eliminating per-action container startup overhead. This is the highest-throughput way to run a
large map of short tasks.

Attach a `flyte.ReusePolicy` to the task's `flyte.TaskEnvironment`, then map over it as usual:

```python
import flyte

env = flyte.TaskEnvironment(
    name="map-reusable",
    image=flyte.Image.from_debian_base().with_pip_packages("unionai-reuse"),
    reusable=flyte.ReusePolicy(replicas=4, concurrency=3),
)


@env.task
async def process(x: int) -> str:
    return f"result-{x}"


@env.task
async def main(n: int) -> list[str]:
    results: list[str] = []
    async for r in flyte.map.aio(process, range(n)):
        if isinstance(r, Exception):
            raise r
        results.append(r)
    return results
```

The mapped actions are routed onto the reusable pool instead of each spinning up a fresh container.
Two concurrency controls are in play, and they are independent:

- **`ReusePolicy(replicas, concurrency)`** sizes the pool — total capacity is
  `replicas × concurrency` actions running at once (here, `4 × 3 = 12`).
- **`flyte.map(concurrency=N)`** bounds how many map actions are submitted at once. Leave it at `0`
  to let the pool absorb the full fan-out, or set it to shape submission independently of pool size.

> [!NOTE]
> Reusable containers require the
> [`unionai-reuse`](https://pypi.org/project/unionai-reuse/) runtime library in the task image, as
> shown above. See [Reusable containers](../task-configuration/reusable-containers) for the full
> `ReusePolicy` parameter reference and lifecycle details.
{{< /markdown >}}
{{< /variant >}}

## When to use `flyte.map`

Reach for `flyte.map` when:

- Every item goes through the **same** task.
- You want built-in, in-order result collection and per-item error capture.
- You want simple, declarative concurrency control via the `concurrency` parameter.

Use [`asyncio.gather`](./fanout) instead when you are fanning out across **different** tasks in one
batch, or when you need full control over how the coroutines are assembled. Use an
[`asyncio.Semaphore`](./controlling-parallelism) when different task types in the same batch need
different concurrency limits.
