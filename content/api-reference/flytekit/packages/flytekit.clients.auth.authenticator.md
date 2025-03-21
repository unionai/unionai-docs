---
title: flytekit.clients.auth.authenticator
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clients.auth.authenticator

## Directory

### Classes

| Class | Description |
|-|-|
| [`Authenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthenticator) | Base authenticator for all authentication flows. |
| [`AuthorizationClient`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthorizationclient) | Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the. |
| [`ClientConfig`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfig) | Client Configuration that is needed by the authenticator. |
| [`ClientConfigStore`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientconfigstore) | Client Config store retrieve client config. |
| [`ClientCredentialsAuthenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorclientcredentialsauthenticator) | This Authenticator uses ClientId and ClientSecret to authenticate. |
| [`CommandAuthenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorcommandauthenticator) | This Authenticator retrieves access_token using the provided command. |
| [`Credentials`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorcredentials) | Stores the credentials together. |
| [`DeviceCodeAuthenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatordevicecodeauthenticator) | This Authenticator implements the Device Code authorization flow useful for headless user authentication. |
| [`KeyringStore`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorkeyringstore) | Methods to access Keyring Store. |
| [`PKCEAuthenticator`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorpkceauthenticator) | This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login. |
| [`StaticClientConfigStore`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorstaticclientconfigstore) | Client Config store retrieve client config. |

### Errors

* [`AccessTokenNotFoundError`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatoraccesstokennotfounderror)
* [`AuthenticationError`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthenticationerror)
* [`AuthenticationPending`](.././flytekit.clients.auth.authenticator#flytekitclientsauthauthenticatorauthenticationpending)

## flytekit.clients.auth.authenticator.AccessTokenNotFoundError

This error is raised with Access token is not found or if Refreshing the token fails


## flytekit.clients.auth.authenticator.AuthenticationError

This is raised for any AuthenticationError


## flytekit.clients.auth.authenticator.AuthenticationPending

This is raised if the token endpoint returns authentication pending


## flytekit.clients.auth.authenticator.Authenticator

Base authenticator for all authentication flows


```python
def Authenticator(
    endpoint: str,
    header_key: str,
    credentials: flytekit.clients.auth.keyring.Credentials,
    http_proxy_url: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
):
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
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) | None |
| [`get_credentials()`](#get_credentials) | None |
| [`refresh_credentials()`](#refresh_credentials) | None |


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
## flytekit.clients.auth.authenticator.AuthorizationClient

Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the
credentials. NOTE: This will open an web browser to retrieve the credentials.


```python
def AuthorizationClient(
    endpoint: str,
    auth_endpoint: str,
    token_endpoint: str,
    audience: typing.Optional[str],
    scopes: typing.Optional[typing.List[str]],
    client_id: typing.Optional[str],
    redirect_uri: typing.Optional[str],
    endpoint_metadata: typing.Optional[EndpointMetadata],
    verify: typing.Optional[typing.Union[bool, str]],
    session: typing.Optional[requests.Session],
    request_auth_code_params: typing.Optional[typing.Dict[str, str]],
    request_access_token_params: typing.Optional[typing.Dict[str, str]],
    refresh_access_token_params: typing.Optional[typing.Dict[str, str]],
    add_request_auth_code_params_to_request_access_token_params: typing.Optional[bool],
):
```
Create new AuthorizationClient



| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `auth_endpoint` | `str` |
| `token_endpoint` | `str` |
| `audience` | `typing.Optional[str]` |
| `scopes` | `typing.Optional[typing.List[str]]` |
| `client_id` | `typing.Optional[str]` |
| `redirect_uri` | `typing.Optional[str]` |
| `endpoint_metadata` | `typing.Optional[EndpointMetadata]` |
| `verify` | `typing.Optional[typing.Union[bool, str]]` |
| `session` | `typing.Optional[requests.Session]` |
| `request_auth_code_params` | `typing.Optional[typing.Dict[str, str]]` |
| `request_access_token_params` | `typing.Optional[typing.Dict[str, str]]` |
| `refresh_access_token_params` | `typing.Optional[typing.Dict[str, str]]` |
| `add_request_auth_code_params_to_request_access_token_params` | `typing.Optional[bool]` |

### Methods

| Method | Description |
|-|-|
| [`get_creds_from_remote()`](#get_creds_from_remote) | This is the entrypoint method |
| [`refresh_access_token()`](#refresh_access_token) | None |


#### get_creds_from_remote()

```python
def get_creds_from_remote()
```
This is the entrypoint method. It will kickoff the full authentication
flow and trigger a web-browser to retrieve credentials. Because this
needs to open a port on localhost and may be called from a
multithreaded context (e.g. pyflyte register), this call may block
multiple threads and return a cached result for up to 60 seconds.


#### refresh_access_token()

```python
def refresh_access_token(
    credentials: Credentials,
):
```
| Parameter | Type |
|-|-|
| `credentials` | `Credentials` |

## flytekit.clients.auth.authenticator.ClientConfig

Client Configuration that is needed by the authenticator


```python
def ClientConfig(
    token_endpoint: str,
    authorization_endpoint: str,
    redirect_uri: str,
    client_id: str,
    device_authorization_endpoint: typing.Optional[str],
    scopes: typing.List[str],
    header_key: str,
    audience: typing.Optional[str],
):
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
| [`get_client_config()`](#get_client_config) | None |


#### get_client_config()

```python
def get_client_config()
```
## flytekit.clients.auth.authenticator.ClientCredentialsAuthenticator

This Authenticator uses ClientId and ClientSecret to authenticate


```python
def ClientCredentialsAuthenticator(
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
):
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
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) | None |
| [`get_credentials()`](#get_credentials) | None |
| [`refresh_credentials()`](#refresh_credentials) | This function is used by the _handle_rpc_error() decorator, depending on the AUTH_MODE config object |


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
def CommandAuthenticator(
    command: typing.List[str],
    header_key: str,
):
```
| Parameter | Type |
|-|-|
| `command` | `typing.List[str]` |
| `header_key` | `str` |

### Methods

| Method | Description |
|-|-|
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) | None |
| [`get_credentials()`](#get_credentials) | None |
| [`refresh_credentials()`](#refresh_credentials) | This function is used when the configuration value for AUTH_MODE is set to 'external_process' |


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


## flytekit.clients.auth.authenticator.Credentials

Stores the credentials together


```python
def Credentials(
    access_token: str,
    refresh_token: typing.Optional[str],
    for_endpoint: str,
    expires_in: typing.Optional[int],
    id_token: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `access_token` | `str` |
| `refresh_token` | `typing.Optional[str]` |
| `for_endpoint` | `str` |
| `expires_in` | `typing.Optional[int]` |
| `id_token` | `typing.Optional[str]` |

## flytekit.clients.auth.authenticator.DeviceCodeAuthenticator

This Authenticator implements the Device Code authorization flow useful for headless user authentication.

Examples described
- https://developer.okta.com/docs/guides/device-authorization-grant/main/
- https://auth0.com/docs/get-started/authentication-and-authorization-flow/device-authorization-flow#device-flow


```python
def DeviceCodeAuthenticator(
    endpoint: str,
    cfg_store: flytekit.clients.auth.authenticator.ClientConfigStore,
    header_key: typing.Optional[str],
    audience: typing.Optional[str],
    scopes: typing.Optional[typing.List[str]],
    http_proxy_url: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
    session: typing.Optional[requests.sessions.Session],
):
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
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) | None |
| [`get_credentials()`](#get_credentials) | None |
| [`refresh_credentials()`](#refresh_credentials) | None |


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
## flytekit.clients.auth.authenticator.KeyringStore

Methods to access Keyring Store.


### Methods

| Method | Description |
|-|-|
| [`delete()`](#delete) | None |
| [`retrieve()`](#retrieve) | None |
| [`store()`](#store) | None |


#### delete()

```python
def delete(
    for_endpoint: str,
):
```
| Parameter | Type |
|-|-|
| `for_endpoint` | `str` |

#### retrieve()

```python
def retrieve(
    for_endpoint: str,
):
```
| Parameter | Type |
|-|-|
| `for_endpoint` | `str` |

#### store()

```python
def store(
    credentials: flytekit.clients.auth.keyring.Credentials,
):
```
| Parameter | Type |
|-|-|
| `credentials` | `flytekit.clients.auth.keyring.Credentials` |

## flytekit.clients.auth.authenticator.PKCEAuthenticator

This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login

For Auth0 - you will need to manually configure your config.yaml to include a scopes list of the syntax:
admin.scopes: ["offline_access", "offline", "all", "openid"] and/or similar scopes in order to get the refresh token +
caching. Otherwise, it will just receive the access token alone. Your FlyteCTL Helm config however should only
contain ["offline", "all"] - as OIDC scopes are ungrantable in Auth0 customer APIs. They are simply requested
for in the POST request during the token caching process.


```python
def PKCEAuthenticator(
    endpoint: str,
    cfg_store: flytekit.clients.auth.authenticator.ClientConfigStore,
    scopes: typing.Optional[typing.List[str]],
    header_key: typing.Optional[str],
    verify: typing.Union[bool, str, NoneType],
    session: typing.Optional[requests.sessions.Session],
):
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
| [`fetch_grpc_call_auth_metadata()`](#fetch_grpc_call_auth_metadata) | None |
| [`get_credentials()`](#get_credentials) | None |
| [`refresh_credentials()`](#refresh_credentials) | None |


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
def StaticClientConfigStore(
    cfg: flytekit.clients.auth.authenticator.ClientConfig,
):
```
| Parameter | Type |
|-|-|
| `cfg` | `flytekit.clients.auth.authenticator.ClientConfig` |

### Methods

| Method | Description |
|-|-|
| [`get_client_config()`](#get_client_config) | None |


#### get_client_config()

```python
def get_client_config()
```
