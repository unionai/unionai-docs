---
title: WorkerGroup
version: 2.0.0b58
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkerGroup

**Package:** `flyteplugins.dask`

Configuration for a group of dask worker pods



```python
class WorkerGroup(
    number_of_workers: typing.Optional[int],
    image: typing.Optional[str],
    resources: typing.Optional[flyte._resources.Resources],
)
```
| Parameter | Type | Description |
|-|-|-|
| `number_of_workers` | `typing.Optional[int]` | Number of workers to use. Optional, defaults to 1. |
| `image` | `typing.Optional[str]` | Custom image to use. If ``None``, will use the same image the task was registered with. Optional, defaults to None. The image must have ``dask[distributed]`` installed. The provided image should have the same Python environment as the job runner/driver as well as the scheduler. |
| `resources` | `typing.Optional[flyte._resources.Resources]` | Resources to request for the worker pods. Optional, defaults to None. |

