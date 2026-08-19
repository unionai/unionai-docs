---
title: flytekitplugins.async_fsspec.s3fs.s3fs
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekitplugins.async_fsspec.s3fs.s3fs

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncS3FileSystem`](.././flytekitplugins.async_fsspec.s3fs.s3fs#flytekitpluginsasync_fsspecs3fss3fsasyncs3filesystem) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_CONCURRENT_DOWNLOAD` | `int` |  |
| `DEFAULT_CONCURRENT_UPLOAD` | `int` |  |
| `DEFAULT_DOWNLOAD_BODY_READ_SIZE` | `int` |  |
| `DEFAULT_DOWNLOAD_CHUNK_SIZE` | `int` |  |
| `DEFAULT_UPLOAD_CHUNK_SIZE` | `int` |  |
| `S3_RETRYABLE_ERRORS` | `tuple` |  |
| `SINGLE_OBJECT_UPLOAD_LIMIT` | `int` |  |

## flytekitplugins.async_fsspec.s3fs.s3fs.AsyncS3FileSystem

### Parameters

```python
class AsyncS3FileSystem(
    **s3kwargs,
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
| `**s3kwargs` |  | |

