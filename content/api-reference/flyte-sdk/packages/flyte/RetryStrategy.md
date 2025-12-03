---
title: RetryStrategy
version: 2.0.0b34
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
@task(retries=RetryStrategy(count=5, max_backoff=10, backoff=2))
def my_task():
    pass
```



```python
class RetryStrategy(
    count: int,
    backoff: typing.Union[float, datetime.timedelta, NoneType],
    backoff_factor: typing.Union[int, float, NoneType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `count` | `int` | The number of retries. |
| `backoff` | `typing.Union[float, datetime.timedelta, NoneType]` | The backoff exponential factor. This can be an integer or a float. |
| `backoff_factor` | `typing.Union[int, float, NoneType]` | |

