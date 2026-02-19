---
title: LegacyConfigEntry
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LegacyConfigEntry

**Package:** `flytekit.configuration.file`

Creates a record for the config entry. contains


```python
class LegacyConfigEntry(
    section: str,
    option: str,
    type_: typing.Type,
)
```
| Parameter | Type | Description |
|-|-|-|
| `section` | `str` | section the option should be found under |
| `option` | `str` | the option str to lookup |
| `type_` | `typing.Type` | Expected type of the value |

## Methods

| Method | Description |
|-|-|
| [`get_env_name()`](#get_env_name) |  |
| [`read_from_env()`](#read_from_env) | Reads the config entry from environment variable, the structure of the env var is current. |
| [`read_from_file()`](#read_from_file) |  |


### get_env_name()

```python
def get_env_name()
```
### read_from_env()

```python
def read_from_env(
    transform: typing.Optional[typing.Callable],
) -> typing.Optional[typing.Any]
```
Reads the config entry from environment variable, the structure of the env var is current
``FLYTE_{SECTION}_{OPTION}`` all upper cased. We will change this in the future.
:return:


| Parameter | Type | Description |
|-|-|-|
| `transform` | `typing.Optional[typing.Callable]` | |

### read_from_file()

```python
def read_from_file(
    cfg: ConfigFile,
    transform: typing.Optional[typing.Callable],
) -> typing.Optional[typing.Any]
```
| Parameter | Type | Description |
|-|-|-|
| `cfg` | `ConfigFile` | |
| `transform` | `typing.Optional[typing.Callable]` | |

