---
title: Build an agent
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
mermaid: true
llm_readable_bundle: true
---

# Getting Started with Agentic AI on Union

---


**What's in this guide:**

1. [Quickstart (5 minutes)](#1-quickstart-5-minutes): install, define a task, run it
2. [Deploy an Agent as a Service](#2-deploy-an-agent-as-a-service): host a FastAPI app, webhook pattern, model serving
3. [Building Agents on Union](#3-building-agents-on-union): ReAct pattern, Plan-and-Execute with fan-out, LangGraph integration, more patterns, and how Union maps to the agent stack
4. [Developer Tooling](#4-developer-tooling): V1-to-V2 migration, Claude Code agents, MCP
5. [Resources](#5-resources): docs, tutorials, hands-on labs

## 1. Quickstart (5 minutes)

**How Union maps to what you already know:**

- **`TaskEnvironment`:** the sandboxed execution environment for your agent steps. Configures the container image, hardware resources (CPU, GPU), and secrets (API keys). Think of it as defining "where this code runs."
- **`@env.task`:** turns any Python function into a remotely-executed step. Each task runs in its own container with the resources you specified. This is the equivalent of a node in LangGraph or n8n.
- **Tasks calling tasks:** a task can `await` other tasks, and each called task gets its own container automatically. No separate workflow decorator needed. The calling task IS your workflow, and this is how you build multi-step agentic pipelines.
- **`@flyte.trace`:** marks helper functions inside a task for fine-grained observability. Each traced call appears as a span in the Union dashboard, with its inputs and outputs captured and checkpointed. Use this on your LLM calls, tool executions, and routing decisions to get full visibility into every turn of the agent loop.

> Full docs: [Quickstart](https://www.union.ai/docs/v2/byoc/user-guide/quickstart/)

## 5. Resources

| Resource | Link |
|----------|------|
| V2 User Guide | https://www.union.ai/docs/v2/byoc/user-guide/ |
| V2 SDK (flyte-sdk) | https://github.com/flyteorg/flyte-sdk |
| Quickstart | https://www.union.ai/docs/v2/byoc/user-guide/quickstart/ |
| Deploy Apps & Agent Services (FastAPI, Streamlit, vLLM) | https://www.union.ai/docs/v2/byoc/user-guide/build-apps/ |
| Agentic Refinement (Evaluator-Optimizer pattern) | https://www.union.ai/docs/v2/byoc/user-guide/advanced-project/agentic-refinement/ |
| LangGraph + Union tutorial | https://github.com/unionai/workshops/tree/main/tutorials/langgraph |
| Multi-agent patterns (ReAct, Planner, Debate, etc.) | https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows |
| Hands-on labs (quickstart through apps) | https://github.com/unionai/solutions-engineering/tree/main/hands_on |
| Flyte 2 quickstart notebook | https://github.com/unionai/workshops/tree/main/tutorials/flyte2-quickstarts |
| V1 to V2 migration (docs) | https://www.union.ai/docs/v2/byoc/user-guide/flyte-2/ |
| V1 to V2 migration (context file) | https://gist.github.com/LeonKolyang/2151397b78e30e7ea8f717a6702f47f1 |
| Claude Code agents for Flyte/Union | https://github.com/unionai/claude-agents-public |