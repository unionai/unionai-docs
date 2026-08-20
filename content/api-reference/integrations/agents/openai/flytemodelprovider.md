---
title: FlyteModelProvider
version: 2.6.2
variants: +flyte +union
layout: py_api
---

# FlyteModelProvider

**Package:** `flyteplugins.agents.openai`

Wrap a `ModelProvider` so every model it returns produces durable turns.

Pass an explicit `inner` provider to keep custom routing (Azure, a gateway,
a local OpenAI-compatible server); defaults to the SDK's `MultiProvider`.
Set it on `RunConfig.model_provider` (`run_agent` does this for you).


## Parameters

```python
class FlyteModelProvider(
    inner: ModelProvider | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `inner` | `ModelProvider \| None` | |

## Methods

| Method | Description |
|-|-|
| [`aclose()`](#aclose) | Release any resources held by the provider. |
| [`get_model()`](#get_model) | Get a model by name. |


### aclose()

```python
def aclose()
```
Release any resources held by the provider.

Providers that cache persistent models or network connections can override this. The
default implementation is a no-op.


### get_model()

```python
def get_model(
    model_name: str | None,
) -> Model
```
Get a model by name.



| Parameter | Type | Description |
|-|-|-|
| `model_name` | `str \| None` | The name of the model to get. |

**Returns:** The model.

