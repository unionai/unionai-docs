---
title: Resilient generation
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Resilient generation

This section covers the foundational patterns for building resilient LLM-powered
tasks: reusable environments, traced function calls, and retry strategies.

## Two environments

This example uses two task environments with different characteristics:

1. **`llm_env`** (reusable): For tasks that make many LLM calls in a loop or
   process batches in parallel. Container reuse avoids cold starts.
2. **`driver_env`** (standard): For orchestration tasks that fan out work to
   other tasks but don't make LLM calls themselves.

### Reusable environment for LLM work

When processing a batch of topics, each topic goes through multiple LLM calls
(generate, critique, revise, repeat). With 5 topics × ~7 calls each, that's ~35
LLM calls. `ReusePolicy` keeps containers warm to handle this efficiently:

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/generate.py" lang="python" fragment="reusable-env" >}}

### ReusePolicy parameters

| Parameter | Description |
|-----------|-------------|
| `replicas` | Number of container instances to keep ready (or `(min, max)` tuple) |
| `concurrency` | Maximum tasks per container at once |
| `scaledown_ttl` | Minimum wait before scaling down a replica |
| `idle_ttl` | Time after which idle containers shut down completely |

The configuration above keeps 2 containers ready, allows 4 concurrent tasks per
container, waits 5 minutes before scaling down, and shuts down after 30 minutes
of inactivity.

{{< note >}}
Both `scaledown_ttl` and `idle_ttl` must be at least 30 seconds.
{{< /note >}}

### Standard environment for orchestration

The driver environment doesn't need container reuse—it just coordinates work.
The `depends_on` parameter declares that tasks in this environment call tasks
in `llm_env`, ensuring both environments are deployed together:

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/generate.py" lang="python" fragment="driver-env" >}}

## Traced LLM calls

The `@flyte.trace` decorator provides automatic checkpointing at the function level.
When a traced function completes successfully, its result is cached. If the task
fails and restarts, previously completed traced calls return their cached results
instead of re-executing.

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/generate.py" lang="python" fragment="traced-llm-call" >}}

### Benefits of tracing

1. **Cost savings**: Failed tasks don't re-run expensive API calls that already succeeded
2. **Faster recovery**: Resuming from checkpoints skips completed work
3. **Observability**: Each traced call appears in the Flyte UI with timing data

### When to use @flyte.trace

Use `@flyte.trace` for:
- LLM API calls (OpenAI, Anthropic, etc.)
- External API requests
- Any expensive operation you don't want to repeat on retry

Don't use `@flyte.trace` for:
- Simple computations (overhead outweighs benefit)
- Operations with side effects that shouldn't be skipped

## Traced helper functions

The LLM-calling functions are decorated with `@flyte.trace` rather than being
separate tasks. This keeps the architecture simple while still providing
checkpointing:

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/generate.py" lang="python" fragment="generate-draft" >}}

These traced functions run inside the `refine_report` task. If the task fails
and retries, completed traced calls return cached results instead of re-executing.

## Retry strategies

The task that orchestrates the LLM calls uses `retries` to handle transient failures:

```python
@llm_env.task(retries=3)
async def refine_report(topic: str, ...) -> str:
    # Traced functions are called here
    draft = await generate_initial_draft(topic)
    ...
```

### Configuring retries

You can specify retries as a simple integer:

```python
@llm_env.task(retries=3)
async def my_task():
    ...
```

Or use `RetryStrategy` for more control:

```python
@llm_env.task(retries=flyte.RetryStrategy(count=3))
async def my_task():
    ...
```

### Combining tracing with retries

When you combine `@flyte.trace` with task-level retries, you get the best of both:

1. Task fails after completing some traced calls
2. Flyte retries the task
3. Previously completed traced calls return cached results
4. Only the failed operation (and subsequent ones) re-execute

This pattern is essential for multi-step LLM workflows where you don't want to
re-run the entire chain when a single call fails.

## Structured prompts

The example uses a separate `prompts.py` module for system prompts and Pydantic models:

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/prompts.py" lang="python" fragment="system-prompts" >}}

### Pydantic models for structured output

LLM responses can be unpredictable. Using Pydantic models with JSON mode ensures
you get structured, validated data:

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/prompts.py" lang="python" fragment="critique-model" >}}

The `Critique` model validates that:
- `score` is an integer between 1 and 10
- `strengths` and `improvements` are lists of strings
- All required fields are present

If the LLM returns malformed JSON, Pydantic raises a validation error, which
triggers a retry (if configured).

## Next steps

With resilient generation in place, you're ready to build the
[agentic refinement loop](./agentic-refinement).
