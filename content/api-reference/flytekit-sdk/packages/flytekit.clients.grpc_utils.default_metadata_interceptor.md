---
title: flytekit.clients.grpc_utils.default_metadata_interceptor
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clients.grpc_utils.default_metadata_interceptor

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultMetadataInterceptor`](.././flytekit.clients.grpc_utils.default_metadata_interceptor#flytekitclientsgrpc_utilsdefault_metadata_interceptordefaultmetadatainterceptor) |  |

## flytekit.clients.grpc_utils.default_metadata_interceptor.DefaultMetadataInterceptor

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


| Parameter | Type | Description |
|-|-|-|
| `continuation` | `typing.Callable` | |
| `client_call_details` | `grpc.ClientCallDetails` | |
| `request` | `typing.Any` | |

#### intercept_unary_unary()

```python
def intercept_unary_unary(
    continuation: typing.Callable,
    client_call_details: grpc.ClientCallDetails,
    request: typing.Any,
)
```
Intercepts unary calls and inject default metadata


| Parameter | Type | Description |
|-|-|-|
| `continuation` | `typing.Callable` | |
| `client_call_details` | `grpc.ClientCallDetails` | |
| `request` | `typing.Any` | |

