---
title: Scheduler
version: 2.0.0b56
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Scheduler

**Package:** `flyteplugins.dask`

Configuration for the scheduler pod



```python
class Scheduler(
    image: typing.Optional[str],
    resources: typing.Optional[flyte._resources.Resources],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | Custom image to use. If ``None``, will use the same image the task was registered with. Optional, defaults to None. The image must have ``dask[distributed]`` installed and should have the same Python environment as the rest of the cluster (job runner pod + worker pods). |
| `resources` | `typing.Optional[flyte._resources.Resources]` | Resources to request for the scheduler pod. Optional, defaults to None. |

