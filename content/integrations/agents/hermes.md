---
title: Hermes
weight: 11
variants: +flyte +union
---

# Hermes

Run [Hermes](https://pypi.org/project/hermes-agent/) agents on Flyte. Hermes, from Nous Research, drives the loop through `AIAgent.run_conversation`. Flyte supplies the runtime: tools become durable child actions, the run renders into the task report, and `memory_key` carries the conversation across runs.

Hermes is the one adapter without model-turn replay. The package exposes no per-turn hook, so `durable=` is accepted for contract consistency and does nothing. Tool calls are durable regardless, so a retried task still self-heals at tool granularity.

## Installation

```bash
pip install flyteplugins-agents-hermes
```

Requires Python 3.11 or later.

## Quick start

```python{hl_lines=[2, 6, 11, "20-25"]}
import flyte
from flyteplugins.agents.hermes import run_agent, tool

env = flyte.TaskEnvironment(
    "hermes-agent",
    secrets=[flyte.Secret(key="openai_api_key", as_env_var="OPENAI_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-agents-hermes"),
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
        model="gpt-4o",
        instructions="You are a concise assistant. Use the tools to answer.",
    )
```

`model` is required on the builder path. There is no default.

## Credentials

Hermes normally reads credentials from its own `hermes setup` configuration, which a fresh container does not have. To make the common case work, `run_agent` fills in the gap: when none of `api_key`, `base_url` or `provider` are passed and `OPENAI_API_KEY` is set in the environment, the built agent is pointed at OpenAI with that key.

For any other provider, pass the credentials explicitly. They go through `**agent_kwargs` to the `AIAgent` constructor.

```python{hl_lines=[5, 6]}
await run_agent(
    question,
    tools=[get_weather],
    model="Hermes-4-405B",
    api_key=os.environ["NOUS_API_KEY"],
    base_url="https://inference-api.nousresearch.com/v1",
)
```

## How it maps to Flyte

**Tools:** Hermes does not accept tool callables on the agent object. Tools live in a process-global registry keyed by name and grouped into toolsets, and an `AIAgent` exposes whatever its `enabled_toolsets` resolve to.

`tool` therefore does two things: it wraps the `@env.task` so a call dispatches to `task.aio()` as a durable child action, and it registers that wrapper in the Hermes registry under the `FLYTE_TOOLSET` toolset, with an OpenAI-format schema derived through the Flyte type engine.

**Toolset scoping:** Every `tool` registers under the same shared toolset. To keep two agents in one process from seeing each other's tools, `run_agent` creates a scoped toolset per built agent, named from the agent's `name`, holding exactly the tools you passed.

**The loop:** `run_conversation` is synchronous. The adapter runs it off the event loop through `asyncio.to_thread`, which propagates the Flyte task context into the worker thread.

## Bring your own agent

Pass a pre-configured `AIAgent`. It needs `FLYTE_TOOLSET` in its `enabled_toolsets` to see Flyte-backed tools.

```python{hl_lines=[1, 2, 7, 9]}
from run_agent import AIAgent
from flyteplugins.agents.hermes import FLYTE_TOOLSET


@env.task(report=True, retries=3)
async def support(request: str) -> str:
    agent = AIAgent(
        model="gpt-4o",
        enabled_toolsets=[FLYTE_TOOLSET],
        quiet_mode=True,
    )
    return await run_agent(request, agent=agent, instructions="Be concise.")
```

On this path, `instructions` is passed as the run's `system_message` rather than replacing the agent's own prompt, and `**agent_kwargs` is rejected, since those configure a built agent.

`agent` and `tools` are mutually exclusive.

> [!NOTE] The `AIAgent` import path
> `hermes-agent` exposes `AIAgent` from a top-level module named `run_agent`, which is easy to confuse with this adapter's `run_agent` function. The `from run_agent import AIAgent` form above does not bind the name `run_agent`, so the two coexist, but a bare `import run_agent` would shadow the function.

## Memory

```python
await run_agent(message, model="gpt-4o", memory_key="user-alice")
```

The transcript is persisted to a durable, keyed `MemoryStore` and passed back to Hermes as `conversation_history` on the next run with the same key.

## `run_agent` parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `str` | required | The user prompt |
| `tools` | `Sequence` | `()` | Tools to expose. Accepts `tool`-wrapped tools or bare `@env.task` templates |
| `model` | `str \| None` | `None` | Model name. Required when `agent` is not given |
| `instructions` | `str \| None` | `None` | System prompt. Becomes `ephemeral_system_prompt` on the builder path, or the run's `system_message` with a pre-built agent |
| `agent` | `Any` | `None` | A pre-built Hermes `AIAgent`. Mutually exclusive with `tools` |
| `name` | `str` | `"hermes-agent"` | Agent name. Also names the scoped toolset |
| `durable` | `bool` | `True` | Accepted for contract consistency. No effect on Hermes |
| `observability` | `bool` | `True` | Render the timeline into the task report |
| `memory_key` | `str \| None` | `None` | Stable user or thread ID for cross-run memory |
| `**agent_kwargs` | | | Forwarded to the built `AIAgent`, including `api_key`, `base_url`, `provider` and `max_iterations`. Builder path only |

Returns the final text from the result's `final_response` field. Use `run_agent_sync` with the same signature from a sync task.

## Examples

Full runnable examples live in the SDK repository under [`plugins/agents/hermes/examples`](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/agents/hermes/examples):

- `hermes_durable_agent.py`: a single agent with durable tool calls.
- `hermes_custom_agent.py`: building the `AIAgent` yourself and passing it as `agent=`.
- `hermes_multi_agent.py`: a planner, parallel researchers and an editor, each its own durable action.
- `hermes_crash_resume.py`: the task crashes on its first attempt and completed tool calls are cache hits on retry.
- `hermes_memory.py`: two separate runs sharing a `memory_key`.
