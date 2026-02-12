---
title: flyte.extras
version: 2.0.0b57
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.extras


Flyte extras package.
This package provides various utilities that make it possible to build highly customized workflows.

1. ContainerTask: Execute arbitrary pre-containerized applications, without needed the `flyte-sdk` to be installed.
                  This extra uses `flyte copilot` system to inject inputs and slurp outputs from the container run.

2. Time utilities: Usage of Time.now, time.sleep or asyncio.sleep bring non-determinism to a program. This module
                   provides a few utilities that make it possible to bring determinism to workflows that need to access
                   time related functions. This determinism persists across crashes and restarts making the process
                   durable.

## Directory

### Classes

| Class | Description |
|-|-|
| [`ContainerTask`](../flyte.extras/containertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |

### Methods

| Method | Description |
|-|-|
| [`durable_sleep()`](#durable_sleep) | durable_sleep enables the process to sleep for `seconds` seconds even if the process recovers from a crash. |
| [`durable_time()`](#durable_time) | Returns the current time for every unique invocation of durable_time. |


## Methods

#### durable_sleep()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await durable_sleep.aio()`.
```python
def durable_sleep(
    seconds: float,
)
```
durable_sleep enables the process to sleep for `seconds` seconds even if the process recovers from a crash.
This method can be invoked multiple times. If the process crashes, the invocation of durable_sleep will behave
like as-if the process has been sleeping since the first time this method was invoked.

Examples:
```python
    import flyte.durable

    env = flyte.TaskEnvironment("env")

    @env.task
    async def main():
        # Do something
        my_work()
        # Now we need to sleep for 1 hour before proceeding.
        await flyte.durable.sleep.aio(3600)  # Even if process crashes, it will resume and only sleep for
                                              # 1 hour in agregate. If the scheduling takes longer, it
                                              # will simply return immediately.
        # thing to be done after 1 hour
        my_work()
```



| Parameter | Type | Description |
|-|-|-|
| `seconds` | `float` | float time to sleep for |

#### durable_time()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await durable_time.aio()`.
```python
def durable_time()
```
Returns the current time for every unique invocation of durable_time. If the same invocation is encountered again
the previously returned time is returned again, ensuring determinism.
Similar to using `time.time()` just durable!
Returns: float


