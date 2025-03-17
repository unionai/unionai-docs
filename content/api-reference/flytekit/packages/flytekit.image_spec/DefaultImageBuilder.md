---
title: DefaultImageBuilder
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# DefaultImageBuilder

**Package:** `flytekit.image_spec`

Image builder using Docker and buildkit.


## Methods

### build_image()

```python
def build_image(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
Build the docker image and push it to the registry.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
### should_build()

```python
def should_build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
Whether or not the builder should build the ImageSpec.



| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
