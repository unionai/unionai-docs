---
title: OpenAI agents
weight: 3
variants: +flyte +serverless +union
mermaid: true
---

# OpenAI agents

The [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) is a lightweight framework for building multi-tool, multi-agent applications. {{< key product_name >}} ships a first-party integration, `flyteplugins-openai`, that lets you expose durable Flyte tasks as Agents SDK tools with a single decorator.

The integration provides `function_tool` from `flyteplugins.openai.agents`. Stack it on top of `@env.task` and the resulting object is both a durable Flyte task and an OpenAI Agents SDK tool. When the agent calls the tool, it executes on-cluster — durable, retryable, and observable in the dashboard.

## Tools that are also durable tasks

Each tool below is a Flyte task wrapped as an Agents SDK tool. The `agent` task builds an Agents SDK `Agent`, hands it the tools, and runs it with `Runner.run`:

{{< code file="/unionai-examples/v2/user-guide/build-agent/frameworks/openai_agents_agent.py" fragment="all" lang="python" >}}

**What's happening under the hood:**

- `@function_tool` (from `flyteplugins.openai.agents`) adapts the durable `@env.task` into an OpenAI Agents SDK tool, so the agent can call it through the SDK's normal tool-calling mechanism.
- Each tool call executes as a Flyte task on the cluster — durable and observable — even though the agent loop itself orchestrates them.
- `flyte.group(...)` groups each agent's tool calls under a named span, and `asyncio.gather()` fans out the per-goal agents in parallel, each in its own container.

## Next steps

- [Deploy an agent as a service](../build-agent/deploy-agent-as-service): run your Agents SDK agent on a schedule or behind a webhook.
- [LangGraph](./langgraph) and [PydanticAI](./pydantic-ai): the same pattern for other frameworks.
