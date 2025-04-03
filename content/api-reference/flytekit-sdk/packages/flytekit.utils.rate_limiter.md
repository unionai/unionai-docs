---
title: flytekit.utils.rate_limiter
version: 0.1.dev2184+g1e0cbe7.d20250401
variants: +flyte +byoc +byok +serverless
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
