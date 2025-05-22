---
title: flytekitplugins.inference.ollama.serve
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.inference.ollama.serve

## Directory

### Classes

| Class | Description |
|-|-|
| [`Model`](.././flytekitplugins.inference.ollama.serve#flytekitpluginsinferenceollamaservemodel) | Represents the configuration for a model used in a Kubernetes pod template. |
| [`Ollama`](.././flytekitplugins.inference.ollama.serve#flytekitpluginsinferenceollamaserveollama) |  |

## flytekitplugins.inference.ollama.serve.Model

Represents the configuration for a model used in a Kubernetes pod template.



```python
class Model(
    name: str,
    mem: str,
    cpu: int,
    modelfile: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `mem` | `str` |
| `cpu` | `int` |
| `modelfile` | `typing.Optional[str]` |

## flytekitplugins.inference.ollama.serve.Ollama

```python
class Ollama(
    model: flytekitplugins.inference.ollama.serve.Model,
    image: str,
    port: int,
    cpu: int,
    gpu: int,
    mem: str,
    download_inputs_mem: str,
    download_inputs_cpu: int,
)
```
Initialize Ollama class for managing a Kubernetes pod template.



| Parameter | Type |
|-|-|
| `model` | `flytekitplugins.inference.ollama.serve.Model` |
| `image` | `str` |
| `port` | `int` |
| `cpu` | `int` |
| `gpu` | `int` |
| `mem` | `str` |
| `download_inputs_mem` | `str` |
| `download_inputs_cpu` | `int` |

### Methods

| Method | Description |
|-|-|
| [`setup_ollama_pod_template()`](#setup_ollama_pod_template) |  |


#### setup_ollama_pod_template()

```python
def setup_ollama_pod_template()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `base_url` |  |  |
| `pod_template` |  |  |

