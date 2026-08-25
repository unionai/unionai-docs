---
title: HFSource
version: 2.6.2
variants: +flyte +union
layout: py_api
---

# HFSource

**Package:** `flyteplugins.huggingface.datasets`

Hugging Face dataset source for task parameter defaults.


## Parameters

```python
class HFSource(
    repo: str,
    name: str | None = None,
    split: str | None = None,
    revision: str | None = None,
    cache_root: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | |
| `name` | `str \| None` | |
| `split` | `str \| None` | |
| `revision` | `str \| None` | |
| `cache_root` | `str \| None` | |

## Methods

| Method | Description |
|-|-|
| [`from_hf_uri()`](#from_hf_uri) |  |
| [`to_hf_uri()`](#to_hf_uri) |  |


### from_hf_uri()

```python
def from_hf_uri(
    uri: str,
) -> 'HFSource'
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | |

### to_hf_uri()

```python
def to_hf_uri()
```
