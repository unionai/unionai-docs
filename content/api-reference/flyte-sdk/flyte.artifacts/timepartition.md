---
title: TimePartition
description: "A time partition value with an explicit granularity."
icon: braces
version: 2.10.2
variants: +flyte +union
layout: py_api
---

# TimePartition

**Package:** `flyte.artifacts`

A time partition value with an explicit granularity.

`date` and `datetime` values already imply "day" and "hour"; use this for
"week" and "month", or to be explicit:

```python
Metadata(name="monthly_report", partitions={"date": TimePartition(date(2026, 8, 1), "month")})
```


## Parameters

```python
class TimePartition(
    value: date | datetime,
    granularity: Granularity = 'day',
)
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `date \| datetime` | |
| `granularity` | `Granularity` | |

