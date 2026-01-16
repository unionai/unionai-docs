---
title: Scaling
version: 2.0.0b48
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Scaling

**Package:** `flyte.app`

```python
class Scaling(
    replicas: typing.Union[int, typing.Tuple[int, int]],
    metric: typing.Union[flyte.app._types.Scaling.Concurrency, flyte.app._types.Scaling.RequestRate, NoneType],
    scaledown_after: int | datetime.timedelta | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `replicas` | `typing.Union[int, typing.Tuple[int, int]]` | |
| `metric` | `typing.Union[flyte.app._types.Scaling.Concurrency, flyte.app._types.Scaling.RequestRate, NoneType]` | |
| `scaledown_after` | `int \| datetime.timedelta \| None` | |

## Methods

| Method | Description |
|-|-|
| [`get_replicas()`](#get_replicas) |  |


### get_replicas()

```python
def get_replicas()
```
