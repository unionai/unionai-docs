---
title: HeadNodeConfig
version: 2.1.3.dev1+ge23e739d5
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

