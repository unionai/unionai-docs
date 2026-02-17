---
title: Advanced project
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
mermaid: true
llm_readable_bundle: true
---

# Advanced project: LLM reporting agent

{{< llm-bundle-note >}}

This example demonstrates a resilient agentic report generator that showcases
Flyte 2.0's advanced features for building production-grade AI workflows.

## What you'll build

A batch report generator that:
1. Processes multiple topics in parallel
2. Iteratively critiques and refines each report until it meets a quality threshold
3. Produces multiple output formats (Markdown, HTML, summary) for each report
4. Serves results through an interactive UI

## Concepts covered

| Feature | Description |
|---------|-------------|
| `ReusePolicy` | Keep containers warm for high-throughput batch processing |
| `@flyte.trace` | Checkpoint LLM calls for recovery and observability |
| `RetryStrategy` | Handle transient API failures gracefully |
| `flyte.group` | Organize parallel batches and iterations in the UI |
| `asyncio.gather` | Fan out to process multiple topics concurrently |
| Pydantic models | Structured LLM outputs |
| `AppEnvironment` | Deploy interactive Streamlit apps |
| `RunOutput` | Connect apps to pipeline outputs |

## Architecture

```mermaid
flowchart TD
    A[Topics List] --> B

    B["report_batch_pipeline<br/><i>driver_env</i>"]

    subgraph B1 ["refine_all (parallel)"]
        direction LR
        R1["refine_report<br/>topic 1"]
        R2["refine_report<br/>topic 2"]
        R3["refine_report<br/>topic N"]
    end
    B --> B1

    subgraph B2 ["format_all (parallel)"]
        direction LR
        F1["format_outputs<br/>report 1"]
        F2["format_outputs<br/>report 2"]
        F3["format_outputs<br/>report N"]
    end
    B1 --> B2

    B2 --> C["Output: List of Dirs"]
```

Each `refine_report` task runs in a reusable container (`llm_env`) and performs
multiple LLM calls through traced functions:

```mermaid
flowchart TD
    A[Topic] --> B["generate_initial_draft<br/><i>@flyte.trace</i>"]
    B --> C

    subgraph C ["refinement_loop"]
        direction TB
        D["critique_content<br/><i>@flyte.trace</i>"] -->|score >= threshold| E[exit loop]
        D -->|score < threshold| F["revise_content<br/><i>@flyte.trace</i>"]
        F --> D
    end
    C --> G[Refined Report]
```

## Prerequisites

- A {{< key product_name >}} account with an active project
- An OpenAI API key stored as a secret named `openai-api-key`

To create the secret:

```bash
flyte secret create openai-api-key
```

## Parts

1. **[Resilient generation](./resilient-generation)**: Set up reusable environments, traced LLM calls, and retry strategies
2. **[Agentic refinement](./agentic-refinement)**: Build the iterative critique-and-revise loop
3. **[Parallel outputs](./parallel-outputs)**: Generate multiple formats concurrently
4. **[Serving app](./serving-app)**: Deploy an interactive UI for report generation

[Resilient generation]()

## Key takeaways

1. **Reusable environments for batch processing**: `ReusePolicy` keeps containers warm,
   enabling efficient processing of multiple topics without cold start overhead. With
   5 topics × ~7 LLM calls each, the reusable pool handles ~35 calls efficiently.

2. **Checkpointed LLM calls**: `@flyte.trace` provides automatic checkpointing at the
   function level, enabling recovery without re-running expensive API calls.

3. **Agentic patterns**: The generate-critique-revise loop demonstrates how to build
   self-improving AI workflows with clear observability through `flyte.group`.

4. **Parallel fan-out**: `asyncio.gather` processes multiple topics concurrently,
   maximizing throughput by running refinement tasks in parallel across the batch.
