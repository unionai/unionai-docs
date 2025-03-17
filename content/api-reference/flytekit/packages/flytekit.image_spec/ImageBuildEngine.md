---
title: ImageBuildEngine
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# ImageBuildEngine

**Package:** `flytekit.image_spec`

ImageBuildEngine contains a list of builders that can be used to build an ImageSpec.


## Methods

### build()

```python
def build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |
### get_registry()

```python
def get_registry()
```
No parameters
### register()

```python
def register(
    builder_type: str,
    image_spec_builder: flytekit.image_spec.image_spec.ImageSpecBuilder,
    priority: int,
):
```
| Parameter | Type |
|-|-|
| `builder_type` | `str` |
| `image_spec_builder` | `flytekit.image_spec.image_spec.ImageSpecBuilder` |
| `priority` | `int` |
