---
title: union.ucimage
version: 0.1.171.dev4+g052020f1.d20250404
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union.ucimage

## Directory

### Classes

| Class | Description |
|-|-|
| [`UCImageSpecBuilder`](.././union.ucimage#unionucimageucimagespecbuilder) | ImageSpec builder for UnionAI. |

## union.ucimage.UCImageSpecBuilder

ImageSpec builder for UnionAI.


### Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) | Build image using UnionAI. |
| [`should_build()`](#should_build) | Check whether the image should be built. |


#### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
)
```
Build image using UnionAI.


| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
) -> bool
```
Check whether the image should be built.


| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

