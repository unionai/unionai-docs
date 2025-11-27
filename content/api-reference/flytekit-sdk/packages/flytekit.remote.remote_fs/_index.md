---
title: flytekit.remote.remote_fs
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.remote.remote_fs

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlytePathResolver`](../flytekit.remote.remote_fs/flytepathresolver) |  |

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

