---
title: flytekit.configuration.internal
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.configuration.internal

## Directory

### Classes

| Class | Description |
|-|-|
| [`AWS`](.././flytekit.configuration.internal#flytekitconfigurationinternalaws) | None. |
| [`AZURE`](.././flytekit.configuration.internal#flytekitconfigurationinternalazure) | None. |
| [`ConfigEntry`](.././flytekit.configuration.internal#flytekitconfigurationinternalconfigentry) | A top level Config entry holder, that holds multiple different representations of the config. |
| [`ConfigFile`](.././flytekit.configuration.internal#flytekitconfigurationinternalconfigfile) | None. |
| [`Credentials`](.././flytekit.configuration.internal#flytekitconfigurationinternalcredentials) | None. |
| [`GCP`](.././flytekit.configuration.internal#flytekitconfigurationinternalgcp) | None. |
| [`Images`](.././flytekit.configuration.internal#flytekitconfigurationinternalimages) | None. |
| [`LegacyConfigEntry`](.././flytekit.configuration.internal#flytekitconfigurationinternallegacyconfigentry) | Creates a record for the config entry. |
| [`Local`](.././flytekit.configuration.internal#flytekitconfigurationinternallocal) | None. |
| [`LocalSDK`](.././flytekit.configuration.internal#flytekitconfigurationinternallocalsdk) | None. |
| [`Persistence`](.././flytekit.configuration.internal#flytekitconfigurationinternalpersistence) | None. |
| [`Platform`](.././flytekit.configuration.internal#flytekitconfigurationinternalplatform) | None. |
| [`Secrets`](.././flytekit.configuration.internal#flytekitconfigurationinternalsecrets) | None. |
| [`StatsD`](.././flytekit.configuration.internal#flytekitconfigurationinternalstatsd) | None. |
| [`YamlConfigEntry`](.././flytekit.configuration.internal#flytekitconfigurationinternalyamlconfigentry) | Creates a record for the config entry. |

## flytekit.configuration.internal.AWS

## flytekit.configuration.internal.AZURE

## flytekit.configuration.internal.ConfigEntry

A top level Config entry holder, that holds multiple different representations of the config.
Legacy means the INI style config files. YAML support is for the flytectl config file, which is there by default
when flytectl starts a sandbox


```python
def ConfigEntry(
    legacy: LegacyConfigEntry,
    yaml_entry: typing.Optional[YamlConfigEntry],
    transform: typing.Optional[typing.Callable[[str], typing.Any]],
):
```
| Parameter | Type |
|-|-|
| `legacy` | `LegacyConfigEntry` |
| `yaml_entry` | `typing.Optional[YamlConfigEntry]` |
| `transform` | `typing.Optional[typing.Callable[[str], typing.Any]]` |

### Methods

| Method | Description |
|-|-|
| [`read()`](#read) | Reads the config Entry from the various sources in the following order, |


#### read()

```python
def read(
    cfg: typing.Optional[ConfigFile],
):
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
def ConfigFile(
    location: str,
):
```
Load the config from this location


| Parameter | Type |
|-|-|
| `location` | `str` |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | None |


#### get()

```python
def get(
    c: typing.Union[LegacyConfigEntry, YamlConfigEntry],
):
```
| Parameter | Type |
|-|-|
| `c` | `typing.Union[LegacyConfigEntry, YamlConfigEntry]` |

### Properties

| Property | Type | Description |
|-|-|-|
| legacy_config |  |  |
| yaml_config |  |  |

## flytekit.configuration.internal.Credentials

## flytekit.configuration.internal.GCP

## flytekit.configuration.internal.Images

### Methods

| Method | Description |
|-|-|
| [`get_specified_images()`](#get_specified_images) | This section should contain options, where the option name is the friendly name of the image and the corresponding |


#### get_specified_images()

```python
def get_specified_images(
    cfg: typing.Optional[flytekit.configuration.file.ConfigFile],
):
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
def LegacyConfigEntry(
    section: str,
    option: str,
    type_: typing.Type,
):
```
| Parameter | Type |
|-|-|
| `section` | `str` |
| `option` | `str` |
| `type_` | `typing.Type` |

### Methods

| Method | Description |
|-|-|
| [`get_env_name()`](#get_env_name) | None |
| [`read_from_env()`](#read_from_env) | Reads the config entry from environment variable, the structure of the env var is current |
| [`read_from_file()`](#read_from_file) | None |


#### get_env_name()

```python
def get_env_name()
```
#### read_from_env()

```python
def read_from_env(
    transform: typing.Optional[typing.Callable],
):
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
):
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
def YamlConfigEntry(
    switch: str,
    config_value_type: typing.Type,
):
```
| Parameter | Type |
|-|-|
| `switch` | `str` |
| `config_value_type` | `typing.Type` |

### Methods

| Method | Description |
|-|-|
| [`read_from_file()`](#read_from_file) | None |


#### read_from_file()

```python
def read_from_file(
    cfg: ConfigFile,
    transform: typing.Optional[typing.Callable],
):
```
| Parameter | Type |
|-|-|
| `cfg` | `ConfigFile` |
| `transform` | `typing.Optional[typing.Callable]` |

