---
title: MetricResult
description: "The result of querying one metric."
icon: braces
version: 0.13.0
variants: -flyte +union
layout: py_api
---

# MetricResult

**Package:** `flyteplugins.union.remote`

The result of querying one metric.

Wraps the prometheus range-query result the dataplane answers with. A result may
carry multiple time series, differentiated by their metric labels (e.g. one per
GPU device), or an error when this metric could not be queried — each metric in
a request is queried independently, so one failing leaves the others intact.


## Parameters

```python
class MetricResult(
    pb2: dataproxy_pb2.ExecutionMetricResult,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `dataproxy_pb2.ExecutionMetricResult` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `data` | `dict` | The raw prometheus range-query result, as a dict.  See https://prometheus.io/docs/prometheus/latest/querying/api/#expression-query-result-formats |
| `error` | `str` | Why this metric could not be queried; empty on success. |
| `metric` | `int` | The ``ExecutionMetric`` enum value this result answers for. |
| `name` | `str` | Short metric name, e.g. ``cpu_utilization``. |
| `series` | `list[MetricSeries]` | The result parsed into time series, one per label set. |

## Methods

| Method | Description |
|-|-|
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

