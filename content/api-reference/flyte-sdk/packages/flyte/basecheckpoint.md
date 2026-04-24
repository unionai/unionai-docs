---
title: BaseCheckpoint
version: 2.1.10.dev6+ga8f3f9bfa
variants: +flyte +union
layout: py_api
---

# BaseCheckpoint

**Package:** `flyte`

Base type for task checkpoint helpers. Subclasses load prior checkpoint data from
`prev_checkpoint` into a local workspace and upload new state to `checkpoint_path`.


## Properties

| Property | Type | Description |
|-|-|-|
| `path` | `pathlib.Path` | Local directory for reading and writing checkpoint files (your format). |

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

