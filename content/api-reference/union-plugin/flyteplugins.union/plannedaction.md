---
title: PlannedAction
description: "One source-run action, as a fork plan sees it."
icon: braces
version: 0.26.2
variants: -flyte +union
layout: py_api
---

# PlannedAction

**Package:** `flyteplugins.union`

One source-run action, as a fork plan sees it.


## Parameters

```python
class PlannedAction(
    name: str,
    task_name: Optional[str],
    phase: ActionPhase,
    started_at: Optional[datetime] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `task_name` | `Optional[str]` | |
| `phase` | `ActionPhase` | |
| `started_at` | `Optional[datetime]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `short_task_name` | `Optional[str]` | The task's name without its environment prefix: `slow_features` for `env.slow_features`. |

## Methods

| Method | Description |
|-|-|
| [`to_dict()`](#to_dict) |  |


### to_dict()

```python
def to_dict()
```
