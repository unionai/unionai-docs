---
title: ABFS
version: 2.0.0b57
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ABFS

**Package:** `flyte.storage`

Any Azure Blob Storage specific configuration.



```python
class ABFS(
    retries: int,
    backoff: datetime.timedelta,
    enable_debug: bool,
    attach_execution_metadata: bool,
    account_name: typing.Optional[str],
    account_key: typing.Optional[str],
    tenant_id: typing.Optional[str],
    client_id: typing.Optional[str],
    client_secret: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `retries` | `int` | |
| `backoff` | `datetime.timedelta` | |
| `enable_debug` | `bool` | |
| `attach_execution_metadata` | `bool` | |
| `account_name` | `typing.Optional[str]` | |
| `account_key` | `typing.Optional[str]` | |
| `tenant_id` | `typing.Optional[str]` | |
| `client_id` | `typing.Optional[str]` | |
| `client_secret` | `typing.Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Construct the config object automatically from environment variables. |
| [`get_fsspec_kwargs()`](#get_fsspec_kwargs) | Returns the configuration as kwargs for constructing an fsspec filesystem. |


### auto()

```python
def auto()
```
Construct the config object automatically from environment variables.


### get_fsspec_kwargs()

```python
def get_fsspec_kwargs(
    anonymous: bool,
    kwargs,
) -> typing.Dict[str, typing.Any]
```
Returns the configuration as kwargs for constructing an fsspec filesystem.


| Parameter | Type | Description |
|-|-|-|
| `anonymous` | `bool` | |
| `kwargs` | `**kwargs` | |

