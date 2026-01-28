---
title: SnowflakeJobMetadata
version: 2.0.0b53.dev3+g082aa0f49
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SnowflakeJobMetadata

**Package:** `flyteplugins.connectors.snowflake.connector`

Metadata for a Snowflake query job.

Attributes:
    account: Snowflake account identifier.
    user: Snowflake user name.
    database: Snowflake database name.
    schema: Snowflake schema name.
    warehouse: Snowflake warehouse name.
    query_id: Unique identifier for the submitted query.
    has_output: Indicates if the query produces output.
    connection_kwargs: Additional connection parameters.


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


