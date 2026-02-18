---
title: ImageBuild
version: 2.0.0b60
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ImageBuild

**Package:** `flyte`

Result of an image build operation.

Attributes:
    uri: The fully qualified image URI. None if the build was started asynchronously
        and hasn't completed yet.
    remote_run: The Run object that kicked off an image build job when using the remote
        builder. None when using the local builder.



```python
class ImageBuild(
    uri: str | None,
    remote_run: Optional['remote.Run'],
)
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `str \| None` | |
| `remote_run` | `Optional['remote.Run']` | |

