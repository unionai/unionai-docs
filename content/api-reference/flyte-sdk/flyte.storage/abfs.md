---
title: ABFS
description: "Any Azure Blob Storage specific configuration."
icon: braces
version: 2.12.4
variants: +flyte +union
layout: py_api
---

# ABFS

**Package:** `flyte.storage`

Any Azure Blob Storage specific configuration.

`auto()` reads the Flyte-prefixed environment variables (`FLYTE_AZURE_STORAGE_ACCOUNT_NAME`,
`FLYTE_AZURE_STORAGE_ACCOUNT_KEY`, `FLYTE_AZURE_TENANT_ID`, `FLYTE_AZURE_CLIENT_ID`,
`FLYTE_AZURE_CLIENT_SECRET`) when any of them is set, and otherwise falls back to the generic
`AZURE_*` names. The generic names are shared with adlfs, deltalake, the Azure SDKs and others,
so set the prefixed ones when a task uses the generic names for its own data access.

When a URI names its storage account (`abfs://container@account.dfs.core.windows.net/...`),
that account takes precedence over a configured `account_name` that differs from it, and the
configured `account_key` (which belongs to the other account) is not sent.


## Parameters

```python
class ABFS(
    retries: int = 3,
    backoff: datetime.timedelta = datetime.timedelta(seconds=5),
    enable_debug: bool = False,
    attach_execution_metadata: bool = True,
    account_name: typing.Optional[str] = None,
    account_key: typing.Optional[str] = None,
    tenant_id: typing.Optional[str] = None,
    client_id: typing.Optional[str] = None,
    client_secret: typing.Optional[str] = None,
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
    anonymous: bool = False,
    **kwargs,
) -> typing.Dict[str, typing.Any]
```
Returns the configuration as kwargs for constructing an fsspec filesystem.


| Parameter | Type | Description |
|-|-|-|
| `anonymous` | `bool` | |
| `**kwargs` |  | |

