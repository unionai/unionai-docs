---
title: flytekit.tools.ignore
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.tools.ignore

## Directory

### Classes

| Class | Description |
|-|-|
| [`DockerIgnore`](.././flytekit.tools.ignore#flytekittoolsignoredockerignore) | Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`FlyteIgnore`](.././flytekit.tools.ignore#flytekittoolsignoreflyteignore) | Uses a. |
| [`GitIgnore`](.././flytekit.tools.ignore#flytekittoolsignoregitignore) | Uses git cli (if available) to list all ignored files and compare with those. |
| [`Ignore`](.././flytekit.tools.ignore#flytekittoolsignoreignore) | Base for Ignores, implements core logic. |
| [`IgnoreGroup`](.././flytekit.tools.ignore#flytekittoolsignoreignoregroup) | Groups multiple Ignores and checks a path against them. |
| [`StandardIgnore`](.././flytekit.tools.ignore#flytekittoolsignorestandardignore) | Retains the standard ignore functionality that previously existed. |

### Variables

| Property | Type | Description |
|-|-|-|
| `STANDARD_IGNORE_PATTERNS` | `list` |  |

## flytekit.tools.ignore.DockerIgnore

Uses docker-py's PatternMatcher to check whether a path is ignored.


```python
class DockerIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.ignore.FlyteIgnore

Uses a .flyteignore file to determine ignored files.


```python
class FlyteIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.ignore.GitIgnore

Uses git cli (if available) to list all ignored files and compare with those.


```python
class GitIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.ignore.Ignore

Base for Ignores, implements core logic. Children have to implement _is_ignored


```python
class Ignore(
    root: str,
)
```
| Parameter | Type |
|-|-|
| `root` | `str` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.ignore.IgnoreGroup

Groups multiple Ignores and checks a path against them. A file is ignored if any
Ignore considers it ignored.


```python
class IgnoreGroup(
    root: str,
    ignores: typing.List[typing.Type[flytekit.tools.ignore.Ignore]],
)
```
| Parameter | Type |
|-|-|
| `root` | `str` |
| `ignores` | `typing.List[typing.Type[flytekit.tools.ignore.Ignore]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`list_ignored()`](#list_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### list_ignored()

```python
def list_ignored()
```
#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.ignore.StandardIgnore

Retains the standard ignore functionality that previously existed. Could in theory
by fed with custom ignore patterns from cli.


```python
class StandardIgnore(
    root: pathlib._local.Path,
    patterns: typing.Optional[typing.List[str]],
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |
| `patterns` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

