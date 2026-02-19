---
title: ConfigFile
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConfigFile

**Package:** `flytekit.configuration.file`

```python
class ConfigFile(
    location: str,
)
```
Load the config from this location


| Parameter | Type | Description |
|-|-|-|
| `location` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `legacy_config` | `None` |  |
| `yaml_config` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) |  |


### get()

```python
def get(
    c: typing.Union[LegacyConfigEntry, YamlConfigEntry],
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `c` | `typing.Union[LegacyConfigEntry, YamlConfigEntry]` | |

