---
title: flytekit.clients.grpc_utils.wrap_exception_interceptor
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.grpc_utils.wrap_exception_interceptor

## Directory

### Classes

| Class | Description |
|-|-|
| [`RetryExceptionWrapperInterceptor`](.././flytekit.clients.grpc_utils.wrap_exception_interceptor#flytekitclientsgrpc_utilswrap_exception_interceptorretryexceptionwrapperinterceptor) | Affords intercepting unary-unary invocations. |

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

