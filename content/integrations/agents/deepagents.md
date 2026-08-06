---
title: Deep Agents
weight: 8
variants: +flyte +union
---

# Deep Agents

Run [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) on Flyte. Deep Agents is LangChain's agent harness, with built-in planning through todos, a virtual filesystem, and subagents. `create_deep_agent` returns a compiled LangGraph graph; `run_agent` drives it inside your task.

The virtual filesystem is the part worth calling out. It is agent state that outlives a single turn, and `memory_key` persists it alongside the conversation, so a later run picks up both the transcript and whatever files the agent wrote.

## Installation

```bash
pip install flyteplugins-agents-deepagents
```

Requires Python 3.11 or later.

## Quick start

```python{hl_lines=[2, 6, 11, "20-30"]}
import flyte
from flyteplugins.agents.deepagents import run_agent, tool

env = flyte.TaskEnvironment(
    "deep-agent",
    secrets=[flyte.Secret(key="anthropic_api_key", as_env_var="ANTHROPIC_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-agents-deepagents"),
)


@tool
@env.task(cache="auto", retries=3)
async def search_web(query: str) -> str:
    """Search the web for a query."""
    ...


@env.task(report=True, retries=3)
async def research_agent(question: str) -> str:
    return await run_agent(
        question,
        tools=[search_web],
        instructions="You are an expert researcher.",
        model="anthropic:claude-sonnet-4-6",
        subagents=[{
            "name": "critic",
            "description": "Critiques draft answers.",
            "system_prompt": "You are a ruthless critic.",
        }],
    )
```

Deep-Agents-specific options such as `subagents`, `skills`, `backend` and `interrupt_on` pass straight through as keyword arguments.

## How it maps to Flyte

**Tools:** `tool` turns an `@env.task` into a LangChain `StructuredTool`. It attaches to the main agent through `create_deep_agent(tools=[...])` and equally to a subagent's tool list, so a subagent's tool calls are durable child actions too.

**Model turns:** `model` accepts a chat model instance or a `provider:model` string. A string is resolved through `init_chat_model` first, then wrapped in `DurableChatModel`, so both forms get per-turn replay.

**Observability:** The run timeline renders into the task report.

## Bring your own agent

Pass a compiled `create_deep_agent` graph as `agent=`. Wrap the model in `DurableChatModel` when you build it, since a compiled graph cannot be rewrapped from outside.

```python{hl_lines=[1, "9-14"]}
from deepagents import create_deep_agent
from flyteplugins.agents.deepagents import DurableChatModel


@env.task(report=True, retries=3)
async def research_agent(question: str) -> str:
    from langchain_anthropic import ChatAnthropic

    graph = create_deep_agent(
        model=DurableChatModel(inner=ChatAnthropic(model="claude-sonnet-4-6")),
        tools=[search_web],
        system_prompt="You are an expert researcher.",
    )
    return await run_agent(question, agent=graph)
```

Tool calls remain durable regardless.

`agent` and `tools` are mutually exclusive.

## Memory

```python
await run_agent(message, model="anthropic:claude-sonnet-4-6", memory_key="user-alice")
```

Both the conversation and the agent's virtual filesystem are persisted to a durable, keyed `MemoryStore`. On the next run with the same key, prior messages are prepended to the new turn and the `files` state is restored, so an agent that wrote notes in one run can read them back in the next.

## Composing with Flyte

Deep agents plan internally and can spawn their own subagents. That composes with Flyte's orchestration rather than competing with it: Flyte fans out the team, and each member is a full deep agent with its own internal planning.

```python{hl_lines=[13, 14]}
@env.task(retries=3)
async def research(subtopic: str) -> str:
    return await run_agent(
        f"Research this subtopic:\n{subtopic}",
        tools=[search_web],
        model="anthropic:claude-sonnet-4-6",
    )


@env.task(report=True, retries=3)
async def pipeline(topic: str) -> str:
    subtopics = await plan(topic)
    with flyte.group("parallel-research"):
        findings = await asyncio.gather(*(research(s) for s in subtopics))
    return await synthesize(topic, list(findings))
```

## `run_agent` parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `str` | required | The user prompt |
| `tools` | `Sequence` | `()` | Tools to expose. Accepts `tool`-wrapped tools or bare `@env.task` templates |
| `model` | `Any` | `None` | A chat model instance or `provider:model` string. Required when `agent` is not given |
| `instructions` | `str \| None` | `None` | System prompt for the built agent |
| `agent` | `Any` | `None` | A pre-built compiled `create_deep_agent` graph. Mutually exclusive with `tools` |
| `name` | `str` | `"deep-agent"` | Agent name, used for debugging and observability |
| `durable` | `bool` | `True` | Record and replay each model turn. Applies on the builder path |
| `observability` | `bool` | `True` | Render the timeline into the task report |
| `memory_key` | `str \| None` | `None` | Stable user or thread ID for the conversation and the virtual filesystem |
| `**agent_kwargs` | | | Forwarded to `create_deep_agent`, including `subagents`, `skills` and `backend` |

Returns the final text, taken from the content of the last message. Use `run_agent_sync` with the same signature from a sync task.

## Examples

Full runnable examples live in the SDK repository under [`plugins/agents/deepagents/examples`](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/agents/deepagents/examples):

- `deepagents_durable_agent.py`: a single durable deep agent with traced model turns.
- `deepagents_custom_agent.py`: building the graph yourself with `create_deep_agent`.
- `deepagents_multi_agent.py`: a planner, parallel researchers and an editor, each its own durable action.
- `deepagents_crash_resume.py`: the task crashes on its first attempt and replays completed turns on retry.
- `deepagents_memory.py`: two separate runs sharing a `memory_key`, carrying the virtual filesystem across.
