---
title: flytekit.configuration.default_images
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.configuration.default_images

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultImages`](.././flytekit.configuration.default_images#flytekitconfigurationdefault_imagesdefaultimages) | We may want to load the default images from remote - maybe s3 location etc?. |

### Variables

| Property | Type | Description |
|-|-|-|
| `FLYTE_INTERNAL_IMAGE_ENV_VAR` | `str` |  |

## flytekit.configuration.default_images.DefaultImages

We may want to load the default images from remote - maybe s3 location etc?


### Methods

| Method | Description |
|-|-|
| [`default_image()`](#default_image) |  |
| [`find_image_for()`](#find_image_for) |  |
| [`get_version_suffix()`](#get_version_suffix) |  |


#### default_image()

```python
def default_image()
```
#### find_image_for()

```python
def find_image_for(
    python_version: typing.Optional[flytekit.configuration.default_images.PythonVersion],
    flytekit_version: typing.Optional[str],
) -> str
```
| Parameter | Type |
|-|-|
| `python_version` | `typing.Optional[flytekit.configuration.default_images.PythonVersion]` |
| `flytekit_version` | `typing.Optional[str]` |

#### get_version_suffix()

```python
def get_version_suffix()
```
