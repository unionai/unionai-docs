---
title: DatabricksJobMetadata
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DatabricksJobMetadata

**Package:** `flyteplugins.connectors.databricks.connector`

```python
class DatabricksJobMetadata(
    databricks_instance: str,
    run_id: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `databricks_instance` | `str` | |
| `run_id` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes. |
| [`encode()`](#encode) | Encode the resource meta to bytes. |


### decode()

```python
def decode(
    data: bytes,
) -> ResourceMeta
```
Decode the resource meta from bytes.


| Parameter | Type | Description |
|-|-|-|
| `data` | `bytes` | |

### encode()

```python
def encode()
```
Encode the resource meta to bytes.


