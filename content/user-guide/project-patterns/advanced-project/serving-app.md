---
title: Serving app
description: Connect a serving app to a pipeline so it can display results and take input.
icon: window
weight: 4
variants: +flyte +union
---

# Serving app

The final piece is a serving application that displays generated reports and
provides an interactive interface. This demonstrates how to connect apps to
pipeline outputs using `RunOutput`.

## App environment configuration

The `AppEnvironment` defines how the Streamlit application runs and connects to
the batch report pipeline:

{{< code file="/unionai-examples/v2/user-guide/advanced-project/serve.py" lang="python" fragment="app-env" >}}

### Key configuration

| Setting | Purpose |
|---------|---------|
| `args` | Command to run the Streamlit app |
| `port` | Port the app listens on |
| `parameters` | Inputs to the app, including pipeline connections |
| `include` | Additional files to bundle with the app |

### Connecting to pipeline output with RunOutput

The `RunOutput` parameter connects the app to the batch pipeline's output:

```python
Parameter(
    name="reports",
    value=RunOutput(
        task_name="driver.report_batch_pipeline",
        type="directory",
    ),
    download=True,
    env_var="REPORTS_PATH",
)
```

This configuration:

1. **Finds the latest successful run** of `report_batch_pipeline` in the `driver` environment when you deploy the app
2. **Downloads the output** to local storage (`download=True`)
3. **Sets an environment variable** with the path (`REPORTS_PATH`)

The app can then scan this directory for all generated reports.

## The Streamlit application

The app loads and displays all generated reports from the batch pipeline:

{{< code file="/unionai-examples/v2/user-guide/advanced-project/app.py" lang="python" fragment="load-reports" >}}

### Displaying multiple reports

The app provides a sidebar for selecting between reports when multiple are available:

{{< code file="/unionai-examples/v2/user-guide/advanced-project/app.py" lang="python" fragment="display-reports" >}}

Features:

- **Report selector**: Sidebar navigation when multiple reports exist
- **Executive summary**: Expandable section with key takeaways
- **Tabbed views**: Switch between Markdown and HTML preview
- **Download buttons**: Export in any format

### Generation instructions

The app includes instructions for generating new reports:

{{< code file="/unionai-examples/v2/user-guide/advanced-project/app.py" lang="python" fragment="generation-ui" >}}

## Deploying the app

To deploy the report generator application:

{{< code file="/unionai-examples/v2/user-guide/advanced-project/serve.py" lang="python" fragment="main" >}}

```bash
uv run serve.py
```

The deployment process:

1. Builds a container image with the app code
2. Deploys the app to {{< key product_name >}}
3. Connects to the latest pipeline output
4. Returns the app URL

## Workflow: Generate then view

The typical workflow is:

1. **Run the batch pipeline** to generate reports:

   ```bash
   uv run generate.py
   ```

2. **Deploy the app again** to view results:

   ```bash
   uv run serve.py
   ```

3. **Access the app** at the provided URL and browse all generated reports

Each deployment picks up the latest successful pipeline run, so after you generate a new
batch, deploy the app again to see the most recent results.

## Pick up new runs with RunOutput

The `RunOutput` connection is resolved when you deploy the app: the latest successful
batch pipeline output is looked up at deploy time and its path is stored in the
deployed app. Restarting the app reuses that stored output. To pick up a newer
run, deploy the app again.

For real-time updates without redeployment, you could:

1. Poll for new runs using the Flyte API
2. Implement a webhook that triggers app refresh
3. Use a database to track run status

## Complete example structure

Here's the full project structure:

```
advanced-project/
├── generate.py    # Main pipeline with agentic refinement
├── prompts.py     # System prompts and Pydantic models
├── serve.py       # App deployment configuration
└── app.py         # Streamlit user interface
```

## Running the complete example

1. **Set up the secret**:

   ```bash
   flyte create secret openai-api-key
   ```

2. **Run the pipeline**:

   ```bash
   cd /path/to/unionai-examples/v2/user-guide/advanced-project
   uv run generate.py
   ```

3. **Deploy the app**:

   ```bash
   uv run serve.py
   ```

4. **Open the app URL** and view your generated report

## Summary

This example demonstrated:

| Feature | What it does |
|---------|--------------|
| `ReusePolicy` | Keeps containers warm for high-throughput batch processing |
| `@flyte.trace` | Checkpoints LLM calls for recovery and observability |
| `RetryStrategy` | Handles transient API failures gracefully |
| `flyte.group` | Organizes parallel batches and iterations in the UI |
| `asyncio.gather` | Fans out to process multiple topics concurrently |
| Pydantic models | Structured LLM outputs |
| `AppEnvironment` | Deploys interactive Streamlit apps |
| `RunOutput` | Connects apps to pipeline outputs |

These patterns form the foundation for building production-grade AI workflows
that are resilient, observable, and cost-efficient at scale.
