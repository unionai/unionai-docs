---
title: HeadNodeConfig
version: 2.0.12.dev22+g879ad6de4
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# HeadNodeConfig

**Package:** `flyteplugins.ray`

## Parameters

```python
class HeadNodeConfig(
    ray_start_params: typing.Optional[typing.Dict[str, str]],
    pod_template: typing.Optional[flyte._pod.PodTemplate],
    requests: typing.Optional[flyte._resources.Resources],
    limits: typing.Optional[flyte._resources.Resources],
)
```
| Parameter | Type | Description |
|-|-|-|
| `ray_start_params` | `typing.Optional[typing.Dict[str, str]]` | |
| `pod_template` | `typing.Optional[flyte._pod.PodTemplate]` | |
| `requests` | `typing.Optional[flyte._resources.Resources]` | |
| `limits` | `typing.Optional[flyte._resources.Resources]` | |

