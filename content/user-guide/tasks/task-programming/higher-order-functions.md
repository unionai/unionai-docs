---
title: Higher-order functions
weight: 22
variants: +flyte +union
---

# Higher-order functions

A *higher-order function* is a function that takes other functions as arguments or returns them. Because Flyte 2 tasks execute as native Python and can be [passed as arguments](./other-features#passing-tasks-and-functions-as-arguments) like any other callable, you can write higher-order functions that operate on **tasks themselves**: reusable orchestration components that wrap a task with retry, fallback, batching, or fault-tolerance logic, without changing the task's business logic.

This is possible because Flyte 2 workflows run as ordinary Python:

- **Tasks are callables.** You can accept a task as a parameter and `await` it, `.override(...)` its resources, or hand it to `asyncio`.
- **Arbitrary nesting.** A task can invoke other tasks at any depth, so an orchestration wrapper can drive a task from inside another task.
- **Native control flow.** Loops, conditionals, and `try`/`except` work directly on task results (task outputs are plain Python objects, not promises), so a wrapper can inspect a result or catch an exception and react.

> [!NOTE] Higher-order functions are plain functions, not tasks
> The wrappers below are **not** decorated with `@env.task`. They are regular `async` Python functions that orchestrate tasks. You call them from inside a driver task (an `@env.task`), which is where the actual task invocations happen. Keep the reusable orchestration logic in a plain function so it can be applied to any task.

The patterns on this page are drawn from the runnable [`higher_order_patterns`](https://github.com/flyteorg/flyte-sdk/tree/main/examples/higher_order_patterns) examples in the Flyte SDK repository.

## Fallback runner

Run a primary task and, if it fails with a matching exception, automatically fall back to an alternative task. Useful for degrading to a cheaper model, a different region, or a simpler algorithm when the preferred path fails.

```python
from typing import Callable, List, Optional, Type, TypeVar

R = TypeVar("R")

async def run_with_fallback(
    primary_task: Callable[..., R],
    fallback_task: Callable[..., R],
    *args,
    fallback_exceptions: Optional[List[Type[Exception]]] = None,
    **kwargs,
) -> R:
    try:
        return await primary_task(*args, **kwargs)
    except Exception as e:
        # Fall back only on the exceptions we opted into (None means any).
        should_fallback = fallback_exceptions is None or any(
            isinstance(e, exc) for exc in fallback_exceptions
        )
        if not should_fallback:
            raise
        return await fallback_task(*args, **kwargs)
```

Call it from a driver task, passing the two tasks as arguments:

```python
import flyte
import flyte.errors

env = flyte.TaskEnvironment("fallback")

@env.task
async def primary(x: int) -> int:
    # Business logic that may fail, e.g. raise ValueError(...) on bad input.
    ...

@env.task
async def backup(x: int) -> int:
    ...

@env.task
async def main(x: int) -> int:
    return await run_with_fallback(primary, backup, x, fallback_exceptions=[flyte.errors.RuntimeUserError])
```

Note the `fallback_exceptions` list holds `flyte.errors` types, not bare Python exceptions. An exception raised inside a task does not reach the parent as its original Python type: Flyte wraps it as a `flyte.errors` type (a `ValueError` raised in a task surfaces to the caller as a `flyte.errors.RuntimeUserError` whose `code` is `"ValueError"`). So `isinstance`/type-matching in a wrapper must target the `flyte.errors.*` hierarchy; matching on `ValueError` here would never fire and the fallback would never run. See [Error handling](./error-handling) for how failures propagate.

## Retry with increasing memory (OOM retrier)

Retry a task with progressively larger memory allocations when it hits an out-of-memory error, so you don't have to hard-code a worst-case memory request. The wrapper uses `.override()` to raise the task's `flyte.Resources` on each attempt and catches `flyte.errors.OOMError`.

```python
import flyte
import flyte.errors

async def retry_with_memory(
    task_fn,
    *args,
    initial_memory_mi: int = 250,
    increment_mi: int = 200,
    max_memory_mi: int = 4096,
    cpu: int = 1,
    **kwargs,
):
    current = initial_memory_mi
    while current <= max_memory_mi:
        try:
            return await task_fn.override(
                resources=flyte.Resources(cpu=cpu, memory=f"{current}Mi")
            )(*args, **kwargs)
        except flyte.errors.OOMError:
            if current >= max_memory_mi:
                break
            current = min(current + increment_mi, max_memory_mi)
    raise RuntimeError(f"Task still OOMing at {max_memory_mi}Mi")
```

Because the wrapper only takes the task and its arguments, it works with any task:

```python
@env.task
async def process(data: list[int]) -> int:
    # Business logic that may run out of memory on large inputs.
    return sum(data)

@env.task
async def main(data: list[int]) -> int:
    return await retry_with_memory(process, data, initial_memory_mi=500, max_memory_mi=8192)
```

See [Error handling](./error-handling) for more on `flyte.errors.OOMError` and resource-based recovery.

## Circuit breaker

Run a task over many items in parallel, but stop early ("open the circuit") once failures exceed a threshold, so a systemic problem doesn't burn resources on every remaining item. It launches all invocations with `asyncio.create_task`, processes them as they complete, and cancels the rest when the limit is crossed.

```python
import asyncio
from typing import Callable, List, Optional, TypeVar

T = TypeVar("T")
R = TypeVar("R")

class CircuitBreakerError(Exception):
    """Raised when too many failures occur."""

async def circuit_breaker_execute(
    task_fn: Callable[[T], R], items: List[T], max_failures: int = 3
) -> List[Optional[R]]:
    tasks = [asyncio.create_task(task_fn(item)) for item in items]
    results: List[Optional[R]] = [None] * len(items)
    failures = 0
    pending = set(tasks)

    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            idx = tasks.index(task)
            if task.exception():
                failures += 1
                if failures > max_failures:
                    for remaining in pending:
                        remaining.cancel()
                    raise CircuitBreakerError(
                        f"{failures} failures exceed limit of {max_failures}"
                    )
            else:
                results[idx] = task.result()
    return results
```

Failed items come back as `None`; if the failure threshold is crossed, the remaining tasks are cancelled and `CircuitBreakerError` is raised. See [Fanout](./fanout) for the basics of running tasks in parallel and [Controlling parallel execution](./controlling-parallelism) for bounding concurrency.

## Auto batcher

Split a large input into batches, run a map task over each batch in parallel, then combine the results with a reduce step. This bounds how many invocations are in flight at once while still processing everything.

```python
import asyncio
from typing import Any, Callable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")

def create_batches(data: List[T], batch_size: int) -> List[List[T]]:
    return [data[i : i + batch_size] for i in range(0, len(data), batch_size)]

async def batch_map_reduce(
    map_fn: Callable[[T], R],
    reduce_fn: Callable[[List[R]], Any],
    data: List[T],
    batch_size: int = 10,
) -> Any:
    all_results: List[R] = []
    for batch in create_batches(data, batch_size):
        coros = [asyncio.create_task(map_fn(item)) for item in batch]
        all_results.extend(await asyncio.gather(*coros))
    return reduce_fn(all_results)
```

The map step is a task; the reduce step can be a task or a plain function:

```python
@env.task
async def square(x: int) -> int:
    return x * x

@env.task
async def main(data: list[int]) -> int:
    return await batch_map_reduce(square, sum, data, batch_size=25)
```

For a first-class parallel-map primitive, see `flyte.map` in [Fanout](./fanout).

## Composing the patterns

Because each wrapper is just a function that takes a task, you can layer them (for example, wrap a task in the OOM retrier and then hand *that* to the fallback runner) to build orchestration behavior out of small, reusable pieces without touching the underlying task code.
