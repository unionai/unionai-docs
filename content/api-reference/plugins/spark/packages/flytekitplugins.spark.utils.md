---
title: flytekitplugins.spark.utils
version: 1.16.19
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# flytekitplugins.spark.utils

## Directory

### Methods

| Method | Description |
|-|-|
| [`is_serverless_config()`](#is_serverless_config) | Detect if the Databricks configuration is for serverless compute. |


## Methods

#### is_serverless_config()

```python
def is_serverless_config(
    databricks_conf: dict,
) -> bool
```
Detect if the Databricks configuration is for serverless compute.

Serverless is indicated by having ``environment_key`` or ``environments``
without any cluster config (``existing_cluster_id`` or ``new_cluster``).



| Parameter | Type | Description |
|-|-|-|
| `databricks_conf` | `dict` | The databricks job configuration dict. |

**Returns:** bool: True if the configuration targets serverless compute.

