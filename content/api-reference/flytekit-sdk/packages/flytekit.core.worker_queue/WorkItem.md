---
title: WorkItem
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkItem

**Package:** `flytekit.core.worker_queue`

This is a class to keep track of what the user requested. Since it captures the arguments that the user wants
to run the entity with, an arbitrary map, can't make this frozen.


```python
class WorkItem(
    entity: RunnableEntity,
    input_kwargs: dict[str, typing.Any],
    result: typing.Any,
    error: typing.Optional[BaseException],
    status: ItemStatus,
    wf_exec: typing.Optional[FlyteWorkflowExecution],
    python_interface: typing.Optional[Interface],
    uuid: typing.Optional[uuid.UUID],
)
```
| Parameter | Type | Description |
|-|-|-|
| `entity` | `RunnableEntity` | |
| `input_kwargs` | `dict[str, typing.Any]` | |
| `result` | `typing.Any` | |
| `error` | `typing.Optional[BaseException]` | |
| `status` | `ItemStatus` | |
| `wf_exec` | `typing.Optional[FlyteWorkflowExecution]` | |
| `python_interface` | `typing.Optional[Interface]` | |
| `uuid` | `typing.Optional[uuid.UUID]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_in_terminal_state` |  |  |

