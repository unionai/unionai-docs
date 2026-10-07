---
title: FlyteIdentityBinding
description: "Binds Flyte's run, task, and version onto agento11y's context for each task."
icon: braces
version: 2.11.1.dev2+g6d3d72b81
variants: +flyte +union
layout: py_api
---

# FlyteIdentityBinding

**Package:** `flyteplugins.agento11y`

Binds Flyte's run, task, and version onto agento11y's context for each task.


## Parameters

```python
class FlyteIdentityBinding(
    bind_conversation: bool = True,
    bind_agent_name: bool = True,
)
```
| Parameter | Type | Description |
|-|-|-|
| `bind_conversation` | `bool` | |
| `bind_agent_name` | `bool` | |

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

