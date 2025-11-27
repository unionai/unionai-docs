---
title: GitIgnore
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# GitIgnore

**Package:** `flytekit.tools.ignore`

Uses git cli (if available) to list all ignored files and compare with those.


```python
class GitIgnore(
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

