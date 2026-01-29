---
title: Dask
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Dask

**Package:** `flyteplugins.dask.task`

Configuration for the dask task



```python
class Dask(
    scheduler: flyteplugins.dask.task.Scheduler,
    workers: flyteplugins.dask.task.WorkerGroup,
)
```
| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `flyteplugins.dask.task.Scheduler` | Configuration for the scheduler pod. Optional, defaults to ``Scheduler()``. |
| `workers` | `flyteplugins.dask.task.WorkerGroup` | Configuration for the pods of the default worker group. Optional, defaults to ``WorkerGroup()``. |

