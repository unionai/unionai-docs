---
title: UCImageSpecBuilder
version: 0.1.201
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# UCImageSpecBuilder

**Package:** `union.ucimage`

ImageSpec builder for UnionAI.


## Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build image using UnionAI. |
| [`should_build()`](#should_build) | Check whether the image should be built. |


### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
)
```
Build image using UnionAI.


| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | |

### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> bool
```
Check whether the image should be built.


| Parameter | Type | Description |
|-|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` | |

