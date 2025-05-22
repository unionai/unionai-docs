---
title: flytekit.core.checkpointer
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.checkpointer

## Directory

### Classes

| Class | Description |
|-|-|
| [`Checkpoint`](.././flytekit.core.checkpointer#flytekitcorecheckpointercheckpoint) | Base class for Checkpoint system. |
| [`SyncCheckpoint`](.././flytekit.core.checkpointer#flytekitcorecheckpointersynccheckpoint) | This class is NOT THREAD-SAFE!. |

## flytekit.core.checkpointer.Checkpoint

Base class for Checkpoint system. Checkpoint system allows reading and writing custom checkpoints from user
scripts


### Methods

| Method | Description |
|-|-|
| [`prev_exists()`](#prev_exists) |  |
| [`read()`](#read) | This should only be used if there is a singular checkpoint file written. |
| [`restore()`](#restore) | Given a path, if a previous checkpoint exists, will be downloaded to this path. |
| [`save()`](#save) |  |
| [`write()`](#write) | This will overwrite the checkpoint. |


#### prev_exists()

```python
def prev_exists()
```
#### read()

```python
def read()
```
This should only be used if there is a singular checkpoint file written. If more than one checkpoint file is
found, this will raise a ValueError


#### restore()

```python
def restore(
    path: typing.Union[pathlib._local.Path, str],
) -> typing.Optional[pathlib._local.Path]
```
Given a path, if a previous checkpoint exists, will be downloaded to this path.
If download is successful the downloaded path is returned

> [!NOTE]
> Download will not be performed, if the checkpoint was previously restored. The method will return the
  previously downloaded path.


| Parameter | Type |
|-|-|
| `path` | `typing.Union[pathlib._local.Path, str]` |

#### save()

```python
def save(
    cp: typing.Union[pathlib._local.Path, str, _io.BufferedReader],
)
```
| Parameter | Type |
|-|-|
| `cp` | `typing.Union[pathlib._local.Path, str, _io.BufferedReader]` |

#### write()

```python
def write(
    b: bytes,
)
```
This will overwrite the checkpoint. It can be retrieved using read or restore


| Parameter | Type |
|-|-|
| `b` | `bytes` |

## flytekit.core.checkpointer.SyncCheckpoint

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
| Parameter | Type |
|-|-|
| `checkpoint_dest` | `str` |
| `checkpoint_src` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`prev_exists()`](#prev_exists) |  |
| [`read()`](#read) | This should only be used if there is a singular checkpoint file written. |
| [`restore()`](#restore) | Given a path, if a previous checkpoint exists, will be downloaded to this path. |
| [`save()`](#save) |  |
| [`write()`](#write) | This will overwrite the checkpoint. |


#### prev_exists()

```python
def prev_exists()
```
#### read()

```python
def read()
```
This should only be used if there is a singular checkpoint file written. If more than one checkpoint file is
found, this will raise a ValueError


#### restore()

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


| Parameter | Type |
|-|-|
| `path` | `typing.Union[pathlib._local.Path, str, NoneType]` |

#### save()

```python
def save(
    cp: typing.Union[pathlib._local.Path, str, _io.BufferedReader],
)
```
| Parameter | Type |
|-|-|
| `cp` | `typing.Union[pathlib._local.Path, str, _io.BufferedReader]` |

#### write()

```python
def write(
    b: bytes,
)
```
This will overwrite the checkpoint. It can be retrieved using read or restore


| Parameter | Type |
|-|-|
| `b` | `bytes` |

