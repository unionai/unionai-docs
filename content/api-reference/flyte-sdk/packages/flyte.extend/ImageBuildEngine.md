---
title: ImageBuildEngine
version: 2.0.0b47
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ImageBuildEngine

**Package:** `flyte.extend`

ImageBuildEngine contains a list of builders that can be used to build an ImageSpec.


## Methods

| Method | Description |
|-|-|
| [`build()`](#build) | Build the image. |


### build()

```python
def build(
    image: Image,
    builder: ImageBuildEngine.ImageBuilderType | None,
    dry_run: bool,
    force: bool,
) -> str
```
Build the image. Images to be tagged with latest will always be built. Otherwise, this engine will check the
registry to see if the manifest exists.



| Parameter | Type | Description |
|-|-|-|
| `image` | `Image` | |
| `builder` | `ImageBuildEngine.ImageBuilderType \| None` | |
| `dry_run` | `bool` | Tell the builder to not actually build. Different builders will have different behaviors. |
| `force` | `bool` | Skip the existence check. Normally if the image already exists we won't build it. :return: |

