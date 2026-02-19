---
title: flytekit.clients.auth_helper
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.auth_helper

## Directory

### Classes

| Class | Description |
|-|-|
| [`AuthenticationHTTPAdapter`](../flytekit.clients.auth_helper/authenticationhttpadapter) | A custom HTTPAdapter that adds authentication headers to requests of a session. |
| [`RemoteClientConfigStore`](../flytekit.clients.auth_helper/remoteclientconfigstore) | This class implements the ClientConfigStore that is served by the Flyte Server, that implements AuthMetadataService. |

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


| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | |
| `cfg_store` | `flytekit.clients.auth.authenticator.ClientConfigStore` | |

#### get_channel()

```python
def get_channel(
    cfg: flytekit.configuration.PlatformConfig,
    kwargs,
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
| `kwargs` | `**kwargs` | Optional arguments to be passed to channel method. Refer to usage example above :return: grpc.Channel (secure / insecure) |

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
    kwargs,
) -> requests.sessions.Session
```
Return a new session for the given platform config.


| Parameter | Type | Description |
|-|-|-|
| `cfg` | `flytekit.configuration.PlatformConfig` | |
| `kwargs` | `**kwargs` | |

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
| `in_channel` | `grpc.Channel` | grpc.Channel Precreated channel :return: grpc.Channel. New composite channel |

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
| `in_channel` | `grpc.Channel` | grpc.Channel Precreated channel :return: grpc.Channel. New composite channel |

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
| `session` | `requests.sessions.Session` | requests.Session Precreated session :return: requests.Session. New session with custom HTTPAdapter mounted |

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
| `in_channel` | `grpc.Channel` | grpc.Channel :return: grpc.Channel |

