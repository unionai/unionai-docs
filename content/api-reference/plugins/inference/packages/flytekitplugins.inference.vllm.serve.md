---
title: flytekitplugins.inference.vllm.serve
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.inference.vllm.serve

## Directory

### Classes

| Class | Description |
|-|-|
| [`HFSecret`](.././flytekitplugins.inference.vllm.serve#flytekitpluginsinferencevllmservehfsecret) | . |
| [`VLLM`](.././flytekitplugins.inference.vllm.serve#flytekitpluginsinferencevllmservevllm) |  |

## flytekitplugins.inference.vllm.serve.HFSecret

```python
class HFSecret(
    secrets_prefix: str,
    hf_token_key: str,
    hf_token_group: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `secrets_prefix` | `str` |
| `hf_token_key` | `str` |
| `hf_token_group` | `typing.Optional[str]` |

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



| Parameter | Type |
|-|-|
| `hf_secret` | `flytekitplugins.inference.vllm.serve.HFSecret` |
| `arg_dict` | `typing.Optional[dict]` |
| `image` | `str` |
| `health_endpoint` | `str` |
| `port` | `int` |
| `cpu` | `int` |
| `gpu` | `int` |
| `mem` | `str` |

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
### Properties

| Property | Type | Description |
|-|-|-|
| `base_url` |  |  |
| `pod_template` |  |  |

