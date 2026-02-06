---
title: SnowflakeConfig
version: 2.0.0b54
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SnowflakeConfig

**Package:** `flyteplugins.snowflake.task`

SnowflakeConfig should be used to configure a Snowflake Task.

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
| `account` | `str` | |
| `database` | `str` | |
| `schema` | `str` | |
| `warehouse` | `str` | |
| `user` | `str` | |
| `connection_kwargs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

