---
title: Checkpoint
version: 2.1.9
variants: +flyte +union
layout: py_api
---

# Checkpoint

**Package:** `flyte`

Checkpoint helper using `flyte.io.File` for all checkpoint blob I/O (load/save, async and sync).
Remote paths are a **single object**.

In async tasks use `flyte.Checkpoint.load` and `flyte.Checkpoint.save`. In ordinary `def` tasks use
`flyte.Checkpoint.load_sync` and `flyte.Checkpoint.save_sync`.

Saving a **directory** uploads a gzip tar of its top-level entries; saving a **file** or **bytes** uploads
that payload directly. After `flyte.Checkpoint.load` / `flyte.Checkpoint.load_sync`, a non-tar remote object
appears as `path / "payload"` and those methods return that path. Tarball checkpoints unpack under
`flyte.Checkpoint.path`;
they return `flyte.Checkpoint.path` so callers can scan the restored tree (e.g. `pathlib.Path.rglob`).


## Parameters

```python
class Checkpoint(
    checkpoint_dest: str,
    checkpoint_src: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `checkpoint_dest` | `str` | |
| `checkpoint_src` | `str \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `path` | `pathlib.Path` | Local directory for reading checkpoint files. |
| `remote_destination` | `str` | Object-store prefix where `flyte.Checkpoint.save` writes. |
| `remote_source` | `Optional[str]` | Object-store prefix for the previous attempt's checkpoint, if any. |

## Methods

| Method | Description |
|-|-|
| [`load()`](#load) | Load checkpoint data from the remote source (async). |
| [`load_sync()`](#load_sync) | Load checkpoint data from the remote source (sync task code). |
| [`prev_exists()`](#prev_exists) | Whether the runtime provided a previous-checkpoint prefix (retry / resume). |
| [`save()`](#save) | Save checkpoint data to the remote destination (async). |
| [`save_sync()`](#save_sync) | Save checkpoint data to the remote destination (sync task code). |


### load()

```python
def load()
```
Load checkpoint data from the remote source (async).


### load_sync()

```python
def load_sync()
```
Load checkpoint data from the remote source (sync task code).


### prev_exists()

```python
def prev_exists()
```
Whether the runtime provided a previous-checkpoint prefix (retry / resume).


### save()

```python
def save(
    data: pathlib.Path | str | bytes,
)
```
Save checkpoint data to the remote destination (async).


| Parameter | Type | Description |
|-|-|-|
| `data` | `pathlib.Path \| str \| bytes` | |

### save_sync()

```python
def save_sync(
    data: pathlib.Path | str | bytes,
)
```
Save checkpoint data to the remote destination (sync task code).


| Parameter | Type | Description |
|-|-|-|
| `data` | `pathlib.Path \| str \| bytes` | |

