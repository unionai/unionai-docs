---
title: Authenticator
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Authenticator

**Package:** `flytekit.clients.auth.authenticator`

Base authenticator for all authentication flows


```python
class Authenticator(
    endpoint: str,
    header_key: str,
    credentials: flytekit.clients.auth.keyring.Credentials,
    http_proxy_url: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `header_key` | `str` | |
| `credentials` | `flytekit.clients.auth.keyring.Credentials` | |
| `http_proxy_url` | `typing.Optional[str]` | |
| `verify` | `typing.Union[bool, str, NoneType]` | |

## Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) |  |
| [`get_credentials()`](#get_credentials) |  |
| [`refresh_credentials()`](#refresh_credentials) |  |


### fetch_grpc_call_auth_metadata()

```python
def fetch_grpc_call_auth_metadata()
```
### get_credentials()

```python
def get_credentials()
```
### refresh_credentials()

```python
def refresh_credentials()
```
