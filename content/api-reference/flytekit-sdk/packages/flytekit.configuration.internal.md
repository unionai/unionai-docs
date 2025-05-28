---
title: flytekit.configuration.internal
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.configuration.internal

## Directory

### Classes

| Class | Description |
|-|-|
| [`AWS`](.././flytekit.configuration.internal#flytekitconfigurationinternalaws) |  |
| [`AZURE`](.././flytekit.configuration.internal#flytekitconfigurationinternalazure) |  |
| [`Credentials`](.././flytekit.configuration.internal#flytekitconfigurationinternalcredentials) |  |
| [`GCP`](.././flytekit.configuration.internal#flytekitconfigurationinternalgcp) |  |
| [`Images`](.././flytekit.configuration.internal#flytekitconfigurationinternalimages) |  |
| [`Local`](.././flytekit.configuration.internal#flytekitconfigurationinternallocal) |  |
| [`LocalSDK`](.././flytekit.configuration.internal#flytekitconfigurationinternallocalsdk) |  |
| [`Persistence`](.././flytekit.configuration.internal#flytekitconfigurationinternalpersistence) |  |
| [`Platform`](.././flytekit.configuration.internal#flytekitconfigurationinternalplatform) |  |
| [`Secrets`](.././flytekit.configuration.internal#flytekitconfigurationinternalsecrets) |  |
| [`StatsD`](.././flytekit.configuration.internal#flytekitconfigurationinternalstatsd) |  |

## flytekit.configuration.internal.AWS

## flytekit.configuration.internal.AZURE

## flytekit.configuration.internal.Credentials

## flytekit.configuration.internal.GCP

## flytekit.configuration.internal.Images

### Methods

| Method | Description |
|-|-|
| [`get_specified_images()`](#get_specified_images) | This section should contain options, where the option name is the friendly name of the image and the corresponding. |


#### get_specified_images()

```python
def get_specified_images(
    cfg: typing.Optional[flytekit.configuration.file.ConfigFile],
) -> typing.Dict[str, str]
```
This section should contain options, where the option name is the friendly name of the image and the corresponding
value is actual FQN of the image. Example of how the section is structured
[images]
my_image1=docker.io/flyte:tag
# Note that the tag is optional. If not specified it will be the default version identifier specified
my_image2=docker.io/flyte

:returns a dictionary of name: image<fqn+version> Version is optional


| Parameter | Type |
|-|-|
| `cfg` | `typing.Optional[flytekit.configuration.file.ConfigFile]` |

## flytekit.configuration.internal.Local

## flytekit.configuration.internal.LocalSDK

## flytekit.configuration.internal.Persistence

## flytekit.configuration.internal.Platform

## flytekit.configuration.internal.Secrets

## flytekit.configuration.internal.StatsD

