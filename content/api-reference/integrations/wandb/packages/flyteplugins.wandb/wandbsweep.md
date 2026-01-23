---
title: WandbSweep
version: 2.0.0b49.dev15+g590cd201b
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WandbSweep

**Package:** `flyteplugins.wandb`

Generates a Weights & Biases Sweep link.


```python
class WandbSweep(
    host: str,
    project: typing.Optional[str],
    entity: typing.Optional[str],
    id: typing.Optional[str],
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `host` | `str` | |
| `project` | `typing.Optional[str]` | |
| `entity` | `typing.Optional[str]` | |
| `id` | `typing.Optional[str]` | |
| `name` | `str` | |

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
    context: typing.Dict[str, str],
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
| `context` | `typing.Dict[str, str]` | Additional context for generating the link. |
| `parent_action_name` | `str` | The name of the parent action. |
| `action_name` | `str` | The name of the action. |
| `pod_name` | `str` | The name of the pod. :return: The generated link. |
| `kwargs` | `**kwargs` | |

