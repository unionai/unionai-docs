---
title: YamlConfigEntry
version: 1.16.14
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
| `switch` | `str` | dot-delimited string that should match flytectl args. Leaving it as dot-delimited instead of a list of strings because it's easier to maintain alignment with flytectl. |
| `config_value_type` | `typing.Type` | Expected type of the value |

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

