---
title: HeadNodeConfig
version: 2.6.1
variants: +flyte +union
layout: py_api
---

# HeadNodeConfig

**Package:** `flyteplugins.ray`

## Parameters

```python
class HeadNodeConfig(
    ray_start_params: typing.Optional[typing.Dict[str, str]] = None,
    pod_template: typing.Optional[flyte._pod.PodTemplate] = None,
    requests: typing.Optional[flyte._resources.Resources] = None,
    limits: typing.Optional[flyte._resources.Resources] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ray_start_params` | `typing.Optional[typing.Dict[str, str]]` | |
| `pod_template` | `typing.Optional[flyte._pod.PodTemplate]` | |
| `requests` | `typing.Optional[flyte._resources.Resources]` | |
| `limits` | `typing.Optional[flyte._resources.Resources]` | |

