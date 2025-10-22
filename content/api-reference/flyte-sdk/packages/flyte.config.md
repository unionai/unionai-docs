---
title: flyte.config
version: 2.0.0b25
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.config

## Directory

### Classes

| Class | Description |
|-|-|
| [`Config`](.././flyte.config#flyteconfigconfig) | This the parent configuration object and holds all the underlying configuration object types. |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically constructs the Config Object. |
| [`set_if_exists()`](#set_if_exists) | Given a dict ``d`` sets the key ``k`` with value of config ``v``, if the config value ``v`` is set. |


## Methods

#### auto()

```python
def auto(
    config_file: typing.Union[str, pathlib.Path, ConfigFile, None],
) -> Config
```
Automatically constructs the Config Object. The order of precedence is as follows
  1. If specified, read the config from the provided file path.
  2. If not specified, the config file is searched in the default locations.
        a. ./config.yaml if it exists  (current working directory)
        b. ./.flyte/config.yaml if it exists (current working directory)
        c. <git_root>/.flyte/config.yaml if it exists
        d. `UCTL_CONFIG` environment variable
        e. `FLYTECTL_CONFIG` environment variable
        f. ~/.union/config.yaml if it exists
        g. ~/.flyte/config.yaml if it exists
3. If any value is not found in the config file, the default value is used.
4. For any value there are environment variables that match the config variable names, those will override



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, pathlib.Path, ConfigFile, None]` |

#### set_if_exists()

```python
def set_if_exists(
    d: dict,
    k: str,
    val: typing.Any,
) -> dict
```
Given a dict ``d`` sets the key ``k`` with value of config ``v``, if the config value ``v`` is set
and return the updated dictionary.


| Parameter | Type |
|-|-|
| `d` | `dict` |
| `k` | `str` |
| `val` | `typing.Any` |

## flyte.config.Config

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
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `task` | `TaskConfig` |
| `image` | `ImageConfig` |
| `source` | `pathlib.Path \| None` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically constructs the Config Object. |
| [`with_params()`](#with_params) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, pathlib.Path, ConfigFile, None],
) -> 'Config'
```
Automatically constructs the Config Object. The order of precedence is as follows
  1. first try to find any env vars that match the config vars specified in the FLYTE_CONFIG format.
  2. If not found in environment then values ar read from the config file
  3. If not found in the file, then the default values are used.



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, pathlib.Path, ConfigFile, None]` |

#### with_params()

```python
def with_params(
    platform: PlatformConfig | None,
    task: TaskConfig | None,
    image: ImageConfig | None,
) -> 'Config'
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig \| None` |
| `task` | `TaskConfig \| None` |
| `image` | `ImageConfig \| None` |

