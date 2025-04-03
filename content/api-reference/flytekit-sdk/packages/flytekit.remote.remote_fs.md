---
title: flytekit.remote.remote_fs
version: 0.1.dev2184+g1e0cbe7.d20250401
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.remote.remote_fs

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteFS`](.././flytekit.remote.remote_fs#flytekitremoteremote_fsflytefs) | Want this to behave mostly just like the HTTP file system. |
| [`FlytePathResolver`](.././flytekit.remote.remote_fs#flytekitremoteremote_fsflytepathresolver) |  |
| [`HttpFileWriter`](.././flytekit.remote.remote_fs#flytekitremoteremote_fshttpfilewriter) | Convenient class to derive from to provide buffering. |

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

