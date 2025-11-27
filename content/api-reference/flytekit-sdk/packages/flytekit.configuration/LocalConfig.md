---
title: LocalConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LocalConfig

**Package:** `flytekit.configuration`

Any configuration specific to local runs.


```python
class LocalConfig(
    cache_enabled: bool,
    cache_overwrite: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cache_enabled` | `bool` | |
| `cache_overwrite` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> LocalConfig
```
| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` | |

