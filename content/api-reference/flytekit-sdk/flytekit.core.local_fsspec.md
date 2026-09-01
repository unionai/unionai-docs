---
title: flytekit.core.local_fsspec
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.core.local_fsspec


## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteLocalFileSystem`](./flytekit.core.local_fsspec#flytekitcorelocal_fsspecflytelocalfilesystem) | This class doesn't do anything except override the separator so that it works on windows. |

## flytekit.core.local_fsspec.FlyteLocalFileSystem

This class doesn't do anything except override the separator so that it works on windows


### Parameters

```python
class FlyteLocalFileSystem(
    auto_mkdir = False,
    **kwargs,
)
```
Create and configure file-system instance

Instances may be cachable, so if similar enough arguments are seen
a new instance is not required. The token attribute exists to allow
implementations to cache instances if they wish.

A reasonable default should be provided if there are no arguments.

Subclasses should call this method.

Parameters
----------
use_listings_cache, listings_expiry_time, max_paths:
    passed to ``DirCache``, if the implementation supports
    directory listing caching. Pass use_listings_cache=False
    to disable such caching.
skip_instance_cache: bool
    If this is a cachable implementation, pass True here to force
    creating a new instance even if a matching instance exists, and prevent
    storing this instance.
asynchronous: bool
loop: asyncio-compatible IOLoop or None


| Parameter | Type | Description |
|-|-|-|
| `auto_mkdir` |  | |
| `**kwargs` |  | |

