---
title: Dask
version: 2.0.0b54
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Dask

**Package:** `flyteplugins.dask`

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

