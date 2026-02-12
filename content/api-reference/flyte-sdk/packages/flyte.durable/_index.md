---
title: flyte.durable
version: 2.0.0b57
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.durable


Flyte durable utilities.

This module provides deterministic, crash-resilient replacements for time-related functions.
Usage of ``time.time()``, ``time.sleep()`` or ``asyncio.sleep()`` introduces non-determinism.
The utilities here persist state across crashes and restarts, making workflows durable.

- :func:`sleep` - a durable replacement for ``time.sleep`` / ``asyncio.sleep``
- :func:`time` - a durable replacement for ``time.time``
- :func:`now` - a durable replacement for ``datetime.now``

## Directory

### Methods

| Method | Description |
|-|-|
| [`now()`](#now) | Returns the current time for every unique invocation of durable_time. |
| [`sleep()`](#sleep) | durable_sleep enables the process to sleep for `seconds` seconds even if the process recovers from a crash. |
| [`time()`](#time) | Returns the current time for every unique invocation of durable_time. |


## Methods

#### now()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await now.aio()`.
```python
def now()
```
Returns the current time for every unique invocation of durable_time. If the same invocation is encountered
the previously returned time is returned again, ensuring determinism.
Similar to using `datetime.now()` just durable!
Returns: datetime.datetime


#### sleep()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await sleep.aio()`.
```python
def sleep(
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

#### time()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await time.aio()`.
```python
def time()
```
Returns the current time for every unique invocation of durable_time. If the same invocation is encountered again
the previously returned time is returned again, ensuring determinism.
Similar to using `time.time()` just durable!
Returns: float


