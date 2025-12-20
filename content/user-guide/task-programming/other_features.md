---
title: Other features
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

This guide covers advanced programming patterns and techniques for working with Flyte tasks.

## Task Forwarding

When one task calls another task using the normal invocation syntax (e.g., `await inner_task(x)`), Flyte creates a durable action that's recorded in the UI with data passed through the metadata store. However, if you want to execute a task in the same Python VM without this overhead, use the `.forward()` method.

**When to use**: You want to avoid durability overhead and execute task logic directly in the current VM.

```python
import flyte

env = flyte.TaskEnvironment("my-env")

@env.task
async def inner_task(x: int) -> int:
    return x + 1

@env.task
async def outer_task(x: int) -> int:
    # Executes in same VM, no durable action created
    v = await inner_task.forward(x=10)

    # Creates a durable action, recorded in UI
    return await inner_task(v)
```

The `.forward()` method works with both sync and async tasks:

```python
@env.task
def sync_inner_task(x: int) -> int:
    return x + 1

@env.task
def sync_outer_task(x: int) -> int:
    # Direct execution, no remote call
    v = sync_inner_task.forward(x=10)
    return sync_inner_task(v)
```

## Passing Tasks and Functions as Arguments

You can pass both Flyte tasks and regular Python functions as arguments to other tasks. Flyte handles this through pickling, so the code appears as pickled data in the UI.

```python
import typing
import flyte

env = flyte.TaskEnvironment("udfs")

@env.task
async def add_one_udf(x: int) -> int:
    return x + 1

# Regular async function (not a task)
async def fn_add_two_udf(x: int) -> int:
    return x + 2

@env.task
async def run_udf(x: int, udf: typing.Callable[[int], typing.Awaitable[int]]) -> int:
    return await udf(x)

@env.task
async def main() -> list[int]:
    # Pass a Flyte task as an argument
    result_one = await run_udf(5, add_one_udf)

    # Pass a regular function as an argument
    result_two = await run_udf(5, fn_add_two_udf)

    return [result_one, result_two]
```

**Note**: Both tasks and regular functions are serialized via pickling when passed as arguments.

## Custom Action Names

By default, actions in the UI use the task's function name. You can provide custom, user-friendly names using the `short_name` parameter.

### Set at Task Definition

```python
import flyte

env = flyte.TaskEnvironment("friendly_names")

@env.task(short_name="my_task")
async def some_task() -> str:
    return "Hello, Flyte!"
```

### Override at Call Time

```python
@env.task(short_name="entrypoint")
async def main() -> str:
    # Uses the default short_name "my_task"
    s = await some_task()

    # Overrides to use "my_name" for this specific action
    return s + await some_task.override(short_name="my_name")()
```

This is useful when the same task is called multiple times with different contexts, making the UI more readable.

## Invoking Async Functions from Sync Tasks

When migrating from Flyte 1.x to 2.0, you may have legacy sync code that needs to call async functions. Use `nest_asyncio.apply()` to enable `asyncio.run()` within sync tasks.

```python
import asyncio
import nest_asyncio
import flyte

env = flyte.TaskEnvironment(
    "async_in_sync",
    image=flyte.Image.from_debian_base().with_pip_packages("nest_asyncio"),
)

# Apply at module level
nest_asyncio.apply()

async def async_function() -> str:
    await asyncio.sleep(1)
    return "done"

@env.task
def sync_task() -> str:
    # Now you can use asyncio.run() in a sync task
    return asyncio.run(async_function())
```

**Important**:
- Call `nest_asyncio.apply()` at the module level before defining tasks
- Add `nest_asyncio` to your image dependencies
- This is particularly useful during migration when you have mixed sync/async code

## Async and Sync Task Interoperability

When migrating from older sync-based code to async tasks, or when working with mixed codebases, you need to call sync tasks from async parent tasks. Flyte provides the `.aio` method on every task (even sync ones) to enable this.

### Calling Sync Tasks from Async Tasks

Every sync task automatically has an `.aio` property that returns an async-compatible version:

```python
import flyte

env = flyte.TaskEnvironment("mixed-tasks")

@env.task
def sync_task(x: int) -> str:
    """Legacy sync task"""
    return f"Processed {x}"

@env.task
async def async_task(x: int) -> str:
    """New async task that calls legacy sync task"""
    # Use .aio to call sync task from async context
    result = await sync_task.aio(x)
    return result
```

### Using with `flyte.map.aio()`

When you need to call sync tasks in parallel from an async context, use `flyte.map.aio()`:

```python
from typing import List
import flyte

env = flyte.TaskEnvironment("map-example")

@env.task
def sync_process(x: int) -> str:
    """Synchronous processing task"""
    return f"Task {x}"

@env.task
async def async_main(n: int) -> List[str]:
    """Async task that maps over sync task"""
    results = []

    # Map over sync task from async context
    async for result in flyte.map.aio(sync_process, range(n)):
        if isinstance(result, Exception):
            raise result
        results.append(result)

    return results
```

**Why this matters**: This pattern is powerful when migrating from Flyte 1.x or integrating legacy sync tasks with new async code. You don't need to rewrite all sync tasks at once—they can be called seamlessly from async contexts.

## Using AnyIO in Async Tasks

Flyte async tasks support `anyio` for structured concurrency as an alternative to `asyncio.gather()`.

```python
import anyio
import aioresult
import flyte

env = flyte.TaskEnvironment(
    "anyio_example",
    image=flyte.Image.from_debian_base().with_pip_packages("anyio", "aioresult"),
)

@env.task
async def process_item(x: int) -> int:
    return x * 2

@env.task
async def batch_process(items: list[int]) -> list[int]:
    captured_results = []

    async with anyio.create_task_group() as tg:
        # Start multiple tasks concurrently
        for item in items:
            captured_results.append(
                aioresult.ResultCapture.start_soon(tg, process_item, item)
            )

    # Extract results
    return [r.result() for r in captured_results]
```

**Note**: You can use anyio's task groups, timeouts, and other structured concurrency primitives within Flyte async tasks.

