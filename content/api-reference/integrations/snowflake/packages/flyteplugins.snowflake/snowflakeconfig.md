---
title: SnowflakeConfig
version: 2.0.0b55
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SnowflakeConfig

**Package:** `flyteplugins.snowflake`

Configure a Snowflake Task using a `SnowflakeConfig` object.

Additional connection parameters (role, authenticator, session_parameters, etc.) can be passed
via connection_kwargs.
See: https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api



```python
class SnowflakeConfig(
    account: str,
    database: str,
    schema: str,
    warehouse: str,
    user: str,
    connection_kwargs: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `account` | `str` | The Snowflake account identifier. |
| `database` | `str` | The Snowflake database name. |
| `schema` | `str` | The Snowflake schema name. |
| `warehouse` | `str` | The Snowflake warehouse name. |
| `user` | `str` | The Snowflake user name. |
| `connection_kwargs` | `typing.Optional[typing.Dict[str, typing.Any]]` | Optional dictionary of additional Snowflake connection parameters. |

