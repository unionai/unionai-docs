---
title: GenericPersistenceConfig
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# GenericPersistenceConfig

**Package:** `flytekit.configuration`

Data storage configuration that applies across any provider.


```python
def GenericPersistenceConfig(
    attach_execution_metadata: bool,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `attach_execution_metadata` | `bool` |
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
