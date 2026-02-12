---
title: ImageBuildEngine
version: 2.0.0b57
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
    wait: bool,
) -> 'ImageBuild'
```
Build the image. Images to be tagged with latest will always be built. Otherwise, this engine will check the
registry to see if the manifest exists.



| Parameter | Type | Description |
|-|-|-|
| `image` | `Image` | |
| `builder` | `ImageBuildEngine.ImageBuilderType \| None` | |
| `dry_run` | `bool` | Tell the builder to not actually build. Different builders will have different behaviors. |
| `force` | `bool` | Skip the existence check. Normally if the image already exists we won't build it. |
| `wait` | `bool` | Wait for the build to finish. If wait is False when using the remote image builder, the function will return the build image task URL. :return: An ImageBuild object with the image URI and remote run (if applicable). |

