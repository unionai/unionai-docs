---
title: FlyteIgnore
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteIgnore

**Package:** `flytekit.tools.ignore`

Uses a .flyteignore file to determine ignored files.


```python
class FlyteIgnore(
    root: pathlib.Path,
)
```
| Parameter | Type | Description |
|-|-|-|
| `root` | `pathlib.Path` | |

## Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |

### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type | Description |
|-|-|-|
| `tarinfo` | `tarfile.TarInfo` | |

