---
title: Hugging Face
version: 2.6.2
variants: +flyte +union
layout: py_api
---

# Hugging Face



## Directory

### Classes

| Class | Description |
|-|-|
| [`HFSource`](./hfsource) | Hugging Face dataset source for task parameter defaults. |

### Methods

| Method | Description |
|-|-|
| [`from_hf()`](#from_hf) | Return a DataFrame reference for use as a task parameter default. |


## Methods

#### from_hf()

```python
def from_hf(
    repo: str,
    name: str | None = None,
    split: str | None = None,
    revision: str | None = None,
    cache_root: str | None = None,
) -> DataFrame
```
Return a DataFrame reference for use as a task parameter default.

cache_root optionally points at a stable remote directory that can be reused
across runs. Without it, the dataset is materialized to a generated Flyte raw-data
path for this run. If name is omitted, the plugin resolves the dataset's
default converted-parquet config, or the only available config when there is
exactly one.


| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | |
| `name` | `str \| None` | |
| `split` | `str \| None` | |
| `revision` | `str \| None` | |
| `cache_root` | `str \| None` | |

