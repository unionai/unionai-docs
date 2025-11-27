---
title: flyte.config
version: 2.0.0b34.dev10+g162555e05
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.config

## Directory

### Classes

| Class | Description |
|-|-|
| [`Config`](../flyte.config/config) | This the parent configuration object and holds all the underlying configuration object types. |

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
        c. &lt;git_root&gt;/.flyte/config.yaml if it exists
        d. `UCTL_CONFIG` environment variable
        e. `FLYTECTL_CONFIG` environment variable
        f. ~/.union/config.yaml if it exists
        g. ~/.flyte/config.yaml if it exists
3. If any value is not found in the config file, the default value is used.
4. For any value there are environment variables that match the config variable names, those will override



| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, pathlib.Path, ConfigFile, None]` | file path to read the config from, if not specified default locations are searched :return: Config |

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


| Parameter | Type | Description |
|-|-|-|
| `d` | `dict` | |
| `k` | `str` | |
| `val` | `typing.Any` | |

