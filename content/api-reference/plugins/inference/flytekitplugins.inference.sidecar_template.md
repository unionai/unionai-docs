---
title: flytekitplugins.inference.sidecar_template
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekitplugins.inference.sidecar_template

## Directory

### Classes

| Class | Description |
|-|-|
| [`ModelInferenceTemplate`](./flytekitplugins.inference.sidecar_template#flytekitpluginsinferencesidecar_templatemodelinferencetemplate) |  |

## flytekitplugins.inference.sidecar_template.ModelInferenceTemplate

### Parameters

```python
class ModelInferenceTemplate(
    image: typing.Optional[str] = None,
    health_endpoint: typing.Optional[str] = None,
    port: int = 8000,
    cpu: int = 1,
    gpu: int = 1,
    mem: str = '1Gi',
    ephemeral_storage: str = '1Gi',
    env: typing.Optional[dict[str, str]] = None,
    download_inputs: bool = False,
    download_inputs_mem: str = '500Mi',
    download_inputs_cpu: int = 2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | |
| `health_endpoint` | `typing.Optional[str]` | |
| `port` | `int` | |
| `cpu` | `int` | |
| `gpu` | `int` | |
| `mem` | `str` | |
| `ephemeral_storage` | `str` | |
| `env` | `typing.Optional[dict[str, str]]` | |
| `download_inputs` | `bool` | |
| `download_inputs_mem` | `str` | |
| `download_inputs_cpu` | `int` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `base_url` | `None` |  |
| `pod_template` | `None` |  |

