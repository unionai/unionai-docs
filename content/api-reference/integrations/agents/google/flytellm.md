---
title: FlyteLlm
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# FlyteLlm

**Package:** `flyteplugins.agents.google`

A `BaseLlm` that records each model turn via `durable_step` for replay.

Wraps an inner `BaseLlm` (resolved from the agent's `model`); `model` is set
to the inner model name so ADK behaves identically. Construct via
`flyteplugins.agents.google.durable_model`.


## Parameters

```python
class FlyteLlm(
    model: str,
    inner: typing.Any = None,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `model` | `str` | |
| `inner` | `typing.Any` | |

## Methods

| Method | Description |
|-|-|
| [`generate_content_async()`](#generate_content_async) | Generates content for a single model turn. |


### generate_content_async()

```python
def generate_content_async(
    llm_request: typing.Any,
    stream: bool = False,
) -> typing.AsyncGenerator[typing.Any, None]
```
Generates content for a single model turn.

This method handles Server-Sent Events (SSE) streaming for unidirectional
content generation. For bidirectional streaming (e.g., Gemini Live API),
use the `connect()` method instead.

Yields:
  LlmResponse objects representing the model's response for one turn.

  **Non-streaming mode (stream=False):**

    Yields exactly one LlmResponse containing the complete model output
    (text, function calls, bytes, etc.). This response has `partial=False`.

  **Streaming mode (stream=True):**

    Yields multiple LlmResponse objects as chunks arrive:

    - Intermediate chunks: `partial=True` (progressive updates)
    - Final chunk: `partial=False` (aggregated content from entire turn,
      identical to stream=False output)
    - Text consolidation: Consecutive text parts of the same type
      (thought/non-thought) SHOULD merge without separator, but client
      code must not rely on this - unconsolidated parts are unusual but also
      valid

  **Common content in partial chunks:**

    All intermediate chunks have `partial=True` regardless of content type.
    Common examples include:

    - Text: Streams incrementally as tokens arrive
    - Function calls: May arrive in separate chunks
    - Bytes (e.g., images): Typically arrive as single chunk, interleaved
      with text
    - Thoughts: Stream incrementally when thinking_config is enabled

  **Examples:**

  1. Simple text streaming::

       LlmResponse(partial=True,  parts=["The weather"])
       LlmResponse(partial=True,  parts=[" in Tokyo is"])
       LlmResponse(partial=True,  parts=[" sunny."])
       LlmResponse(partial=False, parts=["The weather in Tokyo is sunny."])

  2. Text + function call::

       LlmResponse(partial=True,  parts=[Text("Let me check...")])
       LlmResponse(partial=True,  parts=[FunctionCall("get_weather", ...)])
       LlmResponse(partial=False, parts=[Text("Let me check..."),
                                         FunctionCall("get_weather", ...)])

  3. Parallel function calls across chunks::

       LlmResponse(partial=True,  parts=[Text("Checking both cities...")])
       LlmResponse(partial=True,  parts=[FunctionCall("get_weather", Tokyo)])
       LlmResponse(partial=True,  parts=[FunctionCall("get_weather", NYC)])
       LlmResponse(partial=False, parts=[Text("Checking both cities..."),
                                         FunctionCall("get_weather", Tokyo),
                                         FunctionCall("get_weather", NYC)])

  4. Text + bytes (image generation with gemini-2.5-flash-image)::

       LlmResponse(partial=True,  parts=[Text("Here's an image of a dog.")])
       LlmResponse(partial=True,  parts=[Text("
")])
       LlmResponse(partial=True,  parts=[Blob(image/png, 1.6MB)])
       LlmResponse(partial=True,  parts=[Text("It carries a bone")])
       LlmResponse(partial=True,  parts=[Text(" and running around.")])
       LlmResponse(partial=False, parts=[Text("Here's an image of a dog.
"),
                                         Blob(image/png, 1.6MB),
                                         Text("It carries a bone and running around.")])

     Note: Consecutive text parts before and after blob merge separately.

  5. Text with thinking (gemini-2.5-flash with thinking_config)::

       LlmResponse(partial=True,  parts=[Thought("Let me analyze...")])
       LlmResponse(partial=True,  parts=[Thought("The user wants...")])
       LlmResponse(partial=True,  parts=[Text("Based on my analysis,")])
       LlmResponse(partial=True,  parts=[Text(" the answer is 42.")])
       LlmResponse(partial=False, parts=[Thought("Let me analyze...The user wants..."),
                                         Text("Based on my analysis, the answer is 42.")])

     Note: Consecutive parts of same type merge (thoughts→thought, text→text).

  **Important:** All yielded responses represent one logical model turn.
  The final response with `partial=False` should be identical to the
  response that would be received with `stream=False`.



| Parameter | Type | Description |
|-|-|-|
| `llm_request` | `typing.Any` | LlmRequest, the request to send to the LLM. |
| `stream` | `bool` | bool = False, whether to enable SSE streaming mode. |

