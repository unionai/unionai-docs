---
title: MetricSeries
description: "One time series of a metric result, e.g. one container or one GPU device."
icon: braces
version: 0.14.0
variants: -flyte +union
layout: py_api
---

# MetricSeries

**Package:** `flyteplugins.union.remote`

One time series of a metric result, e.g. one container or one GPU device.


## Parameters

```python
class MetricSeries(
    labels: dict[str, str],
    values: list[tuple[datetime, float]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `labels` | `dict[str, str]` | |
| `values` | `list[tuple[datetime, float]]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `latest` | `float \| None` |  |

