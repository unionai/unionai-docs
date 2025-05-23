---
title: flytekit.utils.rate_limiter
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
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
