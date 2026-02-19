---
title: RetryExceptionWrapperInterceptor
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RetryExceptionWrapperInterceptor

**Package:** `flytekit.clients.grpc_utils.wrap_exception_interceptor`

```python
class RetryExceptionWrapperInterceptor(
    max_retries: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `max_retries` | `int` | |

## Methods

| Method | Description |
|-|-|
| [`intercept_unary_stream()`](#intercept_unary_stream) | Intercepts a unary-stream invocation. |
| [`intercept_unary_unary()`](#intercept_unary_unary) | Intercepts a unary-unary invocation asynchronously. |


### intercept_unary_stream()

```python
def intercept_unary_stream(
    continuation,
    client_call_details,
    request,
)
```
Intercepts a unary-stream invocation.



| Parameter | Type | Description |
|-|-|-|
| `continuation` |  | A function that proceeds with the invocation by executing the next interceptor in chain or invoking the actual RPC on the underlying Channel. It is the interceptor's responsibility to call it if it decides to move the RPC forward. The interceptor can use `response_iterator = continuation(client_call_details, request)` to continue with the RPC. `continuation` returns an object that is both a Call for the RPC and an iterator for response values. Drawing response values from the returned Call-iterator may raise RpcError indicating termination of the RPC with non-OK status. |
| `client_call_details` |  | A ClientCallDetails object describing the outgoing RPC. |
| `request` |  | The request value for the RPC. |

### intercept_unary_unary()

```python
def intercept_unary_unary(
    continuation,
    client_call_details,
    request,
)
```
Intercepts a unary-unary invocation asynchronously.



| Parameter | Type | Description |
|-|-|-|
| `continuation` |  | A function that proceeds with the invocation by executing the next interceptor in chain or invoking the actual RPC on the underlying Channel. It is the interceptor's responsibility to call it if it decides to move the RPC forward. The interceptor can use `response_future = continuation(client_call_details, request)` to continue with the RPC. `continuation` returns an object that is both a Call for the RPC and a Future. In the event of RPC completion, the return Call-Future's result value will be the response message of the RPC. Should the event terminate with non-OK status, the returned Call-Future's exception value will be an RpcError. |
| `client_call_details` |  | A ClientCallDetails object describing the outgoing RPC. |
| `request` |  | The request value for the RPC. |

