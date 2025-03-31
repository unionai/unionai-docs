---
title: flytekit.utils.rate_limiter
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.utils.rate_limiter

## Directory

### Classes

| Class | Description |
|-|-|
| [`RateLimiter`](.././flytekit.utils.rate_limiter#flytekitutilsrate_limiterratelimiter) | Rate limiter that allows up to a certain number of requests per minute. |
| [`datetime`](.././flytekit.utils.rate_limiter#flytekitutilsrate_limiterdatetime) | datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`deque`](.././flytekit.utils.rate_limiter#flytekitutilsrate_limiterdeque) | A list-like sequence optimized for data accesses near its endpoints. |
| [`timedelta`](.././flytekit.utils.rate_limiter#flytekitutilsrate_limitertimedelta) | Difference between two datetime values. |

### Methods

| Method | Description |
|-|-|
| [`run_sync()`](#run_sync) | This should be called from synchronous functions to run an async function. |


### Variables

| Property | Type | Description |
|-|-|-|
| `developer_logger` | `Logger` |  |

## Methods

#### run_sync()

```python
def run_sync(
    coro_func: typing.Callable[..., typing.Awaitable[~T]],
    args,
    kwargs,
) -> ~T
```
This should be called from synchronous functions to run an async function.


| Parameter | Type |
|-|-|
| `coro_func` | `typing.Callable[..., typing.Awaitable[~T]]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

## flytekit.utils.rate_limiter.RateLimiter

Rate limiter that allows up to a certain number of requests per minute.


```python
class RateLimiter(
    rpm: int,
)
```
| Parameter | Type |
|-|-|
| `rpm` | `int` |

### Methods

| Method | Description |
|-|-|
| [`acquire()`](#acquire) |  |
| [`sync_acquire()`](#sync_acquire) |  |


#### acquire()

```python
def acquire()
```
#### sync_acquire()

```python
def sync_acquire()
```
## flytekit.utils.rate_limiter.datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.


## flytekit.utils.rate_limiter.deque

A list-like sequence optimized for data accesses near its endpoints.


## flytekit.utils.rate_limiter.timedelta

Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.


