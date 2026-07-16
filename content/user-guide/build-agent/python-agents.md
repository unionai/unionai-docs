---
title: Pure Python agents
weight: 1
variants: +flyte +serverless +union
mermaid: true
---

# Pure Python agents

The lightest way to build an agent on {{< key product_name >}} is to write the loop yourself in plain Python. {{< key product_name >}} is framework-agnostic: use any Python LLM library (OpenAI SDK, Anthropic SDK, LiteLLM, etc.) inside your tasks. The platform provides the production infrastructure layer: sandboxed execution, parallel fan-out, durable checkpointing, and observability for every step of the agent loop.

This approach gives you full control over the loop and the smallest possible dependency footprint. If you'd rather not hand-roll the tool-call loop, see [The Flyte Agent harness](./flyte-agents), which provides a batteries-included loop with tools, MCP servers, memory, and HITL. If you already have agents written in a third-party framework, see [Agent framework integrations](../agent-framework-integrations/_index) for [LangGraph](../agent-framework-integrations/langgraph), [PydanticAI](../agent-framework-integrations/pydantic-ai), and [OpenAI Agents SDK](../agent-framework-integrations/openai-agents-sdk).

Two decorators are all you need:

| Decorator | What it does | Think of it as... |
|-----------|-------------|-------------------|
| **`@env.task`** | Runs a function in its own container on {{< key product_name >}} with dedicated resources, dependencies, and secrets | A sandboxed agent step with its own execution environment |
| **`@flyte.trace`** | Marks a helper function for observability, where each call appears as a span in the {{< key product_name >}} dashboard with captured I/O | An observability hook on your LLM calls, tool executions, and routing decisions |

## ReAct pattern: Reason, Act, Observe (no framework needed)

The [ReAct pattern](https://arxiv.org/abs/2210.03629) is the most common agent architecture: the LLM reasons about what to do, calls a tool, observes the result, and repeats until done. This example is implemented directly with flyte:

```
Thought → Action → Observation → repeat until done
```

{{< code file="/unionai-examples/v2/user-guide/build-agent/building-agents/react_agent.py" fragment="all" lang="python" >}}

```bash
flyte run agent.py react_agent --goal "What is (12 + 8) * 3?"
# => AgentResult(answer='60', steps=3)
```

**What's happening under the hood:**

- `react_agent` runs in a container with only `openai` installed and 2 CPU / 2GB RAM
- Each `reason()` and `act()` call is traced, so you see every LLM call, every tool invocation, and every intermediate result in the {{< key product_name >}} dashboard
- The agent's inputs and final output are durably persisted, letting you inspect any past run end-to-end
- Swap in your own tools (web search, database queries, API calls) by adding to the `TOOLS` dict

> [!TIP]
> See the [Agentic Refinement docs](../advanced-project/agentic-refinement), [Traces docs](../task-programming/traces), and [more patterns (planner, debate, etc.)](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows).

## Plan-and-Execute with parallel fan-out

The [Plan-and-Execute pattern](https://blog.langchain.com/plan-and-execute-agents/) splits a complex query into sub-tasks, fans them out in parallel, then synthesizes the results. With {{< key product_name >}} the fan-out is just `asyncio.gather()`, and each sub-task gets its own container, giving you true parallelism on separate hardware.

```python
# workflow.py
import os, json, asyncio, flyte
from openai import AsyncOpenAI

env = flyte.TaskEnvironment(
    name="research_env",
    image=flyte.Image.from_debian_base(python_version=(3, 13)).with_pip_packages("openai"),
    resources=flyte.Resources(cpu=2, memory="2Gi"),
    secrets=[flyte.Secret(key="OPENAI_API_KEY")],
)

@flyte.trace
async def llm(prompt: str) -> str:
    r = await AsyncOpenAI().chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{"role": "user", "content": prompt}],
    )
    return r.choices[0].message.content

@env.task
async def plan(query: str, n: int = 3) -> list[str]:
    """Split the query into sub-topics."""
    raw = await llm(
        f'Break this into exactly {n} sub-topics. Return ONLY a JSON array of strings.\n\n{query}'
    )
    return json.loads(raw)[:n]

@env.task
async def research(topic: str) -> str:
    """Research one sub-topic (each call = its own container)."""
    return await llm(f"Write a short, factual report on: {topic}")

@env.task
async def synthesize(query: str, reports: list[str]) -> str:
    """Combine the sub-reports into a final answer."""
    sections = "\n\n".join(reports)
    return await llm(f"Synthesize a final answer to '{query}' from:\n\n{sections}")

@env.task
async def research_workflow(query: str, num_topics: int = 3) -> str:
    topics = await plan(query, num_topics)
    reports = list(await asyncio.gather(*[research(t) for t in topics]))  # parallel fan-out
    return await synthesize(query, reports)
```

```bash
flyte run workflow.py research_workflow --query "Impact of storms on travel insurance payouts"
```

**What's happening under the hood:**

```
research_workflow (orchestrator)
  ├── plan          → LLM breaks query into N sub-topics      [container 1]
  ├── research(t1)  → researches one sub-topic                [container 2]  ┐
  ├── research(t2)  → researches one sub-topic                [container 3]  ├ parallel
  ├── research(t3)  → researches one sub-topic                [container 4]  ┘
  └── synthesize    → LLM combines reports into final answer  [container 5]
```

- **Fan-out:** `asyncio.gather()` launches all research tasks in parallel, each in its own container
- **Observability:** `@flyte.trace` on each LLM call means every prompt and response is visible as a span in the {{< key product_name >}} dashboard
- **Durable checkpointing:** Each task's output is persisted. If `synthesize` fails, re-running skips the completed `plan` and `research` steps (with caching enabled)

> [!TIP]
> The same fan-out works with any framework inside the `research` task. See [LangGraph](../agent-framework-integrations/langgraph) for a version that runs a LangGraph research agent (with web-search tool calling) inside each parallel container.

## More agentic patterns

{{< key product_name >}} is framework-agnostic, so these patterns work with any LLM library. Each maps to well-known agent architectures:

| Pattern | What it does | When to use it | Link |
|---------|-------------|----------------|------|
| **ReAct** | Reason → Act → Observe loop with tool calling | Single-agent tasks with tools (API calls, search, code execution) | [multi-agent-workflows/react](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |
| **Plan-and-Execute** | LLM creates a plan, independent steps fan out in parallel, results are synthesized | Complex queries that decompose into parallel sub-tasks | [multi-agent-workflows/planner](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |
| **Evaluator-Optimizer (Reflection)** | Generate → Critique → Refine loop until quality threshold met | Content generation, code generation, any task with clear quality criteria | [Agentic Refinement docs](../advanced-project/agentic-refinement) |
| **Orchestrator-Workers (Manager)** | Supervisor agent delegates to specialist worker agents, reviews quality, requests revisions | Multi-agent systems where sub-tasks require different expertise | [multi-agent-workflows/manager](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |
| **Debate** | Multiple agents solve independently, then debate to consensus | High-stakes decisions where diverse reasoning improves accuracy | [multi-agent-workflows/debate](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |
| **Sequential (Prompt Chaining)** | Static pipeline of LLM calls, no dynamic routing | Predictable multi-step transformations (extract → validate → format) | [multi-agent-workflows/sequential](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |

## How {{< key product_name >}}'s primitives map to the agent stack

If you're coming from LangGraph, CrewAI, OpenAI Agents SDK, or similar frameworks, here's how the concepts you already know translate:

**Your agent loop** is a Python `for`/`while` loop inside an `@env.task`. Each iteration calls `@flyte.trace`-decorated functions for reasoning and tool execution. {{< key product_name >}} doesn't impose a loop structure; you write it in plain Python, which means any pattern (ReAct, reflection, plan-and-execute) works naturally.

**Tool calling** is just calling Python functions. Define your tools as regular functions, decorate them with `@flyte.trace` for observability, and call them from within the agent loop. Use any tool-calling mechanism your LLM SDK provides (OpenAI function calling, Anthropic tool use, LangChain `bind_tools()`). MCP servers can be accessed from within tasks using the MCP Python SDK.

**Parallel fan-out** (LangGraph's `Send()`, n8n's Split in Batches) is `asyncio.gather()`. Each awaited task gets its own container, giving you true parallelism on separate hardware, not just concurrent coroutines.

**State and checkpointing** (LangGraph's Checkpointers, Threads) is automatic. Every task's inputs and outputs are durably persisted. `@flyte.trace` adds sub-step checkpoints within a task. Re-running with caching enabled skips completed steps, {{< key product_name >}}'s equivalent of replaying from a checkpoint.

**Routing and conditional logic** (LangGraph's `add_conditional_edges`, n8n's If/Switch nodes) is Python `if/else`. No special API needed.

**Environment isolation** (different dependencies per step) is `TaskEnvironment`. Your LLM step can use `langchain==0.3`; your data step can use `pandas` + GPU. Each gets its own container image.

**Guardrails and validation** are Python code between steps: `if/else` checks, Pydantic validation, structured output parsing, or libraries like NeMo Guardrails. Raise an exception to fail a step and trigger retries.

**Observability:** The {{< key product_name >}} dashboard shows the full execution tree with per-step inputs, outputs, logs, resource usage, and timing. `@flyte.trace` adds spans within a task for fine-grained visibility into individual LLM calls and tool invocations. For LLM-specific metrics (token usage, cost per call), integrate with Langfuse or LangSmith from within your tasks.

## Next steps

- [The Flyte Agent harness](./flyte-agents): skip the boilerplate with a built-in tool-use loop.
- [Deploy an agent as a service](./deploy-agent-as-service): run this agent on a schedule or behind a webhook.
