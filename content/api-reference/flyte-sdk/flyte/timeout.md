---
title: Timeout
description: "Timeout bounds for a task."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# Timeout

**Package:** `flyte`

Timeout bounds for a task. See module docstring for semantics.

```python
flyte.Timeout(
    max_runtime=timedelta(minutes=30),
    max_queued_time=timedelta(minutes=15),
    deadline=timedelta(hours=2),
)
```



## Parameters

```python
class Timeout(
    max_runtime: datetime.timedelta | int | None = None,
    max_queued_time: datetime.timedelta | int | None = None,
    deadline: datetime.timedelta | int | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_runtime` | `datetime.timedelta \| int \| None` | Per-attempt RUNNING-phase bound. `int` is interpreted as seconds. `None` or `0` means unlimited. |
| `max_queued_time` | `datetime.timedelta \| int \| None` | Per-attempt queue-wait bound. `int` is interpreted as seconds. `None` or `0` means unlimited. |
| `deadline` | `datetime.timedelta \| int \| None` | Absolute wall-clock budget across all attempts. `int` is interpreted as seconds. `None` or `0` means unlimited. |

