---
title: Ignore
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Ignore

**Package:** `flytekit.tools.ignore`

Base for Ignores, implements core logic. Children have to implement _is_ignored


```python
class Ignore(
    root: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `root` | `str` | |

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

