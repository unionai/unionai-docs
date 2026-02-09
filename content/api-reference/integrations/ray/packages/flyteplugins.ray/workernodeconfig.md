---
title: WorkerNodeConfig
version: 2.0.0b55
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkerNodeConfig

**Package:** `flyteplugins.ray`

```python
class WorkerNodeConfig(
    group_name: str,
    replicas: int,
    min_replicas: typing.Optional[int],
    max_replicas: typing.Optional[int],
    ray_start_params: typing.Optional[typing.Dict[str, str]],
    pod_template: typing.Optional[flyte._pod.PodTemplate],
    requests: typing.Optional[flyte._resources.Resources],
    limits: typing.Optional[flyte._resources.Resources],
)
```
| Parameter | Type | Description |
|-|-|-|
| `group_name` | `str` | |
| `replicas` | `int` | |
| `min_replicas` | `typing.Optional[int]` | |
| `max_replicas` | `typing.Optional[int]` | |
| `ray_start_params` | `typing.Optional[typing.Dict[str, str]]` | |
| `pod_template` | `typing.Optional[flyte._pod.PodTemplate]` | |
| `requests` | `typing.Optional[flyte._resources.Resources]` | |
| `limits` | `typing.Optional[flyte._resources.Resources]` | |

