---
title: flyte.ai.agents.agent
description: "Agent — a flyte-native tool-use agent harness."
icon: box-seam
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# flyte.ai.agents.agent

Agent — a flyte-native tool-use agent harness.

The harness operates a simple, robust LLM tool-call loop:

1. Send the conversation + tool catalog to the LLM.
2. If the assistant returns tool calls, execute each one (sequentially or
   concurrently), append the results back into the message history, and loop.
3. Stop when the assistant returns a plain text reply (no tool calls) or when
   `max_turns` is reached.

Design goals
------------

- **Minimal core**: a single agent loop with clear extension points.
- **Tools = anything callable**: plain functions, `@flyte.trace` helpers,
  `@env.task` `flyte.TaskTemplate` instances (durable, on-cluster
  execution), `LazyEntity` references to remote tasks, or pre-built
  `flyte.ai.agents.AgentTool` instances.
- **MCP integration**: connect to external MCP servers (Slack, GitHub, Linear,
  filesystem, etc.) and surface their tools to the agent transparently.
- **Memory**: optional `flyte.ai.agents.MemoryStore` that serializes conversation
  history plus path-addressed artifacts to / from `flyte.io.Dir`,
  letting the agent persist state across runs (e.g. across scheduled wake-ups
  or webhook invocations). Includes opt-in audit log, read-only prefixes, and
  optimistic concurrency for multi-agent / sleep-wake patterns.
- **HITL**: opt-in per-tool human approval that pauses the loop on a
  flyte-native condition (`flyte.new_condition`) and waits for a human
  to signal it before executing the tool.
- **Flyte-native**: implements the `flyte.ai.agents.AgentProtocol` so it works
  seamlessly with `flyte.ai.chat.AgentChatAppEnvironment` and is happy
  to be wrapped in `@env.task(triggers=...)` for scheduled or webhook-driven
  wake-ups.

Heavy inspiration is taken from the [pi](https://github.com/earendil-works/pi)
agent harness — in particular its event model and the separation of the loop
from message conversion / tool invocation.

Implementation note: the tool/MCP/LLM building blocks live in sibling modules
(`._tools`, `._mcp`, `._llm`); this module focuses on the
`Agent` class and the loop.
## Directory

### Classes

| Class | Description |
|-|-|
| [`Agent`](../flyte.ai.agents.agent/agent) | A flyte-native tool-use agent harness. |
| [`AgentEvent`](../flyte.ai.agents.agent/agentevent) | Lightweight event emitted by the agent loop. |

### Variables

| Property | Type | Description |
|-|-|-|
| `agent_progress_cb` | `ContextVar` |  |

