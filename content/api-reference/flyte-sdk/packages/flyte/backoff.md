---
title: Backoff
version: 2.5.1
variants: +flyte +union
layout: py_api
---

# Backoff

**Package:** `flyte`

Exponential backoff policy applied between user retries.

The delay before the n-th retry (0-indexed) is::

    min(base * factor**n, cap)



## Parameters

```python
class Backoff(
    base: datetime.timedelta,
    factor: float,
    cap: typing.Optional[datetime.timedelta],
)
```
| Parameter | Type | Description |
|-|-|-|
| `base` | `datetime.timedelta` | Initial delay before the first retry. Must be &gt;= 0. |
| `factor` | `float` | Per-retry multiplier. ``1.0`` yields constant delay (``base`` for every retry); ``2.0`` doubles each time. Must be &gt;= 1.0. |
| `cap` | `typing.Optional[datetime.timedelta]` | Upper bound on the computed delay. Required when ``factor &gt; 1`` to prevent unbounded growth. Must be &gt;= 0 when set. |

## Methods

| Method | Description |
|-|-|
| [`compute_delay()`](#compute_delay) | Returns the delay for the n-th retry (0-indexed). |


### compute_delay()

```python
def compute_delay(
    n: int,
) -> datetime.timedelta
```
Returns the delay for the n-th retry (0-indexed).

Used by the local controller to pace local retries; the remote leasor
applies the same formula.


| Parameter | Type | Description |
|-|-|-|
| `n` | `int` | |

