---
title: NoOpBuilder
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NoOpBuilder

**Package:** `flytekit.image_spec.noop_builder`

Noop image builder.


## Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build the docker image and push it to the registry. |
| [`should_build()`](#should_build) | The build_image function of NoOpBuilder does not actually build a Docker image. |


### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> str
```
Build the docker image and push it to the registry.



| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | image spec of the task. |

### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> bool
```
The build_image function of NoOpBuilder does not actually build a Docker image.
Since no Docker build process occurs, we do not need to check for Docker daemon
or existing images. Therefore, should_build should always return True.



| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | Image specification |

