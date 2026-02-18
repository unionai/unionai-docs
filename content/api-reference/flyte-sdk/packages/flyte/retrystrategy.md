---
title: RetryStrategy
version: 2.0.0b59
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RetryStrategy

**Package:** `flyte`

Retry strategy for the task or task environment. Retry strategy is optional or can be a simple number of retries.

Example:
- This will retry the task 5 times.
```
@task(retries=5)
def my_task():
    pass
```
- This will retry the task 5 times with a maximum backoff of 10 seconds and a backoff factor of 2.
```
@task(retries=RetryStrategy(count=5))
def my_task():
    pass
```



```python
class RetryStrategy(
    count: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `count` | `int` | The number of retries. |

