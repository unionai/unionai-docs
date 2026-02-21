---
title: flytekitplugins.inference.vllm.serve
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.inference.vllm.serve

## Directory

### Classes

| Class | Description |
|-|-|
| [`HFSecret`](.././flytekitplugins.inference.vllm.serve#flytekitpluginsinferencevllmservehfsecret) |  |
| [`VLLM`](.././flytekitplugins.inference.vllm.serve#flytekitpluginsinferencevllmservevllm) |  |

## flytekitplugins.inference.vllm.serve.HFSecret

```python
class HFSecret(
    secrets_prefix: str,
    hf_token_key: str,
    hf_token_group: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `secrets_prefix` | `str` | The secrets prefix that Flyte appends to all mounted secrets. |
| `hf_token_key` | `str` | The key name for the HuggingFace token. |
| `hf_token_group` | `typing.Optional[str]` | The group name for the HuggingFace token. |

## flytekitplugins.inference.vllm.serve.VLLM

```python
class VLLM(
    hf_secret: flytekitplugins.inference.vllm.serve.HFSecret,
    arg_dict: typing.Optional[dict],
    image: str,
    health_endpoint: str,
    port: int,
    cpu: int,
    gpu: int,
    mem: str,
)
```
Initialize NIM class for managing a Kubernetes pod template.



| Parameter | Type | Description |
|-|-|-|
| `hf_secret` | `flytekitplugins.inference.vllm.serve.HFSecret` | Instance of HFSecret for managing hugging face secrets. |
| `arg_dict` | `typing.Optional[dict]` | A dictionary of arguments for the VLLM model server (https |
| `image` | `str` | The Docker image to be used for the model server container. Default is "vllm/vllm-openai". |
| `health_endpoint` | `str` | The health endpoint for the model server container. Default is "/health". |
| `port` | `int` | The port number for the model server container. Default is 8000. |
| `cpu` | `int` | The number of CPU cores requested for the model server container. Default is 2. |
| `gpu` | `int` | The number of GPU cores requested for the model server container. Default is 1. |
| `mem` | `str` | The amount of memory requested for the model server container. Default is "10Gi". |

### Properties

| Property | Type | Description |
|-|-|-|
| `base_url` | `None` |  |
| `pod_template` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`build_vllm_args()`](#build_vllm_args) |  |
| [`setup_vllm_pod_template()`](#setup_vllm_pod_template) |  |


#### build_vllm_args()

```python
def build_vllm_args()
```
#### setup_vllm_pod_template()

```python
def setup_vllm_pod_template()
```
