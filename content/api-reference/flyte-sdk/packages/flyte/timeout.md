---
title: Timeout
version: 2.0.0b57
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Timeout

**Package:** `flyte`

Timeout class to define a timeout for a task.
The task timeout can be set to a maximum runtime and a maximum queued time.
Maximum runtime is the maximum time the task can run for (in one attempt).
Maximum queued time is the maximum time the task can stay in the queue before it starts executing.

Example usage:
```python
timeout = Timeout(max_runtime=timedelta(minutes=5), max_queued_time=timedelta(minutes=10))
@env.task(timeout=timeout)
async def my_task():
    pass
```


```python
class Timeout(
    max_runtime: datetime.timedelta | int,
    max_queued_time: datetime.timedelta | int | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_runtime` | `datetime.timedelta \| int` | timedelta or int - Maximum runtime for the task. If specified int, it will be converted to timedelta as seconds. |
| `max_queued_time` | `datetime.timedelta \| int \| None` | optional, timedelta or int - Maximum queued time for the task. If specified int, it will be converted to timedelta as seconds. Defaults to None. |

