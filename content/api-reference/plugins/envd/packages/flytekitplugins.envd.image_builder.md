---
title: flytekitplugins.envd.image_builder
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.envd.image_builder

## Directory

### Classes

| Class | Description |
|-|-|
| [`EnvdImageSpecBuilder`](.././flytekitplugins.envd.image_builder#flytekitpluginsenvdimage_builderenvdimagespecbuilder) | This class is used to build a docker image using envd. |

### Methods

| Method | Description |
|-|-|
| [`create_envd_config()`](#create_envd_config) |  |
| [`envd_context_switch()`](#envd_context_switch) |  |
| [`execute_command()`](#execute_command) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `FLYTE_ENVD_CONTEXT` | `str` |  |
| `FLYTE_LOCAL_REGISTRY` | `str` |  |
| `REQUIREMENTS_FILE_NAME` | `str` |  |

## Methods

#### create_envd_config()

```python
def create_envd_config(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> str
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### envd_context_switch()

```python
def envd_context_switch(
    registry: str,
)
```
| Parameter | Type |
|-|-|
| `registry` | `str` |

#### execute_command()

```python
def execute_command(
    command: str,
)
```
| Parameter | Type |
|-|-|
| `command` | `str` |

## flytekitplugins.envd.image_builder.EnvdImageSpecBuilder

This class is used to build a docker image using envd.


### Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build the docker image and push it to the registry. |
| [`should_build()`](#should_build) | Whether or not the builder should build the ImageSpec. |


#### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
)
```
Build the docker image and push it to the registry.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> bool
```
Whether or not the builder should build the ImageSpec.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

