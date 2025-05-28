---
title: flytekitplugins.inference.nim.serve
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.inference.nim.serve

## Directory

### Classes

| Class | Description |
|-|-|
| [`NIM`](.././flytekitplugins.inference.nim.serve#flytekitpluginsinferencenimservenim) |  |
| [`NIMSecrets`](.././flytekitplugins.inference.nim.serve#flytekitpluginsinferencenimservenimsecrets) | . |

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
    shm_size: str,
    env: typing.Optional[dict[str, str]],
    hf_repo_ids: typing.Optional[list[str]],
    lora_adapter_mem: typing.Optional[str],
)
```
Initialize NIM class for managing a Kubernetes pod template.



| Parameter | Type |
|-|-|
| `secrets` | `flytekitplugins.inference.nim.serve.NIMSecrets` |
| `image` | `str` |
| `health_endpoint` | `str` |
| `port` | `int` |
| `cpu` | `int` |
| `gpu` | `int` |
| `mem` | `str` |
| `shm_size` | `str` |
| `env` | `typing.Optional[dict[str, str]]` |
| `hf_repo_ids` | `typing.Optional[list[str]]` |
| `lora_adapter_mem` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`setup_nim_pod_template()`](#setup_nim_pod_template) |  |


#### setup_nim_pod_template()

```python
def setup_nim_pod_template()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `base_url` |  |  |
| `pod_template` |  |  |

## flytekitplugins.inference.nim.serve.NIMSecrets

```python
class NIMSecrets(
    ngc_image_secret: str,
    ngc_secret_key: str,
    secrets_prefix: str,
    ngc_secret_group: typing.Optional[str],
    hf_token_group: typing.Optional[str],
    hf_token_key: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `ngc_image_secret` | `str` |
| `ngc_secret_key` | `str` |
| `secrets_prefix` | `str` |
| `ngc_secret_group` | `typing.Optional[str]` |
| `hf_token_group` | `typing.Optional[str]` |
| `hf_token_key` | `typing.Optional[str]` |

