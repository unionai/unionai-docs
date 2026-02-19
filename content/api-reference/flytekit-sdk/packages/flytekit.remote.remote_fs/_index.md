---
title: flytekit.remote.remote_fs
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.remote.remote_fs

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteFS`](../flytekit.remote.remote_fs/flytefs) | Want this to behave mostly just like the HTTP file system. |
| [`FlytePathResolver`](../flytekit.remote.remote_fs/flytepathresolver) |  |
| [`HttpFileWriter`](../flytekit.remote.remote_fs/httpfilewriter) |  |

### Methods

| Method | Description |
|-|-|
| [`get_flyte_fs()`](#get_flyte_fs) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `REMOTE_PLACEHOLDER` | `str` |  |

## Methods

#### get_flyte_fs()

```python
def get_flyte_fs(
    remote: FlyteRemote,
) -> typing.Type[FlyteFS]
```
| Parameter | Type | Description |
|-|-|-|
| `remote` | `FlyteRemote` | |

