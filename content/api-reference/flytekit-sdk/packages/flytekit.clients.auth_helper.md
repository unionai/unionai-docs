---
title: flytekit.clients.auth_helper
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.auth_helper

## Directory

### Classes

| Class | Description |
|-|-|
| [`AuthenticationHTTPAdapter`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperauthenticationhttpadapter) | A custom HTTPAdapter that adds authentication headers to requests of a session. |
| [`RemoteClientConfigStore`](.././flytekit.clients.auth_helper#flytekitclientsauth_helperremoteclientconfigstore) | This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService. |

### Methods

| Method | Description |
|-|-|
| [`bootstrap_creds_from_server()`](#bootstrap_creds_from_server) | Retrieves the SSL cert from the remote and uses that. |
| [`get_authenticated_channel()`](#get_authenticated_channel) | Returns a new channel for the given config that is authenticated. |
| [`get_authenticator()`](#get_authenticator) | Returns a new authenticator based on the platform config. |
| [`get_channel()`](#get_channel) | Creates a new grpc. |
| [`get_proxy_authenticator()`](#get_proxy_authenticator) |  |
| [`get_session()`](#get_session) | Return a new session for the given platform config. |
| [`upgrade_channel_to_authenticated()`](#upgrade_channel_to_authenticated) | Given a grpc. |
| [`upgrade_channel_to_proxy_authenticated()`](#upgrade_channel_to_proxy_authenticated) | If activated in the platform config, given a grpc. |
| [`upgrade_session_to_proxy_authenticated()`](#upgrade_session_to_proxy_authenticated) | Given a requests. |
| [`wrap_exceptions_channel()`](#wrap_exceptions_channel) | Wraps the input channel with RetryExceptionWrapperInterceptor. |


## Methods

#### bootstrap_creds_from_server()

```python
def bootstrap_creds_from_server(
    endpoint: str,
) -> grpc.ChannelCredentials
```
Retrieves the SSL cert from the remote and uses that. should be used only if insecure-skip-verify


| Parameter | Type |
|-|-|
| `endpoint` | `str` |

#### get_authenticated_channel()

```python
def get_authenticated_channel(
    cfg: flytekit.configuration.PlatformConfig,
) -> grpc.Channel
```
Returns a new channel for the given config that is authenticated


| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` |

#### get_authenticator()

```python
def get_authenticator(
    cfg: flytekit.configuration.PlatformConfig,
    cfg_store: flytekit.clients.auth.authenticator.ClientConfigStore,
) -> flytekit.clients.auth.authenticator.Authenticator
```
Returns a new authenticator based on the platform config.


| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` |
| `cfg_store` | `flytekit.clients.auth.authenticator.ClientConfigStore` |

#### get_channel()

```python
def get_channel(
    cfg: flytekit.configuration.PlatformConfig,
    kwargs,
) -> n: grpc.Channel (secure / insecure)
```
Creates a new grpc.Channel given a platformConfig.
It is possible to pass additional options to the underlying channel. Examples for various options are as below

```python
get_channel(cfg=PlatformConfig(...))
```

> [!NOTE]
> Additional options to insecure / secure channel. Example `options` and `compression` refer to grpc guide

```python
get_channel(cfg=PlatformConfig(...), options=..., compression=...)
```


> [!NOTE]
> Create secure channel with custom `grpc.ssl_channel_credentials`

 ```python
get_channel(cfg=PlatformConfig(insecure=False,...), credentials=...)
```




| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` |
| `kwargs` | ``**kwargs`` |

#### get_proxy_authenticator()

```python
def get_proxy_authenticator(
    cfg: flytekit.configuration.PlatformConfig,
) -> flytekit.clients.auth.authenticator.Authenticator
```
| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` |

#### get_session()

```python
def get_session(
    cfg: flytekit.configuration.PlatformConfig,
    kwargs,
) -> requests.sessions.Session
```
Return a new session for the given platform config.


| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` |
| `kwargs` | ``**kwargs`` |

#### upgrade_channel_to_authenticated()

```python
def upgrade_channel_to_authenticated(
    cfg: flytekit.configuration.PlatformConfig,
    in_channel: grpc.Channel,
) -> n: grpc.Channel. New composite channel
```
Given a grpc.Channel, preferably a secure channel, it returns a composed channel that uses Interceptor to
perform an Oauth2.0 Auth flow


| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` |
| `in_channel` | `grpc.Channel` |

#### upgrade_channel_to_proxy_authenticated()

```python
def upgrade_channel_to_proxy_authenticated(
    cfg: flytekit.configuration.PlatformConfig,
    in_channel: grpc.Channel,
) -> n: grpc.Channel. New composite channel
```
If activated in the platform config, given a grpc.Channel, preferably a secure channel, it returns a composed
channel that uses Interceptor to perform authentication with a proxy in front of Flyte



| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` |
| `in_channel` | `grpc.Channel` |

#### upgrade_session_to_proxy_authenticated()

```python
def upgrade_session_to_proxy_authenticated(
    cfg: flytekit.configuration.PlatformConfig,
    session: requests.sessions.Session,
) -> n: requests.Session. New session with custom HTTPAdapter mounted
```
Given a requests.Session, it returns a new session that uses a custom HTTPAdapter to
perform authentication with a proxy in front of Flyte



| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` |
| `session` | `requests.sessions.Session` |

#### wrap_exceptions_channel()

```python
def wrap_exceptions_channel(
    cfg: flytekit.configuration.PlatformConfig,
    in_channel: grpc.Channel,
) -> n: grpc.Channel
```
Wraps the input channel with RetryExceptionWrapperInterceptor. This wrapper will cover all
exceptions and raise Exception from the Family flytekit.exceptions

> [!NOTE]
> This channel should be usually the outermost channel. This channel will raise a FlyteException



| Parameter | Type |
|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` |
| `in_channel` | `grpc.Channel` |

## flytekit.clients.auth_helper.AuthenticationHTTPAdapter

A custom HTTPAdapter that adds authentication headers to requests of a session.


```python
class AuthenticationHTTPAdapter(
    authenticator,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `authenticator` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`add_auth_header()`](#add_auth_header) | Adds authentication headers to the request. |
| [`add_headers()`](#add_headers) | Add any headers needed by the connection. |
| [`build_connection_pool_key_attributes()`](#build_connection_pool_key_attributes) | Build the PoolKey attributes used by urllib3 to return a connection. |
| [`build_response()`](#build_response) | Builds a :class:`Response <requests. |
| [`cert_verify()`](#cert_verify) | Verify a SSL certificate. |
| [`close()`](#close) | Disposes of any internal state. |
| [`get_connection()`](#get_connection) | DEPRECATED: Users should move to `get_connection_with_tls_context`. |
| [`get_connection_with_tls_context()`](#get_connection_with_tls_context) | Returns a urllib3 connection for the given request and TLS settings. |
| [`init_poolmanager()`](#init_poolmanager) | Initializes a urllib3 PoolManager. |
| [`proxy_headers()`](#proxy_headers) | Returns a dictionary of the headers to add to any request sent. |
| [`proxy_manager_for()`](#proxy_manager_for) | Return urllib3 ProxyManager for the given proxy. |
| [`request_url()`](#request_url) | Obtain the url to use when making the final request. |
| [`send()`](#send) | Sends the request with added authentication headers. |


#### add_auth_header()

```python
def add_auth_header(
    request,
)
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
)
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
)
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
) -> e: requests.Response
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
)
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
) -> e: urllib3.ConnectionPool
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
) -> e:
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
)
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
) -> e: dict
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
) -> e: urllib3.ProxyManager
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
) -> e: str
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
) -> n: The response object.
```
Sends the request with added authentication headers.
If the response returns a 401 status code, refreshes the credentials and retries the request.


| Parameter | Type |
|-|-|
| `request` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

## flytekit.clients.auth_helper.RemoteClientConfigStore

This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService


```python
class RemoteClientConfigStore(
    secure_channel: grpc.Channel,
)
```
| Parameter | Type |
|-|-|
| `secure_channel` | `grpc.Channel` |

### Methods

| Method | Description |
|-|-|
| [`get_client_config()`](#get_client_config) | Retrieves the ClientConfig from the given grpc. |


#### get_client_config()

```python
def get_client_config()
```
Retrieves the ClientConfig from the given grpc.Channel assuming  AuthMetadataService is available


