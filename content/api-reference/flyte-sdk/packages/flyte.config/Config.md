---
title: Config
version: 2.0.0b40
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Config

**Package:** `flyte.config`

This the parent configuration object and holds all the underlying configuration object types. An instance of
this object holds all the config necessary to

1. Interactive session with Flyte backend
2. Some parts are required for Serialization, for example Platform Config is not required
3. Runtime of a task


```python
class Config(
    platform: PlatformConfig,
    task: TaskConfig,
    image: ImageConfig,
    source: pathlib.Path | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `platform` | `PlatformConfig` | |
| `task` | `TaskConfig` | |
| `image` | `ImageConfig` | |
| `source` | `pathlib.Path \| None` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically constructs the Config Object. |
| [`with_params()`](#with_params) |  |


### auto()

```python
def auto(
    config_file: typing.Union[str, pathlib.Path, ConfigFile, None],
) -> 'Config'
```
Automatically constructs the Config Object. The order of precedence is as follows
  1. first try to find any env vars that match the config vars specified in the FLYTE_CONFIG format.
  2. If not found in environment then values ar read from the config file
  3. If not found in the file, then the default values are used.



| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, pathlib.Path, ConfigFile, None]` | file path to read the config from, if not specified default locations are searched :return: Config |

### with_params()

```python
def with_params(
    platform: PlatformConfig | None,
    task: TaskConfig | None,
    image: ImageConfig | None,
) -> 'Config'
```
| Parameter | Type | Description |
|-|-|-|
| `platform` | `PlatformConfig \| None` | |
| `task` | `TaskConfig \| None` | |
| `image` | `ImageConfig \| None` | |

