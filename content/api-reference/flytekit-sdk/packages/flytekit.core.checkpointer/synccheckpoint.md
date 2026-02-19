---
title: SyncCheckpoint
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SyncCheckpoint

**Package:** `flytekit.core.checkpointer`

This class is NOT THREAD-SAFE!
Sync Checkpoint, will synchronously checkpoint a user given file or folder.
It will also synchronously download / restore previous checkpoints, when restore is invoked.

TODO: Implement an async checkpoint system



```python
class SyncCheckpoint(
    checkpoint_dest: str,
    checkpoint_src: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `checkpoint_dest` | `str` | Location where the new checkpoint should be copied to |
| `checkpoint_src` | `typing.Optional[str]` | If a previous checkpoint should exist, this path should be set to the folder that contains the checkpoint information |

## Methods

| Method | Description |
|-|-|
| [`prev_exists()`](#prev_exists) |  |
| [`read()`](#read) | This should only be used if there is a singular checkpoint file written. |
| [`restore()`](#restore) | Given a path, if a previous checkpoint exists, will be downloaded to this path. |
| [`save()`](#save) |  |
| [`write()`](#write) | This will overwrite the checkpoint. |


### prev_exists()

```python
def prev_exists()
```
### read()

```python
def read()
```
This should only be used if there is a singular checkpoint file written. If more than one checkpoint file is
found, this will raise a ValueError


### restore()

```python
def restore(
    path: typing.Union[pathlib._local.Path, str, NoneType],
) -> typing.Optional[pathlib._local.Path]
```
Given a path, if a previous checkpoint exists, will be downloaded to this path.
If download is successful the downloaded path is returned

> [!NOTE]
> Download will not be performed, if the checkpoint was previously restored. The method will return the
  previously downloaded path.


| Parameter | Type | Description |
|-|-|-|
| `path` | `typing.Union[pathlib._local.Path, str, NoneType]` | |

### save()

```python
def save(
    cp: typing.Union[pathlib._local.Path, str, _io.BufferedReader],
)
```
| Parameter | Type | Description |
|-|-|-|
| `cp` | `typing.Union[pathlib._local.Path, str, _io.BufferedReader]` | Checkpoint file (path, str path or a io.BufferedReader) |

### write()

```python
def write(
    b: bytes,
)
```
This will overwrite the checkpoint. It can be retrieved using read or restore


| Parameter | Type | Description |
|-|-|-|
| `b` | `bytes` | |

