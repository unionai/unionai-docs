---
title: SnowflakeJobMetadata
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SnowflakeJobMetadata

**Package:** `flyteplugins.connectors.snowflake.connector`

```python
class SnowflakeJobMetadata(
    account: str,
    user: str,
    database: str,
    schema: str,
    warehouse: str,
    query_id: str,
    has_output: bool,
    connection_kwargs: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `account` | `str` | |
| `user` | `str` | |
| `database` | `str` | |
| `schema` | `str` | |
| `warehouse` | `str` | |
| `query_id` | `str` | |
| `has_output` | `bool` | |
| `connection_kwargs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

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


