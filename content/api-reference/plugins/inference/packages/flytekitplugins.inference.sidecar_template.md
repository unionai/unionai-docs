---
title: flytekitplugins.inference.sidecar_template
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.inference.sidecar_template

## Directory

### Classes

| Class | Description |
|-|-|
| [`ModelInferenceTemplate`](.././flytekitplugins.inference.sidecar_template#flytekitpluginsinferencesidecar_templatemodelinferencetemplate) |  |

## flytekitplugins.inference.sidecar_template.ModelInferenceTemplate

```python
class ModelInferenceTemplate(
    image: typing.Optional[str],
    health_endpoint: typing.Optional[str],
    port: int,
    cpu: int,
    gpu: int,
    mem: str,
    env: typing.Optional[dict[str, str]],
    download_inputs: bool,
    download_inputs_mem: str,
    download_inputs_cpu: int,
)
```
| Parameter | Type |
|-|-|
| `image` | `typing.Optional[str]` |
| `health_endpoint` | `typing.Optional[str]` |
| `port` | `int` |
| `cpu` | `int` |
| `gpu` | `int` |
| `mem` | `str` |
| `env` | `typing.Optional[dict[str, str]]` |
| `download_inputs` | `bool` |
| `download_inputs_mem` | `str` |
| `download_inputs_cpu` | `int` |

### Properties

| Property | Type | Description |
|-|-|-|
| `base_url` |  |  |
| `pod_template` |  |  |

