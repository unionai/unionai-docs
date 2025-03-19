---
title: flytekit.clients.grpc_utils.wrap_exception_interceptor
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clients.grpc_utils.wrap_exception_interceptor

## Directory

### Classes

| Class | Description |
|-|-|
| [`RetryExceptionWrapperInterceptor`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorretryexceptionwrapperinterceptor) | Affords intercepting unary-unary invocations. |

### Errors

* [`FlyteAuthenticationException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteauthenticationexception)
* [`FlyteEntityAlreadyExistsException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteentityalreadyexistsexception)
* [`FlyteEntityNotExistException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteentitynotexistexception)
* [`FlyteException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteexception)
* [`FlyteInvalidInputException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteinvalidinputexception)
* [`FlyteSystemException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflytesystemexception)
* [`FlyteSystemUnavailableException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflytesystemunavailableexception)

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteAuthenticationException

Assertion failed.


```python
def FlyteAuthenticationException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteEntityAlreadyExistsException

Assertion failed.


```python
def FlyteEntityAlreadyExistsException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteEntityNotExistException

Assertion failed.


```python
def FlyteEntityNotExistException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteException

Common base class for all non-exit exceptions.


```python
def FlyteException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteInvalidInputException

Common base class for all non-exit exceptions.


```python
def FlyteInvalidInputException(
    request: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `request` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteSystemException

Common base class for all non-exit exceptions.


```python
def FlyteSystemException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteSystemUnavailableException

Common base class for all non-exit exceptions.


```python
def FlyteSystemUnavailableException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.RetryExceptionWrapperInterceptor

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

