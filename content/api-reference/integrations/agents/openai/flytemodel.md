---
title: FlyteModel
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# FlyteModel

**Package:** `flyteplugins.agents.openai`

Wrap a :class:`~agents.models.interface.Model` so each turn is durable.

``get_response`` is recorded/replayed via ``durable_step``. ``stream_response``
is delegated unchanged: streamed turns are not memoized in this version (tool
calls remain durable regardless).


## Parameters

```python
class FlyteModel(
    inner: Model,
)
```
| Parameter | Type | Description |
|-|-|-|
| `inner` | `Model` | |

## Methods

| Method | Description |
|-|-|
| [`close()`](#close) | Release any resources held by the model. |
| [`get_response()`](#get_response) | Get a response from the model. |
| [`get_retry_advice()`](#get_retry_advice) | Return provider-specific retry guidance for a failed model request. |
| [`stream_response()`](#stream_response) | Stream a response from the model. |


### close()

```python
def close()
```
Release any resources held by the model.

Models that maintain persistent connections can override this. The default implementation
is a no-op.


### get_response()

```python
def get_response(
    args: *args,
    kwargs: **kwargs,
) -> typing.Any
```
Get a response from the model.



| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

**Returns:** The full model response.

### get_retry_advice()

```python
def get_retry_advice(
    request: ModelRetryAdviceRequest,
) -> ModelRetryAdvice | None
```
Return provider-specific retry guidance for a failed model request.

Models can override this to surface transport- or provider-specific hints such as replay
safety, retry-after delays, or explicit server retry guidance.


| Parameter | Type | Description |
|-|-|-|
| `request` | `ModelRetryAdviceRequest` | |

### stream_response()

```python
def stream_response(
    args: *args,
    kwargs: **kwargs,
) -> AsyncIterator[typing.Any]
```
Stream a response from the model.



| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

**Returns:** An iterator of response stream events, in OpenAI Responses format.

