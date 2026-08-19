---
title: union.filesystems
version: 0.1.203
variants: -flyte +union
layout: py_api
---

# union.filesystems

Module for fsspec implementations.
## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncUnionFS`](.././union.filesystems#unionfilesystemsasyncunionfs) |  |
| [`AsyncUnionMetaFS`](.././union.filesystems#unionfilesystemsasyncunionmetafs) |  |

## union.filesystems.AsyncUnionFS

### Parameters

```python
class AsyncUnionFS(
    logger: logging.Logger = <Logger union.filesystems._unionfs (WARNING)>,
    loop: typing.Optional[asyncio.events.AbstractEventLoop] = None,
    *args,
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
| `logger` | `logging.Logger` | |
| `loop` | `typing.Optional[asyncio.events.AbstractEventLoop]` | |
| `*args` |  | |
| `**kwargs` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `max_attempts` | `int` |  |
| `max_concurrent_tasks` | `int` |  |
| `retries` | `int` |  |

### Methods

| Method | Description |
|-|-|
| [`open_async()`](#open_async) |  |


#### open_async()

```python
def open_async(
    path: str,
    mode = 'rb',
    **kwargs,
) -> fsspec.asyn.AbstractAsyncStreamedFile
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `mode` |  | |
| `**kwargs` |  | |

## union.filesystems.AsyncUnionMetaFS

### Parameters

```python
class AsyncUnionMetaFS(
    logger: logging.Logger = <Logger union.filesystems._unionmetafs (WARNING)>,
    loop: typing.Optional[asyncio.events.AbstractEventLoop] = None,
    *args,
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
| `logger` | `logging.Logger` | |
| `loop` | `typing.Optional[asyncio.events.AbstractEventLoop]` | |
| `*args` |  | |
| `**kwargs` |  | |

### Methods

| Method | Description |
|-|-|
| [`open_async()`](#open_async) |  |


#### open_async()

```python
def open_async(
    path: str,
    mode = 'rb',
    **kwargs,
) -> fsspec.asyn.AbstractAsyncStreamedFile
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `mode` |  | |
| `**kwargs` |  | |

