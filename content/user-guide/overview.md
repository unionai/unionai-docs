---
title: Flyte overview
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Flyte overview

In this guide we cover how to build AI applications, data pipelines, and ML workflows using the Flyte 2 SDK.

Programs written using the Flyte 2 SDK can run on either a Union.ai or Flyte OSS back-end. This guide applies to both.

## Pure Python, no DSL

Flyte lets you write workflows in standard Python—no domain-specific language, no special syntax, no restrictions.

Your "workflow" is simply a task that calls other tasks:

```python
@env.task()
async def my_workflow(data: list[str]) -> list[str]:
    results = []
    for item in data:
        if should_process(item):
            result = await process_item(item)
            results.append(result)
    return results
```

You can use everything Python offers:

- **Loops and conditionals** — standard `for`, `while`, `if-elif-else`
- **Error handling** — `try/except` blocks work as expected
- **Async/await** — native Python concurrency model
- **Any library** — import and use whatever you need

This means no learning curve beyond Python itself, and no fighting a DSL when your requirements don't fit its constraints.

## Durability

Every task execution in Flyte is automatically persisted. Inputs, outputs, and intermediate results are stored in an object store, giving you:

- **Full observability** — see exactly what data flowed through each step
- **Audit trail** — track what ran, when, and with what parameters
- **Data lineage** — trace outputs back to their inputs

This persistence happens automatically. You don't need to add logging or manually save state—Flyte handles it.

## Reproducibility

Flyte ensures that runs can be reproduced exactly:

- **Deterministic execution** — same inputs produce same outputs
- **Caching** — task results are cached and reused when inputs match
- **Versioned containers** — code runs in the same environment every time

Caching is configurable per task:

```python
@env.task(cache=True)
async def expensive_computation(data: str) -> str:
    # This result will be cached and reused for identical inputs
    ...
```

When you rerun a workflow, Flyte serves cached results for unchanged tasks rather than recomputing them.

## Recoverability

When something fails, Flyte doesn't make you start over. Failed workflows can resume from where they left off:

- **Completed tasks are preserved** — successful outputs remain cached
- **Retry from failure point** — no need to re-execute what already succeeded
- **Fine-grained checkpoints** — the `@flyte.trace` decorator creates checkpoints within tasks

This reduces wasted compute and speeds up debugging. When a task fails after hours of prior computation, you fix the issue and continue—not restart.

## Built for scale

Flyte handles the hard parts of distributed execution:

- **Parallel execution** — express parallelism with `asyncio.gather()`, Flyte handles the rest
- **Dynamic workflows** — construct workflows based on runtime data, not just static definitions
- **Fast scheduling** — reusable containers achieve millisecond-level task startup
- **Resource management** — specify CPU, memory, and GPU requirements per task

## What this means in practice

Consider a data pipeline that processes thousands of files, trains a model, and deploys it:

- If file processing fails on item 847, you fix the issue and resume from item 847
- If training succeeds but deployment fails, you redeploy without retraining
- If you rerun next week with the same data, cached results skip redundant computation
- If you need to audit what happened, every step is recorded

Flyte gives you the flexibility of Python scripts with the reliability of a production system.
