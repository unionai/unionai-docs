---
title: S3Config
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# S3Config

**Package:** `flytekit.configuration`

S3 specific configuration



```python
class S3Config(
    enable_debug: bool,
    endpoint: typing.Optional[str],
    retries: int,
    backoff: datetime.timedelta,
    access_key_id: typing.Optional[str],
    secret_access_key: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `enable_debug` | `bool` | |
| `endpoint` | `typing.Optional[str]` | |
| `retries` | `int` | |
| `backoff` | `datetime.timedelta` | |
| `access_key_id` | `typing.Optional[str]` | |
| `secret_access_key` | `typing.Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically configure. |


### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> S3Config
```
Automatically configure


| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` | :return: Config |

