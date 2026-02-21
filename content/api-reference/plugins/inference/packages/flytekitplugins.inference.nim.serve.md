---
title: flytekitplugins.inference.nim.serve
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.inference.nim.serve

## Directory

### Classes

| Class | Description |
|-|-|
| [`NIM`](.././flytekitplugins.inference.nim.serve#flytekitpluginsinferencenimservenim) |  |
| [`NIMSecrets`](.././flytekitplugins.inference.nim.serve#flytekitpluginsinferencenimservenimsecrets) |  |

## flytekitplugins.inference.nim.serve.NIM

```python
class NIM(
    secrets: flytekitplugins.inference.nim.serve.NIMSecrets,
    image: str,
    health_endpoint: str,
    port: int,
    cpu: int,
    gpu: int,
    mem: str,
    ephemeral_storage: str,
    shm_size: str,
    env: typing.Optional[dict[str, str]],
    hf_repo_ids: typing.Optional[list[str]],
    lora_adapter_mem: typing.Optional[str],
)
```
Initialize NIM class for managing a Kubernetes pod template.



| Parameter | Type | Description |
|-|-|-|
| `secrets` | `flytekitplugins.inference.nim.serve.NIMSecrets` | Instance of NIMSecrets for managing secrets. |
| `image` | `str` | The Docker image to be used for the model server container. Default is "nvcr.io/nim/meta/llama3-8b-instruct |
| `health_endpoint` | `str` | The health endpoint for the model server container. Default is "v1/health/ready". |
| `port` | `int` | The port number for the model server container. Default is 8000. |
| `cpu` | `int` | The number of CPU cores requested for the model server container. Default is 1. |
| `gpu` | `int` | The number of GPU cores requested for the model server container. Default is 1. |
| `mem` | `str` | The amount of memory requested for the model server container. Default is "20Gi". |
| `ephemeral_storage` | `str` | The amount of ephemeral storage requested for the model server container. Default is "20Gi". |
| `shm_size` | `str` | The size of the shared memory volume. Default is "16Gi". |
| `env` | `typing.Optional[dict[str, str]]` | A dictionary of environment variables to be set in the model server container. |
| `hf_repo_ids` | `typing.Optional[list[str]]` | A list of Hugging Face repository IDs for LoRA adapters to be downloaded. |
| `lora_adapter_mem` | `typing.Optional[str]` | The amount of memory requested for the init container that downloads LoRA adapters. |

### Properties

| Property | Type | Description |
|-|-|-|
| `base_url` | `None` |  |
| `pod_template` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`setup_nim_pod_template()`](#setup_nim_pod_template) |  |


#### setup_nim_pod_template()

```python
def setup_nim_pod_template()
```
## flytekitplugins.inference.nim.serve.NIMSecrets

```python
class NIMSecrets(
    ngc_secret_key: str,
    secrets_prefix: str,
    ngc_image_secret: typing.Optional[str],
    ngc_secret_group: typing.Optional[str],
    hf_token_group: typing.Optional[str],
    hf_token_key: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `ngc_secret_key` | `str` | The key name for the NGC API key. |
| `secrets_prefix` | `str` | The secrets prefix that Flyte appends to all mounted secrets. |
| `ngc_image_secret` | `typing.Optional[str]` | The name of the Kubernetes secret containing the NGC image pull credentials. |
| `ngc_secret_group` | `typing.Optional[str]` | The group name for the NGC API key. |
| `hf_token_group` | `typing.Optional[str]` | The group name for the HuggingFace token. |
| `hf_token_key` | `typing.Optional[str]` | The key name for the HuggingFace token. |

