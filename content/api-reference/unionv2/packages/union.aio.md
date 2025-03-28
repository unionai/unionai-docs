---
title: union.aio
version: 0.1.0
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# union.aio

## Directory

### Methods

| Method | Description |
|-|-|
| [`run()`](#run) | Run an async `@env. |
| [`with_runcontext()`](#with_runcontext) | Create a new `AsyncRunnable` instance with the given run context. |


## Methods

#### run()

```python
def run(
    func: union._task.TaskTemplate,
    args,
    kwargs,
) -> union.remote._run.Run
```
Run an async `@env.task` or `TaskTemplate` instance. The existing async context will be used.

Example:
```python
import union
env = union.Environment("example")

@env.task
async def example_task(x: int, y: str) -> str:
    return f"{x} {y}"

if __name__ == "__main__":
    asyncio.run(union.aio.run(example_task, 1, y="hello"))
```


| Parameter | Type |
|-|-|
| `func` | `union._task.TaskTemplate` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### with_runcontext()

```python
def with_runcontext(
    run_id: str | None,
) -> union._run.AsyncRunnable
```
Create a new `AsyncRunnable` instance with the given run context.

Example:
```python
import union
env = union.Environment("example")

@env.task
async def example_task(x: int, y: str) -> str:
    return f"{x} {y}"

if __name__ == "__main__":
    asyncio.run(union.aio.with_runcontext(run_id="example_run_id").run(example_task, 1, y="hello"))
```


| Parameter | Type |
|-|-|
| `run_id` | `str \| None` |

