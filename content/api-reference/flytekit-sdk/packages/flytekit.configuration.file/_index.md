---
title: flytekit.configuration.file
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.configuration.file

## Directory

### Classes

| Class | Description |
|-|-|
| [`ConfigEntry`](../flytekit.configuration.file/configentry) | A top level Config entry holder, that holds multiple different representations of the config. |
| [`ConfigFile`](../flytekit.configuration.file/configfile) |  |
| [`LegacyConfigEntry`](../flytekit.configuration.file/legacyconfigentry) | Creates a record for the config entry. |
| [`YamlConfigEntry`](../flytekit.configuration.file/yamlconfigentry) | Creates a record for the config entry. |

### Methods

| Method | Description |
|-|-|
| [`bool_transformer()`](#bool_transformer) |  |
| [`comma_list_transformer()`](#comma_list_transformer) |  |
| [`int_transformer()`](#int_transformer) |  |
| [`read_file_if_exists()`](#read_file_if_exists) | Reads the contents of the file if passed a path. |
| [`set_if_exists()`](#set_if_exists) | Given a dict ``d`` sets the key ``k`` with value of config ``v``, if the config value ``v`` is set. |


### Variables

| Property | Type | Description |
|-|-|-|
| `FLYTECTL_CONFIG_ENV_VAR` | `str` |  |
| `FLYTECTL_CONFIG_ENV_VAR_OVERRIDE` | `str` |  |

## Methods

#### bool_transformer()

```python
def bool_transformer(
    config_val: typing.Any,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `config_val` | `typing.Any` | |

#### comma_list_transformer()

```python
def comma_list_transformer(
    config_val: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `config_val` | `typing.Any` | |

#### int_transformer()

```python
def int_transformer(
    config_val: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `config_val` | `typing.Any` | |

#### read_file_if_exists()

```python
def read_file_if_exists(
    filename: typing.Optional[str],
    encoding,
) -> typing.Optional[str]
```
Reads the contents of the file if passed a path. Otherwise, returns None.



| Parameter | Type | Description |
|-|-|-|
| `filename` | `typing.Optional[str]` | The file path to load |
| `encoding` |  | The encoding to use when reading the file. :return: The contents of the file as a string or None. |

#### set_if_exists()

```python
def set_if_exists(
    d: dict,
    k: str,
    v: typing.Any,
) -> dict
```
Given a dict ``d`` sets the key ``k`` with value of config ``v``, if the config value ``v`` is set
and return the updated dictionary.

> [!NOTE]
> The input dictionary ``d`` will be mutated.


| Parameter | Type | Description |
|-|-|-|
| `d` | `dict` | |
| `k` | `str` | |
| `v` | `typing.Any` | |

