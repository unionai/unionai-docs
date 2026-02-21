---
title: flytekitplugins.inference.ollama.serve
version: 1.16.14
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
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the model. |
| `mem` | `str` | The amount of memory allocated for the model, specified as a string. Default is "500Mi". |
| `cpu` | `int` | The number of CPU cores allocated for the model. Default is 1. |
| `modelfile` | `typing.Optional[str]` | The actual model file as a JSON-serializable string. This represents the file content. Default is `None` if not applicable. |

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



| Parameter | Type | Description |
|-|-|-|
| `model` | `flytekitplugins.inference.ollama.serve.Model` | An instance of the Model class containing the model's configuration, including its name, memory, CPU, and file. |
| `image` | `str` | The Docker image to be used for the container. Default is "ollama/ollama". |
| `port` | `int` | The port number on which the container should expose its service. Default is 11434. |
| `cpu` | `int` | The number of CPU cores requested for the container. Default is 1. |
| `gpu` | `int` | The number of GPUs requested for the container. Default is 1. |
| `mem` | `str` | The amount of memory requested for the container, specified as a string. Default is "15Gi". |
| `download_inputs_mem` | `str` | The amount of memory requested for downloading inputs, specified as a string. Default is "500Mi". |
| `download_inputs_cpu` | `int` | The number of CPU cores requested for downloading inputs. Default is 2. |

### Properties

| Property | Type | Description |
|-|-|-|
| `base_url` | `None` |  |
| `pod_template` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`setup_ollama_pod_template()`](#setup_ollama_pod_template) |  |


#### setup_ollama_pod_template()

```python
def setup_ollama_pod_template()
```
