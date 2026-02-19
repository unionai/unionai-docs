---
title: RateLimiter
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RateLimiter

**Package:** `flytekit.utils.rate_limiter`

Rate limiter that allows up to a certain number of requests per minute.


```python
class RateLimiter(
    rpm: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `rpm` | `int` | |

## Methods

| Method | Description |
|-|-|
| [`acquire()`](#acquire) |  |
| [`sync_acquire()`](#sync_acquire) |  |


### acquire()

```python
def acquire()
```
### sync_acquire()

```python
def sync_acquire()
```
