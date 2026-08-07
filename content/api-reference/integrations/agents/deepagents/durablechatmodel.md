---
title: DurableChatModel
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# DurableChatModel

**Package:** `flyteplugins.agents.deepagents`

Wrap a `BaseChatModel` so each model turn is durable and replayable.

`_agenerate` (async) delegates to the inner model and records the turn via
`durable_step`. Pass an instance as the deep agent's model —
`create_deep_agent(model=DurableChatModel(inner=model), ...)` — or as a
subagent's `model`; `bind_tools` and other capabilities are delegated to
the inner model so tool-calling behaves exactly as the inner model does.

Durability is best-effort: if anything in the durable path raises, the turn
falls back to a direct inner call so a run is never broken by it.


## Parameters

```python
class DurableChatModel(
    name: str | None = None,
    cache: langchain_core.caches.BaseCache | bool | None = None,
    verbose: bool = _get_verbosity(),
    callbacks: list[langchain_core.callbacks.base.BaseCallbackHandler] | langchain_core.callbacks.base.BaseCallbackManager | None = None,
    tags: list[str] | None = None,
    metadata: dict[str, typing.Any] | None = None,
    custom_get_token_ids: collections.abc.Callable[[str], list[int]] | None = None,
    rate_limiter: langchain_core.rate_limiters.BaseRateLimiter | None = None,
    disable_streaming: typing.Union[bool, typing.Literal['tool_calling']] = False,
    output_version: str | None = get_from_env_fn(),
    profile: langchain_core.language_models.model_profile.ModelProfile | None = None,
    inner: langchain_core.language_models.chat_models.BaseChatModel,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str \| None` | |
| `cache` | `langchain_core.caches.BaseCache \| bool \| None` | |
| `verbose` | `bool` | |
| `callbacks` | `list[langchain_core.callbacks.base.BaseCallbackHandler] \| langchain_core.callbacks.base.BaseCallbackManager \| None` | |
| `tags` | `list[str] \| None` | |
| `metadata` | `dict[str, typing.Any] \| None` | |
| `custom_get_token_ids` | `collections.abc.Callable[[str], list[int]] \| None` | |
| `rate_limiter` | `langchain_core.rate_limiters.BaseRateLimiter \| None` | |
| `disable_streaming` | `typing.Union[bool, typing.Literal['tool_calling']]` | |
| `output_version` | `str \| None` | |
| `profile` | `langchain_core.language_models.model_profile.ModelProfile \| None` | |
| `inner` | `langchain_core.language_models.chat_models.BaseChatModel` | |

## Methods

| Method | Description |
|-|-|
| [`bind_tools()`](#bind_tools) | Format tools via the inner model, but bind them to *this* wrapper. |
| [`get_num_tokens()`](#get_num_tokens) | Get the number of tokens present in the text. |
| [`get_num_tokens_from_messages()`](#get_num_tokens_from_messages) | Get the number of tokens in the messages. |


### bind_tools()

```python
def bind_tools(
    tools: typing.Sequence[typing.Any],
    **kwargs: typing.Any,
) -> 'Runnable'
```
Format tools via the inner model, but bind them to *this* wrapper.

The inner model knows how to convert tools into its provider format; we
reuse that, then re-bind the resulting kwargs to `self` so the runnable
the deep agent invokes still routes generation through the durable
override (rather than the inner model directly).


| Parameter | Type | Description |
|-|-|-|
| `tools` | `typing.Sequence[typing.Any]` | |
| `**kwargs` | `typing.Any` | |

### get_num_tokens()

```python
def get_num_tokens(
    text: str,
) -> int
```
Get the number of tokens present in the text.

Useful for checking if an input fits in a model's context window.

This should be overridden by model-specific implementations to provide accurate
token counts via model-specific tokenizers.



| Parameter | Type | Description |
|-|-|-|
| `text` | `str` | The string input to tokenize. |

**Returns:** The integer number of tokens in the text.

### get_num_tokens_from_messages()

```python
def get_num_tokens_from_messages(
    messages,
    tools = None,
) -> int
```
Get the number of tokens in the messages.

Useful for checking if an input fits in a model's context window.

This should be overridden by model-specific implementations to provide accurate
token counts via model-specific tokenizers.

> [!NOTE]
> * The base implementation of `get_num_tokens_from_messages` ignores tool
>     schemas.
> * The base implementation of `get_num_tokens_from_messages` adds additional
>     prefixes to messages in represent user roles, which will add to the
>     overall token count. Model-specific implementations may choose to
>     handle this differently.



| Parameter | Type | Description |
|-|-|-|
| `messages` |  | The message inputs to tokenize. |
| `tools` |  | If provided, sequence of dict, `BaseModel`, function, or `BaseTool` objects to be converted to tool schemas. |

**Returns:** The sum of the number of tokens across the messages.

