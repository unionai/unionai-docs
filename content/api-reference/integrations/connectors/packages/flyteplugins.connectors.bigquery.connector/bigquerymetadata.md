---
title: BigQueryMetadata
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# BigQueryMetadata

**Package:** `flyteplugins.connectors.bigquery.connector`

```python
class BigQueryMetadata(
    job_id: str,
    project: str,
    location: str,
    user_agent: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `job_id` | `str` | |
| `project` | `str` | |
| `location` | `str` | |
| `user_agent` | `str` | |

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


