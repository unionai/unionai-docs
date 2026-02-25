---
title: Build an agent
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
mermaid: true
llm_readable_bundle: true
---

# Build an agent

{{< llm-bundle-note >}}

This section covers how to build, deploy, and run agentic AI applications on Union. You'll learn how to deploy agents as hosted services, implement common agent patterns like ReAct and Plan-and-Execute, and use developer tooling to accelerate your workflow.

## Quickstart

Here's how Union maps to what you already know:

- **`TaskEnvironment`**: The sandboxed execution environment for your agent steps. It configures the container image, hardware resources (CPU, GPU), and secrets (API keys). Think of it as defining "where this code runs."
- **`@env.task`**: Turns any Python function into a remotely-executed step. Each task runs in its own container with the resources you specified. This is the equivalent of a node in LangGraph or n8n.
- **Tasks calling tasks**: A task can `await` other tasks, and each called task gets its own container automatically. No separate workflow decorator needed. The calling task IS your workflow, this is how you build multi-step agentic pipelines.
- **`@flyte.trace`**: Marks helper functions inside a task for fine-grained observability. Each traced call appears as a span in the Union dashboard, with its inputs and outputs captured and checkpointed. Use this on your LLM calls, tool executions, and routing decisions to get full visibility into every turn of the agent loop.

> [!TIP]
> See the [Quickstart](https://www.union.ai/docs/v2/byoc/user-guide/quickstart/) for a hands-on walkthrough.

## Resources

- [V2 User Guide](https://www.union.ai/docs/v2/byoc/user-guide/)
- [V2 SDK (flyte-sdk)](https://github.com/flyteorg/flyte-sdk)
- [Quickstart](https://www.union.ai/docs/v2/byoc/user-guide/quickstart/)
- [Deploy Apps & Agent Services (FastAPI, Streamlit, vLLM)](https://www.union.ai/docs/v2/byoc/user-guide/build-apps/)
- [Agentic Refinement (Evaluator-Optimizer pattern)](https://www.union.ai/docs/v2/byoc/user-guide/advanced-project/agentic-refinement/)
- [LangGraph + Union tutorial](https://github.com/unionai/workshops/tree/main/tutorials/langgraph)
- [Multi-agent patterns (ReAct, Planner, Debate, etc.)](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows)
- [Hands-on labs (quickstart through apps)](https://github.com/unionai/solutions-engineering/tree/main/hands_on)
- [Flyte 2 quickstart notebook](https://github.com/unionai/workshops/tree/main/tutorials/flyte2-quickstarts)
- [V1 to V2 migration (docs)](https://www.union.ai/docs/v2/byoc/user-guide/flyte-2/)
- [V1 to V2 migration (context file)](https://gist.github.com/LeonKolyang/2151397b78e30e7ea8f717a6702f47f1)
- [Claude Code agents for Flyte/Union](https://github.com/unionai/claude-agents-public)

## Next steps

- [**Deploy an agent as a service**](./deploy-agent-as-service): Host a FastAPI app, webhook pattern, model serving
- [**Building agents on Union**](./building-agents): ReAct pattern, Plan-and-Execute with fan-out, LangGraph integration, and more patterns
- [**Developer tooling**](./developer-tooling): V1-to-V2 migration, Claude Code agents, MCP
