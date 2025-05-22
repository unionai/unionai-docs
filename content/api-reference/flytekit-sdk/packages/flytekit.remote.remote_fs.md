---
title: flytekit.remote.remote_fs
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.remote.remote_fs

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlytePathResolver`](.././flytekit.remote.remote_fs#flytekitremoteremote_fsflytepathresolver) |  |

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
| Parameter | Type |
|-|-|
| `remote` | `FlyteRemote` |

## flytekit.remote.remote_fs.FlytePathResolver

### Methods

| Method | Description |
|-|-|
| [`add_mapping()`](#add_mapping) | Thread safe method to dd a mapping from a flyte uri to a remote path. |
| [`resolve_remote_path()`](#resolve_remote_path) | Given a flyte uri, return the remote path if it exists or was created in current session, otherwise return None. |


#### add_mapping()

```python
def add_mapping(
    flyte_uri: str,
    remote_path: str,
)
```
Thread safe method to dd a mapping from a flyte uri to a remote path


| Parameter | Type |
|-|-|
| `flyte_uri` | `str` |
| `remote_path` | `str` |

#### resolve_remote_path()

```python
def resolve_remote_path(
    flyte_uri: str,
) -> typing.Optional[str]
```
Given a flyte uri, return the remote path if it exists or was created in current session, otherwise return None


| Parameter | Type |
|-|-|
| `flyte_uri` | `str` |

