---
title: flytekit.clients.auth_helper
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clients.auth_helper

## Directory

### Classes

| Class | Description |
|-|-|
| [`AuthMetadataServiceStub`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperauthmetadataservicestub) | The following defines an RPC service that is also served over HTTP via grpc-gateway. |
| [`AuthType`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperauthtype) | Create a collection of name/value pairs. |
| [`AuthUnaryInterceptor`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperauthunaryinterceptor) | This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication. |
| [`AuthenticationHTTPAdapter`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperauthenticationhttpadapter) | A custom HTTPAdapter that adds authentication headers to requests of a session. |
| [`Authenticator`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperauthenticator) | Base authenticator for all authentication flows. |
| [`ClientConfig`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperclientconfig) | Client Configuration that is needed by the authenticator. |
| [`ClientConfigStore`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperclientconfigstore) | Client Config store retrieve client config. |
| [`ClientCredentialsAuthenticator`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperclientcredentialsauthenticator) | This Authenticator uses ClientId and ClientSecret to authenticate. |
| [`CommandAuthenticator`](.././flytekit.clients.auth_helper#flytekitclientsauth_helpercommandauthenticator) | This Authenticator retrieves access_token using the provided command. |
| [`DefaultMetadataInterceptor`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperdefaultmetadatainterceptor) | Affords intercepting unary-unary invocations. |
| [`DeviceCodeAuthenticator`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperdevicecodeauthenticator) | This Authenticator implements the Device Code authorization flow useful for headless user authentication. |
| [`HTTPStatus`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperhttpstatus) | HTTP status codes and reason phrases. |
| [`OAuth2MetadataRequest`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperoauth2metadatarequest) | A ProtocolMessage. |
| [`PKCEAuthenticator`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperpkceauthenticator) | This Authenticator encapsulates the entire PKCE flow and automatically opens a browser window for login. |
| [`PlatformConfig`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperplatformconfig) | This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`PublicClientAuthConfigRequest`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperpublicclientauthconfigrequest) | A ProtocolMessage. |
| [`RemoteClientConfigStore`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperremoteclientconfigstore) | This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService. |
| [`RetryExceptionWrapperInterceptor`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperretryexceptionwrapperinterceptor) | Affords intercepting unary-unary invocations. |

## flytekit.clients.auth_helper.AuthMetadataServiceStub

The following defines an RPC service that is also served over HTTP via grpc-gateway.
Standard response codes for both are defined here: https://github.com/grpc-ecosystem/grpc-gateway/blob/master/runtime/errors.go
RPCs defined in this service must be anonymously accessible.


```python
def AuthMetadataServiceStub(
    channel,
):
```
Constructor.



| Parameter | Type |
|-|-|
| `channel` |  |

## flytekit.clients.auth_helper.AuthType

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## flytekit.clients.auth_helper.AuthUnaryInterceptor

This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication
is needed.


```python
def AuthUnaryInterceptor(
    get_authenticator: typing.Callable[[], flytekit.clients.auth.authenticator.Authenticator],
):
```
| Parameter | Type |
|-|-|
| `get_authenticator` | `typing.Callable[[], flytekit.clients.auth.authenticator.Authenticator]` |

### Methods

| Method | Description |
|-|-|
| [`intercept_unary_stream()`](#intercept_unary_stream) | Handles a stream call and adds authentication metadata if needed |
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts unary calls and adds auth metadata if available |


#### intercept_unary_stream()

```python
def intercept_unary_stream(
    continuation,
    client_call_details,
    request,
):
```
Handles a stream call and adds authentication metadata if needed


| Parameter | Type |
|-|-|
| `continuation` |  |
| `client_call_details` |  |
| `request` |  |

#### intercept_unary_unary()

```python
def intercept_unary_unary(
    continuation: typing.Callable,
    client_call_details: grpc.ClientCallDetails,
    request: typing.Any,
):
```
Intercepts unary calls and adds auth metadata if available. On Unauthenticated, resets the token and refreshes
and then retries with the new token


| Parameter | Type |
|-|-|
| `continuation` | `typing.Callable` |
| `client_call_details` | `grpc.ClientCallDetails` |
| `request` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| authenticator |  |  |

## flytekit.clients.auth_helper.AuthenticationHTTPAdapter

A custom HTTPAdapter that adds authentication headers to requests of a session.


```python
def AuthenticationHTTPAdapter(
    authenticator,
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `authenticator` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`add_auth_header()`](#add_auth_header) | Adds authentication headers to the request |
| [`add_headers()`](#add_headers) | Add any headers needed by the connection |
| [`build_connection_pool_key_attributes()`](#build_connection_pool_key_attributes) | Build the PoolKey attributes used by urllib3 to return a connection |
| [`build_response()`](#build_response) | Builds a :class:`Response <requests |
| [`cert_verify()`](#cert_verify) | Verify a SSL certificate |
| [`close()`](#close) | Disposes of any internal state |
| [`get_connection()`](#get_connection) | DEPRECATED: Users should move to `get_connection_with_tls_context` |
| [`get_connection_with_tls_context()`](#get_connection_with_tls_context) | Returns a urllib3 connection for the given request and TLS settings |
| [`init_poolmanager()`](#init_poolmanager) | Initializes a urllib3 PoolManager |
| [`proxy_headers()`](#proxy_headers) | Returns a dictionary of the headers to add to any request sent |
| [`proxy_manager_for()`](#proxy_manager_for) | Return urllib3 ProxyManager for the given proxy |
| [`request_url()`](#request_url) | Obtain the url to use when making the final request |
| [`send()`](#send) | Sends the request with added authentication headers |


#### add_auth_header()

```python
def add_auth_header(
    request,
):
```
Adds authentication headers to the request.


| Parameter | Type |
|-|-|
| `request` |  |

#### add_headers()

```python
def add_headers(
    request,
    kwargs,
):
```
Add any headers needed by the connection. As of v2.0 this does
nothing by default, but is left for overriding by users that subclass
the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

This should not be called from user code, and is only exposed for use
when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.



| Parameter | Type |
|-|-|
| `request` |  |
| `kwargs` | ``**kwargs`` |

#### build_connection_pool_key_attributes()

```python
def build_connection_pool_key_attributes(
    request,
    verify,
    cert,
):
```
Build the PoolKey attributes used by urllib3 to return a connection.

This looks at the PreparedRequest, the user-specified verify value,
and the value of the cert parameter to determine what PoolKey values
to use to select a connection from a given urllib3 Connection Pool.

The SSL related pool key arguments are not consistently set. As of
this writing, use the following to determine what keys may be in that
dictionary:

* If ``verify`` is ``True``, ``"ssl_context"`` will be set and will be the
default Requests SSL Context
* If ``verify`` is ``False``, ``"ssl_context"`` will not be set but
``"cert_reqs"`` will be set
* If ``verify`` is a string, (i.e., it is a user-specified trust bundle)
``"ca_certs"`` will be set if the string is not a directory recognized
by :py:func:`os.path.isdir`, otherwise ``"ca_certs_dir"`` will be
set.
* If ``"cert"`` is specified, ``"cert_file"`` will always be set. If
``"cert"`` is a tuple with a second item, ``"key_file"`` will also
be present

To override these settings, one may subclass this class, call this
method and use the above logic to change parameters as desired. For
example, if one wishes to use a custom :py:class:`ssl.SSLContext` one
must both set ``"ssl_context"`` and based on what else they require,
alter the other keys to ensure the desired behaviour.



| Parameter | Type |
|-|-|
| `request` |  |
| `verify` |  |
| `cert` |  |

#### build_response()

```python
def build_response(
    req,
    resp,
):
```
Builds a :class:`Response <requests.Response>` object from a urllib3
response. This should not be called from user code, and is only exposed
for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`



| Parameter | Type |
|-|-|
| `req` |  |
| `resp` |  |

#### cert_verify()

```python
def cert_verify(
    conn,
    url,
    verify,
    cert,
):
```
Verify a SSL certificate. This method should not be called from user
code, and is only exposed for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.



| Parameter | Type |
|-|-|
| `conn` |  |
| `url` |  |
| `verify` |  |
| `cert` |  |

#### close()

```python
def close()
```
Disposes of any internal state.

Currently, this closes the PoolManager and any active ProxyManager,
which closes any pooled connections.


#### get_connection()

```python
def get_connection(
    url,
    proxies,
):
```
DEPRECATED: Users should move to `get_connection_with_tls_context`
for all subclasses of HTTPAdapter using Requests>=2.32.2.

Returns a urllib3 connection for the given URL. This should not be
called from user code, and is only exposed for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.



| Parameter | Type |
|-|-|
| `url` |  |
| `proxies` |  |

#### get_connection_with_tls_context()

```python
def get_connection_with_tls_context(
    request,
    verify,
    proxies,
    cert,
):
```
Returns a urllib3 connection for the given request and TLS settings.
This should not be called from user code, and is only exposed for use
when subclassing the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.



| Parameter | Type |
|-|-|
| `request` |  |
| `verify` |  |
| `proxies` |  |
| `cert` |  |

#### init_poolmanager()

```python
def init_poolmanager(
    connections,
    maxsize,
    block,
    pool_kwargs,
):
```
Initializes a urllib3 PoolManager.

This method should not be called from user code, and is only
exposed for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.



| Parameter | Type |
|-|-|
| `connections` |  |
| `maxsize` |  |
| `block` |  |
| `pool_kwargs` |  |

#### proxy_headers()

```python
def proxy_headers(
    proxy,
):
```
Returns a dictionary of the headers to add to any request sent
through a proxy. This works with urllib3 magic to ensure that they are
correctly sent to the proxy, rather than in a tunnelled request if
CONNECT is being used.

This should not be called from user code, and is only exposed for use
when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.



| Parameter | Type |
|-|-|
| `proxy` |  |

#### proxy_manager_for()

```python
def proxy_manager_for(
    proxy,
    proxy_kwargs,
):
```
Return urllib3 ProxyManager for the given proxy.

This method should not be called from user code, and is only
exposed for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.



| Parameter | Type |
|-|-|
| `proxy` |  |
| `proxy_kwargs` |  |

#### request_url()

```python
def request_url(
    request,
    proxies,
):
```
Obtain the url to use when making the final request.

If the message is being sent through a HTTP proxy, the full URL has to
be used. Otherwise, we should only use the path portion of the URL.

This should not be called from user code, and is only exposed for use
when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.



| Parameter | Type |
|-|-|
| `request` |  |
| `proxies` |  |

#### send()

```python
def send(
    request,
    args,
    kwargs,
):
```
Sends the request with added authentication headers.
If the response returns a 401 status code, refreshes the credentials and retries the request.


| Parameter | Type |
|-|-|
| `request` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

## flytekit.clients.auth_helper.Authenticator

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
## flytekit.clients.auth_helper.ClientConfig

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

## flytekit.clients.auth_helper.ClientConfigStore

Client Config store retrieve client config. this can be done in multiple ways


### Methods

| Method | Description |
|-|-|
| [`get_client_config()`](#get_client_config) | None |


#### get_client_config()

```python
def get_client_config()
```
## flytekit.clients.auth_helper.ClientCredentialsAuthenticator

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


## flytekit.clients.auth_helper.CommandAuthenticator

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


## flytekit.clients.auth_helper.DefaultMetadataInterceptor

Affords intercepting unary-unary invocations.


### Methods

| Method | Description |
|-|-|
| [`intercept_unary_stream()`](#intercept_unary_stream) | Handles a stream call and inject default metadata |
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts unary calls and inject default metadata |


#### intercept_unary_stream()

```python
def intercept_unary_stream(
    continuation: typing.Callable,
    client_call_details: grpc.ClientCallDetails,
    request: typing.Any,
):
```
Handles a stream call and inject default metadata


| Parameter | Type |
|-|-|
| `continuation` | `typing.Callable` |
| `client_call_details` | `grpc.ClientCallDetails` |
| `request` | `typing.Any` |

#### intercept_unary_unary()

```python
def intercept_unary_unary(
    continuation: typing.Callable,
    client_call_details: grpc.ClientCallDetails,
    request: typing.Any,
):
```
Intercepts unary calls and inject default metadata


| Parameter | Type |
|-|-|
| `continuation` | `typing.Callable` |
| `client_call_details` | `grpc.ClientCallDetails` |
| `request` | `typing.Any` |

## flytekit.clients.auth_helper.DeviceCodeAuthenticator

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
## flytekit.clients.auth_helper.HTTPStatus

HTTP status codes and reason phrases

Status codes from the following RFCs are all observed:

* RFC 7231: Hypertext Transfer Protocol (HTTP/1.1), obsoletes 2616
* RFC 6585: Additional HTTP Status Codes
* RFC 3229: Delta encoding in HTTP
* RFC 4918: HTTP Extensions for WebDAV, obsoletes 2518
* RFC 5842: Binding Extensions to WebDAV
* RFC 7238: Permanent Redirect
* RFC 2295: Transparent Content Negotiation in HTTP
* RFC 2774: An HTTP Extension Framework
* RFC 7725: An HTTP Status Code to Report Legal Obstacles
* RFC 7540: Hypertext Transfer Protocol Version 2 (HTTP/2)
* RFC 2324: Hyper Text Coffee Pot Control Protocol (HTCPCP/1.0)
* RFC 8297: An HTTP Status Code for Indicating Hints
* RFC 8470: Using Early Data in HTTP


```python
def HTTPStatus(
    args,
    kwds,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwds` |  |

## flytekit.clients.auth_helper.OAuth2MetadataRequest

A ProtocolMessage


## flytekit.clients.auth_helper.PKCEAuthenticator

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
## flytekit.clients.auth_helper.PlatformConfig

This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically).



```python
def PlatformConfig(
    endpoint: str,
    insecure: bool,
    insecure_skip_verify: bool,
    ca_cert_file_path: typing.Optional[str],
    console_endpoint: typing.Optional[str],
    command: typing.Optional[typing.List[str]],
    proxy_command: typing.Optional[typing.List[str]],
    client_id: typing.Optional[str],
    client_credentials_secret: typing.Optional[str],
    scopes: List[str],
    auth_mode: AuthType,
    audience: typing.Optional[str],
    rpc_retries: int,
    http_proxy_url: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `insecure_skip_verify` | `bool` |
| `ca_cert_file_path` | `typing.Optional[str]` |
| `console_endpoint` | `typing.Optional[str]` |
| `command` | `typing.Optional[typing.List[str]]` |
| `proxy_command` | `typing.Optional[typing.List[str]]` |
| `client_id` | `typing.Optional[str]` |
| `client_credentials_secret` | `typing.Optional[str]` |
| `scopes` | `List[str]` |
| `auth_mode` | `AuthType` |
| `audience` | `typing.Optional[str]` |
| `rpc_retries` | `int` |
| `http_proxy_url` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from Config file, and overrides from Environment variables |
| [`for_endpoint()`](#for_endpoint) | None |


#### auto()

```python
def auto(
    config_file: typing.Optional[typing.Union[str, ConfigFile]],
):
```
Reads from Config file, and overrides from Environment variables. Refer to ConfigEntry for details


| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[typing.Union[str, ConfigFile]]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
):
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |

## flytekit.clients.auth_helper.PublicClientAuthConfigRequest

A ProtocolMessage


## flytekit.clients.auth_helper.RemoteClientConfigStore

This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService


```python
def RemoteClientConfigStore(
    secure_channel: grpc.Channel,
):
```
| Parameter | Type |
|-|-|
| `secure_channel` | `grpc.Channel` |

### Methods

| Method | Description |
|-|-|
| [`get_client_config()`](#get_client_config) | Retrieves the ClientConfig from the given grpc |


#### get_client_config()

```python
def get_client_config()
```
Retrieves the ClientConfig from the given grpc.Channel assuming  AuthMetadataService is available


## flytekit.clients.auth_helper.RetryExceptionWrapperInterceptor

Affords intercepting unary-unary invocations.


```python
def RetryExceptionWrapperInterceptor(
    max_retries: int,
):
```
| Parameter | Type |
|-|-|
| `max_retries` | `int` |

### Methods

| Method | Description |
|-|-|
| [`intercept_unary_stream()`](#intercept_unary_stream) | Intercepts a unary-stream invocation |
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts a unary-unary invocation asynchronously |


#### intercept_unary_stream()

```python
def intercept_unary_stream(
    continuation,
    client_call_details,
    request,
):
```
Intercepts a unary-stream invocation.



| Parameter | Type |
|-|-|
| `continuation` |  |
| `client_call_details` |  |
| `request` |  |

#### intercept_unary_unary()

```python
def intercept_unary_unary(
    continuation,
    client_call_details,
    request,
):
```
Intercepts a unary-unary invocation asynchronously.



| Parameter | Type |
|-|-|
| `continuation` |  |
| `client_call_details` |  |
| `request` |  |

