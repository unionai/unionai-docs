---
title: DockerIgnore
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DockerIgnore

**Package:** `flytekit.tools.ignore`

Uses docker-py's PatternMatcher to check whether a path is ignored.


```python
class DockerIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type | Description |
|-|-|-|
| `root` | `pathlib._local.Path` | |

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

