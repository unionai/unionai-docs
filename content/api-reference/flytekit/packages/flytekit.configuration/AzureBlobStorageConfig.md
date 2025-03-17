---
title: AzureBlobStorageConfig
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# AzureBlobStorageConfig

**Package:** `flytekit.configuration`

Any Azure Blob Storage specific configuration.


```python
def AzureBlobStorageConfig(
    account_name: typing.Optional[str],
    account_key: typing.Optional[str],
    tenant_id: typing.Optional[str],
    client_id: typing.Optional[str],
    client_secret: typing.Optional[str],
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `account_name` | `typing.Optional[str]` |
| `account_key` | `typing.Optional[str]` |
| `tenant_id` | `typing.Optional[str]` |
| `client_id` | `typing.Optional[str]` |
| `client_secret` | `typing.Optional[str]` |
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
