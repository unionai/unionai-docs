---
title: ImageBuildEngine
description: "ImageBuildEngine contains a list of builders that can be used to build an ImageSpec."
icon: braces
version: 2.13.4
variants: +flyte +union
layout: py_api
---

# ImageBuildEngine

**Package:** `flyte.extend`

ImageBuildEngine contains a list of builders that can be used to build an ImageSpec.


## Methods

| Method | Description |
|-|-|
| [`build()`](#build) | Build the image. |
| [`image_exists()`](#image_exists) | Whether the image exists, by `builder`'s checkers (the configured builder when None), for `queue` (else the queue the current run is sent to, `flyte._upload_queue`). |


### build()

```python
def build(
    image: Image,
    builder: ImageBuildEngine.ImageBuilderType | str | ImageBuilder | None = None,
    dry_run: bool = False,
    force: bool = False,
    wait: bool = True,
    queue: str | None = None,
) -> 'ImageBuild'
```
Build the image. Images to be tagged with latest will always be built. Otherwise, this engine will check the
registry to see if the manifest exists.



| Parameter | Type | Description |
|-|-|-|
| `image` | `Image` | |
| `builder` | `ImageBuildEngine.ImageBuilderType \| str \| ImageBuilder \| None` | |
| `dry_run` | `bool` | Tell the builder to not actually build. Different builders will have different behaviors. |
| `force` | `bool` | Skip the existence check and force a rebuild. When using the remote builder, this also sets overwrite_cache=True on the build run. |
| `wait` | `bool` | Wait for the build to finish. If wait is False when using the remote image builder, the function will return the build image task URL. |
| `queue` | `str \| None` | Queue of the cluster pool a remote build is for (the run's queue when None): the lookup, the uploads, the build run and the cache entries all use it. Ignored by the local builders. |

**Returns:** An ImageBuild object with the image URI and remote run (if applicable).

### image_exists()

```python
def image_exists(
    image: Image,
    queue: str | None = None,
    builder: ImageBuildEngine.ImageBuilderType | str | ImageBuilder | None = None,
) -> Optional[str]
```
Whether the image exists, by `builder`'s checkers (the configured builder when None), for
`queue` (else the queue the current run is sent to, `flyte._upload_queue`). A remote lookup asks
a cluster of that queue's pool, and its result is cached per queue; for the local builders the
queue does not matter.


| Parameter | Type | Description |
|-|-|-|
| `image` | `Image` | |
| `queue` | `str \| None` | |
| `builder` | `ImageBuildEngine.ImageBuilderType \| str \| ImageBuilder \| None` | |

