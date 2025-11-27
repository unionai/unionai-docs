---
title: YamlConfigEntry
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# YamlConfigEntry

**Package:** `flytekit.configuration.file`

Creates a record for the config entry.


```python
class YamlConfigEntry(
    switch: str,
    config_value_type: typing.Type,
)
```
| Parameter | Type | Description |
|-|-|-|
| `switch` | `str` | |
| `config_value_type` | `typing.Type` | |

## Methods

| Method | Description |
|-|-|
| [`read_from_file()`](#read_from_file) |  |


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

