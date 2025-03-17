---
title: LocalConfig
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# LocalConfig

**Package:** `flytekit.configuration`

Any configuration specific to local runs.


```python
def LocalConfig(
    cache_enabled: bool,
    cache_overwrite: bool,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `cache_enabled` | `bool` |
| `cache_overwrite` | `bool` |
## Methods

### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |
