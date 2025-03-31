---
title: flytekit.clients.grpc_utils.auth_interceptor
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clients.grpc_utils.auth_interceptor

## Directory

### Classes

| Class | Description |
|-|-|
| [`AuthUnaryInterceptor`](.././flytekit.clients.grpc_utils.auth_interceptor#flytekitclientsgrpc_utilsauth_interceptorauthunaryinterceptor) | This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication. |
| [`Authenticator`](.././flytekit.clients.grpc_utils.auth_interceptor#flytekitclientsgrpc_utilsauth_interceptorauthenticator) | Base authenticator for all authentication flows. |

## flytekit.clients.grpc_utils.auth_interceptor.AuthUnaryInterceptor

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

## flytekit.clients.grpc_utils.auth_interceptor.Authenticator

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
