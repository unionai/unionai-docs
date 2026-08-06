---
title: OpenAI
weight: 2
variants: +flyte +union
---

# OpenAI Agents SDK

Run [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) agents on Flyte. The SDK's `Runner` still drives the loop, including handoffs, guardrails and structured output. Flyte supplies the runtime: tools become durable child actions, model turns replay on retry, and the SDK's trace telemetry renders into the task report instead of being shipped to OpenAI's traces dashboard.

## Installation

```bash
pip install flyteplugins-agents-openai
```

Requires Python 3.10 or later.

## Quick start

```python{hl_lines=[2, 6, 11, "20-25"]}
import flyte
from flyteplugins.agents.openai import run_agent, tool

env = flyte.TaskEnvironment(
    "openai-agent",
    secrets=[flyte.Secret(key="openai_api_key", as_env_var="OPENAI_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-agents-openai"),
)


@tool
@env.task(cache="auto", retries=3)
async def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny, 22C."


@env.task(report=True, retries=3)
async def city_agent(question: str) -> str:
    return await run_agent(
        question,
        tools=[get_weather],
        instructions="You are a concise assistant. Use the tools to answer.",
        model="gpt-4.1",
    )
```

The API key is read from the environment, so it never lands in task inputs. Wire it as a Flyte secret.

## How it maps to Flyte

**Tools:** `tool` turns an `@env.task` into an `agents.FunctionTool`. The SDK derives the JSON schema, name and description from the task signature, so strict tool calling works unchanged. When the agent invokes the tool, the call dispatches to the task instead of running inline.

Applied to a plain function or a `@flyte.trace` helper, `tool` forwards to the SDK's native `function_tool`, so you can mix durable and inline tools in one agent.

**Model turns:** `FlyteModelProvider` wraps whatever `ModelProvider` the run is configured with and records each turn through `flyte.trace`. That is the seam directly below the loop, so the `Runner` above it is untouched.

**Tracing:** `install_flyte_tracing()` registers a trace processor that forwards turns, tool calls, handoffs and token usage into the Flyte report. It runs with `exclusive=True` by default, which replaces the SDK's trace processors so the run's trace telemetry is not exported to OpenAI's traces dashboard. Pass `exclusive=False` to keep the SDK's default exporter and render into the report alongside it.

This applies to the observability spans, not the inference. The model calls themselves still go to OpenAI whenever you use an OpenAI model, carrying the prompts, tool schemas, tool-call arguments and completions, because that is how the model runs. To keep prompt data off OpenAI entirely, point the run at a self-hosted or OpenAI-compatible endpoint with a custom `RunConfig(model_provider=...)`, which is a separate choice from tracing.

## Bring your own agent

If you already have an `agents.Agent` with handoffs and guardrails configured, pass it through. Durability spans the handoff: a crash mid-chain replays both agents' turns.

```python{hl_lines=[3, 8]}
from agents import Agent

triage = Agent(name="triage", handoffs=[billing, technical], input_guardrails=[...])


@env.task(report=True, retries=3)
async def support(request: str) -> str:
    return await run_agent(request, agent=triage)
```

`agent` and `tools` are mutually exclusive. A pre-built agent carries its own tools.

## Custom run configuration

Pass a `RunConfig` to control the client, model settings or provider. The `model_provider` you set is wrapped for durability unless you pass `durable=False`.

```python{hl_lines=[1, 12]}
from agents import OpenAIProvider, RunConfig
from openai import AsyncOpenAI


@env.task(report=True, retries=3)
async def city_agent(question: str) -> str:
    client = AsyncOpenAI(max_retries=5, timeout=30)
    return await run_agent(
        question,
        tools=[get_weather],
        model="gpt-4.1",
        run_config=RunConfig(model_provider=OpenAIProvider(openai_client=client)),
    )
```

Client-level retries sit below the durable wrapper, so a 429 is retried in place and the turn is recorded only once it succeeds.

## Memory

```python
await run_agent(message, model="gpt-4.1", memory_key="user-alice")
```

This backs the SDK's `Session` with a durable, keyed `MemoryStore` on object storage. The SDK's default session is local SQLite, which does not survive a distributed backend. The same store also holds path-addressed facts for long-term recall.

See [How it works](./how-it-works) for the full memory model.

## Building blocks

`run_agent` wires three independently usable pieces together. Reach for them directly when you want to drive `Runner.run` yourself.

| Export | Purpose |
|---|---|
| `tool` | Turn a Flyte task into an Agents SDK tool |
| `FunctionTool` | The task-backed `FunctionTool` subclass `tool` produces |
| `FlyteModelProvider` | Set on `RunConfig.model_provider` for durable turns |
| `FlyteModel` | The per-model durable wrapper the provider hands out |
| `FlyteSession` | The `MemoryStore`-backed `Session` implementation |
| `install_flyte_tracing` | Register the Flyte trace processor |
| `FlyteTracingProcessor` | The processor itself, if you want to configure it |

## `run_agent` parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `str \| list` | required | The user prompt, or a list of input items |
| `agent` | `Agent \| None` | `None` | A pre-built `agents.Agent`. Mutually exclusive with `tools` |
| `tools` | `Sequence` | `()` | Tools to expose. Accepts `tool`-wrapped tools or bare `@env.task` templates |
| `model` | `str` | `"gpt-4.1"` | Model name, when `agent` is not given |
| `instructions` | `str \| None` | `None` | System instructions, when `agent` is not given |
| `name` | `str` | `"flyte-agent"` | Agent name, when `agent` is not given |
| `max_turns` | `int` | `10` | Maximum model-to-tool turns before the SDK raises |
| `durable` | `bool` | `True` | Record and replay each model turn |
| `observability` | `bool` | `True` | Render the timeline into the task report |
| `run_config` | `RunConfig \| None` | `None` | Custom run configuration. Its `model_provider` is wrapped unless `durable=False` |
| `memory_key` | `str \| None` | `None` | Stable user or thread ID for cross-run memory |

Returns the agent's final output as a string. Use `run_agent_sync` with the same signature from a sync task.

## Notes

- Streamed runs via `Runner.run_streamed` are not memoized per turn in this version. Tool calls remain durable.
- `max_turns` counts model-to-tool turns, not model calls. To bound the whole run in wall-clock terms, set `timeout=` on the enclosing task.

## Examples

Full runnable examples live in the SDK repository under [`plugins/agents/openai/examples`](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/agents/openai/examples):

- `openai_durable_agent.py`: a single durable agent, with both the async and sync call forms.
- `openai_multi_agent.py`: a planner, parallel researchers and an editor, each its own durable action.
- `openai_handoffs.py`: handoffs plus a human approval gate on a sensitive refund tool.
- `openai_crash_resume.py`: the task crashes on its first attempt and finishes on retry without re-calling the model.
- `openai_memory.py`: two separate runs sharing a `memory_key`.
