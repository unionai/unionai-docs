---
title: S3Config
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# S3Config

**Package:** `flytekit.configuration`

S3 specific configuration


```python
def S3Config(
    enable_debug: bool,
    endpoint: typing.Optional[str],
    retries: int,
    backoff: datetime.timedelta,
    access_key_id: typing.Optional[str],
    secret_access_key: typing.Optional[str],
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `enable_debug` | `bool` |
| `endpoint` | `typing.Optional[str]` |
| `retries` | `int` |
| `backoff` | `datetime.timedelta` |
| `access_key_id` | `typing.Optional[str]` |
| `secret_access_key` | `typing.Optional[str]` |
## Methods

### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
Automatically configure


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |
