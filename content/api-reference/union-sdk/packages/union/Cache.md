---
title: Cache
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# Cache

**Package:** `union`

Cache configuration for a task.



```python
class Cache(
    version: typing.Optional[str],
    serialize: bool,
    ignored_inputs: typing.Union[typing.Tuple[str, ...], str],
    salt: str,
    policies: typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `version` | `typing.Optional[str]` | |
| `serialize` | `bool` | |
| `ignored_inputs` | `typing.Union[typing.Tuple[str, ...], str]` | |
| `salt` | `str` | |
| `policies` | `typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType]` | |

## Methods

| Method | Description |
|-|-|
| [`get_ignored_inputs()`](#get_ignored_inputs) |  |
| [`get_version()`](#get_version) |  |


### get_ignored_inputs()

```python
def get_ignored_inputs()
```
### get_version()

```python
def get_version(
    params: flytekit.core.cache.VersionParameters,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `params` | `flytekit.core.cache.VersionParameters` | |

