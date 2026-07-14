---
title: LangGraph agents
weight: 1
variants: +flyte +serverless +union
mermaid: true
---

# LangGraph agents

If you already build agents with [LangGraph](https://langchain-ai.github.io/langgraph/), you can run them on {{< key product_name >}} unchanged. {{< key product_name >}} doesn't replace your graph. It provides the production layer around it: each graph runs inside a sandboxed `@env.task` container, and you can fan out many graphs in parallel, one container each.

The pattern is: define your LangGraph graph as you normally would, then invoke it from inside a task. Decorate the graph's nodes with `@flyte.trace` so each LLM call, tool call, and routing decision shows up as a span in the {{< key product_name >}} dashboard.

## A single LangGraph agent in a task

Put your graph behind an `@env.task`. The `langgraph` and `langchain` dependencies live in the task's image, isolated from the rest of your project:

{{< code file="/unionai-examples/v2/user-guide/build-agent/frameworks/langgraph_agent.py" fragment="all" lang="python" >}}

## Plan-and-Execute: fan out LangGraph agents in parallel

A common production pattern is to plan a set of sub-topics, run a LangGraph research agent on each in parallel, then synthesize. {{< key product_name >}} handles the parallelization: each `research` call gets its own container via `asyncio.gather()`.

First, the graph (`graph.py`), a LangGraph agent with web-search tool calling:

```python
import flyte
from langchain_openai import ChatOpenAI
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

Then the workflow (`workflow.py`), which plans, fans out, and synthesizes:

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
        f'Break into exactly {n} sub-topics. Return ONLY a JSON array of strings.\n\n{query}')
    return json.loads(r.content)[:n]

@env.task
async def research(topic: str) -> str:
    """Run the LangGraph agent on one topic (each call = its own container)."""
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

- **Fan-out:** `asyncio.gather()` launches all research tasks in parallel, each in its own container.
- **Tool calling inside each graph:** The LangGraph agent calls Tavily web search, observes results, reasons, and loops until done.
- **Observability:** `@flyte.trace` on the LangGraph nodes makes every LLM call, tool call, and routing decision visible as a span.
- **Durable checkpointing:** Each task's output is persisted. If `synthesize` fails, re-running skips completed steps (with caching enabled).

## Next steps

- [Deploy an agent as a service](../build-agent/deploy-agent-as-service): run your LangGraph agent on a schedule or behind a webhook.
- [PydanticAI](./pydantic-ai) and [OpenAI Agents SDK](./openai-agents-sdk): the same pattern for other frameworks.
