---
title: DurableChatModel
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# DurableChatModel

**Package:** `flyteplugins.agents.deepagents`

Wrap a ``BaseChatModel`` so each model turn is durable and replayable.

``_agenerate`` (async) delegates to the inner model and records the turn via
``durable_step``. Pass an instance as the deep agent's model —
``create_deep_agent(model=DurableChatModel(inner=model), ...)`` — or as a
subagent's ``model``; ``bind_tools`` and other capabilities are delegated to
the inner model so tool-calling behaves exactly as the inner model does.

Durability is best-effort: if anything in the durable path raises, the turn
falls back to a direct inner call so a run is never broken by it.


## Parameters

```python
class DurableChatModel(
    name: str | None,
    cache: langchain_core.caches.BaseCache | bool | None,
    verbose: bool,
    callbacks: list[langchain_core.callbacks.base.BaseCallbackHandler] | langchain_core.callbacks.base.BaseCallbackManager | None,
    tags: list[str] | None,
    metadata: dict[str, typing.Any] | None,
    custom_get_token_ids: collections.abc.Callable[[str], list[int]] | None,
    rate_limiter: langchain_core.rate_limiters.BaseRateLimiter | None,
    disable_streaming: typing.Union[bool, typing.Literal['tool_calling']],
    output_version: str | None,
    profile: langchain_core.language_models.model_profile.ModelProfile | None,
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

## Properties

| Property | Type | Description |
|-|-|-|
| `InputType` | `TypeAlias` | Get the input type for this `Runnable`. |
| `OutputType` | `Any` | Get the output type for this `Runnable`. |
| `config_specs` | `list[ConfigurableFieldSpec]` | List configurable fields for this `Runnable`. |
| `input_schema` | `TypeBaseModel` | The type of input this `Runnable` accepts specified as a Pydantic model. |
| `lc_attributes` | `dict[str, typing.Any]` | List of attribute names that should be included in the serialized kwargs.  These attributes must be accepted by the constructor.  Default is an empty dictionary. |
| `lc_secrets` | `dict[str, str]` | A map of constructor argument names to secret ids.  For example, `{"openai_api_key": "OPENAI_API_KEY"}` |
| `output_schema` | `TypeBaseModel` | Output schema.  The type of output this `Runnable` produces specified as a Pydantic model. |

## Methods

| Method | Description |
|-|-|
| [`abatch()`](#abatch) | Default implementation runs `ainvoke` in parallel using `asyncio. |
| [`abatch_as_completed()`](#abatch_as_completed) | Run `ainvoke` in parallel on a list of inputs. |
| [`agenerate()`](#agenerate) | Asynchronously pass a sequence of prompts to a model and return generations. |
| [`agenerate_prompt()`](#agenerate_prompt) | Asynchronously pass a sequence of prompts and return model generations. |
| [`ainvoke()`](#ainvoke) | Transform a single input into an output. |
| [`as_tool()`](#as_tool) |  |
| [`asdict()`](#asdict) | Return a dictionary representation of the chat model. |
| [`assign()`](#assign) | Assigns new fields to the `dict` output of this `Runnable`. |
| [`astream()`](#astream) | Default implementation of `astream`, which calls `ainvoke`. |
| [`astream_events()`](#astream_events) | Async variant of `stream_events`. |
| [`astream_log()`](#astream_log) | Stream all output from a `Runnable`, as reported to the callback system. |
| [`atransform()`](#atransform) | Transform inputs to outputs. |
| [`batch()`](#batch) | Default implementation runs invoke in parallel using a thread pool executor. |
| [`batch_as_completed()`](#batch_as_completed) | Run `invoke` in parallel on a list of inputs. |
| [`bind()`](#bind) | Bind kwargs to this chat model, returning a typed `_ChatModelBinding`. |
| [`bind_tools()`](#bind_tools) | Format tools via the inner model, but bind them to *this* wrapper. |
| [`config_schema()`](#config_schema) | The type of config this `Runnable` accepts specified as a Pydantic model. |
| [`configurable_alternatives()`](#configurable_alternatives) | Configure alternatives for `Runnable` objects that can be set at runtime. |
| [`configurable_fields()`](#configurable_fields) | Configure particular `Runnable` fields at runtime. |
| [`dict()`](#dict) | DEPRECATED - use `asdict()` instead. |
| [`generate()`](#generate) | Pass a sequence of prompts to the model and return model generations. |
| [`generate_prompt()`](#generate_prompt) | Pass a sequence of prompts to the model and return model generations. |
| [`get_config_jsonschema()`](#get_config_jsonschema) | Get a JSON schema that represents the config of the `Runnable`. |
| [`get_graph()`](#get_graph) | Return a graph representation of this `Runnable`. |
| [`get_input_jsonschema()`](#get_input_jsonschema) | Get a JSON schema that represents the input to the `Runnable`. |
| [`get_input_schema()`](#get_input_schema) | Get a Pydantic model that can be used to validate input to the `Runnable`. |
| [`get_lc_namespace()`](#get_lc_namespace) | Get the namespace of the LangChain object. |
| [`get_name()`](#get_name) | Get the name of the `Runnable`. |
| [`get_num_tokens()`](#get_num_tokens) | Get the number of tokens present in the text. |
| [`get_num_tokens_from_messages()`](#get_num_tokens_from_messages) | Get the number of tokens in the messages. |
| [`get_output_jsonschema()`](#get_output_jsonschema) | Get a JSON schema that represents the output of the `Runnable`. |
| [`get_output_schema()`](#get_output_schema) | Get a Pydantic model that can be used to validate output to the `Runnable`. |
| [`get_prompts()`](#get_prompts) | Return a list of prompts used by this `Runnable`. |
| [`get_token_ids()`](#get_token_ids) | Return the ordered IDs of the tokens in a text. |
| [`invoke()`](#invoke) | Transform a single input into an output. |
| [`is_lc_serializable()`](#is_lc_serializable) | Is this class serializable?. |
| [`lc_id()`](#lc_id) | Return a unique identifier for this class for serialization purposes. |
| [`map()`](#map) | Return a new `Runnable` that maps a list of inputs to a list of outputs. |
| [`model_post_init()`](#model_post_init) | Pydantic V2 lifecycle hook called automatically after `__init__`. |
| [`pick()`](#pick) | Pick keys from the output `dict` of this `Runnable`. |
| [`pipe()`](#pipe) | Pipe `Runnable` objects. |
| [`set_verbose()`](#set_verbose) | If verbose is `None`, set it. |
| [`stream()`](#stream) | Default implementation of `stream`, which calls `invoke`. |
| [`stream_events()`](#stream_events) | Stream events from this chat model. |
| [`to_json()`](#to_json) | Serialize the `Runnable` to JSON. |
| [`to_json_not_implemented()`](#to_json_not_implemented) | Serialize a "not implemented" object. |
| [`transform()`](#transform) | Transform inputs to outputs. |
| [`with_alisteners()`](#with_alisteners) | Bind async lifecycle listeners to a `Runnable`. |
| [`with_config()`](#with_config) | Bind config to a `Runnable`, returning a new `Runnable`. |
| [`with_fallbacks()`](#with_fallbacks) | Add fallbacks to a `Runnable`, returning a new `Runnable`. |
| [`with_listeners()`](#with_listeners) | Bind lifecycle listeners to a `Runnable`, returning a new `Runnable`. |
| [`with_retry()`](#with_retry) | Create a new `Runnable` that retries the original `Runnable` on exceptions. |
| [`with_structured_output()`](#with_structured_output) | Model wrapper that returns outputs formatted to match the given schema. |
| [`with_types()`](#with_types) | Bind input and output types to a `Runnable`, returning a new `Runnable`. |


### abatch()

```python
def abatch(
    inputs: list[Input],
    config: RunnableConfig | list[RunnableConfig] | None,
    return_exceptions: bool,
    kwargs: **kwargs,
) -> list[Output]
```
Default implementation runs `ainvoke` in parallel using `asyncio.gather`.

The default implementation of `batch` works well for IO bound runnables.

Subclasses must override this method if they can batch more efficiently;
e.g., if the underlying `Runnable` uses an API which supports a batch mode.



| Parameter | Type | Description |
|-|-|-|
| `inputs` | `list[Input]` | A list of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| list[RunnableConfig] \| None` | A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. |
| `return_exceptions` | `bool` | Whether to return exceptions instead of raising them. |
| `kwargs` | `**kwargs` | |

**Returns:** A list of outputs from the `Runnable`.

### abatch_as_completed()

```python
def abatch_as_completed(
    inputs: Sequence[Input],
    config: RunnableConfig | Sequence[RunnableConfig] | None,
    return_exceptions: bool,
    kwargs: **kwargs,
) -> AsyncIterator[tuple[int, Output | Exception]]
```
Run `ainvoke` in parallel on a list of inputs.

Yields results as they complete.

Yields:
    A tuple of the index of the input and the output from the `Runnable`.


| Parameter | Type | Description |
|-|-|-|
| `inputs` | `Sequence[Input]` | A list of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| Sequence[RunnableConfig] \| None` | A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. |
| `return_exceptions` | `bool` | Whether to return exceptions instead of raising them. |
| `kwargs` | `**kwargs` | |

### agenerate()

```python
def agenerate(
    messages: list[list[BaseMessage]],
    stop: list[str] | None,
    callbacks: Callbacks,
    tags: list[str] | None,
    metadata: builtins.dict[str, Any] | None,
    run_name: str | None,
    run_id: uuid.UUID | None,
    kwargs: **kwargs,
) -> LLMResult
```
Asynchronously pass a sequence of prompts to a model and return generations.

This method should make use of batched calls for models that expose a batched
API.

Use this method when you want to:

1. Take advantage of batched calls,
2. Need more output from the model than just the top generated value,
3. Are building chains that are agnostic to the underlying language model
    type (e.g., pure text completion models vs chat models).



| Parameter | Type | Description |
|-|-|-|
| `messages` | `list[list[BaseMessage]]` | List of list of messages. |
| `stop` | `list[str] \| None` | Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings. |
| `callbacks` | `Callbacks` | `Callbacks` to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation. |
| `tags` | `list[str] \| None` | The tags to apply. |
| `metadata` | `builtins.dict[str, Any] \| None` | The metadata to apply. |
| `run_name` | `str \| None` | The name of the run. |
| `run_id` | `uuid.UUID \| None` | The ID of the run. |
| `kwargs` | `**kwargs` | |

**Returns**

An `LLMResult`, which contains a list of candidate `Generations` for each
    input prompt and additional model provider-specific output.

### agenerate_prompt()

```python
def agenerate_prompt(
    prompts: list[PromptValue],
    stop: list[str] | None,
    callbacks: Callbacks,
    kwargs: **kwargs,
) -> LLMResult
```
Asynchronously pass a sequence of prompts and return model generations.

This method should make use of batched calls for models that expose a batched
API.

Use this method when you want to:

1. Take advantage of batched calls,
2. Need more output from the model than just the top generated value,
3. Are building chains that are agnostic to the underlying language model
    type (e.g., pure text completion models vs chat models).



| Parameter | Type | Description |
|-|-|-|
| `prompts` | `list[PromptValue]` | List of `PromptValue` objects. A `PromptValue` is an object that can be converted to match the format of any language model (string for pure text generation models and `BaseMessage` objects for chat models). |
| `stop` | `list[str] \| None` | Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings. |
| `callbacks` | `Callbacks` | `Callbacks` to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation. |
| `kwargs` | `**kwargs` | |

**Returns**

An `LLMResult`, which contains a list of candidate `Generation` objects for
    each input prompt and additional model provider-specific output.

### ainvoke()

```python
def ainvoke(
    input: LanguageModelInput,
    config: RunnableConfig | None,
    stop: list[str] | None,
    kwargs: **kwargs,
) -> AIMessage
```
Transform a single input into an output.



| Parameter | Type | Description |
|-|-|-|
| `input` | `LanguageModelInput` | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. |
| `stop` | `list[str] \| None` | |
| `kwargs` | `**kwargs` | |

**Returns:** The output of the `Runnable`.

### as_tool()

```python
def as_tool(
    args_schema: type[BaseModel] | None,
    name: str | None,
    description: str | None,
    arg_types: dict[str, type] | None,
) -> BaseTool
```
.. beta::
   This API is in beta and may change in the future.

Create a `BaseTool` from a `Runnable`.

`as_tool` will instantiate a `BaseTool` with a name, description, and
`args_schema` from a `Runnable`. Where possible, schemas are inferred
from `runnable.get_input_schema`.

Alternatively (e.g., if the `Runnable` takes a dict as input and the specific
`dict` keys are not typed), the schema can be specified directly with
`args_schema`.

You can also pass `arg_types` to just specify the required arguments and their
types.

!!! example "`TypedDict` input"

    ```python
    from typing_extensions import TypedDict
    from langchain_core.runnables import RunnableLambda


    class Args(TypedDict):
        a: int
        b: list[int]


    def f(x: Args) -> str:
        return str(x["a"] * max(x["b"]))


    runnable = RunnableLambda(f)
    as_tool = runnable.as_tool()
    as_tool.invoke({"a": 3, "b": [1, 2]})
    ```

!!! example "`dict` input, specifying schema via `args_schema`"

    ```python
    from typing import Any
    from pydantic import BaseModel, Field
    from langchain_core.runnables import RunnableLambda

    def f(x: dict[str, Any]) -> str:
        return str(x["a"] * max(x["b"]))

    class FSchema(BaseModel):
        """Apply a function to an integer and list of integers."""

        a: int = Field(..., description="Integer")
        b: list[int] = Field(..., description="List of ints")

    runnable = RunnableLambda(f)
    as_tool = runnable.as_tool(FSchema)
    as_tool.invoke({"a": 3, "b": [1, 2]})
    ```

!!! example "`dict` input, specifying schema via `arg_types`"

    ```python
    from typing import Any
    from langchain_core.runnables import RunnableLambda


    def f(x: dict[str, Any]) -> str:
        return str(x["a"] * max(x["b"]))


    runnable = RunnableLambda(f)
    as_tool = runnable.as_tool(arg_types={"a": int, "b": list[int]})
    as_tool.invoke({"a": 3, "b": [1, 2]})
    ```

!!! example "`str` input"

    ```python
    from langchain_core.runnables import RunnableLambda


    def f(x: str) -> str:
        return x + "a"


    def g(x: str) -> str:
        return x + "z"


    runnable = RunnableLambda(f) | g
    as_tool = runnable.as_tool()
    as_tool.invoke("b")
    ```


| Parameter | Type | Description |
|-|-|-|
| `args_schema` | `type[BaseModel] \| None` | The schema for the tool. |
| `name` | `str \| None` | The name of the tool. |
| `description` | `str \| None` | The description of the tool. |
| `arg_types` | `dict[str, type] \| None` | A dictionary of argument names to types. |

**Returns**

A `BaseTool` instance.


### asdict()

```python
def asdict()
```
Return a dictionary representation of the chat model.


### assign()

```python
def assign(
    kwargs: **kwargs,
) -> RunnableSerializable[Any, Any]
```
Assigns new fields to the `dict` output of this `Runnable`.

```python
from langchain_core.language_models.fake import FakeStreamingListLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate
from langchain_core.runnables import Runnable
from operator import itemgetter

prompt = (
    SystemMessagePromptTemplate.from_template("You are a nice assistant.")
    + "{question}"
)
model = FakeStreamingListLLM(responses=["foo-lish"])

chain: Runnable = prompt | model | {"str": StrOutputParser()}

chain_with_assign = chain.assign(hello=itemgetter("str") | model)

print(chain_with_assign.input_schema.model_json_schema())
# {'title': 'PromptInput', 'type': 'object', 'properties':
{'question': {'title': 'Question', 'type': 'string'}}}
print(chain_with_assign.output_schema.model_json_schema())
# {'title': 'RunnableSequenceOutput', 'type': 'object', 'properties':
{'str': {'title': 'Str',
'type': 'string'}, 'hello': {'title': 'Hello', 'type': 'string'}}}
```



| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

**Returns:** A new `Runnable`.

### astream()

```python
def astream(
    input: LanguageModelInput,
    config: RunnableConfig | None,
    stop: list[str] | None,
    kwargs: **kwargs,
) -> AsyncIterator[AIMessageChunk]
```
Default implementation of `astream`, which calls `ainvoke`.

Subclasses must override this method if they support streaming output.

Yields:
    The output of the `Runnable`.


| Parameter | Type | Description |
|-|-|-|
| `input` | `LanguageModelInput` | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | The config to use for the `Runnable`. |
| `stop` | `list[str] \| None` | |
| `kwargs` | `**kwargs` | |

### astream_events()

```python
def astream_events(
    input: LanguageModelInput,
    config: RunnableConfig | None,
    version: Literal['v1', 'v2', 'v3'],
    stop: list[str] | None,
    kwargs: **kwargs,
) -> AsyncIterator[StreamEvent] | Awaitable[AsyncChatModelStream]
```
Async variant of `stream_events`. See `stream_events` for full docs.


| Parameter | Type | Description |
|-|-|-|
| `input` | `LanguageModelInput` | |
| `config` | `RunnableConfig \| None` | |
| `version` | `Literal['v1', 'v2', 'v3']` | |
| `stop` | `list[str] \| None` | |
| `kwargs` | `**kwargs` | |

### astream_log()

```python
def astream_log(
    input: Any,
    config: RunnableConfig | None,
    diff: bool,
    with_streamed_output_list: bool,
    include_names: Sequence[str] | None,
    include_types: Sequence[str] | None,
    include_tags: Sequence[str] | None,
    exclude_names: Sequence[str] | None,
    exclude_types: Sequence[str] | None,
    exclude_tags: Sequence[str] | None,
    kwargs: **kwargs,
) -> AsyncIterator[RunLogPatch] | AsyncIterator[RunLog]
```
Stream all output from a `Runnable`, as reported to the callback system.

This includes all inner runs of LLMs, Retrievers, Tools, etc.

Output is streamed as Log objects, which include a list of
Jsonpatch ops that describe how the state of the run has changed in each
step, and the final state of the run.

The Jsonpatch ops can be applied in order to construct state.

Yields:
    A `RunLogPatch` or `RunLog` object.


| Parameter | Type | Description |
|-|-|-|
| `input` | `Any` | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | The config to use for the `Runnable`. |
| `diff` | `bool` | Whether to yield diffs between each step or the current state. |
| `with_streamed_output_list` | `bool` | Whether to yield the `streamed_output` list. |
| `include_names` | `Sequence[str] \| None` | Only include logs with these names. |
| `include_types` | `Sequence[str] \| None` | Only include logs with these types. |
| `include_tags` | `Sequence[str] \| None` | Only include logs with these tags. |
| `exclude_names` | `Sequence[str] \| None` | Exclude logs with these names. |
| `exclude_types` | `Sequence[str] \| None` | Exclude logs with these types. |
| `exclude_tags` | `Sequence[str] \| None` | Exclude logs with these tags. |
| `kwargs` | `**kwargs` | |

### atransform()

```python
def atransform(
    input: AsyncIterator[Input],
    config: RunnableConfig | None,
    kwargs: **kwargs,
) -> AsyncIterator[Output]
```
Transform inputs to outputs.

Default implementation of atransform, which buffers input and calls `astream`.

Subclasses must override this method if they can start producing output while
input is still being generated.

Yields:
    The output of the `Runnable`.


| Parameter | Type | Description |
|-|-|-|
| `input` | `AsyncIterator[Input]` | An async iterator of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| None` | The config to use for the `Runnable`. |
| `kwargs` | `**kwargs` | |

### batch()

```python
def batch(
    inputs: list[Input],
    config: RunnableConfig | list[RunnableConfig] | None,
    return_exceptions: bool,
    kwargs: **kwargs,
) -> list[Output]
```
Default implementation runs invoke in parallel using a thread pool executor.

The default implementation of batch works well for IO bound runnables.

Subclasses must override this method if they can batch more efficiently;
e.g., if the underlying `Runnable` uses an API which supports a batch mode.



| Parameter | Type | Description |
|-|-|-|
| `inputs` | `list[Input]` | A list of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| list[RunnableConfig] \| None` | A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. |
| `return_exceptions` | `bool` | Whether to return exceptions instead of raising them. |
| `kwargs` | `**kwargs` | |

**Returns:** A list of outputs from the `Runnable`.

### batch_as_completed()

```python
def batch_as_completed(
    inputs: Sequence[Input],
    config: RunnableConfig | Sequence[RunnableConfig] | None,
    return_exceptions: bool,
    kwargs: **kwargs,
) -> Iterator[tuple[int, Output | Exception]]
```
Run `invoke` in parallel on a list of inputs.

Yields results as they complete.

Yields:
    Tuples of the index of the input and the output from the `Runnable`.


| Parameter | Type | Description |
|-|-|-|
| `inputs` | `Sequence[Input]` | A list of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| Sequence[RunnableConfig] \| None` | A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. |
| `return_exceptions` | `bool` | Whether to return exceptions instead of raising them. |
| `kwargs` | `**kwargs` | |

### bind()

```python
def bind(
    kwargs: **kwargs,
) -> _ChatModelBinding
```
Bind kwargs to this chat model, returning a typed `_ChatModelBinding`.

Overrides `Runnable.bind` so the result preserves chat-model-specific
`stream_events` / `astream_events` overloads. Without this override,
`model.bind(...).stream_events(version="v3")` would type as
`Iterator[Any]` and `await model.bind(...).astream_events(version="v3")`
as `Any`, forcing callers to `cast`.


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### bind_tools()

```python
def bind_tools(
    tools: typing.Sequence[typing.Any],
    kwargs: **kwargs,
) -> 'Runnable'
```
Format tools via the inner model, but bind them to *this* wrapper.

The inner model knows how to convert tools into its provider format; we
reuse that, then re-bind the resulting kwargs to ``self`` so the runnable
the deep agent invokes still routes generation through the durable
override (rather than the inner model directly).


| Parameter | Type | Description |
|-|-|-|
| `tools` | `typing.Sequence[typing.Any]` | |
| `kwargs` | `**kwargs` | |

### config_schema()

```python
def config_schema(
    include: Sequence[str] | None,
) -> type[BaseModel]
```
The type of config this `Runnable` accepts specified as a Pydantic model.

To mark a field as configurable, see the `configurable_fields`
and `configurable_alternatives` methods.



| Parameter | Type | Description |
|-|-|-|
| `include` | `Sequence[str] \| None` | A list of fields to include in the config schema. |

**Returns:** A Pydantic model that can be used to validate config.

### configurable_alternatives()

```python
def configurable_alternatives(
    which: ConfigurableField,
    default_key: str,
    prefix_keys: bool,
    kwargs: **kwargs,
) -> RunnableSerializable[Input, Output]
```
Configure alternatives for `Runnable` objects that can be set at runtime.

!!! example

    ```python
    from langchain_anthropic import ChatAnthropic
    from langchain_core.runnables.utils import ConfigurableField
    from langchain_openai import ChatOpenAI

    model = ChatAnthropic(
        model_name="claude-sonnet-4-5-20250929"
    ).configurable_alternatives(
        ConfigurableField(id="llm"),
        default_key="anthropic",
        openai=ChatOpenAI(),
    )

    # uses the default model ChatAnthropic
    print(model.invoke("which organization created you?").content)

    # uses ChatOpenAI
    print(
        model.with_config(configurable={"llm": "openai"})
        .invoke("which organization created you?")
        .content
    )
    ```


| Parameter | Type | Description |
|-|-|-|
| `which` | `ConfigurableField` | The `ConfigurableField` instance that will be used to select the alternative. |
| `default_key` | `str` | The default key to use if no alternative is selected. |
| `prefix_keys` | `bool` | Whether to prefix the keys with the `ConfigurableField` id. |
| `kwargs` | `**kwargs` | |

**Returns**

A new `Runnable` with the alternatives configured.


### configurable_fields()

```python
def configurable_fields(
    kwargs: **kwargs,
) -> RunnableSerializable[Input, Output]
```
Configure particular `Runnable` fields at runtime.

!!! example

    ```python
    from langchain_core.runnables import ConfigurableField
    from langchain_openai import ChatOpenAI

    model = ChatOpenAI(max_tokens=20).configurable_fields(
        max_tokens=ConfigurableField(
            id="output_token_number",
            name="Max tokens in the output",
            description="The maximum number of tokens in the output",
        )
    )

    # max_tokens = 20
    print(
        "max_tokens_20: ", model.invoke("tell me something about chess").content
    )

    # max_tokens = 200
    print(
        "max_tokens_200: ",
        model.with_config(configurable={"output_token_number": 200})
        .invoke("tell me something about chess")
        .content,
    )
    ```


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

**Returns**

A new `Runnable` with the fields configured.


**Raises**

| Exception | Description |
|-|-|
| `ValueError` | If a configuration key is not found in the `Runnable`. |

### dict()

```python
def dict(
    _kwargs: Any,
) -> builtins.dict[str, Any]
```
!!! deprecated "1.4.2 Use `asdict` instead. It will be removed in langchain-core==2.0.0."

DEPRECATED - use `asdict()` instead.

Return a dictionary representation of the chat model.


| Parameter | Type | Description |
|-|-|-|
| `_kwargs` | `Any` | |

### generate()

```python
def generate(
    messages: list[list[BaseMessage]],
    stop: list[str] | None,
    callbacks: Callbacks,
    tags: list[str] | None,
    metadata: builtins.dict[str, Any] | None,
    run_name: str | None,
    run_id: uuid.UUID | None,
    kwargs: **kwargs,
) -> LLMResult
```
Pass a sequence of prompts to the model and return model generations.

This method should make use of batched calls for models that expose a batched
API.

Use this method when you want to:

1. Take advantage of batched calls,
2. Need more output from the model than just the top generated value,
3. Are building chains that are agnostic to the underlying language model
    type (e.g., pure text completion models vs chat models).



| Parameter | Type | Description |
|-|-|-|
| `messages` | `list[list[BaseMessage]]` | List of list of messages. |
| `stop` | `list[str] \| None` | Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings. |
| `callbacks` | `Callbacks` | `Callbacks` to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation. |
| `tags` | `list[str] \| None` | The tags to apply. |
| `metadata` | `builtins.dict[str, Any] \| None` | The metadata to apply. |
| `run_name` | `str \| None` | The name of the run. |
| `run_id` | `uuid.UUID \| None` | The ID of the run. |
| `kwargs` | `**kwargs` | |

**Returns**

An `LLMResult`, which contains a list of candidate `Generations` for each
    input prompt and additional model provider-specific output.

### generate_prompt()

```python
def generate_prompt(
    prompts: list[PromptValue],
    stop: list[str] | None,
    callbacks: Callbacks,
    kwargs: **kwargs,
) -> LLMResult
```
Pass a sequence of prompts to the model and return model generations.

This method should make use of batched calls for models that expose a batched
API.

Use this method when you want to:

1. Take advantage of batched calls,
2. Need more output from the model than just the top generated value,
3. Are building chains that are agnostic to the underlying language model
    type (e.g., pure text completion models vs chat models).



| Parameter | Type | Description |
|-|-|-|
| `prompts` | `list[PromptValue]` | List of `PromptValue` objects. A `PromptValue` is an object that can be converted to match the format of any language model (string for pure text generation models and `BaseMessage` objects for chat models). |
| `stop` | `list[str] \| None` | Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings. |
| `callbacks` | `Callbacks` | `Callbacks` to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation. |
| `kwargs` | `**kwargs` | |

**Returns**

An `LLMResult`, which contains a list of candidate `Generation` objects for
    each input prompt and additional model provider-specific output.

### get_config_jsonschema()

```python
def get_config_jsonschema(
    include: Sequence[str] | None,
) -> dict[str, Any]
```
Get a JSON schema that represents the config of the `Runnable`.

!!! version-added "Added in `langchain-core` 0.3.0"


| Parameter | Type | Description |
|-|-|-|
| `include` | `Sequence[str] \| None` | A list of fields to include in the config schema. |

**Returns**

A JSON schema that represents the config of the `Runnable`.


### get_graph()

```python
def get_graph(
    config: RunnableConfig | None,
) -> Graph
```
Return a graph representation of this `Runnable`.


| Parameter | Type | Description |
|-|-|-|
| `config` | `RunnableConfig \| None` | |

### get_input_jsonschema()

```python
def get_input_jsonschema(
    config: RunnableConfig | None,
) -> dict[str, Any]
```
Get a JSON schema that represents the input to the `Runnable`.

!!! version-added "Added in `langchain-core` 0.3.0"


| Parameter | Type | Description |
|-|-|-|
| `config` | `RunnableConfig \| None` | A config to use when generating the schema. |

**Returns**

A JSON schema that represents the input to the `Runnable`.


### get_input_schema()

```python
def get_input_schema(
    config: RunnableConfig | None,
) -> TypeBaseModel
```
Get a Pydantic model that can be used to validate input to the `Runnable`.

`Runnable` objects that leverage the `configurable_fields` and
`configurable_alternatives` methods will have a dynamic input schema that
depends on which configuration the `Runnable` is invoked with.

This method allows to get an input schema for a specific configuration.



| Parameter | Type | Description |
|-|-|-|
| `config` | `RunnableConfig \| None` | A config to use when generating the schema. |

**Returns:** A Pydantic model that can be used to validate input.

### get_lc_namespace()

```python
def get_lc_namespace()
```
Get the namespace of the LangChain object.

The default implementation splits `cls.__module__` on `'.'`, e.g.
`langchain_openai.chat_models` becomes
`["langchain_openai", "chat_models"]`. This value is used by `lc_id` to
build the serialization identifier.

New partner packages should **not** override this method. The default
behavior is correct for any class whose module path already reflects
its package name. Some older packages (e.g. `langchain-openai`,
`langchain-anthropic`) override it to return a legacy-style namespace
like `["langchain", "chat_models", "openai"]`, matching the module
paths that existed before those integrations were split out of the
main `langchain` package. Those overrides are kept for
backwards-compatible deserialization; new packages should not copy them.

Deserialization mapping is handled separately by
`SERIALIZABLE_MAPPING` in `langchain_core.load.mapping`.



**Returns:** The namespace.

### get_name()

```python
def get_name(
    suffix: str | None,
    name: str | None,
) -> str
```
Get the name of the `Runnable`.



| Parameter | Type | Description |
|-|-|-|
| `suffix` | `str \| None` | An optional suffix to append to the name. |
| `name` | `str \| None` | An optional name to use instead of the `Runnable`'s name. |

**Returns:** The name of the `Runnable`.

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
    tools,
) -> int
```
Get the number of tokens in the messages.

Useful for checking if an input fits in a model's context window.

This should be overridden by model-specific implementations to provide accurate
token counts via model-specific tokenizers.

> [!NOTE]

    * The base implementation of `get_num_tokens_from_messages` ignores tool
        schemas.
    * The base implementation of `get_num_tokens_from_messages` adds additional
        prefixes to messages in represent user roles, which will add to the
        overall token count. Model-specific implementations may choose to
        handle this differently.



| Parameter | Type | Description |
|-|-|-|
| `messages` |  | The message inputs to tokenize. |
| `tools` |  | If provided, sequence of dict, `BaseModel`, function, or `BaseTool` objects to be converted to tool schemas. |

**Returns:** The sum of the number of tokens across the messages.

### get_output_jsonschema()

```python
def get_output_jsonschema(
    config: RunnableConfig | None,
) -> dict[str, Any]
```
Get a JSON schema that represents the output of the `Runnable`.

!!! version-added "Added in `langchain-core` 0.3.0"


| Parameter | Type | Description |
|-|-|-|
| `config` | `RunnableConfig \| None` | A config to use when generating the schema. |

**Returns**

A JSON schema that represents the output of the `Runnable`.


### get_output_schema()

```python
def get_output_schema(
    config: RunnableConfig | None,
) -> TypeBaseModel
```
Get a Pydantic model that can be used to validate output to the `Runnable`.

`Runnable` objects that leverage the `configurable_fields` and
`configurable_alternatives` methods will have a dynamic output schema that
depends on which configuration the `Runnable` is invoked with.

This method allows to get an output schema for a specific configuration.



| Parameter | Type | Description |
|-|-|-|
| `config` | `RunnableConfig \| None` | A config to use when generating the schema. |

**Returns:** A Pydantic model that can be used to validate output.

### get_prompts()

```python
def get_prompts(
    config: RunnableConfig | None,
) -> list[BasePromptTemplate[Any]]
```
Return a list of prompts used by this `Runnable`.


| Parameter | Type | Description |
|-|-|-|
| `config` | `RunnableConfig \| None` | |

### get_token_ids()

```python
def get_token_ids(
    text: str,
) -> list[int]
```
Return the ordered IDs of the tokens in a text.



| Parameter | Type | Description |
|-|-|-|
| `text` | `str` | The string input to tokenize. |

**Returns**

A list of IDs corresponding to the tokens in the text, in order they occur
    in the text.

### invoke()

```python
def invoke(
    input: LanguageModelInput,
    config: RunnableConfig | None,
    stop: list[str] | None,
    kwargs: **kwargs,
) -> AIMessage
```
Transform a single input into an output.



| Parameter | Type | Description |
|-|-|-|
| `input` | `LanguageModelInput` | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. |
| `stop` | `list[str] \| None` | |
| `kwargs` | `**kwargs` | |

**Returns:** The output of the `Runnable`.

### is_lc_serializable()

```python
def is_lc_serializable()
```
Is this class serializable?

By design, even if a class inherits from `Serializable`, it is not serializable
by default. This is to prevent accidental serialization of objects that should
not be serialized.



**Returns:** Whether the class is serializable. Default is `False`.

### lc_id()

```python
def lc_id()
```
Return a unique identifier for this class for serialization purposes.

The unique identifier is a list of strings that describes the path
to the object.

For example, for the class `langchain.llms.openai.OpenAI`, the id is
`["langchain", "llms", "openai", "OpenAI"]`.


### map()

```python
def map()
```
Return a new `Runnable` that maps a list of inputs to a list of outputs.

Calls `invoke` with each input.



**Returns**

A new `Runnable` that maps a list of inputs to a list of outputs.


### model_post_init()

```python
def model_post_init(
    _context: Any,
)
```
Pydantic V2 lifecycle hook called automatically after `__init__`.

Seeds `metadata["lc_versions"]` with the installed `langchain-core`
(and `langchain`, if installed) versions so that every LLM trace
carries the package versions that produced it.

Partner packages should **not** override this method. Instead, they
should define a `@model_validator(mode="after")` that calls
`_add_version` to append their own version to the same dict.

> [!WARNING] Validator

    Each subclass's validator **must** have a unique name. Pydantic
    replaces — rather than chains — same-named `model_validator` methods
    in child classes. For example, a `BaseChatOpenAI` subclass should
    use `_set_&lt;partner&gt;_version`, not `_set_version`, to avoid silently
    dropping the parent's entry.



| Parameter | Type | Description |
|-|-|-|
| `_context` | `Any` | Pydantic validation context (typically `None`). |

### pick()

```python
def pick(
    keys: str | list[str],
) -> RunnableSerializable[Any, Any]
```
Pick keys from the output `dict` of this `Runnable`.

!!! example "Pick a single key"

    ```python
    import json

    from langchain_core.runnables import RunnableLambda, RunnableMap

    as_str = RunnableLambda(str)
    as_json = RunnableLambda(json.loads)
    chain = RunnableMap(str=as_str, json=as_json)

    chain.invoke("[1, 2, 3]")
    # -> {"str": "[1, 2, 3]", "json": [1, 2, 3]}

    json_only_chain = chain.pick("json")
    json_only_chain.invoke("[1, 2, 3]")
    # -> [1, 2, 3]
    ```

!!! example "Pick a list of keys"

    ```python
    from typing import Any

    import json

    from langchain_core.runnables import RunnableLambda, RunnableMap

    as_str = RunnableLambda(str)
    as_json = RunnableLambda(json.loads)


    def as_bytes(x: Any) -> bytes:
        return bytes(x, "utf-8")


    chain = RunnableMap(
        str=as_str, json=as_json, bytes=RunnableLambda(as_bytes)
    )

    chain.invoke("[1, 2, 3]")
    # -> {"str": "[1, 2, 3]", "json": [1, 2, 3], "bytes": b"[1, 2, 3]"}

    json_and_bytes_chain = chain.pick(["json", "bytes"])
    json_and_bytes_chain.invoke("[1, 2, 3]")
    # -> {"json": [1, 2, 3], "bytes": b"[1, 2, 3]"}
    ```



| Parameter | Type | Description |
|-|-|-|
| `keys` | `str \| list[str]` | A key or list of keys to pick from the output dict. |

**Returns:** a new `Runnable`.

### pipe()

```python
def pipe(
    others: Runnable[Any, Other] | Callable[[Any], Other],
    name: str | None,
) -> RunnableSerializable[Input, Other]
```
Pipe `Runnable` objects.

Compose this `Runnable` with `Runnable`-like objects to make a
`RunnableSequence`.

Equivalent to `RunnableSequence(self, *others)` or `self | others[0] | ...`



| Parameter | Type | Description |
|-|-|-|
| `others` | `Runnable[Any, Other] \| Callable[[Any], Other]` | |
| `name` | `str \| None` | An optional name for the resulting `RunnableSequence`. |

**Returns:** A new `Runnable`.

### set_verbose()

```python
def set_verbose(
    verbose: bool | None,
) -> bool
```
If verbose is `None`, set it.

This allows users to pass in `None` as verbose to access the global setting.



| Parameter | Type | Description |
|-|-|-|
| `verbose` | `bool \| None` | The verbosity setting to use. |

**Returns:** The verbosity setting to use.

### stream()

```python
def stream(
    input: LanguageModelInput,
    config: RunnableConfig | None,
    stop: list[str] | None,
    kwargs: **kwargs,
) -> Iterator[AIMessageChunk]
```
Default implementation of `stream`, which calls `invoke`.

Subclasses must override this method if they support streaming output.

Yields:
    The output of the `Runnable`.


| Parameter | Type | Description |
|-|-|-|
| `input` | `LanguageModelInput` | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | The config to use for the `Runnable`. |
| `stop` | `list[str] \| None` | |
| `kwargs` | `**kwargs` | |

### stream_events()

```python
def stream_events(
    input: LanguageModelInput,
    config: RunnableConfig | None,
    version: Literal['v1', 'v2', 'v3'],
    stop: list[str] | None,
    kwargs: **kwargs,
) -> Iterator[StreamEvent] | ChatModelStream
```
Stream events from this chat model.

For `version="v1"` / `"v2"`, yields `StreamEvent` dicts (see
`Runnable.stream_events`). For `version="v3"`, returns a
`ChatModelStream` exposing typed projections (`.text`,
`.reasoning`, `.tool_calls`, `.output`).

> [!WARNING] Beta

    `version="v3"` is in beta. The protocol shape, return type,
    and surface area may change in future releases. Calling it
    emits a `LangChainBetaWarning` at runtime.

> [!NOTE]

    `ChatModelStream.output.content` is always a list of v1
    content blocks (text / reasoning / tool_call / image / …),
    regardless of the model's `output_version` attribute. The
    setting only affects the legacy `stream()` / `astream()` /
    `invoke()` paths. If you're mixing
    `stream_events(version="v3")` with those paths in the same
    pipeline and need a consistent output shape across them,
    set `output_version="v1"` on the model.



| Parameter | Type | Description |
|-|-|-|
| `input` | `LanguageModelInput` | The model input. |
| `config` | `RunnableConfig \| None` | Optional runnable config. |
| `version` | `Literal['v1', 'v2', 'v3']` | Streaming-event schema version. `"v3"` selects the content-block-centric streaming protocol. |
| `stop` | `list[str] \| None` | Optional stop sequences. Only used for `version="v3"`; ignored otherwise. |
| `kwargs` | `**kwargs` | |

**Returns**

For `version="v3"`, a `ChatModelStream` with typed
projections. Otherwise an `Iterator[StreamEvent]`.

### to_json()

```python
def to_json()
```
Serialize the `Runnable` to JSON.



**Returns:** A JSON-serializable representation of the `Runnable`.

### to_json_not_implemented()

```python
def to_json_not_implemented()
```
Serialize a "not implemented" object.



**Returns:** `SerializedNotImplemented`.

### transform()

```python
def transform(
    input: Iterator[Input],
    config: RunnableConfig | None,
    kwargs: **kwargs,
) -> Iterator[Output]
```
Transform inputs to outputs.

Default implementation of transform, which buffers input and calls `astream`.

Subclasses must override this method if they can start producing output while
input is still being generated.

Yields:
    The output of the `Runnable`.


| Parameter | Type | Description |
|-|-|-|
| `input` | `Iterator[Input]` | An iterator of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| None` | The config to use for the `Runnable`. |
| `kwargs` | `**kwargs` | |

### with_alisteners()

```python
def with_alisteners(
    on_start: AsyncListener | None,
    on_end: AsyncListener | None,
    on_error: AsyncListener | None,
) -> Runnable[Input, Output]
```
Bind async lifecycle listeners to a `Runnable`.

Returns a new `Runnable`.

The Run object contains information about the run, including its `id`,
`type`, `input`, `output`, `error`, `start_time`, `end_time`, and
any tags or metadata added to the run.



| Parameter | Type | Description |
|-|-|-|
| `on_start` | `AsyncListener \| None` | Called asynchronously before the `Runnable` starts running, with the `Run` object. |
| `on_end` | `AsyncListener \| None` | Called asynchronously after the `Runnable` finishes running, with the `Run` object. |
| `on_error` | `AsyncListener \| None` | Called asynchronously if the `Runnable` throws an error, with the `Run` object. |

**Returns**

A new `Runnable` with the listeners bound.


### with_config()

```python
def with_config(
    config: RunnableConfig | None,
    kwargs: **kwargs,
) -> Runnable[Input, Output]
```
Bind config to a `Runnable`, returning a new `Runnable`.



| Parameter | Type | Description |
|-|-|-|
| `config` | `RunnableConfig \| None` | The config to bind to the `Runnable`. |
| `kwargs` | `**kwargs` | |

**Returns:** A new `Runnable` with the config bound.

### with_fallbacks()

```python
def with_fallbacks(
    fallbacks: Sequence[Runnable[Input, Output]],
    exceptions_to_handle: tuple[type[BaseException], ...],
    exception_key: str | None,
) -> RunnableWithFallbacksT[Input, Output]
```
Add fallbacks to a `Runnable`, returning a new `Runnable`.

The new `Runnable` will try the original `Runnable`, and then each fallback
in order, upon failures.



| Parameter | Type | Description |
|-|-|-|
| `fallbacks` | `Sequence[Runnable[Input, Output]]` | A sequence of runnables to try if the original `Runnable` fails. |
| `exceptions_to_handle` | `tuple[type[BaseException], ...]` | A tuple of exception types to handle. |
| `exception_key` | `str \| None` | If `string` is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If `None`, exceptions will not be passed to fallbacks. If used, the base `Runnable` and its fallbacks must accept a dictionary as input. |

**Returns**

A new `Runnable` that will try the original `Runnable`, and then each
    Fallback in order, upon failures.

A new `Runnable` that will try the original `Runnable`, and then each
    Fallback in order, upon failures.

### with_listeners()

```python
def with_listeners(
    on_start: Callable[[Run], None] | Callable[[Run, RunnableConfig], None] | None,
    on_end: Callable[[Run], None] | Callable[[Run, RunnableConfig], None] | None,
    on_error: Callable[[Run], None] | Callable[[Run, RunnableConfig], None] | None,
) -> Runnable[Input, Output]
```
Bind lifecycle listeners to a `Runnable`, returning a new `Runnable`.

The Run object contains information about the run, including its `id`,
`type`, `input`, `output`, `error`, `start_time`, `end_time`, and
any tags or metadata added to the run.



| Parameter | Type | Description |
|-|-|-|
| `on_start` | `Callable[[Run], None] \| Callable[[Run, RunnableConfig], None] \| None` | Called before the `Runnable` starts running, with the `Run` object. |
| `on_end` | `Callable[[Run], None] \| Callable[[Run, RunnableConfig], None] \| None` | Called after the `Runnable` finishes running, with the `Run` object. |
| `on_error` | `Callable[[Run], None] \| Callable[[Run, RunnableConfig], None] \| None` | Called if the `Runnable` throws an error, with the `Run` object. |

**Returns**

A new `Runnable` with the listeners bound.


### with_retry()

```python
def with_retry(
    retry_if_exception_type: tuple[type[BaseException], ...],
    wait_exponential_jitter: bool,
    exponential_jitter_params: ExponentialJitterParams | None,
    stop_after_attempt: int,
) -> Runnable[Input, Output]
```
Create a new `Runnable` that retries the original `Runnable` on exceptions.



| Parameter | Type | Description |
|-|-|-|
| `retry_if_exception_type` | `tuple[type[BaseException], ...]` | A tuple of exception types to retry on. |
| `wait_exponential_jitter` | `bool` | Whether to add jitter to the wait time between retries. |
| `exponential_jitter_params` | `ExponentialJitterParams \| None` | Parameters for `tenacity.wait_exponential_jitter`. Namely: `initial`, `max`, `exp_base`, and `jitter` (all `float` values). |
| `stop_after_attempt` | `int` | The maximum number of attempts to make before giving up. |

**Returns**

A new `Runnable` that retries the original `Runnable` on exceptions.


### with_structured_output()

```python
def with_structured_output(
    schema: builtins.dict[str, Any] | type,
    include_raw: bool,
    kwargs: **kwargs,
) -> Runnable[LanguageModelInput, builtins.dict[str, Any] | BaseModel]
```
Model wrapper that returns outputs formatted to match the given schema.

???+ example "Pydantic schema (`include_raw=False`)"

    ```python
    from pydantic import BaseModel


    class AnswerWithJustification(BaseModel):
        '''An answer to the user question along with justification for the answer.'''

        answer: str
        justification: str


    model = ChatModel(model="model-name", temperature=0)
    structured_model = model.with_structured_output(AnswerWithJustification)

    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )

    # -> AnswerWithJustification(
    #     answer='They weigh the same',
    #     justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.'
    # )
    ```

??? example "Pydantic schema (`include_raw=True`)"

    ```python
    from pydantic import BaseModel


    class AnswerWithJustification(BaseModel):
        '''An answer to the user question along with justification for the answer.'''

        answer: str
        justification: str


    model = ChatModel(model="model-name", temperature=0)
    structured_model = model.with_structured_output(
        AnswerWithJustification, include_raw=True
    )

    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )
    # -> {
    #     'raw': AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_Ao02pnFYXD6GN1yzc0uXPsvF', 'function': {'arguments': '{"answer":"They weigh the same.","justification":"Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ."}', 'name': 'AnswerWithJustification'}, 'type': 'function'}]}),
    #     'parsed': AnswerWithJustification(answer='They weigh the same.', justification='Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.'),
    #     'parsing_error': None
    # }
    ```

??? example "Dictionary schema (`include_raw=False`)"

    ```python
    from pydantic import BaseModel
    from langchain_core.utils.function_calling import convert_to_openai_tool


    class AnswerWithJustification(BaseModel):
        '''An answer to the user question along with justification for the answer.'''

        answer: str
        justification: str


    dict_schema = convert_to_openai_tool(AnswerWithJustification)
    model = ChatModel(model="model-name", temperature=0)
    structured_model = model.with_structured_output(dict_schema)

    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )
    # -> {
    #     'answer': 'They weigh the same',
    #     'justification': 'Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume and density of the two substances differ.'
    # }
    ```

> [!WARNING] Behavior

    Added support for `TypedDict` class.


| Parameter | Type | Description |
|-|-|-|
| `schema` | `builtins.dict[str, Any] \| type` | The output schema. Can be passed in as: - An OpenAI function/tool schema, - A JSON Schema, - A `TypedDict` class, - Or a Pydantic class. If `schema` is a Pydantic class then the model output will be a Pydantic instance of that class, and the model-generated fields will be validated by the Pydantic class. Otherwise the model output will be a dict and will not be validated. See `langchain_core.utils.function_calling.convert_to_openai_tool` for more on how to properly specify types and descriptions of schema fields when specifying a Pydantic or `TypedDict` class. |
| `include_raw` | `bool` | If `False` then only the parsed structured output is returned. If an error occurs during model output parsing it will be raised. If `True` then both the raw model response (a `BaseMessage`) and the parsed model response will be returned. If an error occurs during output parsing it will be caught and returned as well. The final output is always a `dict` with keys `'raw'`, `'parsed'`, and `'parsing_error'`. |
| `kwargs` | `**kwargs` | |

**Returns**

A `Runnable` that takes same inputs as a
    `langchain_core.language_models.chat.BaseChatModel`. If `include_raw` is
    `False` and `schema` is a Pydantic class, `Runnable` outputs an instance
    of `schema` (i.e., a Pydantic object). Otherwise, if `include_raw` is
    `False` then `Runnable` outputs a `dict`.

    If `include_raw` is `True`, then `Runnable` outputs a `dict` with keys:

    - `'raw'`: `BaseMessage`
    - `'parsed'`: `None` if there was a parsing error, otherwise the type
        depends on the `schema` as described above.
    - `'parsing_error'`: `BaseException | None`


**Raises**

| Exception | Description |
|-|-|
| `ValueError` | If there are any unsupported `kwargs`. |
| `NotImplementedError` | If the model does not implement `with_structured_output()`. |

### with_types()

```python
def with_types(
    input_type: type[Input] | None,
    output_type: type[Output] | None,
) -> Runnable[Input, Output]
```
Bind input and output types to a `Runnable`, returning a new `Runnable`.



| Parameter | Type | Description |
|-|-|-|
| `input_type` | `type[Input] \| None` | The input type to bind to the `Runnable`. |
| `output_type` | `type[Output] \| None` | The output type to bind to the `Runnable`. |

**Returns:** A new `Runnable` with the types bound.

