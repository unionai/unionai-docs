---
title: ClientCredentialsAuthenticator
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ClientCredentialsAuthenticator

**Package:** `flytekit.clients.auth.authenticator`

This Authenticator uses ClientId and ClientSecret to authenticate



```python
class ClientCredentialsAuthenticator(
    endpoint: str,
    client_id: str,
    client_secret: str,
    cfg_store: flytekit.clients.auth.authenticator.ClientConfigStore,
    header_key: typing.Optional[str],
    scopes: typing.Optional[typing.List[str]],
    http_proxy_url: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
    audience: typing.Optional[str],
    session: typing.Optional[requests.sessions.Session],
)
```
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `client_id` | `str` | |
| `client_secret` | `str` | |
| `cfg_store` | `flytekit.clients.auth.authenticator.ClientConfigStore` | |
| `header_key` | `typing.Optional[str]` | |
| `scopes` | `typing.Optional[typing.List[str]]` | |
| `http_proxy_url` | `typing.Optional[str]` | |
| `verify` | `typing.Union[bool, str, NoneType]` | |
| `audience` | `typing.Optional[str]` | |
| `session` | `typing.Optional[requests.sessions.Session]` | |

## Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) |  |
| [`get_credentials()`](#get_credentials) |  |
| [`refresh_credentials()`](#refresh_credentials) | This function is used by the _handle_rpc_error() decorator, depending on the AUTH_MODE config object. |


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
This function is used by the _handle_rpc_error() decorator, depending on the AUTH_MODE config object. This handler
is meant for SDK use-cases of auth (like pyflyte, or when users call SDK functions that require access to Admin,
like when waiting for another workflow to complete from within a task). This function uses basic auth, which means
the credentials for basic auth must be present from wherever this code is running.


