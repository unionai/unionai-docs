---
title: Build an agent
weight: 17
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
mermaid: true
llm_readable_bundle: true
---

# Build an agent

{{< llm-bundle-note >}}

This section covers how to build, deploy, and run agentic AI applications on {{< key product_name >}}. You'll learn how to implement common agent patterns like ReAct and Plan-and-Execute and deploy agents as hosted services.

## Quickstart

Here's how {{< key product_name >}} maps to the agentic world:

- **`TaskEnvironment`**: The sandboxed execution environment for your agent steps. It configures the container image, hardware resources (CPU, GPU), and secrets (API keys). Think of it as defining "where this code runs."
- **`@env.task`**: Turns any Python function into a remotely-executed step. Each task runs in its own container with the resources you specified. This is the equivalent of a node in LangGraph or n8n.
- **Tasks calling tasks**: A task can `await` other tasks, and each called task gets its own container automatically. No separate workflow decorator needed. The calling task IS your workflow, this is how you build multi-step agentic pipelines.
- **`@flyte.trace`**: Marks helper functions inside a task for fine-grained observability and caching. Each traced call appears as a span in the {{< key product_name >}} dashboard, with its inputs and outputs captured and checkpointed. Use this on your LLM calls, tool executions, and routing decisions to get full visibility into every turn of the agent loop.

> [!TIP]
> See the [{{< key product_name >}} Quickstart](../quickstart) for a hands-on walkthrough.

## Next steps

- [**Deploy an agent as a service**](./deploy-agent-as-service): Host a FastAPI app, webhook pattern, model serving
- [**Building agents on {{< key product_name >}}**](./building-agents): ReAct pattern, Plan-and-Execute with fan-out, LangGraph integration, and more patterns
