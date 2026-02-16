---
title: Parallelism and async
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Parallelism and async

## Basic map_task migration

{{< tabs "migration-map-basic" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import task, workflow, map_task

@task
def process_item(x: int) -> int:
    return x * 2

@workflow
def my_workflow(items: list[int]) -> list[int]:
    return map_task(process_item)(x=items)
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def process_item(x: int) -> int:
    return x * 2

@env.task
def main(items: list[int]) -> list[int]:
    return list(flyte.map(process_item, items))
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## map_task with concurrency

{{< tabs "migration-map-concurrency" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
@workflow
def my_workflow(items: list[int]) -> list[int]:
    return map_task(process_item, concurrency=5)(x=items)
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
@env.task
def main(items: list[int]) -> list[int]:
    return list(flyte.map(process_item, items, concurrency=5))
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Async parallel execution with asyncio.gather

This is the recommended approach for parallel execution in Flyte 2.

```python
import asyncio
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def process_item(item: int) -> str:
    return f"processed_{item}"

@env.task
async def main(items: list[int]) -> list[str]:
    tasks = [process_item(item) for item in items]
    results = await asyncio.gather(*tasks)
    return list(results)
```

## Concurrency control with semaphore

```python
import asyncio

@env.task
async def process_item(item: int) -> str:
    await asyncio.sleep(1)
    return f"processed_{item}"

@env.task
async def main_with_concurrency_limit(
    items: list[int],
    max_concurrent: int = 5
) -> list[str]:
    semaphore = asyncio.Semaphore(max_concurrent)

    async def process_with_limit(item: int) -> str:
        async with semaphore:
            return await process_item(item)

    tasks = [process_with_limit(item) for item in items]
    results = await asyncio.gather(*tasks)
    return list(results)
```

## Error handling with asyncio.gather

```python
@env.task
async def main_with_error_handling(
    items: list[int],
    max_concurrent: int = 5
) -> list[str]:
    semaphore = asyncio.Semaphore(max_concurrent)

    async def process_with_limit(item: int) -> str:
        async with semaphore:
            return await process_item(item)

    tasks = [process_with_limit(item) for item in items]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    processed = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Item {items[i]} failed: {result}")
            processed.append(f"Failed: {items[i]}")
        else:
            processed.append(result)
    return processed
```

## flyte.map vs asyncio.gather comparison

| Feature | flyte.map (sync) | asyncio.gather (async) |
|---------|------------------|------------------------|
| Syntax | `list(flyte.map(fn, items))` | `await asyncio.gather(*tasks)` |
| Concurrency limit | Built-in `concurrency=N` | Use `asyncio.Semaphore` |
| Streaming/as-completed | No control | Yes, via `asyncio.as_completed()` |
| Error handling | `return_exceptions=True` | Check return type |
| Flexibility | Less flexible | More flexible |

## Recommended pattern selection

Use **flyte.map** when:
- You are forced to use synchronous Python
- You want minimal code changes from Flyte 1 `map_task`

Use **asyncio.gather** when (recommended):
- You want maximum flexibility and control
- You need streaming results (`asyncio.as_completed`)
- You need fine-grained concurrency control (semaphores)
- You're writing new Flyte 2 code

## Sync and async task patterns

Keep task types consistent within a call chain for clarity and predictability.

### Sync tasks calling sync tasks

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def step1(x: int) -> int:
    return x + 1

@env.task
def step2(y: int) -> int:
    return y * 2

@env.task
def main(x: int) -> int:
    a = step1(x)   # Runs, returns result
    b = step2(a)   # Runs after step1 completes
    return b
```

### Async tasks calling async tasks

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def step1(x: int) -> int:
    return x + 1

@env.task
async def step2(y: int) -> int:
    return y * 2

@env.task
async def main(x: int) -> int:
    a = await step1(x)   # Runs, waits for result
    b = await step2(a)   # Runs after step1 completes
    return b
```

### Sequential execution with await

When you `await` async tasks one after another, they run sequentially, just like Flyte 1 workflows:

{{< tabs "migration-sequential" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
@workflow
def my_workflow(x: int) -> str:
    a = step1(x=x)      # Runs first
    b = step2(y=a)      # Runs second
    c = step3(z=b)      # Runs third
    return c
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
@env.task
async def main(x: int) -> str:
    a = await step1(x)      # Runs first
    b = await step2(a)      # Runs second
    c = await step3(b)      # Runs third
    return c
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

{{< note >}}
`await` means "wait for this to finish before continuing." Sequential `await` calls behave the same as sequential task calls in Flyte 1 workflows.
{{< /note >}}

For full details on async patterns, see [Asynchronous model](../../user-guide/flyte-2/async).
For full details on parallel fanout, see [Fanout](../../user-guide/task-programming/fanout).
