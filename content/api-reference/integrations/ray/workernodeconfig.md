---
title: WorkerNodeConfig
icon: braces
version: 2.6.13
variants: +flyte +union
layout: py_api
---

# WorkerNodeConfig

**Package:** `flyteplugins.ray`

## Parameters

```python
class WorkerNodeConfig(
    group_name: str,
    replicas: int,
    min_replicas: typing.Optional[int] = None,
    max_replicas: typing.Optional[int] = None,
    ray_start_params: typing.Optional[typing.Dict[str, str]] = None,
    pod_template: typing.Optional[flyte._pod.PodTemplate] = None,
    requests: typing.Optional[flyte._resources.Resources] = None,
    limits: typing.Optional[flyte._resources.Resources] = None,
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

