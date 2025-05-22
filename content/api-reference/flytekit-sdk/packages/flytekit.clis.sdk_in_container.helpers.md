---
title: flytekit.clis.sdk_in_container.helpers
version: 0.1.dev2192+g7c539c3.d20250403
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
) -> n: FlyteRemote instance
```
NB: This function will by default mutate the click Context.obj dictionary, adding a remote key with value
    of the created FlyteRemote object.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `project` | `str` |
| `domain` | `str` |
| `save` | `bool` |
| `data_upload_location` | `typing.Optional[str]` |

#### parse_copy()

```python
def parse_copy(
    ctx,
    param,
    value,
) -> typing.Optional[flytekit.constants.CopyFileDetection]
```
Helper function to parse cmd line args into enum


| Parameter | Type |
|-|-|
| `ctx` |  |
| `param` |  |
| `value` |  |

#### patch_image_config()

```python
def patch_image_config(
    config_file: typing.Optional[str],
    image_config: flytekit.configuration.ImageConfig,
) -> flytekit.configuration.ImageConfig
```
Merge ImageConfig object with images defined in config file


| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[str]` |
| `image_config` | `flytekit.configuration.ImageConfig` |

