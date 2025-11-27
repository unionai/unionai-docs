---
title: StandardIgnore
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# StandardIgnore

**Package:** `flytekit.tools.ignore`

Retains the standard ignore functionality that previously existed. Could in theory
by fed with custom ignore patterns from cli.


```python
class StandardIgnore(
    root: pathlib.Path,
    patterns: typing.Optional[typing.List[str]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `root` | `pathlib.Path` | |
| `patterns` | `typing.Optional[typing.List[str]]` | |

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

