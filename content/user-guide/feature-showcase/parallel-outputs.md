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

Each output format has a dedicated traced function:

{{< code file="/external/unionai-examples/v2/user-guide/feature-showcase/generate.py" lang="python" fragment="format-functions" >}}

### Why trace formatting functions?

Even though markdown and HTML conversion are fast, the summary generation calls
the LLM. By tracing all formatting functions:

1. **Consistency**: All formatters follow the same pattern
2. **Recovery**: If summary generation fails, markdown/HTML results are cached
3. **Observability**: Each format appears separately in the UI

## Parallel execution with asyncio.gather

The `format_outputs` task runs all formatters concurrently:

{{< code file="/external/unionai-examples/v2/user-guide/feature-showcase/generate.py" lang="python" fragment="parallel-formatting" >}}

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

In the Flyte UI, this appears as:

```
report_pipeline
├── generate_initial_draft
├── refinement_1
│   └── ...
└── formatting
    ├── format_as_markdown (traced)
    ├── format_as_html (traced)
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

## The main pipeline

The main pipeline task orchestrates everything:

{{< code file="/external/unionai-examples/v2/user-guide/feature-showcase/generate.py" lang="python" fragment="main-pipeline" >}}

### Pipeline flow

1. **refine_report**: Generates and iteratively improves the content
2. **format_outputs**: Creates all output formats in parallel
3. **Return Dir**: Provides the formatted outputs as a directory artifact

## Running the pipeline

To run the complete pipeline:

{{< code file="/external/unionai-examples/v2/user-guide/feature-showcase/generate.py" lang="python" fragment="main" >}}

```bash
uv run generate.py
```

The pipeline will:
1. Generate an initial draft on the given topic
2. Critique and revise until quality threshold is met
3. Generate Markdown, HTML, and summary formats in parallel
4. Return a directory containing all outputs

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
    report_pipeline,
    topic="...",
    max_iterations=2,      # Limit iterations
    quality_threshold=7,   # Accept slightly lower quality
)
```

### 3. Use caching effectively

The `cache="auto"` setting on the environment caches task outputs. Running the
same pipeline with the same inputs returns cached results instantly:

```python
env = flyte.TaskEnvironment(
    ...
    cache="auto",  # Cache task outputs
)
```

### 4. Batch operations

If generating reports for multiple topics, consider batching:

```python
topics = ["Topic A", "Topic B", "Topic C"]
runs = [flyte.run(report_pipeline, topic=t) for t in topics]
for run in runs:
    run.wait()
```

With `ReusePolicy`, the same containers handle all topics, minimizing cold starts.

## Next steps

Learn how to [deploy a serving app](serving-app) that connects to the pipeline
outputs and provides an interactive UI for report generation.
