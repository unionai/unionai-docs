---
title: Build an agent
weight: 18
variants: +flyte +serverless +union
mermaid: true
llm_readable_bundle: true
---

# Build an agent

{{< llm-bundle-note >}}

This section covers how to build, deploy, and run agentic AI applications on {{< key product_name >}}.

Building an agent on {{< key product_name >}} breaks down into two **orthogonal** choices:

1. **How you build the agent loop**: plain Python, the built-in `flyte.ai.agents.Agent` harness, or a third-party framework (LangGraph, PydanticAI, OpenAI Agents SDK).
2. **How you deploy and run it**: as a task you invoke on demand, as a scheduled task driven by a `flyte.Trigger`, or as a long-running app (e.g. a webhook or chat UI).

Any agent from axis (1) can be deployed via any pattern in axis (2). The two are independent, so you can start with a pure-Python loop run on demand and later move it behind a schedule or a webhook without rewriting the agent.

## How {{< key product_name >}} maps to the agentic world

- **`TaskEnvironment`**: The sandboxed execution environment for your agent steps. It configures the container image, hardware resources (CPU, GPU), and secrets (API keys). Think of it as defining "where this code runs."
- **`@env.task`**: Turns any Python function into a remotely-executed step. Each task runs in its own container with the resources you specified. This is the equivalent of a node in LangGraph or n8n.
- **Tasks calling tasks**: A task can `await` other tasks, and each called task gets its own container automatically. No separate workflow decorator needed. The calling task IS your workflow, this is how you build multi-step agentic pipelines.
- **`@flyte.trace`**: Marks helper functions inside a task for fine-grained observability and caching. Each traced call appears as a span in the {{< key product_name >}} dashboard, with its inputs and outputs captured and checkpointed. Use this on your LLM calls, tool executions, and routing decisions to get full visibility into every turn of the agent loop.

> [!TIP]
> See the [{{< key product_name >}} Quickstart](../quickstart) for a hands-on walkthrough.

## Ways to build an agent

| Approach | When to use it | Guide |
|----------|----------------|-------|
| **Pure Python** | You want full control over the loop and the lightest possible dependency footprint | [Build an agent with pure Python](./python-agents) |
| **The `Agent` harness** | You want a batteries-included tool-use loop with tools, MCP servers, memory, and HITL built in | [The Flyte Agent harness](./flyte-agents) |
| **Third-party frameworks** | You already have agents in LangGraph, CrewAI, OpenAI Agents SDK, Pydantic AI, and more | [Agent frameworks](../../integrations/agents/_index) |
| **An unsupported framework** | Your framework has no first-party plugin | [Bring your own framework](./bring-your-own-framework) |

The `Agent` harness has a few dedicated guides of its own:

- [**Extend the Agent class**](./flyte-agents#extending-the-agent-class): customize the loop by overriding `run`.
- [**Agent memory**](./agent-memory): persist conversation history and artifacts across runs with `MemoryStore`.
- [**Add a chat UI**](./agent-chat-ui): give any agent a hosted chat interface.

## Deploying an agent

Once you've built an agent, [**Deploy an agent as a service**](./deploy-agent-as-service) covers running it as a task, on a schedule via `flyte.Trigger`, and behind an `AppEnvironment` webhook.

## Related

- [**Sandboxing**](../sandboxing/_index): safely execute LLM-generated code.
- [**Build an MCP server**](../build-mcp/_index): serve Model Context Protocol servers for AI assistants to interact with {{< key product_name >}}.
