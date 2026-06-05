---
title: Compliance monitoring agent
weight: 4
variants: +flyte +union
---

# Compliance monitoring agent

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/compliance_monitoring_agent).

This example demonstrates how to build a regulatory and compliance monitoring agent on Flyte. The agent watches trusted regulatory sources — FDA guidance, SEC filings, sanctions lists, state-level privacy laws — and routes structured, **citation-precise** findings to the right downstream team (compliance, legal, or clinical ops).

Compliance use cases live or die on **citation precision and recency**. A hallucinated regulatory citation is a liability. The [You.com Research API](https://you.com/docs/research/overview) returns a grounded, synthesized answer plus structured sources (URL, title, snippet). Its `source_control` parameter lets the agent restrict research to trusted government and regulator domains within a recency window. Combined with Flyte's audit lineage, you get end-to-end traceability: Flyte logs which agent issued which You.com query and received which document on which date.

Flyte provides:

- **Fan-out parallelism** across watch items
- **`@flyte.trace`** on every You.com Research and LLM call
- **Retries** on monitoring tasks for robustness
- **Flyte reports** grouped by team and severity

## Setting up the environment

{{< code file="/unionai-examples/v2/tutorials/compliance_monitoring_agent/main.py" fragment=env lang=python >}}

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

Each `WatchItem` specifies a regulatory topic, a list of trusted domains for `source_control`, and a routing destination team. Findings carry citation metadata — source URL, published date, and snippet — so every claim can be verified.

{{< code file="/unionai-examples/v2/tutorials/compliance_monitoring_agent/main.py" fragment=data_types lang=python >}}

## Research with the You.com Research API

The `you_research` helper calls the [You.com Research API](https://you.com/docs/research/overview) at `https://api.you.com/v1/research`. It passes `source_control` with an `include_domains` allowlist and a `freshness` filter, and requests structured output via `output_schema`.

See the [Research API overview](https://you.com/docs/research/overview) for `research_effort` levels (`lite`, `standard`, `deep`, `exhaustive`) and the full `source_control` reference. The `output_schema` field requests structured JSON output — useful when you need machine-readable findings rather than free-form prose.

{{< code file="/unionai-examples/v2/tutorials/compliance_monitoring_agent/main.py" fragment=you_research lang=python >}}

## Triage findings with Claude

After the Research API returns structured findings, Claude assigns a severity (`info`, `watch`, or `action`) and a routing rationale for each one.

{{< code file="/unionai-examples/v2/tutorials/compliance_monitoring_agent/main.py" fragment=llm lang=python >}}

## Monitor one watch item

The `monitor_watch_item` task researches a single regulatory topic, enriches findings with source metadata from the Research API response, and triages each finding for severity and routing.

{{< code file="/unionai-examples/v2/tutorials/compliance_monitoring_agent/main.py" fragment=monitor_watch_item lang=python >}}

## Orchestration

The `compliance_monitoring` driver task fans out across all watch items, aggregates findings, and renders a Flyte report sorted by severity and team.

{{< code file="/unionai-examples/v2/tutorials/compliance_monitoring_agent/main.py" fragment=driver lang=python >}}

## Run the agent

### Create secrets

Get a You.com API key from the [You.com platform](https://you.com/platform) (see the [quickstart guide](https://you.com/docs/quickstart)). Get an Anthropic API key from [console.anthropic.com](https://console.anthropic.com/).

Register both keys as Flyte secrets:

```
flyte create secret youdotcom-api-key <YOUR_YOU_API_KEY>
flyte create secret internal-anthropic-api-key <YOUR_ANTHROPIC_API_KEY>
```

See [Secrets](../../user-guide/task-configuration/secrets) for scoping and file-based secrets.

### Run locally or remotely

```
uv run --script main.py
```

To test locally without Flyte secrets:

```
export YOU_API_KEY=<YOUR_YOU_API_KEY>
export ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY>

uv run --script main.py
```

When the run completes, open the Flyte report to review findings grouped by severity, each with a verifiable You.com Research citation.
