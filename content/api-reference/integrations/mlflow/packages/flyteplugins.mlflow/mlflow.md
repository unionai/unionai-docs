---
title: Mlflow
version: 2.0.11
variants: +flyte +union
layout: py_api
---

# Mlflow

**Package:** `flyteplugins.mlflow`

MLflow UI link for Flyte tasks.

Resolves the link URL from one of two sources (in priority order):

1. **Explicit link** — set at definition or override time::

       @env.task(links=[Mlflow(link="https://mlflow.example.com/...")])

       task.override(links=[Mlflow(link="https://...")])()

2. **Context link** — auto-generated from `link_host` (and optional
   `link_template`) set via `mlflow_config()`. Propagates to child
   tasks that share or nest under the parent's run. Cleared when a task
   creates an independent run (`run_mode="new"`). For nested runs
   (`run_mode="nested"`), the parent link is kept and the link name
   is automatically set to "MLflow (parent)".


## Parameters

```python
class Mlflow(
    name: str,
    link: str,
    _decorator_run_mode: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `link` | `str` | |
| `_decorator_run_mode` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`get_link()`](#get_link) | Returns a task log link given the action. |


### get_link()

```python
def get_link(
    run_name: str,
    project: str,
    domain: str,
    context: dict[str, str],
    parent_action_name: str,
    action_name: str,
    pod_name: str,
    kwargs,
) -> str
```
Returns a task log link given the action.
Link can have template variables that are replaced by the backend.


| Parameter | Type | Description |
|-|-|-|
| `run_name` | `str` | The name of the run. |
| `project` | `str` | The project name. |
| `domain` | `str` | The domain name. |
| `context` | `dict[str, str]` | Additional context for generating the link. |
| `parent_action_name` | `str` | The name of the parent action. |
| `action_name` | `str` | The name of the action. |
| `pod_name` | `str` | The name of the pod. |
| `kwargs` | `**kwargs` | Additional keyword arguments. |

**Returns:** The generated link.

