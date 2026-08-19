---
title: flytekit.clients.auth.auth_client
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.clients.auth.auth_client

## Directory

### Classes

| Class | Description |
|-|-|
| [`AuthorizationClient`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationclient) | Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the. |
| [`AuthorizationCode`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientauthorizationcode) |  |
| [`EndpointMetadata`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientendpointmetadata) | This class can be used to control the rendering of the page on login successful or failure. |
| [`OAuthCallbackHandler`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthcallbackhandler) | A simple wrapper around BaseHTTPServer. |
| [`OAuthHTTPServer`](.././flytekit.clients.auth.auth_client#flytekitclientsauthauth_clientoauthhttpserver) | A simple wrapper around the BaseHTTPServer. |

## flytekit.clients.auth.auth_client.AuthorizationClient

Authorization client that stores the credentials in keyring and uses oauth2 standard flow to retrieve the
credentials. NOTE: This will open an web browser to retrieve the credentials.


### Parameters

```python
class AuthorizationClient(
    endpoint: str,
    auth_endpoint: str,
    token_endpoint: str,
    audience: typing.Optional[str] = None,
    scopes: typing.Optional[typing.List[str]] = None,
    client_id: typing.Optional[str] = None,
    redirect_uri: typing.Optional[str] = None,
    endpoint_metadata: typing.Optional[EndpointMetadata] = None,
    verify: typing.Optional[typing.Union[bool, str]] = None,
    session: typing.Optional[requests.Session] = None,
    request_auth_code_params: typing.Optional[typing.Dict[str, str]] = None,
    request_access_token_params: typing.Optional[typing.Dict[str, str]] = None,
    refresh_access_token_params: typing.Optional[typing.Dict[str, str]] = None,
    add_request_auth_code_params_to_request_access_token_params: typing.Optional[bool] = False,
)
```
Create new AuthorizationClient



| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | str endpoint to connect to |
| `auth_endpoint` | `str` | str endpoint where auth metadata can be found |
| `token_endpoint` | `str` | str endpoint to retrieve token from |
| `audience` | `typing.Optional[str]` | Audience parameter for Auth0 |
| `scopes` | `typing.Optional[typing.List[str]]` | list[str] oauth2 scopes |
| `client_id` | `typing.Optional[str]` | oauth2 client id |
| `redirect_uri` | `typing.Optional[str]` | oauth2 redirect uri |
| `endpoint_metadata` | `typing.Optional[EndpointMetadata]` | EndpointMetadata object to control the rendering of the page on login successful or failure |
| `verify` | `typing.Optional[typing.Union[bool, str]]` | Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to ``True``. When set to ``False``, requests will accept any TLS certificate presented by the server, and will ignore hostname mismatches and/or expired certificates, which will make your application vulnerable to man-in-the-middle (MitM) attacks. Setting verify to ``False`` may be useful during local development or testing. |
| `session` | `typing.Optional[requests.Session]` | A custom requests.Session object to use for making HTTP requests. If not provided, a new Session object will be created. |
| `request_auth_code_params` | `typing.Optional[typing.Dict[str, str]]` | dict of parameters to add to login uri opened in the browser |
| `request_access_token_params` | `typing.Optional[typing.Dict[str, str]]` | dict of parameters to add when exchanging the auth code for the access token |
| `refresh_access_token_params` | `typing.Optional[typing.Dict[str, str]]` | dict of parameters to add when refreshing the access token |
| `add_request_auth_code_params_to_request_access_token_params` | `typing.Optional[bool]` | Whether to add the `request_auth_code_params` to the parameters sent when exchanging the auth code for the access token. Defaults to False. Required e.g. for the PKCE flow with flyteadmin. Not required for e.g. the standard OAuth2 flow on GCP. |

### Methods

| Method | Description |
|-|-|
| [`get_creds_from_remote()`](#get_creds_from_remote) | This is the entrypoint method. |
| [`refresh_access_token()`](#refresh_access_token) |  |


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
) -> Credentials
```
| Parameter | Type | Description |
|-|-|-|
| `credentials` | `Credentials` | |

## flytekit.clients.auth.auth_client.AuthorizationCode

### Parameters

```python
class AuthorizationCode(
    code,
    state,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` |  | |
| `state` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `code` | `None` |  |
| `state` | `None` |  |

## flytekit.clients.auth.auth_client.EndpointMetadata

This class can be used to control the rendering of the page on login successful or failure


### Parameters

```python
class EndpointMetadata(
    endpoint: str,
    success_html: typing.Optional[bytes] = None,
    failure_html: typing.Optional[bytes] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `success_html` | `typing.Optional[bytes]` | |
| `failure_html` | `typing.Optional[bytes]` | |

## flytekit.clients.auth.auth_client.OAuthCallbackHandler

A simple wrapper around BaseHTTPServer.BaseHTTPRequestHandler that handles a callback URL that accepts an
authorization token.


### Parameters

```python
class OAuthCallbackHandler(
    request,
    client_address,
    server,
)
```
| Parameter | Type | Description |
|-|-|-|
| `request` |  | |
| `client_address` |  | |
| `server` |  | |

### Methods

| Method | Description |
|-|-|
| [`do_GET()`](#do_get) |  |
| [`handle_login()`](#handle_login) |  |


#### do_GET()

```python
def do_GET()
```
#### handle_login()

```python
def handle_login(
    data: dict,
)
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `dict` | |

## flytekit.clients.auth.auth_client.OAuthHTTPServer

A simple wrapper around the BaseHTTPServer.HTTPServer implementation that binds an authorization_client for handling
authorization code callbacks.


### Parameters

```python
class OAuthHTTPServer(
    server_address: typing.Tuple[str, int],
    remote_metadata: EndpointMetadata,
    request_handler_class: typing.Type[_BaseHTTPServer.BaseHTTPRequestHandler],
    bind_and_activate: bool = True,
    redirect_path: str = None,
    queue: Queue = None,
)
```
Constructor.  May be extended, do not override.


| Parameter | Type | Description |
|-|-|-|
| `server_address` | `typing.Tuple[str, int]` | |
| `remote_metadata` | `EndpointMetadata` | |
| `request_handler_class` | `typing.Type[_BaseHTTPServer.BaseHTTPRequestHandler]` | |
| `bind_and_activate` | `bool` | |
| `redirect_path` | `str` | |
| `queue` | `Queue` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `redirect_path` | `str` |  |
| `remote_metadata` | `EndpointMetadata` |  |

### Methods

| Method | Description |
|-|-|
| [`handle_authorization_code()`](#handle_authorization_code) |  |
| [`handle_request()`](#handle_request) | Handle one request, possibly blocking. |


#### handle_authorization_code()

```python
def handle_authorization_code(
    auth_code: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `auth_code` | `str` | |

#### handle_request()

```python
def handle_request(
    queue: Queue = None,
) -> typing.Any
```
Handle one request, possibly blocking.

Respects self.timeout.


| Parameter | Type | Description |
|-|-|-|
| `queue` | `Queue` | |

