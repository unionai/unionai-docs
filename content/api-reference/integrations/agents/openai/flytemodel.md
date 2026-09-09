---
title: FlyteModel
description: "Wrap a `agents.models.interface.Model` so each turn is durable."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# FlyteModel

**Package:** `flyteplugins.agents.openai`

Wrap a `agents.models.interface.Model` so each turn is durable.

`get_response` is recorded/replayed via `durable_step`. `stream_response`
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
    *args: typing.Any,
    **kwargs: typing.Any,
) -> typing.Any
```
Get a response from the model.



| Parameter | Type | Description |
|-|-|-|
| `*args` | `typing.Any` | |
| `**kwargs` | `typing.Any` | |

**Returns:** The full model response.

### stream_response()

```python
def stream_response(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> AsyncIterator[typing.Any]
```
Stream a response from the model.



| Parameter | Type | Description |
|-|-|-|
| `*args` | `typing.Any` | |
| `**kwargs` | `typing.Any` | |

**Returns:** An iterator of response stream events, in OpenAI Responses format.

