---
title: Traces
weight: 130
variants: +flyte +serverless +byoc +selfmanaged
---

# Traces

The `@flyte.trace` decorator provides fine-grained observability and resumption capabilities for functions called within your Flyte workflows.
Traces are used on **helper functions** that tasks call to perform specific operations like API calls, data processing, or computations.
Traces are particularly useful for [managing the challenges of non-deterministic behavior in workflows](../considerations#non-deterministic-behavior), allowing you to track execution details and resume from failures.

## What are traced functions for?

At the top level, Flyte workflows are composed of **tasks**. But it is also common practice to break down complex task logic into smaller, reusable functions by defining helper functions that tasks call to perform specific operations.

Any helper functions defined or imported into the same file as a task definition are automatically uploaded to the Flyte environment alongside the task when it is deployed.

At the task level, observability and resumption of failed executions is provided by caching, but what if you want these capabilities at a more granular level, for the individual operations that tasks perform?

This is where **traced functions** come in. By decorating helper functions with `@flyte.trace`, you enable:
- **Detailed observability**: Track execution time, inputs/outputs, and errors for each function call.
- **Fine-grained resumption**: If a workflow fails, resume from the last successful traced function instead of re-running the entire task.
Each traced function is effectively a checkpoint within its task.

Here is an example:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/task_vs_trace.py" fragment="all" lang="python" >}}

## What Gets Traced

Traces capture detailed execution information:
- **Execution time**: How long each function call takes.
- **Inputs and outputs**: Function parameters and return values.
- **Checkpoints**: State that enables workflow resumption.

### Errors are not recorded

Only successful trace executions are recorded in the checkpoint system. When a traced function fails, the exception propagates up to your task code where you can handle it with standard error handling patterns.

### Supported Function Types

The trace decorator works with:
- **Asynchronous functions**: Functions defined with `async def`.
- **Generator functions**: Functions that `yield` values.
- **Async generators**: Functions that `async yield` values.

> [!NOTE]
> Currently tracing only works for asynchronous functions. Tracing of synchronous functions is coming soon.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/function_types.py" fragment="all" lang="python" >}}

## Task Orchestration Pattern

The typical Flyte workflow follows this pattern:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/pattern.py" fragment="all" lang="python" >}}

**Benefits of this pattern:**
- If `search_web` succeeds but `summarize_content` fails, resumption skips the search step
- Each operation is independently observable and debuggable
- Clear separation between workflow coordination (task) and execution (traced functions)

## Relationship to Caching and Checkpointing

Understanding how traces work with Flyte's other execution features:

| Feature | Scope | Purpose | Default Behavior |
|---------|-------|---------|------------------|
| **Task Caching** | Entire task execution (`@env.task`) | Skip re-running tasks with same inputs | Enabled (`cache="auto"`) |
| **Traces** | Individual helper functions | Observability and fine-grained resumption | Manual (requires `@flyte.trace`) |
| **Checkpointing** | Workflow state | Resume workflows from failure points | Automatic when traces are used |

### How They Work Together

<!-- TODO
Lets use better typing for all of these examples, we have the opportunity to make this right for our users
-->

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/caching_vs_checkpointing.py" fragment="all" lang="python" >}}

### Execution Flow

1. **Task Submission**: Task is submitted with input parameters
2. **Cache Check**: Flyte checks if identical task execution exists in cache
3. **Cache Hit**: If cached, return cached result immediately (no traces needed)
4. **Cache Miss**: Begin fresh execution
5. **Trace Checkpoints**: Each `@flyte.trace` function creates resumption points
6. **Failure Recovery**: If workflow fails, resume from last successful checkpoint
7. **Task Completion**: Final result is cached for future identical inputs

<!--
Clarify what actually happens on error vs success with traces

## Error Handling and Observability

Traces capture comprehensive execution information for debugging and monitoring:


{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/error_handling.py" fragment="all" lang="python" >}}

**What traces capture:**
- **Execution time**: Duration of each function call
- **Inputs and outputs**: Function parameters and return values
- **Checkpoints**: State that enables workflow resumption from successful executions
- **Action IDs**: Unique identifiers for each execution

**Error handling:**
- Errors from traced functions are not recorded in checkpoints
- Exceptions propagate to your task code for standard error handling
- The error_handling example shows how to catch and handle these exceptions in your task


TODO:
Ketan Umare:
we should show an example where tasks and traces can be used interchangeably

## Examples in Practice

### LLM Pipeline with Traces

```python
import flyte

env = flyte.TaskEnvironment("llm-pipeline")

@flyte.trace
async def call_llm(prompt: str, model: str = "gpt-4") -> str:
    """Call LLM with specified model."""
    response = await llm_client.chat(prompt, model=model)
    return response

@flyte.trace
async def extract_entities(text: str) -> list[str]:
    """Extract named entities from text."""
    entities = await nlp_service.extract_entities(text)
    return entities

@env.task
async def process_documents(documents: list[str]) -> dict:
    """Process multiple documents through LLM pipeline."""
    results = []

    for doc in documents:
        # Each call is traced for monitoring and resumption
        summary = await call_llm(f"Summarize: {doc}")
        entities = await extract_entities(summary)

        results.append({
            "document": doc,
            "summary": summary,
            "entities": entities
        })

    return {"processed_documents": results, "total_count": len(results)}
```

This comprehensive tracing system provides visibility into your workflow execution while enabling robust error recovery and resumption capabilities.
-->