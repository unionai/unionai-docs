---
title: flytekit.configuration.internal
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.configuration.internal

## Directory

### Classes

| Class | Description |
|-|-|
| [`AWS`](.././flytekit.configuration.internal#flytekitconfigurationinternalaws) |  |
| [`AZURE`](.././flytekit.configuration.internal#flytekitconfigurationinternalazure) |  |
| [`ConfigEntry`](.././flytekit.configuration.internal#flytekitconfigurationinternalconfigentry) | A top level Config entry holder, that holds multiple different representations of the config. |
| [`ConfigFile`](.././flytekit.configuration.internal#flytekitconfigurationinternalconfigfile) |  |
| [`Credentials`](.././flytekit.configuration.internal#flytekitconfigurationinternalcredentials) |  |
| [`GCP`](.././flytekit.configuration.internal#flytekitconfigurationinternalgcp) |  |
| [`Images`](.././flytekit.configuration.internal#flytekitconfigurationinternalimages) |  |
| [`LegacyConfigEntry`](.././flytekit.configuration.internal#flytekitconfigurationinternallegacyconfigentry) | Creates a record for the config entry. |
| [`Local`](.././flytekit.configuration.internal#flytekitconfigurationinternallocal) |  |
| [`LocalSDK`](.././flytekit.configuration.internal#flytekitconfigurationinternallocalsdk) |  |
| [`Persistence`](.././flytekit.configuration.internal#flytekitconfigurationinternalpersistence) |  |
| [`Platform`](.././flytekit.configuration.internal#flytekitconfigurationinternalplatform) |  |
| [`Secrets`](.././flytekit.configuration.internal#flytekitconfigurationinternalsecrets) |  |
| [`StatsD`](.././flytekit.configuration.internal#flytekitconfigurationinternalstatsd) |  |
| [`YamlConfigEntry`](.././flytekit.configuration.internal#flytekitconfigurationinternalyamlconfigentry) | Creates a record for the config entry. |

## flytekit.configuration.internal.AWS

## flytekit.configuration.internal.AZURE

## flytekit.configuration.internal.ConfigEntry

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
) -> typing.Optional[typing.Any]
```
Reads the config Entry from the various sources in the following order,
#. First try to read from the relevant environment variable,
#. If missing, then try to read from the legacy config file, if one was parsed.
#. If missing, then try to read from the yaml file.

The constructor for ConfigFile currently does not allow specification of both the ini and yaml style formats.



| Parameter | Type |
|-|-|
| `cfg` | `typing.Optional[ConfigFile]` |

## flytekit.configuration.internal.ConfigFile

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

## flytekit.configuration.internal.Credentials

## flytekit.configuration.internal.GCP

## flytekit.configuration.internal.Images

### Methods

| Method | Description |
|-|-|
| [`get_specified_images()`](#get_specified_images) | This section should contain options, where the option name is the friendly name of the image and the corresponding. |


#### get_specified_images()

```python
def get_specified_images(
    cfg: typing.Optional[flytekit.configuration.file.ConfigFile],
) -> typing.Dict[str, str]
```
This section should contain options, where the option name is the friendly name of the image and the corresponding
value is actual FQN of the image. Example of how the section is structured
[images]
my_image1=docker.io/flyte:tag
# Note that the tag is optional. If not specified it will be the default version identifier specified
my_image2=docker.io/flyte

:returns a dictionary of name: image<fqn+version> Version is optional


| Parameter | Type |
|-|-|
| `cfg` | `typing.Optional[flytekit.configuration.file.ConfigFile]` |

## flytekit.configuration.internal.LegacyConfigEntry

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
) -> typing.Optional[typing.Any]
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

## flytekit.configuration.internal.Local

## flytekit.configuration.internal.LocalSDK

## flytekit.configuration.internal.Persistence

## flytekit.configuration.internal.Platform

## flytekit.configuration.internal.Secrets

## flytekit.configuration.internal.StatsD

## flytekit.configuration.internal.YamlConfigEntry

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

