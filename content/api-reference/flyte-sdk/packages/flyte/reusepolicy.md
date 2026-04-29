---
title: ReusePolicy
version: 2.2.1
variants: +flyte +union
layout: py_api
---

# ReusePolicy

**Package:** `flyte`

Configure a task environment for container reuse across multiple task invocations.

When environment creation is expensive relative to task runtime, reusable containers
keep a pool of warm containers ready, avoiding cold-start overhead. The Python process
may be reused by subsequent task invocations.

Total concurrent capacity is `max_replicas * concurrency`. For example,
`ReusePolicy(replicas=(1, 3), concurrency=2)` supports up to 6 concurrent tasks.

Caution: The environment is shared across invocations — manage memory and resources carefully.

```python
env = flyte.TaskEnvironment(
    name="fast_env",
    reusable=flyte.ReusePolicy(replicas=(1, 3), concurrency=2),
)
```



## Parameters

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
| `replicas` | `typing.Union[int, typing.Tuple[int, int]]` | Number of container replicas to maintain.  - `int`: Fixed replica count, always running (e.g., `replicas=3`). - `tuple(min, max)`: Auto-scaling range (e.g., `replicas=(1, 5)`). Scales between min and max based on demand.  Default is `2`. A minimum of 2 replicas is recommended to avoid starvation when the parent task occupies one replica. |
| `idle_ttl` | `typing.Union[int, datetime.timedelta]` | Environment-level idle timeout — shuts down **all** replicas when the entire environment has been idle for this duration. Specified as seconds (`int`) or `timedelta`. Minimum 30 seconds. Default is 30 seconds. |
| `concurrency` | `int` | Maximum concurrent tasks per replica. Values greater than 1 are only supported for `async` tasks. Default is `1`. |
| `scaledown_ttl` | `typing.Union[int, datetime.timedelta]` | Per-replica scale-down delay — minimum time to wait before removing an **individual** idle replica. Prevents rapid scale-down when tasks arrive in bursts. Specified as seconds (`int`) or `timedelta`. Default is 30 seconds.  Note the distinction: `idle_ttl` controls when the whole environment shuts down; `scaledown_ttl` controls when individual replicas are removed during auto-scaling. |

## Properties

| Property | Type | Description |
|-|-|-|
| `max_replicas` | `int` | Returns the maximum number of replicas. |
| `min_replicas` | `int` | Returns the minimum number of replicas. |

## Methods

| Method | Description |
|-|-|
| [`get_scaledown_ttl()`](#get_scaledown_ttl) | Returns the scaledown TTL as a timedelta. |


### get_scaledown_ttl()

```python
def get_scaledown_ttl()
```
Returns the scaledown TTL as a timedelta. If scaledown_ttl is not set, returns None.


