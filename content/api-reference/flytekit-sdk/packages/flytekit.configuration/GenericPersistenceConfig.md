---
title: GenericPersistenceConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# GenericPersistenceConfig

**Package:** `flytekit.configuration`

Data storage configuration that applies across any provider.


```python
class GenericPersistenceConfig(
    attach_execution_metadata: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `attach_execution_metadata` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> GCSConfig
```
| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` | |

