---
title: AutoscalerOptionsConfig
description: "Configuration for the Ray autoscaler sidecar."
icon: braces
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# AutoscalerOptionsConfig

**Package:** `flyteplugins.ray`

Configuration for the Ray autoscaler sidecar.

upscaling_mode: an AutoscalerOptionsConfig.UpscalingMode value, e.g.
                AutoscalerOptionsConfig.UpscalingMode.CONSERVATIVE.
idle_timeout_seconds: seconds before an idle node is removed.
image: custom container image for the autoscaler sidecar.
env: environment variables injected into the autoscaler container.
resources: CPU/memory/GPU resource requests and limits for the sidecar.
           Use tuple values (request, limit) for request/limit pairs,
           e.g. Resources(cpu=("500m", "1"), memory=("512Mi", "1Gi")).


## Parameters

```python
class AutoscalerOptionsConfig(
    upscaling_mode: typing.Optional[ForwardRef('AutoscalerOptions.UpscalingMode')] = None,
    idle_timeout_seconds: typing.Optional[int] = None,
    image: typing.Optional[str] = None,
    env: typing.Optional[typing.Dict[str, str]] = None,
    resources: typing.Optional[flyte._resources.Resources] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `upscaling_mode` | `typing.Optional[ForwardRef('AutoscalerOptions.UpscalingMode')]` | |
| `idle_timeout_seconds` | `typing.Optional[int]` | |
| `image` | `typing.Optional[str]` | |
| `env` | `typing.Optional[typing.Dict[str, str]]` | |
| `resources` | `typing.Optional[flyte._resources.Resources]` | |

