---
title: DefaultImageBuilder
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DefaultImageBuilder

**Package:** `flytekit.image_spec.default_builder`

Image builder using Docker and buildkit.


## Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build the docker image and push it to the registry. |
| [`should_build()`](#should_build) | Whether or not the builder should build the ImageSpec. |


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
Whether or not the builder should build the ImageSpec.



| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | image spec of the task. |

