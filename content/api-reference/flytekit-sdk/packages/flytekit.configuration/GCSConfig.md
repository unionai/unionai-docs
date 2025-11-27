---
title: GCSConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# GCSConfig

**Package:** `flytekit.configuration`

Any GCS specific configuration.


```python
class GCSConfig(
    gsutil_parallelism: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `gsutil_parallelism` | `bool` | |

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

