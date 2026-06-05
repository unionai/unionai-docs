---
title: Competitive intelligence agent
weight: 3
variants: +flyte +union
---

# Competitive intelligence agent

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/competitive_intelligence_agent).

This example demonstrates how to build a continuous competitive and market intelligence agent on Flyte. The agent fans out across a list of competitors, pulls fresh, source-cited web and news results from the [You.com Search API](https://you.com/docs/search/overview), and uses Claude to extract structured **deltas** — pricing changes, product launches, funding events, leadership moves, and more — into a knowledge-graph-ready table.

A competitive-intelligence knowledge graph must be populated with **fresh web data that carries attributable sources**, not training-data recall or brittle SERP scraping. The You.com Search API returns ranked, structured web and news results with snippets and publication timestamps. The agent feeds those into an LLM that emits structured, source-cited deltas.

Flyte is a strong fit for this pattern:

- **Fan-out parallelism** across competitors with `asyncio.gather`
- **`cache="auto"`** so converging parallel or repeat runs reuse prior You.com and LLM results instead of paying for duplicate external calls
- **`@flyte.trace`** on every You.com and LLM call for full prompt → query → source lineage
- **Flyte reports** that render an HTML dashboard grouping deltas by competitor and category

## Setting up the environment

The agent runs in a single `TaskEnvironment` with secrets for the You.com and Anthropic API keys, automatic caching, and a container image built from the `uv` script dependencies.

{{< code file="/unionai-examples/v2/tutorials/competitive_intelligence_agent/main.py" fragment=env lang=python >}}

The Python packages are declared at the top of the file using the `uv` script style:

```
# /// script
# requires-python = "==3.13"
# dependencies = [
#     "flyte>=2.4.0",
#     "httpx>=0.27.0",
#     "litellm>=1.72.0",
# ]
# ///
```

## Data types

The agent models search hits, deltas, and the final report as dataclasses. Each `Delta` links back to a `SearchHit` that preserves You.com metadata — domain, publication date, author, and snippet.

{{< code file="/unionai-examples/v2/tutorials/competitive_intelligence_agent/main.py" fragment=data_types lang=python >}}

## Search with the You.com Search API

The `you_search` helper calls the [You.com Search API](https://you.com/docs/search/overview) at `https://ydc-index.io/v1/search`. It requests unified web and news results with a `freshness` filter (`day`, `week`, `month`, or `year`) and returns structured hits the LLM can cite by index.

See the [Search API reference](https://you.com/docs/api-reference/search/v1-search) for all supported parameters, including `count`, `country`, and search operators.

{{< code file="/unionai-examples/v2/tutorials/competitive_intelligence_agent/main.py" fragment=you_search lang=python >}}

> [!NOTE]
> We use `@flyte.trace` to track intermediate steps within a task, like You.com API calls and LLM invocations. Each traced call appears as a span in the Flyte dashboard with its inputs and outputs captured.

## Extract deltas with Claude

A shared `llm_json` helper calls Claude via LiteLLM and parses structured JSON from the response.

{{< code file="/unionai-examples/v2/tutorials/competitive_intelligence_agent/main.py" fragment=llm lang=python >}}

## Watch one competitor

The `watch_competitor` task builds a category-scoped search query, calls the You.com Search API, and asks Claude to extract only changes that are supported by a specific search result. Each delta carries a confidence score and a link to its source hit.

{{< code file="/unionai-examples/v2/tutorials/competitive_intelligence_agent/main.py" fragment=watch_competitor lang=python >}}

## Orchestration

The `competitive_intelligence` driver task fans out across all competitors with `asyncio.gather`, aggregates the results, and renders a Flyte report.

{{< code file="/unionai-examples/v2/tutorials/competitive_intelligence_agent/main.py" fragment=driver lang=python >}}

## Run the agent

### Create secrets

Get a You.com API key from the [You.com platform](https://you.com/platform) (see the [quickstart guide](https://you.com/docs/quickstart) for details). Get an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/).

Register both keys as Flyte secrets. The secret key names must match those declared in the `TaskEnvironment`:

```
flyte create secret youdotcom-api-key <YOUR_YOU_API_KEY>
flyte create secret internal-anthropic-api-key <YOUR_ANTHROPIC_API_KEY>
```

See [Secrets](../../user-guide/task-configuration/secrets) for scoping and file-based secrets.

### Run locally or remotely

Run the agent with `uv`:

```
uv run --script main.py
```

Or pass custom competitors with the Flyte CLI:

```
flyte run main.py competitive_intelligence \
  --competitors '["Anthropic", "OpenAI"]'
```

To test locally without Flyte secrets, export the environment variables directly:

```
export YOU_API_KEY=<YOUR_YOU_API_KEY>
export ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY>

uv run --script main.py
```

When the run completes, open the Flyte report in the UI to review deltas grouped by competitor, each with a clickable You.com source citation.
