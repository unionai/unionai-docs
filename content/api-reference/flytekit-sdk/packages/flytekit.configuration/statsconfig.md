---
title: StatsConfig
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# StatsConfig

**Package:** `flytekit.configuration`

Configuration for sending statsd.



```python
class StatsConfig(
    host: str,
    port: int,
    disabled: bool,
    disabled_tags: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `host` | `str` | The statsd host |
| `port` | `int` | statsd port |
| `disabled` | `bool` | Whether or not to send |
| `disabled_tags` | `bool` | Turn on to reduce cardinality. |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from environment variable, followed by ConfigFile provided. |


### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> StatsConfig
```
Reads from environment variable, followed by ConfigFile provided


| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` | :return: |

