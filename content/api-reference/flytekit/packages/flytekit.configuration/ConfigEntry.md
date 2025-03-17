---
title: ConfigEntry
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# ConfigEntry

**Package:** `flytekit.configuration`

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
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `legacy` | `LegacyConfigEntry` |
| `yaml_entry` | `typing.Optional[YamlConfigEntry]` |
| `transform` | `typing.Optional[typing.Callable[[str], typing.Any]]` |
## Methods

### read()

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
