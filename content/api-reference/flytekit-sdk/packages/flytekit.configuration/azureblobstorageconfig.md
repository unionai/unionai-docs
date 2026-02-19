---
title: AzureBlobStorageConfig
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# AzureBlobStorageConfig

**Package:** `flytekit.configuration`

Any Azure Blob Storage specific configuration.



```python
class AzureBlobStorageConfig(
    account_name: typing.Optional[str],
    account_key: typing.Optional[str],
    tenant_id: typing.Optional[str],
    client_id: typing.Optional[str],
    client_secret: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `account_name` | `typing.Optional[str]` | |
| `account_key` | `typing.Optional[str]` | |
| `tenant_id` | `typing.Optional[str]` | |
| `client_id` | `typing.Optional[str]` | |
| `client_secret` | `typing.Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> GCSConfig
```
| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` | |

