---
title: Timeout
version: 2.3.8
variants: +flyte +union
layout: py_api
---

# Timeout

**Package:** `flyte`

Timeout bounds for a task. See module docstring for semantics.



## Parameters

```python
class Timeout(
    max_runtime: datetime.timedelta | int | None,
    max_queued_time: datetime.timedelta | int | None,
    deadline: datetime.timedelta | int | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_runtime` | `datetime.timedelta \| int \| None` | Per-attempt RUNNING-phase bound. ``int`` is interpreted as seconds. ``None`` or ``0`` means unlimited. |
| `max_queued_time` | `datetime.timedelta \| int \| None` | Per-attempt queue-wait bound. ``int`` is interpreted as seconds. ``None`` or ``0`` means unlimited. |
| `deadline` | `datetime.timedelta \| int \| None` | Absolute wall-clock budget across all attempts. ``int`` is interpreted as seconds. ``None`` or ``0`` means unlimited. |

