---
title: Update
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Update

**Package:** `flytekit.core.worker_queue`

```python
class Update(
    work_item: WorkItem,
    idx: int,
    status: typing.Optional[ItemStatus],
    wf_exec: typing.Optional[FlyteWorkflowExecution],
    error: typing.Optional[BaseException],
)
```
| Parameter | Type | Description |
|-|-|-|
| `work_item` | `WorkItem` | |
| `idx` | `int` | |
| `status` | `typing.Optional[ItemStatus]` | |
| `wf_exec` | `typing.Optional[FlyteWorkflowExecution]` | |
| `error` | `typing.Optional[BaseException]` | |

