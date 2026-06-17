---
title: PydanticAI agents
weight: 2
variants: +flyte +serverless +union
mermaid: true
---

# PydanticAI agents

[PydanticAI](https://ai.pydantic.dev/) is a type-safe agent framework from the Pydantic team. As with any Python agent framework, you run a PydanticAI agent on {{< key product_name >}} by invoking it from inside an `@env.task` — the framework drives the loop, while {{< key product_name >}} gives you a container, durable checkpointing, and observability.

The key integration point: PydanticAI tools are just Python functions, so a tool can delegate to a durable `@env.task`. That gives you the best of both worlds — PydanticAI's typed tool-calling and {{< key product_name >}}'s durable, observable, on-cluster tool execution.

## A PydanticAI agent in a task

Define a PydanticAI [Agent](https://pydantic.dev/docs/ai/api/pydantic-ai/agent/#pydantic_ai.agent.Agent), register tools that call your durable Flyte tasks, and run it from an `@env.task`:

{{< code file="/unionai-examples/v2/user-guide/build-agent/frameworks/pydantic_ai_agent.py" fragment="all" lang="python" >}}

**What's happening under the hood:**

- `run_agent` runs in a container with only `pydantic-ai-slim` installed.
- PydanticAI drives its own typed tool-call loop. Each tool delegates to an `@env.task`, so `fetch_weather` and `add` execute durably on the cluster and appear in the {{< key product_name >}} dashboard.
- `flyte.group("pydantic-ai-run")` groups the loop's tool calls under one span for readability.
- The task's input prompt and final output are durably persisted for end-to-end inspection.

> [!TIP]
> For lighter, in-process tools you don't need to promote to tasks, decorate them with `@flyte.trace` instead of `@env.task` to still capture them as spans.

## Parallel agents

To run many PydanticAI agents concurrently — each in its own container — fan out with `asyncio.gather()`:

```python
import asyncio


@env.task
async def run_many(prompts: list[str]) -> list[str]:
    results = await asyncio.gather(*[run_agent(p) for p in prompts])
    return list(results)
```

## Next steps

- [Deploy an agent as a service](../build-agent/deploy-agent-as-service): run your PydanticAI agent on a schedule or behind a webhook.
- [LangGraph](./langgraph) and [OpenAI Agents SDK](./openai-agents-sdk): the same pattern for other frameworks.
