---
title: flytekit.clients.auth_helper
version: 1.16.28
variants: +flyte +union
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
| [`register_authenticator_plugin()`](#register_authenticator_plugin) | Register an authenticator factory by name. |
| [`upgrade_channel_to_authenticated()`](#upgrade_channel_to_authenticated) | Given a grpc. |
| [`upgrade_channel_to_proxy_authenticated()`](#upgrade_channel_to_proxy_authenticated) | If activated in the platform config, given a grpc. |
| [`upgrade_session_to_proxy_authenticated()`](#upgrade_session_to_proxy_authenticated) | Given a requests. |
| [`wrap_exceptions_channel()`](#wrap_exceptions_channel) | Wraps the input channel with RetryExceptionWrapperInterceptor. |


### Variables

| Property | Type | Description |
|-|-|-|
| `AUTH_ENTRY_POINT_GROUP` | `str` |  |

## Methods

#### bootstrap_creds_from_server()

```python
def bootstrap_creds_from_server(
    endpoint: str,
) -> grpc.ChannelCredentials
```
Retrieves the SSL cert from the remote and uses that. should be used only if insecure-skip-verify


| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |

#### get_authenticated_channel()

```python
def get_authenticated_channel(
    cfg: flytekit.configuration.PlatformConfig,
) -> grpc.Channel
```
Returns a new channel for the given config that is authenticated


| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | |

#### get_authenticator()

```python
def get_authenticator(
    cfg: flytekit.configuration.PlatformConfig,
    cfg_store: flytekit.clients.auth.authenticator.ClientConfigStore,
) -> flytekit.clients.auth.authenticator.Authenticator
```
Returns a new authenticator based on the platform config.

Built-in auth types (PKCE, ClientSecret, ExternalCommand, DeviceFlow) are
tried first.  If ``auth_mode`` is a string that does not match any built-in
type, the function falls back to entry-point discovery: any installed
package can register an authenticator factory under the
``flytekit.auth`` entry point group and it will be loaded automatically.


| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | |
| `cfg_store` | `flytekit.clients.auth.authenticator.ClientConfigStore` | |

#### get_channel()

```python
def get_channel(
    cfg: flytekit.configuration.PlatformConfig,
    **kwargs,
) -> grpc.Channel
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




| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | PlatformConfig |
| `**kwargs` |  | Optional arguments to be passed to channel method. Refer to usage example above |

**Returns:** grpc.Channel (secure / insecure)

#### get_proxy_authenticator()

```python
def get_proxy_authenticator(
    cfg: flytekit.configuration.PlatformConfig,
) -> flytekit.clients.auth.authenticator.Authenticator
```
| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | |

#### get_session()

```python
def get_session(
    cfg: flytekit.configuration.PlatformConfig,
    **kwargs,
) -> requests.sessions.Session
```
Return a new session for the given platform config.


| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | |
| `**kwargs` |  | |

#### register_authenticator_plugin()

```python
def register_authenticator_plugin(
    name: str,
    factory: typing.Callable[[ForwardRef('PlatformConfig'), flytekit.clients.auth.authenticator.ClientConfigStore], flytekit.clients.auth.authenticator.Authenticator],
)
```
Register an authenticator factory by name.

This is the primary registration mechanism and works in every environment
(pip, Bazel, mono-repo vendoring, etc.).  Entry-point discovery is attempted
as a fallback when no explicit registration exists.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `factory` | `typing.Callable[[ForwardRef('PlatformConfig'), flytekit.clients.auth.authenticator.ClientConfigStore], flytekit.clients.auth.authenticator.Authenticator]` | |

#### upgrade_channel_to_authenticated()

```python
def upgrade_channel_to_authenticated(
    cfg: flytekit.configuration.PlatformConfig,
    in_channel: grpc.Channel,
) -> grpc.Channel
```
Given a grpc.Channel, preferably a secure channel, it returns a composed channel that uses Interceptor to
perform an Oauth2.0 Auth flow


| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | PlatformConfig |
| `in_channel` | `grpc.Channel` | grpc.Channel Precreated channel |

**Returns:** grpc.Channel. New composite channel

#### upgrade_channel_to_proxy_authenticated()

```python
def upgrade_channel_to_proxy_authenticated(
    cfg: flytekit.configuration.PlatformConfig,
    in_channel: grpc.Channel,
) -> grpc.Channel
```
If activated in the platform config, given a grpc.Channel, preferably a secure channel, it returns a composed
channel that uses Interceptor to perform authentication with a proxy in front of Flyte



| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | PlatformConfig |
| `in_channel` | `grpc.Channel` | grpc.Channel Precreated channel |

**Returns:** grpc.Channel. New composite channel

#### upgrade_session_to_proxy_authenticated()

```python
def upgrade_session_to_proxy_authenticated(
    cfg: flytekit.configuration.PlatformConfig,
    session: requests.sessions.Session,
) -> requests.sessions.Session
```
Given a requests.Session, it returns a new session that uses a custom HTTPAdapter to
perform authentication with a proxy in front of Flyte



| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | PlatformConfig |
| `session` | `requests.sessions.Session` | requests.Session Precreated session |

**Returns:** requests.Session. New session with custom HTTPAdapter mounted

#### wrap_exceptions_channel()

```python
def wrap_exceptions_channel(
    cfg: flytekit.configuration.PlatformConfig,
    in_channel: grpc.Channel,
) -> grpc.Channel
```
Wraps the input channel with RetryExceptionWrapperInterceptor. This wrapper will cover all
exceptions and raise Exception from the Family flytekit.exceptions

> [!NOTE]
> This channel should be usually the outermost channel. This channel will raise a FlyteException



| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | PlatformConfig |
| `in_channel` | `grpc.Channel` | grpc.Channel |

**Returns:** grpc.Channel

## flytekit.clients.auth_helper.AuthenticationHTTPAdapter

A custom HTTPAdapter that adds authentication headers to requests of a session.


### Parameters

```python
class AuthenticationHTTPAdapter(
    authenticator,
    *args,
    **kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `authenticator` |  | |
| `*args` |  | |
| `**kwargs` |  | |

### Methods

| Method | Description |
|-|-|
| [`add_auth_header()`](#add_auth_header) | Adds authentication headers to the request. |
| [`send()`](#send) | Sends the request with added authentication headers. |


#### add_auth_header()

```python
def add_auth_header(
    request,
)
```
Adds authentication headers to the request.


| Parameter | Type | Description |
|-|-|-|
| `request` |  | The request object to add headers to. |

#### send()

```python
def send(
    request,
    *args,
    **kwargs,
)
```
Sends the request with added authentication headers.
If the response returns a 401 status code, refreshes the credentials and retries the request.


| Parameter | Type | Description |
|-|-|-|
| `request` |  | The request object to send. |
| `*args` |  | |
| `**kwargs` |  | |

**Returns:** The response object.

## flytekit.clients.auth_helper.RemoteClientConfigStore

This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService


### Parameters

```python
class RemoteClientConfigStore(
    secure_channel: grpc.Channel,
)
```
| Parameter | Type | Description |
|-|-|-|
| `secure_channel` | `grpc.Channel` | |

### Methods

| Method | Description |
|-|-|
| [`get_client_config()`](#get_client_config) | Retrieves the ClientConfig from the given grpc. |


#### get_client_config()

```python
def get_client_config()
```
Retrieves the ClientConfig from the given grpc.Channel assuming  AuthMetadataService is available


