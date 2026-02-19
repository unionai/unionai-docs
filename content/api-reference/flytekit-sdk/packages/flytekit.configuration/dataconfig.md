---
title: DataConfig
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DataConfig

**Package:** `flytekit.configuration`

Any data storage specific configuration. Please do not use this to store secrets, in S3 case, as it is used in
Flyte sandbox environment we store the access key id and secret.
All DataPersistence plugins are passed all DataConfig and the plugin should correctly use the right config



```python
class DataConfig(
    s3: S3Config,
    gcs: GCSConfig,
    azure: AzureBlobStorageConfig,
    generic: GenericPersistenceConfig,
)
```
| Parameter | Type | Description |
|-|-|-|
| `s3` | `S3Config` | |
| `gcs` | `GCSConfig` | |
| `azure` | `AzureBlobStorageConfig` | |
| `generic` | `GenericPersistenceConfig` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> DataConfig
```
| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` | |

