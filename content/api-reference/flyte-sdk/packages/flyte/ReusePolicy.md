---
title: ReusePolicy
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ReusePolicy

**Package:** `flyte`

ReusePolicy can be used to configure a task to reuse the environment. This is useful when the environment creation
is expensive and the runtime of the task is short. The environment will be reused for the next invocation of the
task, even the python process maybe be reused by subsequent task invocations. A good mental model is to think of
the environment as a container that is reused for multiple tasks, more like a long-running service.

Caution: It is important to note that the environment is shared, so managing memory and resources is important.



```python
class ReusePolicy(
    replicas: typing.Union[int, typing.Tuple[int, int]],
    idle_ttl: typing.Union[int, datetime.timedelta],
    concurrency: int,
    scaledown_ttl: typing.Union[int, datetime.timedelta],
)
```
| Parameter | Type | Description |
|-|-|-|
| `replicas` | `typing.Union[int, typing.Tuple[int, int]]` | Either a single int representing number of replicas or a tuple of two ints representing the min and max. |
| `idle_ttl` | `typing.Union[int, datetime.timedelta]` | The maximum idle duration for an environment, specified as either seconds (int) or a timedelta, after which all replicas in the environment are shutdown. When a replica remains idle — meaning no tasks are running — for this duration, it will be automatically terminated, also referred to as environment idle timeout. |
| `concurrency` | `int` | The maximum number of tasks that can run concurrently in one instance of the environment. Concurrency of greater than 1 is only supported for `async` tasks. |
| `scaledown_ttl` | `typing.Union[int, datetime.timedelta]` | The minimum time to wait before scaling down each replica, specified as either seconds (int) or a timedelta. This is useful to prevent rapid scaling down of replicas when tasks are running frequently. If not set, the default is configured in the backend. |

## Properties

| Property | Type | Description |
|-|-|-|
| `max_replicas` | `None` | Returns the maximum number of replicas. |
| `min_replicas` | `None` | Returns the minimum number of replicas. |

## Methods

| Method | Description |
|-|-|
| [`get_scaledown_ttl()`](#get_scaledown_ttl) | Returns the scaledown TTL as a timedelta. |


### get_scaledown_ttl()

```python
def get_scaledown_ttl()
```
Returns the scaledown TTL as a timedelta. If scaledown_ttl is not set, returns None.


