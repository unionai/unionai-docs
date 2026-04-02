---
title: Scaling
version: 2.1.2
variants: +flyte +union
layout: py_api
---

# Scaling

**Package:** `flyte.app`

Controls replica count and autoscaling behavior for app environments.

Common scaling patterns:

- **Scale-to-zero** (default): `Scaling(replicas=(0, 1))` — no replicas when idle,
  scales to 1 on demand.
- **Always-on**: `Scaling(replicas=(1, 1))` — exactly 1 replica at all times.
- **Burstable**: `Scaling(replicas=(1, 5))` — 1 replica minimum, scales up to 5.
- **High-availability**: `Scaling(replicas=(2, 10))` — at least 2 replicas always running.
- **Fixed size**: `Scaling(replicas=3)` — exactly 3 replicas.



## Parameters

```python
class Scaling(
    replicas: typing.Union[int, typing.Tuple[int, int]],
    metric: typing.Union[flyte.app._types.Scaling.Concurrency, flyte.app._types.Scaling.RequestRate, NoneType],
    scaledown_after: int | datetime.timedelta | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `replicas` | `typing.Union[int, typing.Tuple[int, int]]` | Number of replicas. An `int` for fixed count, or a `(min, max)` tuple for autoscaling. Default `(0, 1)`. |
| `metric` | `typing.Union[flyte.app._types.Scaling.Concurrency, flyte.app._types.Scaling.RequestRate, NoneType]` | Autoscaling metric — `Scaling.Concurrency(val)` (scale when concurrent requests per replica exceeds `val`) or `Scaling.RequestRate(val)` (scale when requests per second per replica exceeds `val`). Default `None`. |
| `scaledown_after` | `int \| datetime.timedelta \| None` | Time to wait after the last request before scaling down. Seconds (`int`) or `timedelta`. Default `None` (platform default). |

## Methods

| Method | Description |
|-|-|
| [`get_replicas()`](#get_replicas) |  |


### get_replicas()

```python
def get_replicas()
```
