---
title: Building agentic workflows on Union
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
mermaid: true
---

# Building agentic workflows on Union

Union is framework-agnostic: use any Python LLM library (OpenAI SDK, Anthropic SDK, LangChain, LiteLLM, etc.) inside your tasks. The platform provides the production infrastructure layer: sandboxed execution, parallel fan-out, durable checkpointing, and observability for every step of the agent loop.

Two decorators are all you need:

| Decorator | What it does | Think of it as... |
|-----------|-------------|-------------------|
| **`@env.task`** | Runs a function in its own container on Union with dedicated resources, dependencies, and secrets | A sandboxed agent step with its own execution environment |
| **`@flyte.trace`** | Marks a helper function for observability, where each call appears as a span in the Union dashboard with captured I/O | An observability hook on your LLM calls, tool executions, and routing decisions |

## ReAct pattern: Reason, Act, Observe (no framework needed)

The [ReAct pattern](https://arxiv.org/abs/2210.03629) is the most common agent architecture: the LLM reasons about what to do, calls a tool, observes the result, and repeats until done. This example is implemented directly with flyte:

```
Thought → Action → Observation → repeat until done
```

```python
# agent.py
import json
from pydantic import BaseModel

import flyte
from openai import AsyncOpenAI

env = flyte.TaskEnvironment(
    name="agent_env",
    image=flyte.Image.from_debian_base(python_version=(3, 13)).with_pip_packages("openai"),
    resources=flyte.Resources(cpu=2, memory="2Gi"),
    secrets=[flyte.Secret(key="OPENAI_API_KEY")],
)

TOOLS = {"add": lambda a, b: a + b, "multiply": lambda a, b: a * b}

@flyte.trace                                       # each call = a span in Union dashboard
async def reason(goal: str, history: str) -> dict:
    """LLM picks a tool or returns a final answer."""
    r = await AsyncOpenAI().chat.completions.create(
        model="gpt-4.1-nano",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content":
                f"Tools: {list(TOOLS)}. Respond JSON: "
                '{"thought":..,"tool":..,"args":{}} or {"thought":..,"done":true,"answer":..}'},
            {"role": "user", "content": f"Goal: {goal}\n\n{history}\nWhat next?"},
        ],
    )
    return json.loads(r.choices[0].message.content)

@flyte.trace
async def act(tool: str, args: dict) -> str:
    """Execute the chosen tool."""
    return str(TOOLS[tool](**args))

class AgentResult(BaseModel):
    answer: str
    steps: int

@env.task                                          # runs in its own sandboxed container
async def react_agent(goal: str, max_steps: int = 10) -> AgentResult:
    history = ""
    for step in range(1, max_steps + 1):           # the agent loop
        decision = await reason(goal, history)      # Thought
        if decision.get("done"):
            return AgentResult(answer=str(decision["answer"]), steps=step)
        result = await act(decision["tool"], decision["args"])  # Action
        history += f"Step {step}: {decision['thought']} -> {decision['tool']}({decision['args']}) = {result}\n"  # Observation
    return AgentResult(answer="Max steps reached", steps=max_steps)
```

```bash
flyte run agent.py react_agent --goal "What is (12 + 8) * 3?"
# => AgentResult(answer='60', steps=3)
```

**What's happening under the hood:**
- `react_agent` runs in a sandboxed container with only `openai` installed and 2 CPU / 2GB RAM
- Each `reason()` and `act()` call is traced, so you see every LLM call, every tool invocation, and every intermediate result in the Union dashboard
- The agent's inputs and final output are durably persisted, letting you inspect any past run end-to-end
- Swap in your own tools (web search, database queries, API calls) by adding to the `TOOLS` dict

> [!TIP]
> See the [Agentic Refinement docs](../advanced-project/agentic-refinement), [Traces docs](../task-programming/traces), and [more patterns (planner, debate, etc.)](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows).

## Plan-and-Execute with parallel fan-out (LangGraph on Union)

The [Plan-and-Execute pattern](https://blog.langchain.com/plan-and-execute-agents/) splits a complex query into sub-tasks, fans them out in parallel, then synthesizes the results. This example runs a LangGraph research agent with web search tool calling, and Union handles the parallelization, giving each sub-task its own container.

Here's `graph.py`, a LangGraph agent with tool calling (search the web, then summarize):

```python
import flyte
from langchain_openai import ChatOpenAIe
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, MessagesState
from langgraph.prebuilt import ToolNode
from langchain_community.tools.tavily_search import TavilySearchResults

def build_research_graph(openai_key: str, tavily_key: str):
    tools = [TavilySearchResults(max_results=2, tavily_api_key=tavily_key)]
    llm = ChatOpenAI(model="gpt-4.1-nano", api_key=openai_key).bind_tools(tools)

    @flyte.trace
    async def agent(state: MessagesState):
        msgs = [SystemMessage(content="Research the topic. Use search, then summarize.")] + state["messages"]
        return {"messages": [await llm.ainvoke(msgs)]}

    @flyte.trace
    async def route(state: MessagesState):
        last = state["messages"][-1]
        return "tools" if getattr(last, "tool_calls", None) else "__end__"

    g = StateGraph(MessagesState)
    g.add_node("agent", agent)
    g.add_node("tools", ToolNode(tools))
    g.set_entry_point("agent")
    g.add_conditional_edges("agent", route, {"tools": "tools", "__end__": "__end__"})
    g.add_edge("tools", "agent")
    return g.compile()
```

And `workflow.py`, which plans topics, fans out research in parallel, and synthesizes:

```python
import os, json, asyncio, flyte
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from graph import build_research_graph

env = flyte.TaskEnvironment(
    name="research_env",
    image=flyte.Image.from_debian_base(python_version=(3, 13))
        .with_pip_packages("openai", "langchain-openai", "langchain-community", "langgraph", "tavily-python"),
    resources=flyte.Resources(cpu=2, memory="2Gi"),
    secrets=[flyte.Secret(key="OPENAI_API_KEY"), flyte.Secret(key="TAVILY_API_KEY")],
)

@env.task
async def plan(query: str, n: int = 3) -> list[str]:
    """Split query into sub-topics."""
    r = await ChatOpenAI(model="gpt-4.1-nano", api_key=os.environ["OPENAI_API_KEY"]).ainvoke(
        f"Break into exactly {n} sub-topics. Return ONLY a JSON array of strings, e.g. [\"topic1\", \"topic2\"]. No objects.\n\n{query}")
    topics = json.loads(r.content)[:n]
    return [t if isinstance(t, str) else str(t.get("sub_topic", t)) for t in topics]

@env.task
async def research(topic: str) -> str:
    """Run LangGraph agent on one topic (each call = separate container)."""
    graph = build_research_graph(os.environ["OPENAI_API_KEY"], os.environ["TAVILY_API_KEY"])
    result = await graph.ainvoke({"messages": [HumanMessage(content=f"Research: {topic}")]})
    return json.dumps({"topic": topic, "report": result["messages"][-1].content})

@env.task
async def synthesize(query: str, reports: list[str]) -> str:
    """Combine sub-reports into a final summary."""
    parsed = [json.loads(r) for r in reports]
    sections = "\n\n".join(f"## {r['topic']}\n{r['report']}" for r in parsed)
    r = await ChatOpenAI(model="gpt-4.1-nano", api_key=os.environ["OPENAI_API_KEY"]).ainvoke(
        f"Synthesize reports on: {query}\n\n{sections}\n\nKey takeaways:")
    return r.content

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
  ├── plan          → LLM breaks query into N sub-topics          [container 1]
  ├── research(t1)  → LangGraph agent loop with web search tools  [container 2]  ┐
  ├── research(t2)  → LangGraph agent loop with web search tools  [container 3]  ├ parallel
  ├── research(t3)  → LangGraph agent loop with web search tools  [container 4]  ┘
  └── synthesize    → LLM combines reports into final answer      [container 5]
```

- **Fan-out:** `asyncio.gather()` launches all research tasks in parallel, each in its own sandboxed container
- **Tool calling inside each research task:** The LangGraph agent calls Tavily web search, observes results, reasons about them, and loops until it has enough information (the inner agentic loop)
- **Observability:** `@flyte.trace` on the LangGraph nodes means every LLM call, every tool call, and every routing decision is visible as a span in the Union dashboard
- **Durable checkpointing:** Each task's output is persisted. If `synthesize` fails, re-running skips the completed `plan` and `research` steps (with caching enabled)

## More agentic patterns

Union is framework-agnostic, so these patterns work with any LLM library. Each maps to well-known agent architectures:

| Pattern | What it does | When to use it | Link |
|---------|-------------|----------------|------|
| **ReAct** | Reason → Act → Observe loop with tool calling | Single-agent tasks with tools (API calls, search, code execution) | [multi-agent-workflows/react](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |
| **Plan-and-Execute** | LLM creates a plan, independent steps fan out in parallel, results are synthesized | Complex queries that decompose into parallel sub-tasks | [multi-agent-workflows/planner](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |
| **Evaluator-Optimizer (Reflection)** | Generate → Critique → Refine loop until quality threshold met | Content generation, code generation, any task with clear quality criteria | [Agentic Refinement docs](../advanced-project/agentic-refinement) |
| **Orchestrator-Workers (Manager)** | Supervisor agent delegates to specialist worker agents, reviews quality, requests revisions | Multi-agent systems where sub-tasks require different expertise | [multi-agent-workflows/manager](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |
| **Debate** | Multiple agents solve independently, then debate to consensus | High-stakes decisions where diverse reasoning improves accuracy | [multi-agent-workflows/debate](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |
| **Sequential (Prompt Chaining)** | Static pipeline of LLM calls, no dynamic routing | Predictable multi-step transformations (extract → validate → format) | [multi-agent-workflows/sequential](https://github.com/unionai/workshops/tree/main/tutorials/multi-agent-workflows) |

## How Union's primitives map to the agent stack

If you're coming from LangGraph, CrewAI, OpenAI Agents SDK, or similar frameworks, here's how the concepts you already know translate:

**Your agent loop** is a Python `for`/`while` loop inside an `@env.task`. Each iteration calls `@flyte.trace`-decorated functions for reasoning and tool execution. Union doesn't impose a loop structure; you write it in plain Python, which means any pattern (ReAct, reflection, plan-and-execute) works naturally.

**Tool calling** is just calling Python functions. Define your tools as regular functions, decorate them with `@flyte.trace` for observability, and call them from within the agent loop. Use any tool-calling mechanism your LLM SDK provides (OpenAI function calling, Anthropic tool use, LangChain `bind_tools()`). MCP servers can be accessed from within tasks using the MCP Python SDK.

**Parallel fan-out** (LangGraph's `Send()`, n8n's Split in Batches) is `asyncio.gather()`. Each awaited task gets its own container, giving you true parallelism on separate hardware, not just concurrent coroutines.

**State and checkpointing** (LangGraph's Checkpointers, Threads) is automatic. Every task's inputs and outputs are durably persisted. `@flyte.trace` adds sub-step checkpoints within a task. Re-running with caching enabled skips completed steps, Union's equivalent of replaying from a checkpoint.

**Routing and conditional logic** (LangGraph's `add_conditional_edges`, n8n's If/Switch nodes) is Python `if/else`. No special API needed.

**Environment isolation** (different dependencies per step) is `TaskEnvironment`. Your LLM step can use `langchain==0.3`; your data step can use `pandas` + GPU. Each gets its own container image.

**Guardrails and validation** are Python code between steps: `if/else` checks, Pydantic validation, structured output parsing, or libraries like NeMo Guardrails. Raise an exception to fail a step and trigger retries.

**Observability:** The Union dashboard shows the full execution tree with per-step inputs, outputs, logs, resource usage, and timing. `@flyte.trace` adds spans within a task for fine-grained visibility into individual LLM calls and tool invocations. For LLM-specific metrics (token usage, cost per call), integrate with Langfuse or LangSmith from within your tasks.
