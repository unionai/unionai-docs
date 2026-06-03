---
title: Agent framework integrations
weight: 19
variants: +flyte +serverless +union
sidebar_expanded: false
---

# Agent framework integrations

**Any Python-based agent framework works with {{< key product_name >}}.** {{< key product_name >}} doesn't replace your framework — it provides the production layer around it. You write your agent with whatever framework you prefer, then invoke it from inside an `@env.task`, where it runs in a sandboxed container with durable checkpointing and full observability. Each LLM call, tool call, and routing decision can be captured as a span in the {{< key product_name >}} dashboard.

Because the framework drives the loop and {{< key product_name >}} wraps it, you don't need a dedicated plugin for a framework to use it — if it runs in Python, it runs on {{< key product_name >}}.

{{< note >}}
The `flyte` SDK provides a [native agent harness](../build-agent/flyte-agents) that you can use to build your own agent loop.
{{< /note >}}

## How much control does the framework give you?

Frameworks differ in how much of the agent loop they own, which determines how you integrate them with {{< key product_name >}}:

| Level of control | What it means | Example | Integration pattern |
|------------------|---------------|---------|---------------------|
| **You own the loop** | The framework gives you primitives (graph nodes, tools) and you wire the control flow | [LangGraph](./langgraph) | Decorate nodes with `@flyte.trace`; run the compiled graph inside a task |
| **The framework owns the loop, you own the tools** | The framework runs the tool-calling loop; you provide tools as plain functions | [PydanticAI](./pydantic-ai) | Have tools delegate to durable `@env.task`s |
| **First-party tool adapter** | {{< key product_name >}} ships a decorator that turns a task into a framework tool | [OpenAI Agents SDK](./openai-agents-sdk) | Stack `function_tool` on `@env.task` |

Whichever model your framework uses, the integration is the same in spirit: the framework decides *what* the agent does next, and {{< key product_name >}} decides *where and how durably* each step runs.

## Supported frameworks

- [**LangGraph**](./langgraph) — run compiled graphs inside tasks and fan them out in parallel.
- [**PydanticAI**](./pydantic-ai) — type-safe agents whose tools delegate to durable tasks.
- [**OpenAI Agents SDK**](./openai-agents-sdk) — expose durable tasks as Agents SDK tools with `flyteplugins-openai`.

Don't see your framework? The same pattern — invoke the framework from inside an `@env.task` and trace its calls — applies to any Python agent library. See [Bring your own framework](./bring-your-own-framework) for a framework-agnostic template.

## Next steps

- [Deploy an agent as a service](../build-agent/deploy-agent-as-service): run your agent on a schedule or behind a webhook.
- [Build an agent with pure Python](../build-agent/python-agents): roll the loop yourself with no framework at all.
- [The Flyte Agent harness](../build-agent/flyte-agents): the built-in, batteries-included agent loop.
