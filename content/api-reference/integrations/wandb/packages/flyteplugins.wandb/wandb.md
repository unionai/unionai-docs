---
title: Wandb
version: 2.0.0b56
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Wandb

**Package:** `flyteplugins.wandb`

Generates a Weights & Biases run link.



```python
class Wandb(
    host: str,
    project: typing.Optional[str],
    entity: typing.Optional[str],
    run_mode: typing.Literal['auto', 'new', 'shared'],
    rank_scope: typing.Literal['global', 'worker'],
    id: typing.Optional[str],
    name: str,
    _is_distributed: bool,
    _worker_index: typing.Optional[int],
)
```
| Parameter | Type | Description |
|-|-|-|
| `host` | `str` | Base W&B host URL |
| `project` | `typing.Optional[str]` | W&B project name (overrides context config if provided) |
| `entity` | `typing.Optional[str]` | W&B entity/team name (overrides context config if provided) - "auto" (default): Use parent's run if available, otherwise create new - "new": Always creates a new wandb run with a unique ID - "shared": Always shares the parent's run ID In distributed training context (single-node): - "auto" (default): Only rank 0 logs. - "shared": All ranks log to a single shared W&B run. - "new": Each rank gets its own W&B run (grouped in W&B UI). Multi-node: behavior depends on `rank_scope`. |
| `run_mode` | `typing.Literal['auto', 'new', 'shared']` | |
| `rank_scope` | `typing.Literal['global', 'worker']` | Flyte-specific rank scope - "global" or "worker". Controls which ranks log in distributed training. run_mode="auto": - "global" (default): Only global rank 0 logs (1 run total). - "worker": Local rank 0 of each worker logs (1 run per worker). run_mode="shared": - "global": All ranks log to a single shared W&B run. - "worker": Ranks per worker log to a single shared W&B run (1 run per worker). run_mode="new": - "global": Each rank gets its own W&B run (1 run total). - "worker": Each rank gets its own W&B run grouped per worker -&gt; N runs. |
| `id` | `typing.Optional[str]` | Optional W&B run ID (overrides context config if provided) |
| `name` | `str` | Link name in the Flyte UI |
| `_is_distributed` | `bool` | |
| `_worker_index` | `typing.Optional[int]` | |

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
| `pod_name` | `str` | The name of the pod. |
| `kwargs` | `**kwargs` | Additional keyword arguments. :return: The generated link. |

