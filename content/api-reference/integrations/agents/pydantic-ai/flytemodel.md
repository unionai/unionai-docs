---
title: FlyteModel
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# FlyteModel

**Package:** `flyteplugins.agents.pydantic_ai`

Wrap a :class:`~pydantic_ai.models.Model` so each model turn is durable.

``request`` is recorded/replayed via ``durable_step``. ``request_stream`` is
delegated unchanged: streamed turns are not memoized in this version (tool
calls remain durable regardless). ``model_name`` / ``system`` and any other
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
| `base_url` | `str \| None` | The base URL for the provider API, if available. |
| `label` | `str` | Human-friendly display label for the model.  Handles common patterns: - gpt-5 -&gt; GPT 5 - claude-sonnet-4-5 -&gt; Claude Sonnet 4.5 - gemini-2.5-pro -&gt; Gemini 2.5 Pro - meta-llama/llama-3-70b -&gt; Llama 3 70b (OpenRouter style) |
| `model_id` | `str` | The fully qualified model name in `'provider:model_name'` format. |
| `model_name` | `str` | The model name. |
| `profile` | `ModelProfile` | The model profile.  Resolution order (later layers override earlier ones):   1. `DEFAULT_PROFILE` — base values for every key in `ModelProfile`.   2. The provider's `model_profile(model_name)` result — provider-specific defaults      for this model.   3. The user's `profile=` argument — partial dict merged on top, OR a callable      `(default) -&gt; profile` for full control.  After resolution we compute the intersection of the profile's `supported_native_tools` and the model class's implemented tools, ensuring `model.profile['supported_native_tools']` is the single source of truth for what's actually usable. |
| `provider` | `Provider[InterfaceClient] \| None` | The provider for this model, if any. |
| `settings` | `ModelSettings \| None` | Get the model settings. |
| `system` | `str` | The model provider, ex: openai.  Use to populate the `gen_ai.system` OpenTelemetry semantic convention attribute, so should use well-known values listed in https://opentelemetry.io/docs/specs/semconv/attributes-registry/gen-ai/#gen-ai-system when applicable. |

## Methods

| Method | Description |
|-|-|
| [`cancel_suspended_response()`](#cancel_suspended_response) | Cancel a server-side suspended/background response (e. |
| [`compact_messages()`](#compact_messages) | Compact messages to reduce conversation context size. |
| [`continuation_delay()`](#continuation_delay) | Seconds to wait before continuing a suspended response, or `None` to continue immediately. |
| [`count_tokens()`](#count_tokens) | Make a request to the model for counting tokens. |
| [`customize_request_parameters()`](#customize_request_parameters) | Customize the request parameters for the model. |
| [`prepare_messages()`](#prepare_messages) | Pre-process the message history before it's handed to the adapter's message-prep step. |
| [`prepare_request()`](#prepare_request) | Prepare request inputs before they are passed to the provider. |
| [`request()`](#request) | Make a request to the model. |
| [`request_stream()`](#request_stream) | Make a request to the model and return a streaming response. |
| [`supported_native_tools()`](#supported_native_tools) | Return the set of native tool types this model class can handle. |


### cancel_suspended_response()

```python
def cancel_suspended_response(
    response: ModelResponse,
)
```
Cancel a server-side suspended/background response (e.g. an OpenAI background job).

Called when a continuation is abandoned via cancellation or error. No-op by default;
model classes with cancellable server-side jobs override this.


| Parameter | Type | Description |
|-|-|-|
| `response` | `ModelResponse` | |

### compact_messages()

```python
def compact_messages(
    request_context: ModelRequestContext,
    instructions: str | None,
) -> ModelResponse
```
Compact messages to reduce conversation context size.

This method is optional and only supported by specific providers
(e.g. OpenAI Responses API). Providers that support compaction
override this method with their implementation.


| Parameter | Type | Description |
|-|-|-|
| `request_context` | `ModelRequestContext` | |
| `instructions` | `str \| None` | |

### continuation_delay()

```python
def continuation_delay(
    response: ModelResponse,
) -> float | None
```
Seconds to wait before continuing a suspended response, or `None` to continue immediately.

Called between the segments of a suspended turn. `None` by default (e.g. Anthropic `pause_turn`
continues immediately); a model that polls a server-side job (e.g. OpenAI background mode)
overrides this to return a poll interval so the graph doesn't busy-poll.


| Parameter | Type | Description |
|-|-|-|
| `response` | `ModelResponse` | |

### count_tokens()

```python
def count_tokens(
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
) -> RequestUsage
```
Make a request to the model for counting tokens.


| Parameter | Type | Description |
|-|-|-|
| `messages` | `list[ModelMessage]` | |
| `model_settings` | `ModelSettings \| None` | |
| `model_request_parameters` | `ModelRequestParameters` | |

### customize_request_parameters()

```python
def customize_request_parameters(
    model_request_parameters: ModelRequestParameters,
) -> ModelRequestParameters
```
Customize the request parameters for the model.

This method can be overridden by subclasses to modify the request parameters before sending them to the model.
In particular, this method can be used to make modifications to the generated tool JSON schemas if necessary
for vendor/model-specific reasons.


| Parameter | Type | Description |
|-|-|-|
| `model_request_parameters` | `ModelRequestParameters` | |

### prepare_messages()

```python
def prepare_messages(
    messages: list[ModelMessage],
    model_request_parameters: ModelRequestParameters | None,
) -> list[ModelMessage]
```
Pre-process the message history before it's handed to the adapter's message-prep step.

Translates typed `NativeToolSearch*Part` instances carried over from a
different provider (e.g. Anthropic to OpenAI Responses), or any native
provider when the active model doesn't support `ToolSearchTool`, into the
local-shape `ToolSearch*Part` instances. This splits the single
`ModelResponse(call+return)` carrying the inline server-side result into
`ModelResponse(call) + ModelRequest(return)` so the adapter can render the
provider-agnostic exchange.

Also wraps non-leading `SystemPromptPart`s as `&lt;system&gt;`-tagged `UserPromptPart`s when
the profile's `supports_inline_system_prompts` is `False`.

Subclasses normally don't need to override this; the framework calls it on the
agent's behalf in `_agent_graph._make_request` so per-adapter message-prep code
sees a homogeneous shape regardless of which provider produced the prior turn.



| Parameter | Type | Description |
|-|-|-|
| `messages` | `list[ModelMessage]` | The history to pre-process. |
| `model_request_parameters` | `ModelRequestParameters \| None` | The parameters this history will be sent with. Optional, and only needed to render a `ToolAvailabilityDeltaPart` on a model with no native way to express one: whether that reveal has to be a mechanism or can just be a statement depends on whether any tool actually goes on the wire with its schema withheld, which the profile alone can't answer. Omitting it falls back to the profile-level answer, which differs only for a corpus mixing capability-gated and standalone deferred tools. Framework callers pass it. |

### prepare_request()

```python
def prepare_request(
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
) -> tuple[ModelSettings | None, ModelRequestParameters]
```
Prepare request inputs before they are passed to the provider.

This merges the given `model_settings` with the model's own `settings` attribute and ensures
`customize_request_parameters` is applied to the resolved
[`ModelRequestParameters`][pydantic_ai.models.ModelRequestParameters]. Subclasses can override this method if
they need to customize the preparation flow further, but most implementations should simply call
`self.prepare_request(...)` at the start of their `request` (and related) methods.


| Parameter | Type | Description |
|-|-|-|
| `model_settings` | `ModelSettings \| None` | |
| `model_request_parameters` | `ModelRequestParameters` | |

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
    run_context: typing.Any,
) -> 'AsyncIterator[StreamedResponse]'
```
Make a request to the model and return a streaming response.


| Parameter | Type | Description |
|-|-|-|
| `messages` | `typing.Any` | |
| `model_settings` | `'ModelSettings \| None'` | |
| `model_request_parameters` | `'ModelRequestParameters'` | |
| `run_context` | `typing.Any` | |

### supported_native_tools()

```python
def supported_native_tools()
```
Return the set of native tool types this model class can handle.

Subclasses should override this to reflect their actual capabilities.
Default is empty set - subclasses must explicitly declare support.


