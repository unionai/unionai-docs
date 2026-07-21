---
title: Agent framework integrations
weight: 19
variants: +flyte +serverless +union
sidebar_expanded: false
---

# Agent framework integrations

**Any Python-based agent framework works with {{< key product_name >}}.** {{< key product_name >}} doesn't replace your framework; it provides the production layer around it. You write your agent with whatever framework you prefer, then invoke it from inside an `@env.task`, where it runs in a container with durable checkpointing and full observability. Each LLM call, tool call, and routing decision can be captured as a span in the {{< key product_name >}} dashboard.

Because the framework drives the loop and {{< key product_name >}} wraps it, you don't need a dedicated plugin for a framework to use it: if it runs in Python, it runs on {{< key product_name >}}.

{{< note >}}
The `flyte` SDK provides a [native agent harness](../build-agent/flyte-agents) that you can use to build your own agent loop.
{{< /note >}}

## Two ways in

**Use a supported plugin.** Ten frameworks ship first-party adapters, including OpenAI Agents SDK, Claude Agent SDK, Google ADK, Mistral, LangChain, LangGraph, Deep Agents, CrewAI, Pydantic AI and Hermes. These give you more than a wrapper: tool calls become containerized child actions with their own resources and cache, completed model turns replay on retry instead of re-billing, and conversations persist across runs. See [Agent frameworks](../../integrations/agents/_index) in the Integrations section.

**Bring your own.** For anything else, the integration is a few lines: call the framework's entry point inside a task, delegate tools to tasks, and trace what you want to see. [Bring your own framework](./bring-your-own-framework) is a framework-agnostic template.

## How much control does the framework give you?

Frameworks differ in how much of the agent loop they own, which shapes how you integrate them:

| Level of control | What it means | Integration pattern |
|------------------|---------------|---------------------|
| **You own the loop** | The framework gives you primitives (graph nodes, tools) and you wire the control flow | Use durable node factories, or decorate nodes with `@flyte.trace` and run the compiled graph inside a task |
| **The framework owns the loop, you own the tools** | The framework runs the tool-calling loop; you provide tools as plain functions | Have tools delegate to durable `@env.task`s |
| **The framework owns everything** | The framework builds and runs the agent from configuration | Wrap the whole run in a task and trace the seam below the loop |

Whichever model your framework uses, the integration is the same in spirit: the framework decides *what* the agent does next, and {{< key product_name >}} decides *where and how durably* each step runs.

## Next steps

- [Agent frameworks](../../integrations/agents/_index): the ten supported plugins and what each one gives you.
- [Bring your own framework](./bring-your-own-framework): the framework-agnostic template.
- [Deploy an agent as a service](../build-agent/deploy-agent-as-service): run your agent on a schedule or behind a webhook.
- [Build an agent with pure Python](../build-agent/python-agents): roll the loop yourself with no framework at all.
- [The Flyte Agent harness](../build-agent/flyte-agents): the built-in, batteries-included agent loop.
