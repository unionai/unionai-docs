---
title: DeviceCodeAuthenticator
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DeviceCodeAuthenticator

**Package:** `flytekit.clients.auth.authenticator`

This Authenticator implements the Device Code authorization flow useful for headless user authentication.

Examples described
- https://developer.okta.com/docs/guides/device-authorization-grant/main/
- https://auth0.com/docs/get-started/authentication-and-authorization-flow/device-authorization-flow#device-flow


```python
class DeviceCodeAuthenticator(
    endpoint: str,
    cfg_store: flytekit.clients.auth.authenticator.ClientConfigStore,
    header_key: typing.Optional[str],
    audience: typing.Optional[str],
    scopes: typing.Optional[typing.List[str]],
    http_proxy_url: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
    session: typing.Optional[requests.sessions.Session],
)
```
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `cfg_store` | `flytekit.clients.auth.authenticator.ClientConfigStore` | |
| `header_key` | `typing.Optional[str]` | |
| `audience` | `typing.Optional[str]` | |
| `scopes` | `typing.Optional[typing.List[str]]` | |
| `http_proxy_url` | `typing.Optional[str]` | |
| `verify` | `typing.Union[bool, str, NoneType]` | |
| `session` | `typing.Optional[requests.sessions.Session]` | |

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
