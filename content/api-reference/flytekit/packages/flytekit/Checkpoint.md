---
title: Checkpoint
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# Checkpoint

**Package:** `flytekit`

Base class for Checkpoint system. Checkpoint system allows reading and writing custom checkpoints from user
scripts


## Methods

### prev_exists()

```python
def prev_exists()
```
No parameters
### read()

```python
def read()
```
This should only be used if there is a singular checkpoint file written. If more than one checkpoint file is
found, this will raise a ValueError


No parameters
### restore()

```python
def restore(
    path: typing.Union[pathlib.Path, str],
):
```
Given a path, if a previous checkpoint exists, will be downloaded to this path.
If download is successful the downloaded path is returned

.. note:

Download will not be performed, if the checkpoint was previously restored. The method will return the
previously downloaded path.


| Parameter | Type |
|-|-|
| `path` | `typing.Union[pathlib.Path, str]` |
### save()

```python
def save(
    cp: typing.Union[pathlib.Path, str, _io.BufferedReader],
):
```
| Parameter | Type |
|-|-|
| `cp` | `typing.Union[pathlib.Path, str, _io.BufferedReader]` |
### write()

```python
def write(
    b: bytes,
):
```
This will overwrite the checkpoint. It can be retrieved using read or restore


| Parameter | Type |
|-|-|
| `b` | `bytes` |
