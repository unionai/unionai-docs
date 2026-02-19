---
title: ImageBuildEngine
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ImageBuildEngine

**Package:** `flytekit.image_spec.image_spec`

ImageBuildEngine contains a list of builders that can be used to build an ImageSpec.



## Methods

| Method | Description |
|-|-|
| [`build()`](#build) |  |
| [`get_registry()`](#get_registry) |  |
| [`register()`](#register) |  |


### build()

```python
def build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
)
```
| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | |

### get_registry()

```python
def get_registry()
```
### register()

```python
def register(
    builder_type: str,
    image_spec_builder: flytekit.image_spec.image_spec.ImageSpecBuilder,
    priority: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `builder_type` | `str` | |
| `image_spec_builder` | `flytekit.image_spec.image_spec.ImageSpecBuilder` | |
| `priority` | `int` | |

