---
title: RawDataPath
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RawDataPath

**Package:** `flyte.models`

A class representing the raw data path for a task. This is used to store the raw data for the task execution and
also get mutations on the path.


```python
class RawDataPath(
    path: str,
    path_rewrite: Optional[PathRewrite],
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `path_rewrite` | `Optional[PathRewrite]` | |

## Methods

| Method | Description |
|-|-|
| [`from_local_folder()`](#from_local_folder) | Create a new context attribute object, with local path given. |
| [`get_random_remote_path()`](#get_random_remote_path) | Returns a random path for uploading a file/directory to. |


### from_local_folder()

```python
def from_local_folder(
    local_folder: str | pathlib.Path | None,
) -> RawDataPath
```
Create a new context attribute object, with local path given. Will be created if it doesn't exist.
:return: Path to the temporary directory


| Parameter | Type | Description |
|-|-|-|
| `local_folder` | `str \| pathlib.Path \| None` | |

### get_random_remote_path()

```python
def get_random_remote_path(
    file_name: Optional[str],
) -> str
```
Returns a random path for uploading a file/directory to. This file/folder will not be created, it's just a path.



| Parameter | Type | Description |
|-|-|-|
| `file_name` | `Optional[str]` | If given, will be joined after a randomly generated portion. :return: |

