---
title: flytekit.utils.rate_limiter
version: 1.16.19
variants: +flyte +union
layout: py_api
---

# flytekit.utils.rate_limiter

## Directory

### Classes

| Class | Description |
|-|-|
| [`RateLimiter`](.././flytekit.utils.rate_limiter#flytekitutilsrate_limiterratelimiter) | Rate limiter that allows up to a certain number of requests per minute. |

## flytekit.utils.rate_limiter.RateLimiter

Rate limiter that allows up to a certain number of requests per minute.


### Parameters

```python
class RateLimiter(
    rpm: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `rpm` | `int` | |

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
