---
title: flytekit.image_spec.image_spec
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.image_spec.image_spec

## Directory

### Classes

| Class | Description |
|-|-|
| [`ImageBuildEngine`](../flytekit.image_spec.image_spec/imagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`ImageSpec`](../flytekit.image_spec.image_spec/imagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`ImageSpecBuilder`](../flytekit.image_spec.image_spec/imagespecbuilder) |  |

### Methods

| Method | Description |
|-|-|
| [`validate_container_registry_name()`](#validate_container_registry_name) | Validate Docker container registry name. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DOCKER_HUB` | `str` |  |
| `FLYTE_FORCE_PUSH_IMAGE_SPEC` | `str` |  |
| `FLYTE_IMG_FAST_FAIL` | `str` |  |

## Methods

#### validate_container_registry_name()

```python
def validate_container_registry_name(
    name: str,
) -> bool
```
Validate Docker container registry name.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

