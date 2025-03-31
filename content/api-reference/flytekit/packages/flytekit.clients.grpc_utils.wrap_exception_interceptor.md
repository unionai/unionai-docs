---
title: flytekit.clients.grpc_utils.wrap_exception_interceptor
version: 0.1.dev2175+gcd6bd01.d20250325
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

| Exception | Description |
|-|-|
| [`FlyteAuthenticationException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteauthenticationexception) | Assertion failed. |
| [`FlyteEntityAlreadyExistsException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteentityalreadyexistsexception) | Assertion failed. |
| [`FlyteEntityNotExistException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteentitynotexistexception) | Assertion failed. |
| [`FlyteException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteexception) | Common base class for all non-exit exceptions. |
| [`FlyteInvalidInputException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflyteinvalidinputexception) | Common base class for all non-exit exceptions. |
| [`FlyteSystemException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflytesystemexception) | Common base class for all non-exit exceptions. |
| [`FlyteSystemUnavailableException`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorflytesystemunavailableexception) | Common base class for all non-exit exceptions. |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteAuthenticationException

Assertion failed.


```python
class FlyteAuthenticationException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteEntityAlreadyExistsException

Assertion failed.


```python
class FlyteEntityAlreadyExistsException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteEntityNotExistException

Assertion failed.


```python
class FlyteEntityNotExistException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteException

Common base class for all non-exit exceptions.


```python
class FlyteException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteInvalidInputException

Common base class for all non-exit exceptions.


```python
class FlyteInvalidInputException(
    request: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `request` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteSystemException

Common base class for all non-exit exceptions.


```python
class FlyteSystemException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.FlyteSystemUnavailableException

Common base class for all non-exit exceptions.


```python
class FlyteSystemUnavailableException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clients.grpc_utils.wrap_exception_interceptor.RetryExceptionWrapperInterceptor

Affords intercepting unary-unary invocations.


```python
class RetryExceptionWrapperInterceptor(
    max_retries: int,
)
```
| Parameter | Type |
|-|-|
| `max_retries` | `int` |

### Methods

| Method | Description |
|-|-|
| [`intercept_unary_stream()`](#intercept_unary_stream) | Intercepts a unary-stream invocation. |
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts a unary-unary invocation asynchronously. |


#### intercept_unary_stream()

```python
def intercept_unary_stream(
    continuation,
    client_call_details,
    request,
)
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
)
```
Intercepts a unary-unary invocation asynchronously.



| Parameter | Type |
|-|-|
| `continuation` |  |
| `client_call_details` |  |
| `request` |  |

