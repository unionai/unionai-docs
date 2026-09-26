---
title: Metrics
description: "Pod metrics of a task's action attempt or of an app, as shown in the Union UI."
icon: braces
version: 0.14.0
variants: -flyte +union
layout: py_api
---

# Metrics

**Package:** `flyteplugins.union.remote`

Pod metrics of a task's action attempt or of an app, as shown in the Union UI.

Metrics are collected from the pods an execution ran on (CPU, memory, GPU
utilization and health, and app request metrics) and answered by the cluster's
dataplane as prometheus range-query results.



## Parameters

```python
class Metrics(
    results: list[MetricResult],
)
```
| Parameter | Type | Description |
|-|-|-|
| `results` | `list[MetricResult]` | |

## Methods

| Method | Description |
|-|-|
| [`get_for_action()`](#get_for_action) | Get the pod metrics of a task's action attempt. |
| [`get_for_app()`](#get_for_app) | Get the pod metrics of an app over a time window. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### get_for_action()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Metrics.get_for_action.aio()`.
```python
def get_for_action(
    cls,
    run_name: str,
    action_name: str | None = None,
    attempt: int | None = None,
    metrics: Sequence[str | int] | None = None,
) -> Metrics
```
Get the pod metrics of a task's action attempt.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `run_name` | `str` | The name of the run. |
| `action_name` | `str \| None` | The name of the action within the run. Defaults to the run's root action. |
| `attempt` | `int \| None` | The attempt number to query. Defaults to the latest attempt. |
| `metrics` | `Sequence[str \| int] \| None` | The metrics to query, by short name (see ``METRIC_NAMES``, e.g. ``cpu_utilization``) or ``ExecutionMetric`` value. Defaults to the server's default set for task pods. |

**Returns:** Metrics with one ``MetricResult`` per answered metric.

### get_for_app()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Metrics.get_for_app.aio()`.
```python
def get_for_app(
    cls,
    name: str,
    project: str | None = None,
    domain: str | None = None,
    metrics: Sequence[str | int] | None = None,
    start_time: datetime | None = None,
    end_time: datetime | None = None,
) -> Metrics
```
Get the pod metrics of an app over a time window.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the app. |
| `project` | `str \| None` | The project of the app. Defaults to the configured project. |
| `domain` | `str \| None` | The domain of the app. Defaults to the configured domain. |
| `metrics` | `Sequence[str \| int] \| None` | The metrics to query, by short name (see ``METRIC_NAMES``, e.g. ``app_requests``) or ``ExecutionMetric`` value. Defaults to the server's default set for app pods. |
| `start_time` | `datetime \| None` | Start of the time window. Defaults to 24 hours ago; the earliest possible time is one year ago. |
| `end_time` | `datetime \| None` | End of the time window. Defaults to now. |

**Returns:** Metrics with one ``MetricResult`` per answered metric.

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

