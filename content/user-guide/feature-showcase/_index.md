---
title: Feature showcase
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Feature showcase

This example demonstrates a resilient agentic report generator that showcases
Flyte 2.0's advanced features for building production-grade AI workflows.

## What you'll build

An intelligent report generator that:
1. Generates an initial draft using an LLM
2. Iteratively critiques and refines the draft until it meets a quality threshold
3. Produces multiple output formats (Markdown, HTML, summary) in parallel

## Concepts covered

| Feature | Description | First project? |
|---------|-------------|----------------|
| `ReusePolicy` | Keep containers warm between tasks for cost efficiency | No |
| `@flyte.trace` | Checkpoint LLM calls for recovery and observability | No |
| `RetryStrategy` | Handle transient API failures gracefully | No |
| `flyte.group` | Organize agentic iterations in the UI | No |
| `asyncio.gather` | Run independent operations in parallel | No |
| Pydantic models | Structured LLM outputs | No |

## Architecture

```
[Topic Input]
      │
      ▼
┌─────────────────────────────────────┐
│  generate_initial_draft             │  ← RetryStrategy + @flyte.trace
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│  refinement_loop                    │
│  ┌───────────────────────────────┐  │
│  │ flyte.group("refinement_N")   │  │
│  │  • critique_content (traced)  │  │
│  │  • revise_content (traced)    │  │
│  └───────────────────────────────┘  │
│  [loop until score >= threshold]    │
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│  format_outputs                     │  ← asyncio.gather (parallel)
│  • Markdown, HTML, Summary          │
└─────────────────────────────────────┘
      │
      ▼
[Output: Dir with formatted docs]
```

## Prerequisites

- A {{< key product_name >}} account with an active project
- An OpenAI API key stored as a secret named `openai-api-key`

To create the secret:

```bash
flyte secret create openai-api-key
```

## Parts

1. **[Resilient generation](resilient-generation)**: Set up reusable environments, traced LLM calls, and retry strategies
2. **[Agentic refinement](agentic-refinement)**: Build the iterative critique-and-revise loop
3. **[Parallel outputs](parallel-outputs)**: Generate multiple formats concurrently
4. **[Serving app](serving-app)**: Deploy an interactive UI for report generation

## Key takeaways

1. **Reusable environments**: `ReusePolicy` keeps containers warm, reducing cold start
   latency and improving cost efficiency for bursty LLM workloads.

2. **Checkpointed LLM calls**: `@flyte.trace` provides automatic checkpointing at the
   function level, enabling recovery without re-running expensive API calls.

3. **Agentic patterns**: The generate-critique-revise loop demonstrates how to build
   self-improving AI workflows with clear observability through `flyte.group`.

4. **Parallel execution**: `asyncio.gather` runs independent operations concurrently,
   maximizing throughput when generating multiple output formats.
