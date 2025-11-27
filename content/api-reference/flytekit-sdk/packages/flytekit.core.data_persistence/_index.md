---
title: flytekit.core.data_persistence
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.data_persistence


The Data persistence module is used by core flytekit and most of the core TypeTransformers to manage data fetch & store,
between the durable backend store and the runtime environment. This is designed to be a pluggable system, with a default
simple implementation that ships with the core.

## Directory

### Classes

| Class | Description |
|-|-|
| [`FileAccessProvider`](../flytekit.core.data_persistence/fileaccessprovider) | This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |

### Methods

| Method | Description |
|-|-|
| [`azure_setup_args()`](#azure_setup_args) |  |
| [`get_additional_fsspec_call_kwargs()`](#get_additional_fsspec_call_kwargs) | These are different from the setup args functions defined above. |
| [`get_fsspec_storage_options()`](#get_fsspec_storage_options) |  |
| [`s3_setup_args()`](#s3_setup_args) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `default_local_file_access_provider` | `FileAccessProvider` |  |
| `flyte_tmp_dir` | `str` |  |

## Methods

#### azure_setup_args()

```python
def azure_setup_args(
    azure_cfg: flytekit.configuration.AzureBlobStorageConfig,
    anonymous: bool,
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type | Description |
|-|-|-|
| `azure_cfg` | `flytekit.configuration.AzureBlobStorageConfig` | |
| `anonymous` | `bool` | |

#### get_additional_fsspec_call_kwargs()

```python
def get_additional_fsspec_call_kwargs(
    protocol: typing.Union[str, tuple],
    method_name: str,
) -> typing.Dict[str, typing.Any]
```
These are different from the setup args functions defined above. Those kwargs are applied when asking fsspec
to create the filesystem. These kwargs returned here are for when the filesystem's methods are invoked.



| Parameter | Type | Description |
|-|-|-|
| `protocol` | `typing.Union[str, tuple]` | s3, gcs, etc. |
| `method_name` | `str` | Pass in the __name__ of the fsspec.filesystem function. _'s will be ignored. |

#### get_fsspec_storage_options()

```python
def get_fsspec_storage_options(
    protocol: str,
    data_config: typing.Optional[flytekit.configuration.DataConfig],
    anonymous: bool,
    kwargs,
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type | Description |
|-|-|-|
| `protocol` | `str` | |
| `data_config` | `typing.Optional[flytekit.configuration.DataConfig]` | |
| `anonymous` | `bool` | |
| `kwargs` | `**kwargs` | |

#### s3_setup_args()

```python
def s3_setup_args(
    s3_cfg: flytekit.configuration.S3Config,
    anonymous: bool,
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type | Description |
|-|-|-|
| `s3_cfg` | `flytekit.configuration.S3Config` | |
| `anonymous` | `bool` | |

