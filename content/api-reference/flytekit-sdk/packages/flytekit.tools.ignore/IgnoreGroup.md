---
title: IgnoreGroup
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# IgnoreGroup

**Package:** `flytekit.tools.ignore`

Groups multiple Ignores and checks a path against them. A file is ignored if any
Ignore considers it ignored.


```python
class IgnoreGroup(
    root: str,
    ignores: typing.List[typing.Type[flytekit.tools.ignore.Ignore]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `root` | `str` | |
| `ignores` | `typing.List[typing.Type[flytekit.tools.ignore.Ignore]]` | |

## Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`list_ignored()`](#list_ignored) |  |
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

### list_ignored()

```python
def list_ignored()
```
### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type | Description |
|-|-|-|
| `tarinfo` | `tarfile.TarInfo` | |

