---
title: Multi-agent trading simulation
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Multi-agent trading simulation

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/tutorials-v2/trading_agents) based on work by [TauricResearch](https://github.com/TauricResearch/TradingAgents).

This example walks you through building a multi-agent trading simulation, modeling how agents within a firm might interact, strategize, and make trades collaboratively.

![Trading agents execution visualization](../../_static/images/tutorials/trading-agents/execution.png)
_Trading agents execution visualization_

## TL;DR

- You'll build a trading firm made up of agents that analyze, argue, and act, modeled with Python functions.
- You'll use the Flyte SDK to orchestrate this world — giving you visibility, retries, caching, and durability.
- You'll learn how to plug in tools, structure conversations, and track decisions across agents.
- You'll see how agents debate, use context, generate reports, and retain memory via vector DBs.

## What is an agent, anyway?

Agentic workflows are a rising pattern for complex problem-solving with LLMs. Think of agents as:

- An LLM (like GPT-4 or Mistral)
- A loop that keeps them thinking until a goal is met
- A set of optional tools they can call (APIs, search, calculators, etc.)
- Enough tokens to reason about the problem at hand

That's it.

You define tools, bind them to an agent, and let it run, reasoning step-by-step, optionally using those tools, until it finishes.

## What's different here?

We're not building yet another agent framework. You're free to use LangChain, custom code, or whatever setup you like.

What we're giving you is the missing piece: a way to run these workflows **reliably, observably, and at scale, with zero rewrites.**

With Flyte, you get:

- Prompt + tool traceability and full state retention
- Built-in retries, caching, and failure recovery
- A native way to plug in your agents; no magic syntax required

## How it works: step-by-step walkthrough

This simulation is powered by a Flyte task that orchestrates multiple intelligent agents working together to analyze a company's stock and make informed trading decisions.

![Trading agents schema](../../_static/images/tutorials/trading-agents/schema.png)
_Trading agents schema_

### Entry point

Everything begins with a top-level Flyte task called `main`, which serves as the entry point to the workflow.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/main.py" fragment=main lang=python >}}

This task accepts several inputs:

- the list of analysts to run,
- the number of debate and risk discussion rounds,
- a flag to enable online tools,
- the company you're evaluating,
- and the target trading date.

The most interesting parameter here is the list of analysts to run. It determines which analyst agents will be invoked and shapes the overall structure of the simulation. Based on this input, the task dynamically launches agent tasks, running them in parallel.

The `main` task is written as a regular asynchronous Python function wrapped with Flyte's task decorator. No domain-specific language or orchestration glue is needed — just idiomatic Python, optionally using async for better performance. The task environment is configured once and shared across all tasks for consistency.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/flyte_env.py" fragment=env lang=python >}}

### Analyst agents

Each analyst agent comes equipped with a set of tools and a carefully designed prompt tailored to its specific domain. These tools are modular Flyte tasks — for example, downloading financial reports or computing technical indicators — and benefit from Flyte's built-in caching to avoid redundant computation.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/tools/toolkit.py" fragment=get_stockstats_indicators_report_online lang=python >}}

When initialized, an analyst enters a structured reasoning loop (via LangChain), where it can call tools, observe outputs, and refine its internal state before generating a final report. These reports are later consumed by downstream agents.

Here's an example of a news analyst that interprets global events and macroeconomic signals. We specify the tools accessible to the analyst, and the LLM selects which ones to use based on context.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/agents/analysts.py" fragment=news_analyst lang=python >}}

Each analyst agent uses a helper function to bind tools, iterate through reasoning steps (up to a configurable maximum), and produce an answer. Setting a max iteration count is crucial to prevent runaway loops. As agents reason, their message history is preserved in their internal state and passed along to the next agent in the chain.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/agents/analysts.py" fragment=agent_helper lang=python >}}

Once all analyst reports are complete, their outputs are collected and passed to the next stage of the workflow.

### Research agents

The research phase consists of two agents: a bullish researcher and a bearish one. They evaluate the company from opposing viewpoints, drawing on the analysts' reports. Unlike analysts, they don't use tools. Their role is to interpret, critique, and develop positions based on the evidence.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/agents/researchers.py" fragment=bear_researcher lang=python >}}

To aid reasoning, the agents can also retrieve relevant "memories" from a vector database, giving them richer historical context. The number of debate rounds is configurable, and after a few iterations of back-and-forth between the bull and bear, a research manager agent reviews their arguments and makes a final investment decision.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/agents/managers.py" fragment=research_manager lang=python >}}

### Trading agent

The trader agent consolidates the insights from analysts and researchers to generate a final recommendation. It synthesizes competing signals and produces a conclusion such as _Buy for long-term growth despite short-term volatility_.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/agents/trader.py" fragment=trader lang=python >}}

### Risk agents

Risk agents comprise agents with different risk tolerances: a risky debater, a neutral one, and a conservative one. They assess the portfolio through lenses like market volatility, liquidity, and systemic risk. Similar to the bull-bear debate, these agents engage in internal discussion, after which a risk manager makes the final call.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/agents/risk_debators.py" fragment=risk_debator lang=python >}}

The outcome of the risk manager — whether to proceed with the trade or not — is considered the final decision of the trading simulation.

You can visualize this full pipeline in the Flyte/Union UI, where every step is logged.
You’ll see input/output metadata for each tool and agent task.
Thanks to Flyte's caching, repeated steps are skipped unless inputs change, saving time and compute resources.

### Retaining agent memory with S3 vectors

To help agents learn from past decisions, we persist their memory in a vector store. In this example, we use an [S3 vector](https://aws.amazon.com/s3/features/vectors/) bucket for their simplicity and tight integration with Flyte and Union, but any vector database can be used.

Note: To use the S3 vector store, make sure your IAM role has the following permissions configured:

```
s3vectors:CreateVectorBucket
s3vectors:CreateIndex
s3vectors:PutVectors
s3vectors:GetIndex
s3vectors:GetVectors
s3vectors:QueryVectors
s3vectors:GetVectorBucket
```

After each trade decision, you can run a `reflect_on_decisions` task. This evaluates whether the final outcome aligned with the agent's recommendation and stores that reflection in the vector store. These stored insights can later be retrieved to provide historical context and improve future decision-making.

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/main.py" fragment=reflect_on_decisions lang=python >}}

### Running the simulation

First, set up your OpenAI secret (from [openai.com](https://platform.openai.com/api-keys)) and Finnhub API key (from [finnhub.io](https://finnhub.io/)):

```
flyte create secret openai_api_key <YOUR_OPENAI_API_KEY>
flyte create secret finnhub_api_key <YOUR_FINNHUB_API_KEY>
```

Then [clone the repo](https://github.com/unionai/unionai-examples), navigate to the `tutorials-v2/trading_agents` directory, and run the following commands:

```
flyte create config --endpoint <FLYTE_OR_UNION_ENDPOINT> --project <PROJECT_NAME> --domain <DOMAIN_NAME> --builder remote
uv run main.py
```

If you'd like to run the `reflect_on_decisions` task instead, comment out the `main` function call and uncomment the `reflect_on_decisions` call in the `__main__` block:

{{< code file="/external/unionai-examples/tutorials-v2/trading_agents/main.py" fragment=execute_main lang=python >}}

Then run:

```
uv run main.py
```

## Why Flyte? _(A quick note before you go)_

You might now be wondering: can't I just build all this with Python and LangChain?
Absolutely. But as your project grows, you'll likely run into these challenges:

1.  **Observability**: Agent workflows can feel opaque. You send a prompt, get a response, but what happened in between?

    - Were the right tools used?
    - Were correct arguments passed?
    - How did the LLM reason through intermediate steps?
    - Why did it fail?

    Flyte gives you a window into each of these stages.

2.  **Multi-agent coordination**: Real-world applications often require multiple agents with distinct roles and responsibilities. In such cases, you'll need:

    - Isolated state per agent,
    - Shared context where needed,
    - And coordination — sequential or parallel.

    Managing this manually gets fragile, fast. Flyte handles it for you.

3.  **Scalability**: Agents and tools might need to run in isolated or containerized environments. Whether you're scaling out to more agents or more powerful hardware, Flyte lets you scale without taxing your local machine or racking up unnecessary cloud bills.
4.  **Durability & recovery**: LLM-based workflows are often long-running and expensive. If something fails halfway:

    - Do you lose all progress?
    - Replay everything from scratch?

    With Flyte, you get built-in caching, checkpointing, and recovery, so you can resume where you left off.
