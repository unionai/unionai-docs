---
title: GCSConfig
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# GCSConfig

**Package:** `flytekit.configuration`

Any GCS specific configuration.


```python
def GCSConfig(
    gsutil_parallelism: bool,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `gsutil_parallelism` | `bool` |
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
