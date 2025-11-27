---
title: AuthUnaryInterceptor
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# AuthUnaryInterceptor

**Package:** `flytekit.clients.grpc_utils.auth_interceptor`

This Interceptor can be used to automatically add Auth Metadata for every call - lazily in case authentication
is needed.


```python
class AuthUnaryInterceptor(
    get_authenticator: typing.Callable[[], flytekit.clients.auth.authenticator.Authenticator],
)
```
| Parameter | Type | Description |
|-|-|-|
| `get_authenticator` | `typing.Callable[[], flytekit.clients.auth.authenticator.Authenticator]` | |

## Methods

| Method | Description |
|-|-|
| [`intercept_unary_stream()`](#intercept_unary_stream) | Handles a stream call and adds authentication metadata if needed. |
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts unary calls and adds auth metadata if available. |


### intercept_unary_stream()

```python
def intercept_unary_stream(
    continuation,
    client_call_details,
    request,
)
```
Handles a stream call and adds authentication metadata if needed


| Parameter | Type | Description |
|-|-|-|
| `continuation` |  | |
| `client_call_details` |  | |
| `request` |  | |

### intercept_unary_unary()

```python
def intercept_unary_unary(
    continuation: typing.Callable,
    client_call_details: grpc.ClientCallDetails,
    request: typing.Any,
)
```
Intercepts unary calls and adds auth metadata if available. On Unauthenticated, resets the token and refreshes
and then retries with the new token


| Parameter | Type | Description |
|-|-|-|
| `continuation` | `typing.Callable` | |
| `client_call_details` | `grpc.ClientCallDetails` | |
| `request` | `typing.Any` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `authenticator` |  |  |

