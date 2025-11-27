---
title: SecretsConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SecretsConfig

**Package:** `flytekit.configuration`

Configuration for secrets.



```python
class SecretsConfig(
    env_prefix: str,
    default_dir: str,
    file_prefix: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `env_prefix` | `str` | |
| `default_dir` | `str` | |
| `file_prefix` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from environment variable or from config file. |


### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> SecretsConfig
```
Reads from environment variable or from config file


| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` | :return: |

