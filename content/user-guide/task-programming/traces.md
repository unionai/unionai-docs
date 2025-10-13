---
title: Traces
weight: 130
variants: +flyte +serverless +byoc +selfmanaged
---

# Traces

The `@flyte.trace` decorator provides fine-grained observability and resumption capabilities for functions called within your Flyte workflows.
Traces are primarily used on **helper functions** that tasks call to perform specific operations like API calls, data processing, or computations.
Traces are particularly useful for [managing the challenges of non-deterministic behavior in workflows](../considerations#non-deterministic-behavior)), allowing you to track execution details and resume from failures.

## Tasks vs. traced functions

Flyte differentiates between tasks and traced functions:

- **Tasks** (`@env.task`): The orchestration layer that manages workflow execution, caching, and resources.
- **Traced functions** (`@flyte.trace`) = Helper functions that perform specific operations and create checkpoints.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/traces.py" fragment="tasks-vs-traced" lang="python" >}}

This division has the following benefits:

- **Granular observability**: See exactly which helper functions succeed or fail
- **Efficient resumption**: Skip successful operations when workflows resume after failures
- **Clean architecture**: Tasks handle orchestration, traced functions handle execution

## How traces work

### Context requirement

Traces only function within task execution contexts. They either fail or do nothing when called outside tasks:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/traces.py" fragment="context" lang="python" >}}

> [!NOTE]
> Tracing of synchronous functions (within a task context) is coming soon.

### What Gets Traced

Traces capture detailed execution information:
- **Execution time**: How long each function call takes.
- **Inputs and outputs**: Function parameters and return values.
- **Checkpoints**: State that enables workflow resumption.

### Errors are not recorded

Errors are not traced. Only successful executions are recorded.
Any failure will bubble up and user code can retry it.

### Supported Function Types

The trace decorator works with:
- **Synchronous functions**: Regular Python functions **(Coming soon)**.
- **Asynchronous functions**: Functions defined with `async def`.
- **Generator functions**: Functions that `yield` values.
- **Async generators**: Functions that `async yield` values.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/traces.py" fragment="function-types" lang="python" >}}

## Task Orchestration Pattern

The typical Flyte workflow follows this pattern:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/traces.py" fragment="pattern" lang="python" >}}

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

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/traces.py" fragment="caching-vs-checkpointing" lang="python" >}}

### Execution Flow

1. **Task Submission**: Task is submitted with input parameters
2. **Cache Check**: Flyte checks if identical task execution exists in cache
3. **Cache Hit**: If cached, return cached result immediately (no traces needed)
4. **Cache Miss**: Begin fresh execution
5. **Trace Checkpoints**: Each `@flyte.trace` function creates resumption points
6. **Failure Recovery**: If workflow fails, resume from last successful checkpoint
7. **Task Completion**: Final result is cached for future identical inputs


## Error Handling and Observability

Traces capture comprehensive execution information for debugging and monitoring:

<!-- TODO:
Add more examples of error handling with traces

-->
{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/traces.py" fragment="error-handling" lang="python" >}}

**What traces capture:**
- **Execution time**: Duration of each function call
- **Inputs and outputs**: Function parameters and return values
- **Errors**: Complete exception information when functions fail
- **Action IDs**: Unique identifiers for each execution

## Best Practices

### When to Use Traces

Use `@flyte.trace` for:

- **External API calls**: Track responses, errors, and performance
- **Expensive computations**: Enable resumption for long-running operations
- **Data processing steps**: Monitor transformation pipelines
- **LLM interactions**: Track prompts, responses, and model performance
- **Any operation that benefits from checkpointing**

### Recommended Architecture

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/traces/traces.py" fragment="recommended" lang="python" >}}

### Performance Considerations

- **Minimal overhead**: Traces add negligible performance impact
- **Efficient serialization**: Only occurs when checkpointing is enabled
- **Streaming support**: Generator functions stream efficiently without buffering

<!--
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