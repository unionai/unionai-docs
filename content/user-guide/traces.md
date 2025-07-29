---
title: Traces
weight: 130
variants: +flyte +serverless +byoc +selfmanaged
---

# Traces

The `@flyte.trace` decorator provides fine-grained observability and resumption capabilities for functions called within your Flyte workflows.
Traces are primarily used on **helper functions** that tasks call to perform specific operations like API calls, data processing, or computations.
Traces are particularly useful for [managing the challenges of non-deterministic behavior in workflows](./considerations#non-deterministic-behavior)), allowing you to track execution details and resume from failures.

## Tasks vs. traced functions

Flyte differentiates between tasks and traced functions:

- **Tasks** (`@env.task`): The orchestration layer that manages workflow execution, caching, and resources.
- **Traced functions** (`@flyte.trace`) = Helper functions that perform specific operations and create checkpoints.

```python
import flyte

env = flyte.TaskEnvironment("my-app")

# Traced helper functions - the main use case
@flyte.trace
async def call_llm(prompt: str) -> str:
    """Helper function for LLM calls - traced for observability."""
    response = await llm_client.chat(prompt)
    return response

@flyte.trace
async def process_data(data: str) -> dict:
    """Helper function for data processing - traced for checkpointing."""
    return await expensive_computation(data)

# Tasks orchestrate traced helper functions
@env.task
async def research_workflow(topic: str) -> dict:
    # Task coordinates the workflow
    llm_result = await call_llm(f"Generate research plan for: {topic}")
    processed_data = await process_data(llm_result)

    return {"topic": topic, "result": processed_data}
```

This division has the following benefits:

- **Granular observability**: See exactly which helper functions succeed or fail
- **Efficient resumption**: Skip successful operations when workflows resume after failures
- **Clean architecture**: Tasks handle orchestration, traced functions handle execution

## How traces work

### Context requirement

Traces only function within task execution contexts. They either fail or do nothing when called outside tasks:

```python
@flyte.trace
def sync_function(x: int) -> int:
    return x * 2

@flyte.trace
async def async_function(x: int) -> int:
    return x * 2

# ❌ Outside task context - neither work
sync_function(5)  # Fails
await async_function(5)  # Fails

# ✅ Within task context - both work and are traced
@env.task
async def my_task():
    result1 = sync_function(5)       # ✅ Traced! (Coming soon)
    result2 = await async_function(5) # ✅ Traced!
    return result1 + result2
```

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

```python
@flyte.trace
def sync_process(data: str) -> str:
    """Synchronous data processing."""
    return data.upper()

@flyte.trace
async def async_api_call(url: str) -> dict:
    """Asynchronous API call."""
    response = await http_client.get(url)
    return response.json()

@flyte.trace
def stream_data(items: list[str]):
    """Generator function for streaming."""
    for item in items:
        yield f"Processing: {item}"

@flyte.trace
async def async_stream_llm(prompt: str):
    """Async generator for streaming LLM responses."""
    async for chunk in llm_client.stream(prompt):
        yield chunk
```

## Task Orchestration Pattern

The typical Flyte workflow follows this pattern:

```python
# Helper functions - traced for observability
@flyte.trace
async def search_web(query: str) -> list[dict]:
    """Search the web and return results."""
    results = await search_api.query(query)
    return results

@flyte.trace
async def summarize_content(content: str) -> str:
    """Summarize content using LLM."""
    summary = await llm_client.summarize(content)
    return summary

@flyte.trace
async def extract_insights(summaries: list[str]) -> dict:
    """Extract insights from summaries."""
    insights = await analysis_service.extract_insights(summaries)
    return insights

# Task - orchestrates the traced helper functions
@env.task
async def research_pipeline(topic: str) -> dict:
    """Main research pipeline task."""

    # Each helper function creates a checkpoint
    search_results = await search_web(f"research on {topic}")

    summaries = []
    for result in search_results:
        summary = await summarize_content(result["content"])
        summaries.append(summary)

    final_insights = await extract_insights(summaries)

    return {
        "topic": topic,
        "insights": final_insights,
        "sources_count": len(search_results)
    }
```

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

```python
@env.task  # Task-level caching enabled by default
async def data_pipeline(dataset_id: str) -> dict:
    # 1. If this exact task with these inputs ran before,
    #    the entire task result is returned from cache

    # 2. If not cached, execution begins and each traced function
    #    creates checkpoints for resumption
    cleaned_data = await traced_data_cleaning(dataset_id)      # Checkpoint 1
    features = await traced_feature_extraction(cleaned_data)   # Checkpoint 2
    model_results = await traced_model_training(features)      # Checkpoint 3

    # 3. If workflow fails at step 3, resumption will:
    #    - Skip traced_data_cleaning (checkpointed)
    #    - Skip traced_feature_extraction (checkpointed)
    #    - Re-run only traced_model_training

    return {"dataset_id": dataset_id, "accuracy": model_results["accuracy"]}

@flyte.trace
async def traced_data_cleaning(dataset_id: str) -> list:
    """Creates checkpoint after successful execution."""
    return await expensive_cleaning_process(dataset_id)

@flyte.trace
async def traced_feature_extraction(data: list) -> dict:
    """Creates checkpoint after successful execution."""
    return await expensive_feature_process(data)

@flyte.trace
async def traced_model_training(features: dict) -> dict:
    """Creates checkpoint after successful execution."""
    return await expensive_training_process(features)
```

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
```python
@flyte.trace
async def risky_api_call(endpoint: str, data: dict) -> dict:
    """API call that might fail - traces capture errors."""
    try:
        response = await api_client.post(endpoint, json=data)
        return response.json()
    except Exception as e:
        # Error is automatically captured in trace
        logger.error(f"API call failed: {e}")
        raise

@env.task
async def error_handling_workflow():
    try:
        result = await risky_api_call("/process", {"invalid": "data"})
        return {"status": "success", "result": result}
    except Exception as e:
        # The error is recorded in the trace for debugging
        return {"status": "error", "message": str(e)}
```

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

```python
# ✅ Traced helper functions for specific operations
@flyte.trace
async def call_llm(prompt: str, model: str) -> str:
    """LLM interaction - traced for observability."""
    return await llm_client.chat(prompt, model=model)

@flyte.trace
async def search_database(query: str) -> list[dict]:
    """Database operation - traced for checkpointing."""
    return await db.search(query)

@flyte.trace
async def process_results(data: list[dict]) -> dict:
    """Data processing - traced for error tracking."""
    return await expensive_analysis(data)

# ✅ Tasks that orchestrate traced functions
@env.task
async def research_workflow(topic: str) -> dict:
    """Main workflow - coordinates traced operations."""
    search_results = await search_database(f"research: {topic}")
    analysis_prompt = f"Analyze these results: {search_results}"
    llm_analysis = await call_llm(analysis_prompt, "gpt-4")
    final_results = await process_results([{"analysis": llm_analysis}])

    return final_results
```

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