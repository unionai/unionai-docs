---
title: RayJobConfig
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# RayJobConfig

**Package:** `flyteplugins.ray`

## Parameters

```python
class RayJobConfig(
    worker_node_config: typing.List[flyteplugins.ray.task.WorkerNodeConfig],
    head_node_config: typing.Optional[flyteplugins.ray.task.HeadNodeConfig] = None,
    enable_autoscaling: bool = False,
    runtime_env: typing.Optional[dict] = None,
    address: typing.Optional[str] = None,
    shutdown_after_job_finishes: bool = False,
    ttl_seconds_after_finished: typing.Optional[int] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `worker_node_config` | `typing.List[flyteplugins.ray.task.WorkerNodeConfig]` | |
| `head_node_config` | `typing.Optional[flyteplugins.ray.task.HeadNodeConfig]` | |
| `enable_autoscaling` | `bool` | |
| `runtime_env` | `typing.Optional[dict]` | |
| `address` | `typing.Optional[str]` | |
| `shutdown_after_job_finishes` | `bool` | |
| `ttl_seconds_after_finished` | `typing.Optional[int]` | |

