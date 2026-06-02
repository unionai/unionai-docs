---
title: flytekit.clients.grpc_utils.deadline_interceptor
version: 1.16.23
variants: +flyte +union
layout: py_api
---

# flytekit.clients.grpc_utils.deadline_interceptor

## Directory

### Classes

| Class | Description |
|-|-|
| [`ScopedGrpcDeadlineInterceptor`](.././flytekit.clients.grpc_utils.deadline_interceptor#flytekitclientsgrpc_utilsdeadline_interceptorscopedgrpcdeadlineinterceptor) | Applies the currently scoped gRPC timeout to unary-unary calls. |

### Methods

| Method | Description |
|-|-|
| [`get_scoped_grpc_deadline()`](#get_scoped_grpc_deadline) |  |
| [`scoped_grpc_deadline()`](#scoped_grpc_deadline) |  |


## Methods

#### get_scoped_grpc_deadline()

```python
def get_scoped_grpc_deadline()
```
#### scoped_grpc_deadline()

```python
def scoped_grpc_deadline(
    seconds: float,
)
```
| Parameter | Type | Description |
|-|-|-|
| `seconds` | `float` | |

## flytekit.clients.grpc_utils.deadline_interceptor.ScopedGrpcDeadlineInterceptor

Applies the currently scoped gRPC timeout to unary-unary calls.


### Methods

| Method | Description |
|-|-|
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts a unary-unary invocation asynchronously. |


#### intercept_unary_unary()

```python
def intercept_unary_unary(
    continuation: typing.Callable,
    client_call_details: grpc.ClientCallDetails,
    request: typing.Any,
)
```
Intercepts a unary-unary invocation asynchronously.



| Parameter | Type | Description |
|-|-|-|
| `continuation` | `typing.Callable` | A function that proceeds with the invocation by executing the next interceptor in chain or invoking the actual RPC on the underlying Channel. It is the interceptor's responsibility to call it if it decides to move the RPC forward. The interceptor can use `response_future = continuation(client_call_details, request)` to continue with the RPC. `continuation` returns an object that is both a Call for the RPC and a Future. In the event of RPC completion, the return Call-Future's result value will be the response message of the RPC. Should the event terminate with non-OK status, the returned Call-Future's exception value will be an RpcError. |
| `client_call_details` | `grpc.ClientCallDetails` | A ClientCallDetails object describing the outgoing RPC. |
| `request` | `typing.Any` | The request value for the RPC. |

**Returns**

An object that is both a Call for the RPC and a Future.
In the event of RPC completion, the return Call-Future's
result value will be the response message of the RPC.
Should the event terminate with non-OK status, the returned
Call-Future's exception value will be an RpcError.

