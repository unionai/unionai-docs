---
title: LangGraph research agent
weight: 3
variants: +flyte +union
---

# LangGraph research agent

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/langgraph_agent_research).

This tutorial combines [LangGraph](https://langchain-ai.github.io/langgraph/) for agentic control flow with Flyte for durable compute. A research pipeline plans sub-topics, fans out ReAct agents that search the web with [Tavily](https://tavily.com/), synthesizes findings, and loops on quality gaps until the report is good enough. Each LangGraph step dispatches to a separate Flyte task so planning, research, synthesis, and quality checks appear independently in the run UI.

Flyte provides:

- **Per-step tasks** visible in the Flyte UI while LangGraph orchestrates the graph.
- **Secrets** for OpenAI and Tavily API keys.
- **Live HTML reports** with Mermaid graph visualizations and the final synthesized report.

## Define the task environment

{{< code file="/unionai-examples/v2/tutorials/langgraph_agent_research/langgraph_agent_research.py" fragment=env lang=python >}}

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#    "flyte>=2.4.0",
#    "langgraph>=1.0.7",
#    "langchain-openai",
#    "tavily-python",
#    ...
# ]
# ///
```

## Orchestrate the pipeline

The `research_pipeline` task builds the LangGraph workflow, renders graph diagrams in a report tab, and runs the full plan → research → synthesize → quality-check loop.

{{< code file="/unionai-examples/v2/tutorials/langgraph_agent_research/langgraph_agent_research.py" fragment=pipeline lang=python >}}

Inside each research task, a ReAct subgraph (`graph.py`) uses `@flyte.trace` on Tavily search calls for observability.

## Run the agent

Create secrets for OpenAI and Tavily:

```
flyte create secret openai-api-key <YOUR_OPENAI_API_KEY>
flyte create secret tavily-api-key <YOUR_TAVILY_API_KEY>
```

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/langgraph_agent_research):

```
cd v2/tutorials/langgraph_agent_research
uv run --script langgraph_agent_research.py
```

Or pass a custom query:

```
flyte run langgraph_agent_research.py research_pipeline --query "Compare quantum computing approaches"
```

Check the **Agent Graphs** report tab for the LangGraph diagram and the main report for the synthesized research output.
