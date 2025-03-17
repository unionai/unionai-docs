---
title: StatsConfig
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# StatsConfig

**Package:** `flytekit.configuration`

Configuration for sending statsd.



```python
def StatsConfig(
    host: str,
    port: int,
    disabled: bool,
    disabled_tags: bool,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `host` | `str` |
| `port` | `int` |
| `disabled` | `bool` |
| `disabled_tags` | `bool` |
## Methods

### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
Reads from environment variable, followed by ConfigFile provided


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |
