---
title: RayJobConfig
version: 2.0.0b60
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RayJobConfig

**Package:** `flyteplugins.ray`

```python
class RayJobConfig(
    worker_node_config: typing.List[flyteplugins.ray.task.WorkerNodeConfig],
    head_node_config: typing.Optional[flyteplugins.ray.task.HeadNodeConfig],
    enable_autoscaling: bool,
    runtime_env: typing.Optional[dict],
    address: typing.Optional[str],
    shutdown_after_job_finishes: bool,
    ttl_seconds_after_finished: typing.Optional[int],
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

