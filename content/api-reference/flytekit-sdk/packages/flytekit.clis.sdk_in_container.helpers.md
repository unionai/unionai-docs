---
title: flytekit.clis.sdk_in_container.helpers
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.helpers

## Directory

### Methods

| Method | Description |
|-|-|
| [`get_and_save_remote_with_click_context()`](#get_and_save_remote_with_click_context) | NB: This function will by default mutate the click Context. |
| [`parse_copy()`](#parse_copy) | Helper function to parse cmd line args into enum. |
| [`patch_image_config()`](#patch_image_config) | Merge ImageConfig object with images defined in config file. |


### Variables

| Property | Type | Description |
|-|-|-|
| `CTX_CONFIG_FILE` | `str` |  |
| `FLYTE_REMOTE_INSTANCE_KEY` | `str` |  |

## Methods

#### get_and_save_remote_with_click_context()

```python
def get_and_save_remote_with_click_context(
    ctx: click.core.Context,
    project: str,
    domain: str,
    save: bool,
    data_upload_location: typing.Optional[str],
) -> flytekit.remote.remote.FlyteRemote
```
NB: This function will by default mutate the click Context.obj dictionary, adding a remote key with value
    of the created FlyteRemote object.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | the click context object |
| `project` | `str` | default project for the remote instance |
| `domain` | `str` | default domain |
| `save` | `bool` | If false, will not mutate the context.obj dict |
| `data_upload_location` | `typing.Optional[str]` | if specified, will set the data upload location for the remote instance :return: FlyteRemote instance |

#### parse_copy()

```python
def parse_copy(
    ctx,
    param,
    value,
) -> typing.Optional[flytekit.constants.CopyFileDetection]
```
Helper function to parse cmd line args into enum


| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | |
| `param` |  | |
| `value` |  | |

#### patch_image_config()

```python
def patch_image_config(
    config_file: typing.Optional[str],
    image_config: flytekit.configuration.ImageConfig,
) -> flytekit.configuration.ImageConfig
```
Merge ImageConfig object with images defined in config file


| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Optional[str]` | |
| `image_config` | `flytekit.configuration.ImageConfig` | |

