---
title: flytekit.clients.grpc_utils.default_metadata_interceptor
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.grpc_utils.default_metadata_interceptor

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultMetadataInterceptor`](.././flytekit.clients.grpc_utils.default_metadata_interceptor#flytekitclientsgrpc_utilsdefault_metadata_interceptordefaultmetadatainterceptor) | Affords intercepting unary-unary invocations. |

## flytekit.clients.grpc_utils.default_metadata_interceptor.DefaultMetadataInterceptor

Affords intercepting unary-unary invocations.


### Methods

| Method | Description |
|-|-|
| [`intercept_unary_stream()`](#intercept_unary_stream) | Handles a stream call and inject default metadata. |
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts unary calls and inject default metadata. |


#### intercept_unary_stream()

```python
def intercept_unary_stream(
    continuation: typing.Callable,
    client_call_details: grpc.ClientCallDetails,
    request: typing.Any,
)
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
)
```
Intercepts unary calls and inject default metadata


| Parameter | Type |
|-|-|
| `continuation` | `typing.Callable` |
| `client_call_details` | `grpc.ClientCallDetails` |
| `request` | `typing.Any` |

