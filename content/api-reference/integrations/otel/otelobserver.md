---
title: OtelObserver
description: "A `flyte._observe.Observer` that records spans."
icon: braces
version: 2.11.1
variants: +flyte +union
layout: py_api
---

# OtelObserver

**Package:** `flyteplugins.otel`

A `flyte._observe.Observer` that records spans.

Task spans are roots pinned to the run's derived trace id. Every attempt of a task
therefore starts its own subtree and because the trace id is shared those subtrees all
collect into the one trace: a resumed run reads as the attempt that crashed followed by
the attempt that finished.


## Parameters

```python
class OtelObserver(
    tracer: trace_api.Tracer,
)
```
| Parameter | Type | Description |
|-|-|-|
| `tracer` | `trace_api.Tracer` | |

## Methods

| Method | Description |
|-|-|
| [`step_span()`](#step_span) |  |
| [`task_span()`](#task_span) |  |


### step_span()

```python
def step_span(
    info: 'StepInfo',
    recorder: 'Recorder',
) -> Generator[None, None, None]
```
| Parameter | Type | Description |
|-|-|-|
| `info` | `'StepInfo'` | |
| `recorder` | `'Recorder'` | |

### task_span()

```python
def task_span(
    info: 'TaskInfo',
    recorder: 'Recorder',
) -> Generator[None, None, None]
```
| Parameter | Type | Description |
|-|-|-|
| `info` | `'TaskInfo'` | |
| `recorder` | `'Recorder'` | |

