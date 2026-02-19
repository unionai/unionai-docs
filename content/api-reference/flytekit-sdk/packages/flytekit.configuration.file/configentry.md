---
title: ConfigEntry
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConfigEntry

**Package:** `flytekit.configuration.file`

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
| Parameter | Type | Description |
|-|-|-|
| `legacy` | `LegacyConfigEntry` | |
| `yaml_entry` | `typing.Optional[YamlConfigEntry]` | |
| `transform` | `typing.Optional[typing.Callable[[str], typing.Any]]` | |

## Methods

| Method | Description |
|-|-|
| [`read()`](#read) | Reads the config Entry from the various sources in the following order,. |


### read()

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



| Parameter | Type | Description |
|-|-|-|
| `cfg` | `typing.Optional[ConfigFile]` | :return: |

