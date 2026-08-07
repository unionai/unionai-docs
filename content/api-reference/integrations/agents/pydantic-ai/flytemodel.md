---
title: FlyteModel
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# FlyteModel

**Package:** `flyteplugins.agents.pydantic_ai`

Wrap a `pydantic_ai.models.Model` so each model turn is durable.

`request` is recorded/replayed via `durable_step`. `request_stream` is
delegated unchanged: streamed turns are not memoized in this version (tool
calls remain durable regardless). `model_name` / `system` and any other
members are forwarded to the inner model.


## Parameters

```python
class FlyteModel(
    inner: Model,
)
```
Initialize the model with optional settings and profile.



| Parameter | Type | Description |
|-|-|-|
| `inner` | `Model` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `model_name` | `str` | The model name. |
| `system` | `str` | The model provider, ex: openai.  Use to populate the `gen_ai.system` OpenTelemetry semantic convention attribute, so should use well-known values listed in https://opentelemetry.io/docs/specs/semconv/attributes-registry/gen-ai/#gen-ai-system when applicable. |

## Methods

| Method | Description |
|-|-|
| [`request()`](#request) | Make a request to the model. |
| [`request_stream()`](#request_stream) | Make a request to the model and return a streaming response. |


### request()

```python
def request(
    messages: typing.Any,
    model_settings: 'ModelSettings | None',
    model_request_parameters: 'ModelRequestParameters',
) -> ModelResponse
```
Make a request to the model.

This is ultimately called by `pydantic_ai._agent_graph.ModelRequestNode._make_request(...)`.


| Parameter | Type | Description |
|-|-|-|
| `messages` | `typing.Any` | |
| `model_settings` | `'ModelSettings \| None'` | |
| `model_request_parameters` | `'ModelRequestParameters'` | |

### request_stream()

```python
def request_stream(
    messages: typing.Any,
    model_settings: 'ModelSettings | None',
    model_request_parameters: 'ModelRequestParameters',
    run_context: typing.Any = None,
) -> 'AsyncIterator[StreamedResponse]'
```
Make a request to the model and return a streaming response.


| Parameter | Type | Description |
|-|-|-|
| `messages` | `typing.Any` | |
| `model_settings` | `'ModelSettings \| None'` | |
| `model_request_parameters` | `'ModelRequestParameters'` | |
| `run_context` | `typing.Any` | |

