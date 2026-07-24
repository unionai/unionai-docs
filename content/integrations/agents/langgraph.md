---
title: LangGraph
weight: 7
variants: +flyte +union
---

# LangGraph

Run [LangGraph](https://langchain-ai.github.io/langgraph/) graphs on Flyte. This adapter is shaped differently from the others: LangGraph is a framework for building your own control flow, so rather than hiding the graph behind `run_agent`, it gives you durable node factories and expects you to wire them up yourself.

You build the `StateGraph`. `ai_node` and `tool_node` are the pieces Flyte makes durable and observable.

## Installation

```bash
pip install flyteplugins-agents-langgraph
```

Requires Python 3.10 or later. Install the provider integration you need alongside it, for example `langchain-openai`.

## Quick start

Build the graph with the two node factories, compile it, and hand the compiled graph to `run_agent`.

```python{hl_lines=[2, 6, 13, "38-41"]}
import flyte
from flyteplugins.agents.langgraph import ai_node, run_agent, tool, tool_node

env = flyte.TaskEnvironment(
    "langgraph-agent",
    secrets=[flyte.Secret(key="openai_api_key", as_env_var="OPENAI_API_KEY")],
    image=flyte.Image.from_debian_base().with_pip_packages(
        "flyteplugins-agents-langgraph", "langchain-openai",
    ),
)


@tool
@env.task(cache="auto", retries=3)
async def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"The weather in {city} is sunny, 22C."


def build_city_graph():
    """A standard tool-calling loop: ai, then tools, then back to ai."""
    from langchain_openai import ChatOpenAI
    from langgraph.graph import START, MessagesState, StateGraph
    from langgraph.prebuilt import tools_condition

    tools = [get_weather]
    builder = StateGraph(MessagesState)
    builder.add_node("ai", ai_node(ChatOpenAI(model="gpt-4o"), tools))
    builder.add_node("tools", tool_node(tools))
    builder.add_edge(START, "ai")
    builder.add_conditional_edges("ai", tools_condition)
    builder.add_edge("tools", "ai")
    return builder.compile()


@env.task(report=True, retries=3)
async def city_agent(city: str) -> str:
    return await run_agent(
        f"What's the weather in {city}?",
        agent=build_city_graph(),
    )
```

Build the graph inside the task, where the provider API key is available.

## The node factories

**`ai_node(model, tools, *, name="ai", durable=True, observability=True)`**

The model-calling node. It binds the tools to your chat model and runs one turn over `state["messages"]`, appending the response. With `durable=True`, each turn is recorded as a `flyte.trace` leaf keyed by a fingerprint of the message list, so a retry replays the recorded response instead of calling the model again.

Returns an async node with the signature `state -> {"messages": [ai_message]}`.

**`tool_node(tools, *, name="tools", observability=True)`**

The tool-executing node. It reads the tool calls off the last message and runs each one, appending a `ToolMessage` per call. Tools wrapped with `tool` run as durable Flyte child actions; anything else runs as the tool defines. Tool errors are caught and surfaced back to the model as the tool result rather than failing the node.

Returns an async node with the signature `state -> {"messages": [tool_message, ...]}`.

Both render their activity into the task report.

## How it maps to Flyte

**Tools:** `tool` turns an `@env.task` into a LangChain `StructuredTool`. It is a first-class LangGraph tool, so it works with `model.bind_tools(...)`, with `tool_node`, and with LangGraph's own `ToolNode`. The args schema comes from the task's typed signature.

**Model turns:** Durability lives in `ai_node`, not in a model wrapper. That means any chat model works, including a `provider:model` string, and durability applies uniformly.

## Skipping the graph

If you do not need a custom topology, pass `tools` and a model instead of `agent`, and `run_agent` assembles the same tool-calling loop from the same two factories.

```python{hl_lines=[7, 8]}
@env.task(report=True, retries=3)
async def quick_city_agent(city: str) -> str:
    from langchain_openai import ChatOpenAI

    return await run_agent(
        f"What's the weather in {city}?",
        tools=[get_weather],
        model=ChatOpenAI(model="gpt-4o"),
        instructions="You are a concise assistant. Use the tools to answer.",
    )
```

`model` accepts a chat model instance or a `provider:model` string. The string form is resolved through `init_chat_model`, which requires the `langchain` package.

`agent` and `tools` are mutually exclusive.

## Custom state

`input` accepts a full graph input state as a dict, not just a prompt string, so a graph with a state schema beyond `MessagesState` works.

```python
await run_agent({"messages": [...], "budget": 3}, agent=graph)
```

When memory is in play, prior messages are merged into the `messages` key of whatever state you pass.

## Memory

```python
await run_agent(question, agent=graph, memory_key="user-alice")
```

The conversation transcript is persisted to a durable, keyed `MemoryStore` and prepended to the graph's messages on the next run with the same key. On a resumed run the system prompt is not re-added, since it already lives in the prior transcript.

## `run_agent` parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `input` | `str \| dict` | required | The user prompt, or a full graph input state |
| `tools` | `Sequence` | `()` | Tools for the default graph. Accepts `tool`-wrapped tools or bare `@env.task` templates |
| `model` | `Any` | `None` | A chat model instance or `provider:model` string. Required when building the graph |
| `instructions` | `str \| None` | `None` | System prompt prepended to a built graph's messages |
| `agent` | `Any` | `None` | A pre-built compiled graph. Mutually exclusive with `tools` |
| `name` | `str` | `"langgraph-agent"` | Graph name, used for debugging and observability |
| `durable` | `bool` | `True` | Record each model turn. Applies to built graphs |
| `observability` | `bool` | `True` | Render the timeline into the task report |
| `memory_key` | `str \| None` | `None` | Stable user or thread ID for cross-run memory |
| `**run_kwargs` | | | Forwarded to the graph's `ainvoke` |

Returns the final assistant message as a string. Use `run_agent_sync` with the same signature from a sync task.

> [!NOTE] `durable` applies to graphs `run_agent` builds
> When you build the graph yourself, durability is whatever you configured on `ai_node`. Passing `durable=False` alongside `agent=` does not turn off a node you already built with `durable=True`.

## Examples

Full runnable examples live in the SDK repository under [`plugins/agents/langgraph/examples`](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/agents/langgraph/examples):

- `langgraph_custom_agent.py`: building a `StateGraph` from `ai_node` and `tool_node`, plus the default-graph shortcut.
- `langgraph_durable_agent.py`: a single durable agent with traced model turns.
- `langgraph_multi_agent.py`: a planner, parallel researchers and an editor, each its own durable action.
- `langgraph_crash_resume.py`: the task crashes on its first attempt and replays completed turns on retry.
- `langgraph_memory.py`: two separate runs sharing a `memory_key`.
