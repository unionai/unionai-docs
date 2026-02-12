---
title: Parallel outputs
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Parallel outputs

After refining the report, the pipeline generates multiple output formats in
parallel. This demonstrates how to use `asyncio.gather` for concurrent execution
within a task.

## The formatting functions

The pipeline generates three outputs: markdown, HTML, and an executive summary.
Only `generate_summary` uses `@flyte.trace` because it makes an LLM call.
The markdown and HTML functions are simple, deterministic transformations that
don't benefit from checkpointing:

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/generate.py" lang="python" fragment="format-functions" >}}

### When to trace and when not to

Use `@flyte.trace` for operations that are expensive, non-deterministic, or
call external APIs (like `generate_summary`). Skip it for cheap, deterministic
transformations (like `format_as_markdown` and `format_as_html`) where
re-running on retry is trivial.

## Parallel execution with asyncio.gather

The `format_outputs` task runs all formatters concurrently:

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/generate.py" lang="python" fragment="parallel-formatting" >}}

### How asyncio.gather works

`asyncio.gather` takes multiple coroutines and runs them concurrently:

```python
markdown, html, summary = await asyncio.gather(
    format_as_markdown(content),  # Starts immediately
    format_as_html(content),      # Starts immediately
    generate_summary(content),    # Starts immediately
)
# All three run concurrently, results returned in order
```

Without `gather`, these would run sequentially:

```python
# Sequential (slower)
markdown = await format_as_markdown(content)  # Wait for completion
html = await format_as_html(content)          # Then start this
summary = await generate_summary(content)     # Then start this
```

### When to use asyncio.gather

Use `asyncio.gather` when:
- Operations are independent (don't depend on each other's results)
- Operations are I/O-bound (API calls, file operations)
- You want to minimize total execution time

Don't use `asyncio.gather` when:
- Operations depend on each other
- Operations are CPU-bound (use process pools instead)
- Order of execution matters for side effects

## Grouping parallel operations

The parallel formatting is wrapped in a group for UI clarity:

```python
with flyte.group("formatting"):
    markdown, html, summary = await asyncio.gather(...)
```

In the Flyte UI, the traced call within the group is visible:

```
format_outputs
└── formatting
    ├── format_as_markdown
    ├── format_as_html
    └── generate_summary (traced)
```

## Collecting outputs in a directory

The formatted outputs are written to a temporary directory and returned as a
`Dir` artifact:

```python
output_dir = tempfile.mkdtemp()

with open(os.path.join(output_dir, "report.md"), "w") as f:
    f.write(markdown)

with open(os.path.join(output_dir, "report.html"), "w") as f:
    f.write(html)

with open(os.path.join(output_dir, "summary.txt"), "w") as f:
    f.write(summary)

return await Dir.from_local(output_dir)
```

The `Dir.from_local()` call uploads the directory to {{< key product_name >}}'s
artifact storage, making it available to downstream tasks or applications.

## The batch pipeline

The batch pipeline processes multiple topics in parallel, demonstrating where
`ReusePolicy` truly shines:

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/generate.py" lang="python" fragment="batch-pipeline" >}}

### Pipeline flow

1. **Fan out refine_all**: Process all topics in parallel using `asyncio.gather`
2. **Fan out format_all**: Format all reports in parallel
3. **Return list of Dirs**: Each directory contains one report's outputs

With 5 topics, each making ~7 LLM calls, the reusable container pool handles
~35 LLM calls efficiently without cold starts.

## Running the pipeline

To run the batch pipeline:

{{< code file="/external/unionai-examples/v2/user-guide/advanced-project/generate.py" lang="python" fragment="main" >}}

```bash
uv run generate.py
```

The pipeline will:
1. Process all topics in parallel (each with iterative refinement)
2. Format all reports in parallel
3. Return a list of directories, each containing a report's outputs

## Cost optimization tips

### 1. Choose the right model

The example uses `gpt-4o-mini` for cost efficiency. For higher quality (at higher
cost), you could use `gpt-4o` or `gpt-4-turbo`:

```python
response = await client.chat.completions.create(
    model="gpt-4o",  # More capable, more expensive
    ...
)
```

### 2. Tune iteration parameters

Fewer iterations mean fewer API calls:

```python
run = flyte.run(
    report_batch_pipeline,
    topics=["Topic A", "Topic B"],
    max_iterations=2,      # Limit iterations
    quality_threshold=7,   # Accept slightly lower quality
)
```

### 3. Use caching effectively

The `cache="auto"` setting on the environment caches task outputs. Running the
same pipeline with the same inputs returns cached results instantly:

```python
llm_env = flyte.TaskEnvironment(
    ...
    cache="auto",  # Cache task outputs
)
```

### 4. Scale the batch

The batch pipeline already processes topics in parallel. To handle larger batches,
adjust the `ReusePolicy`:

```python
reusable=flyte.ReusePolicy(
    replicas=4,           # More containers for larger batches
    concurrency=4,        # Tasks per container
    ...
)
```

With 4 replicas × 4 concurrency = 16 slots, you can process 16 topics' refinement
tasks concurrently.

## Next steps

Learn how to [deploy a serving app](./serving-app) that connects to the pipeline
outputs and provides an interactive UI for report generation.
