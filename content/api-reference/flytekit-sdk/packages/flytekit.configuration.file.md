---
title: flytekit.configuration.file
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.configuration.file

## Directory

### Classes

| Class | Description |
|-|-|
| [`ConfigEntry`](.././flytekit.configuration.file#flytekitconfigurationfileconfigentry) | A top level Config entry holder, that holds multiple different representations of the config. |
| [`ConfigFile`](.././flytekit.configuration.file#flytekitconfigurationfileconfigfile) |  |
| [`LegacyConfigEntry`](.././flytekit.configuration.file#flytekitconfigurationfilelegacyconfigentry) | Creates a record for the config entry. |
| [`YamlConfigEntry`](.././flytekit.configuration.file#flytekitconfigurationfileyamlconfigentry) | Creates a record for the config entry. |

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
| Parameter | Type |
|-|-|
| `config_val` | `typing.Any` |

#### comma_list_transformer()

```python
def comma_list_transformer(
    config_val: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `config_val` | `typing.Any` |

#### int_transformer()

```python
def int_transformer(
    config_val: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `config_val` | `typing.Any` |

#### read_file_if_exists()

```python
def read_file_if_exists(
    filename: typing.Optional[str],
    encoding,
) -> n: The contents of the file as a string or None.
```
Reads the contents of the file if passed a path. Otherwise, returns None.



| Parameter | Type |
|-|-|
| `filename` | `typing.Optional[str]` |
| `encoding` |  |

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


| Parameter | Type |
|-|-|
| `d` | `dict` |
| `k` | `str` |
| `v` | `typing.Any` |

## flytekit.configuration.file.ConfigEntry

A top level Config entry holder, that holds multiple different representations of the config.
Legacy means the INI style config files. YAML support is for the flytectl config file, which is there by default
when flytectl starts a sandbox


```python
class ConfigEntry(
    legacy: LegacyConfigEntry,
    yaml_entry: typing.Optional[YamlConfigEntry],
    transform: typing.Optional[typing.Callable[[str], typing.Any]],
)
```
| Parameter | Type |
|-|-|
| `legacy` | `LegacyConfigEntry` |
| `yaml_entry` | `typing.Optional[YamlConfigEntry]` |
| `transform` | `typing.Optional[typing.Callable[[str], typing.Any]]` |

### Methods

| Method | Description |
|-|-|
| [`read()`](#read) | Reads the config Entry from the various sources in the following order,. |


#### read()

```python
def read(
    cfg: typing.Optional[ConfigFile],
) -> n:
```
Reads the config Entry from the various sources in the following order,
#. First try to read from the relevant environment variable,
#. If missing, then try to read from the legacy config file, if one was parsed.
#. If missing, then try to read from the yaml file.

The constructor for ConfigFile currently does not allow specification of both the ini and yaml style formats.



| Parameter | Type |
|-|-|
| `cfg` | `typing.Optional[ConfigFile]` |

## flytekit.configuration.file.ConfigFile

```python
class ConfigFile(
    location: str,
)
```
Load the config from this location


| Parameter | Type |
|-|-|
| `location` | `str` |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) |  |


#### get()

```python
def get(
    c: typing.Union[LegacyConfigEntry, YamlConfigEntry],
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `c` | `typing.Union[LegacyConfigEntry, YamlConfigEntry]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `legacy_config` |  |  |
| `yaml_config` |  |  |

## flytekit.configuration.file.LegacyConfigEntry

Creates a record for the config entry. contains


```python
class LegacyConfigEntry(
    section: str,
    option: str,
    type_: typing.Type,
)
```
| Parameter | Type |
|-|-|
| `section` | `str` |
| `option` | `str` |
| `type_` | `typing.Type` |

### Methods

| Method | Description |
|-|-|
| [`get_env_name()`](#get_env_name) |  |
| [`read_from_env()`](#read_from_env) | Reads the config entry from environment variable, the structure of the env var is current. |
| [`read_from_file()`](#read_from_file) |  |


#### get_env_name()

```python
def get_env_name()
```
#### read_from_env()

```python
def read_from_env(
    transform: typing.Optional[typing.Callable],
) -> n:
```
Reads the config entry from environment variable, the structure of the env var is current
``FLYTE_{SECTION}_{OPTION}`` all upper cased. We will change this in the future.
:return:


| Parameter | Type |
|-|-|
| `transform` | `typing.Optional[typing.Callable]` |

#### read_from_file()

```python
def read_from_file(
    cfg: ConfigFile,
    transform: typing.Optional[typing.Callable],
) -> typing.Optional[typing.Any]
```
| Parameter | Type |
|-|-|
| `cfg` | `ConfigFile` |
| `transform` | `typing.Optional[typing.Callable]` |

## flytekit.configuration.file.YamlConfigEntry

Creates a record for the config entry.


```python
class YamlConfigEntry(
    switch: str,
    config_value_type: typing.Type,
)
```
| Parameter | Type |
|-|-|
| `switch` | `str` |
| `config_value_type` | `typing.Type` |

### Methods

| Method | Description |
|-|-|
| [`read_from_file()`](#read_from_file) |  |


#### read_from_file()

```python
def read_from_file(
    cfg: ConfigFile,
    transform: typing.Optional[typing.Callable],
) -> typing.Optional[typing.Any]
```
| Parameter | Type |
|-|-|
| `cfg` | `ConfigFile` |
| `transform` | `typing.Optional[typing.Callable]` |

