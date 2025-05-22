---
title: flytekit.clients.auth.authenticator
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.auth.authenticator

## Directory

### Classes

| Class | Description |
|-|-|
| [`Authenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthenticator) | Base authenticator for all authentication flows. |
| [`ClientConfig`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfig) | Client Configuration that is needed by the authenticator. |
| [`ClientConfigStore`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfigstore) | Client Config store retrieve client config. |
| [`ClientCredentialsAuthenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientcredentialsauthenticator) | This Authenticator uses ClientId and ClientSecret to authenticate. |
| [`CommandAuthenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorcommandauthenticator) | This Authenticator retrieves access_token using the provided command. |
| [`DeviceCodeAuthenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatordevicecodeauthenticator) | This Authenticator implements the Device Code authorization flow useful for headless user authentication. |
| [`PKCEAuthenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorpkceauthenticator) | This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login. |
| [`StaticClientConfigStore`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorstaticclientconfigstore) | Client Config store retrieve client config. |

## flytekit.clients.auth.authenticator.Authenticator

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
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `header_key` | `str` |
| `credentials` | `flytekit.clients.auth.keyring.Credentials` |
| `http_proxy_url` | `typing.Optional[str]` |
| `verify` | `typing.Union[bool, str, NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) |  |
| [`get_credentials()`](#get_credentials) |  |
| [`refresh_credentials()`](#refresh_credentials) |  |


#### fetch_grpc_call_auth_metadata()

```python
def fetch_grpc_call_auth_metadata()
```
#### get_credentials()

```python
def get_credentials()
```
#### refresh_credentials()

```python
def refresh_credentials()
```
## flytekit.clients.auth.authenticator.ClientConfig

Client Configuration that is needed by the authenticator


```python
class ClientConfig(
    token_endpoint: str,
    authorization_endpoint: str,
    redirect_uri: str,
    client_id: str,
    device_authorization_endpoint: typing.Optional[str],
    scopes: typing.List[str],
    header_key: str,
    audience: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `token_endpoint` | `str` |
| `authorization_endpoint` | `str` |
| `redirect_uri` | `str` |
| `client_id` | `str` |
| `device_authorization_endpoint` | `typing.Optional[str]` |
| `scopes` | `typing.List[str]` |
| `header_key` | `str` |
| `audience` | `typing.Optional[str]` |

## flytekit.clients.auth.authenticator.ClientConfigStore

Client Config store retrieve client config. this can be done in multiple ways


### Methods

| Method | Description |
|-|-|
| [`get_client_config()`](#get_client_config) |  |


#### get_client_config()

```python
def get_client_config()
```
## flytekit.clients.auth.authenticator.ClientCredentialsAuthenticator

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
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `client_id` | `str` |
| `client_secret` | `str` |
| `cfg_store` | `flytekit.clients.auth.authenticator.ClientConfigStore` |
| `header_key` | `typing.Optional[str]` |
| `scopes` | `typing.Optional[typing.List[str]]` |
| `http_proxy_url` | `typing.Optional[str]` |
| `verify` | `typing.Union[bool, str, NoneType]` |
| `audience` | `typing.Optional[str]` |
| `session` | `typing.Optional[requests.sessions.Session]` |

### Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) |  |
| [`get_credentials()`](#get_credentials) |  |
| [`refresh_credentials()`](#refresh_credentials) | This function is used by the _handle_rpc_error() decorator, depending on the AUTH_MODE config object. |


#### fetch_grpc_call_auth_metadata()

```python
def fetch_grpc_call_auth_metadata()
```
#### get_credentials()

```python
def get_credentials()
```
#### refresh_credentials()

```python
def refresh_credentials()
```
This function is used by the _handle_rpc_error() decorator, depending on the AUTH_MODE config object. This handler
is meant for SDK use-cases of auth (like pyflyte, or when users call SDK functions that require access to Admin,
like when waiting for another workflow to complete from within a task). This function uses basic auth, which means
the credentials for basic auth must be present from wherever this code is running.


## flytekit.clients.auth.authenticator.CommandAuthenticator

This Authenticator retrieves access_token using the provided command


```python
class CommandAuthenticator(
    command: typing.List[str],
    header_key: str,
)
```
| Parameter | Type |
|-|-|
| `command` | `typing.List[str]` |
| `header_key` | `str` |

### Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) |  |
| [`get_credentials()`](#get_credentials) |  |
| [`refresh_credentials()`](#refresh_credentials) | This function is used when the configuration value for AUTH_MODE is set to 'external_process'. |


#### fetch_grpc_call_auth_metadata()

```python
def fetch_grpc_call_auth_metadata()
```
#### get_credentials()

```python
def get_credentials()
```
#### refresh_credentials()

```python
def refresh_credentials()
```
This function is used when the configuration value for AUTH_MODE is set to 'external_process'.
It reads an id token generated by an external process started by running the 'command'.


## flytekit.clients.auth.authenticator.DeviceCodeAuthenticator

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
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `cfg_store` | `flytekit.clients.auth.authenticator.ClientConfigStore` |
| `header_key` | `typing.Optional[str]` |
| `audience` | `typing.Optional[str]` |
| `scopes` | `typing.Optional[typing.List[str]]` |
| `http_proxy_url` | `typing.Optional[str]` |
| `verify` | `typing.Union[bool, str, NoneType]` |
| `session` | `typing.Optional[requests.sessions.Session]` |

### Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) |  |
| [`get_credentials()`](#get_credentials) |  |
| [`refresh_credentials()`](#refresh_credentials) |  |


#### fetch_grpc_call_auth_metadata()

```python
def fetch_grpc_call_auth_metadata()
```
#### get_credentials()

```python
def get_credentials()
```
#### refresh_credentials()

```python
def refresh_credentials()
```
## flytekit.clients.auth.authenticator.PKCEAuthenticator

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


| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `cfg_store` | `flytekit.clients.auth.authenticator.ClientConfigStore` |
| `scopes` | `typing.Optional[typing.List[str]]` |
| `header_key` | `typing.Optional[str]` |
| `verify` | `typing.Union[bool, str, NoneType]` |
| `session` | `typing.Optional[requests.sessions.Session]` |

### Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) |  |
| [`get_credentials()`](#get_credentials) |  |
| [`refresh_credentials()`](#refresh_credentials) |  |


#### fetch_grpc_call_auth_metadata()

```python
def fetch_grpc_call_auth_metadata()
```
#### get_credentials()

```python
def get_credentials()
```
#### refresh_credentials()

```python
def refresh_credentials()
```
## flytekit.clients.auth.authenticator.StaticClientConfigStore

Client Config store retrieve client config. this can be done in multiple ways


```python
class StaticClientConfigStore(
    cfg: flytekit.clients.auth.authenticator.ClientConfig,
)
```
| Parameter | Type |
|-|-|
| `cfg` | `flytekit.clients.auth.authenticator.ClientConfig` |

### Methods

| Method | Description |
|-|-|
| [`get_client_config()`](#get_client_config) |  |


#### get_client_config()

```python
def get_client_config()
```
