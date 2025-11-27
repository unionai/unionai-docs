---
title: PKCEAuthenticator
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PKCEAuthenticator

**Package:** `flytekit.clients.auth.authenticator`

This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login

For Auth0 - you will need to manually configure your config.yaml to include a scopes list of the syntax:
admin.scopes: ["offline_access", "offline", "all", "openid"] and/or similar scopes in order to get the refresh token +
caching. Otherwise, it will just receive the access token alone. Your FlyteCTL Helm config however should only
contain ["offline", "all"] - as OIDC scopes are ungrantable in Auth0 customer APIs. They are simply requested
for in the POST request during the token caching process.


```python
class PKCEAuthenticator(
    endpoint: str,
    cfg_store: flytekit.clients.auth.authenticator.ClientConfigStore,
    scopes: typing.Optional[typing.List[str]],
    header_key: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
    session: typing.Optional[requests.sessions.Session],
)
```
Initialize with default creds from KeyStore using the endpoint name


| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `cfg_store` | `flytekit.clients.auth.authenticator.ClientConfigStore` | |
| `scopes` | `typing.Optional[typing.List[str]]` | |
| `header_key` | `typing.Optional[str]` | |
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
