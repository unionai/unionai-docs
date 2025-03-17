---
title: SecretsConfig
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# SecretsConfig

**Package:** `flytekit.configuration`

Configuration for secrets.



```python
def SecretsConfig(
    env_prefix: str,
    default_dir: str,
    file_prefix: str,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `env_prefix` | `str` |
| `default_dir` | `str` |
| `file_prefix` | `str` |
## Methods

### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
Reads from environment variable or from config file


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |
