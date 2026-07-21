---
title: Google ADK
weight: 4
variants: +flyte +union
---

# Google ADK

Run [Google ADK](https://github.com/google/adk-python) (Agent Development Kit) agents on Flyte. ADK's `Runner` drives the loop and yields events. Flyte supplies the runtime: tools become durable child actions, each model turn is recorded for replay, and the event stream renders into the task report.

## Installation

```bash
pip install flyteplugins-agents-google
```

Requires Python 3.10 or later and `google-adk` 2.0 or later.

## Quick start

```python{hl_lines=[2, 6, 11, 20]}
import flyte
from flyteplugins.agents.google import run_agent, tool

env = flyte.TaskEnvironment(
    "google-agent",
    secrets=[flyte.Secret(key="google_api_key", as_env_var="GOOGLE_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-agents-google"),
)


@tool
@env.task(cache="auto", retries=3)
async def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny, 22C."


@env.task(report=True, retries=3)
async def city_agent(question: str) -> str:
    return await run_agent(question, tools=[get_weather], model="gemini-2.0-flash")
```

Credentials come from the environment, whether that is `GOOGLE_API_KEY` for Gemini or your Vertex AI configuration. Wire them as Flyte secrets so they cannot leak into task inputs.

## How it maps to Flyte

**Tools:** ADK accepts plain Python callables and derives the tool declaration from the signature. `tool` produces one whose body dispatches to `task.aio()`, so each call runs as a durable child action.

**Model turns:** With `durable=True`, the agent's model is wrapped in `FlyteLlm`, which records each pass through `BaseLlm.generate_content_async` via `flyte.trace`. That method is the seam directly below the loop, the ADK equivalent of swapping OpenAI's `ModelProvider`. On a retry, completed turns replay from their recorded `LlmResponse` and tool calls come back from cache.

**Observability:** Turns and tool calls render into the report, followed by a usage row summarizing model turns, prompt tokens, completion tokens and total tokens. Gemini's context-cache tokens appear as `cached`, and thinking tokens as `thinking` on models that report them.

## Bring your own agent

Pass a pre-built `LlmAgent` or any `BaseAgent`, including a tree with sub-agent transfers.

```python{hl_lines=[4]}
from google.adk.agents import LlmAgent
from flyteplugins.agents.google import durable_model

triage = LlmAgent(
    name="triage",
    model=durable_model("gemini-2.0-flash"),
    instruction="Route the request to the right specialist.",
    sub_agents=[billing, technical],
)


@env.task(report=True, retries=3)
async def support(request: str) -> str:
    return await run_agent(request, agent=triage)
```

`run_agent` cannot reach inside a pre-built tree to wrap the models, so wrap them yourself with `durable_model` when you want per-turn replay on that path. Tool calls stay durable regardless.

`agent` and `tools` are mutually exclusive.

## Memory

```python
await run_agent(message, model="gemini-2.0-flash", memory_key="user-alice")
```

ADK keeps the conversation as a list of `Event` objects on the session. Those events are persisted to a durable, keyed `MemoryStore` and restored into a fresh session on the next run with the same key.

## Bounding a run

`max_llm_calls` caps model calls before ADK raises `LlmCallsLimitExceededError`, its runaway-loop guard. It counts LLM calls rather than conversational turns, so a single tool round is roughly two calls. Leaving it at `None` uses ADK's default of 500.

For a wall-clock bound on the whole run, including tool calls, set `timeout=` on the enclosing task instead.

## `run_agent` parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `str` | required | The user prompt |
| `agent` | `Any` | `None` | A pre-built ADK agent. Mutually exclusive with `tools` |
| `tools` | `Sequence` | `()` | Tools to expose. Accepts `tool`-wrapped tools or bare `@env.task` templates |
| `model` | `str` | `"gemini-2.0-flash"` | Model name, when `agent` is not given |
| `instructions` | `str \| None` | `None` | System instruction, when `agent` is not given |
| `name` | `str` | `"assistant"` | Agent name. Must be a valid Python identifier |
| `max_llm_calls` | `int \| None` | `None` | Cap on model calls. `None` uses ADK's default of 500 |
| `durable` | `bool` | `True` | Record and replay each model turn |
| `observability` | `bool` | `True` | Render the timeline into the task report |
| `memory_key` | `str \| None` | `None` | Stable user or thread ID for cross-run memory |
| `app_name` | `str` | `"flyte-agent"` | ADK app name, used for namespacing |
| `user_id` | `str` | `"flyte-user"` | ADK user ID |

Returns the final text. Use `run_agent_sync` with the same signature from a sync task.

> [!NOTE] `name` is visible to the model
> ADK injects the agent name into the system prompt as the model's internal name, so it can surface in replies. Keep it natural. An internal or brand-heavy label will show up in the conversation.

## Examples

Full runnable examples live in the SDK repository under [`plugins/agents/google/examples`](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/agents/google/examples):

- `google_durable_agent.py`: a single durable agent with traced model turns.
- `google_multi_agent.py`: a planner, parallel researchers and an editor, each its own durable action.
- `google_crash_resume.py`: the task crashes on its first attempt and replays completed turns on retry.
- `google_memory.py`: two separate runs sharing a `memory_key`.
- `google_handoffs.py`: native agent transfer to a specialist sub-agent, which can pause on a Flyte condition for a human to supply details mid-conversation.
