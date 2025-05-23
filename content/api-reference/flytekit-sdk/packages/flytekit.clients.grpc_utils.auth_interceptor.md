---
title: flytekit.clients.grpc_utils.auth_interceptor
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.grpc_utils.auth_interceptor

## Directory

### Classes

| Class | Description |
|-|-|
| [`AuthUnaryInterceptor`](.././flytekit.clients.grpc_utils.auth_interceptor#flytekitclientsgrpc_utilsauth_interceptorauthunaryinterceptor) | This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication. |

## flytekit.clients.grpc_utils.auth_interceptor.AuthUnaryInterceptor

This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication
is needed.


```python
class AuthUnaryInterceptor(
    get_authenticator: typing.Callable[[], flytekit.clients.auth.authenticator.Authenticator],
)
```
| Parameter | Type |
|-|-|
| `get_authenticator` | `typing.Callable[[], flytekit.clients.auth.authenticator.Authenticator]` |

### Methods

| Method | Description |
|-|-|
| [`intercept_unary_stream()`](#intercept_unary_stream) | Handles a stream call and adds authentication metadata if needed. |
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts unary calls and adds auth metadata if available. |


#### intercept_unary_stream()

```python
def intercept_unary_stream(
    continuation,
    client_call_details,
    request,
)
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
)
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
| `authenticator` |  |  |

