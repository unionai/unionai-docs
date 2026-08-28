---
title: ImageBuild
version: 2.6.10
variants: +flyte +union
layout: py_api
---

# ImageBuild

**Package:** `flyte`

Result of an image build operation.



## Parameters

```python
class ImageBuild(
    uri: str | None,
    remote_run: Optional['remote.Run'],
    build_run: Optional['RunIdentifierData'] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `str \| None` | The fully qualified image URI. None if the build was started asynchronously and hasn't completed yet. |
| `remote_run` | `Optional['remote.Run']` | Live handle to the build run this process launched with the remote builder — wait on it or read its URL. None when no build was launched (local builder, or the image already existed). For the run's identifier, use build_run. |
| `build_run` | `Optional['RunIdentifierData']` | Identifier of the remote build run that built (or, with wait=False, is building) the image — the canonical answer to "which run built this image". Set both when this process launches a remote build and when the registry existence check learns it from the image service on a cache hit. None for locally built images and for backends that don't report it. |

