---
title: Serving app
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Serving app

The final piece is a serving application that displays generated reports and
provides an interactive interface. This demonstrates how to connect apps to
pipeline outputs using `RunOutput`.

## App environment configuration

The `AppEnvironment` defines how the Streamlit application runs and connects to
the report generation pipeline:

{{< code file="/external/unionai-examples/v2/user-guide/feature-showcase/serve.py" lang="python" fragment="app-env" >}}

### Key configuration

| Setting | Purpose |
|---------|---------|
| `args` | Command to run the Streamlit app |
| `port` | Port the app listens on |
| `secrets` | API keys needed by the app |
| `parameters` | Inputs to the app, including pipeline connections |
| `include` | Additional files to bundle with the app |

### Connecting to pipeline output with RunOutput

The `RunOutput` parameter connects the app to the report pipeline's output:

```python
Parameter(
    name="latest_report",
    value=RunOutput(
        task_name="report-generator.report_pipeline",
        type="directory",
    ),
    download=True,
    env_var="LATEST_REPORT_PATH",
)
```

This configuration:
1. **Finds the latest run** of `report_pipeline` in the `report-generator` environment
2. **Downloads the directory** output to local storage (`download=True`)
3. **Sets an environment variable** with the path (`LATEST_REPORT_PATH`)

The app can then read files from this directory without knowing the specific
run ID or storage location.

## The Streamlit application

The app loads and displays the generated report:

{{< code file="/external/unionai-examples/v2/user-guide/feature-showcase/app.py" lang="python" fragment="load-report" >}}

### Displaying the report

The app provides multiple views of the generated content:

{{< code file="/external/unionai-examples/v2/user-guide/feature-showcase/app.py" lang="python" fragment="display-report" >}}

Features:
- **Executive summary**: Expandable section with the key takeaways
- **Tabbed views**: Switch between Markdown and HTML preview
- **Download buttons**: Export in any format

### Generation instructions

The app includes instructions for generating new reports:

{{< code file="/external/unionai-examples/v2/user-guide/feature-showcase/app.py" lang="python" fragment="generation-ui" >}}

## Deploying the app

To deploy the report generator application:

{{< code file="/external/unionai-examples/v2/user-guide/feature-showcase/serve.py" lang="python" fragment="main" >}}

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

1. **Run the pipeline** to generate a report:
   ```bash
   uv run generate.py
   ```

2. **Deploy or refresh the app** to view results:
   ```bash
   uv run serve.py
   ```

3. **Access the app** at the provided URL

The app automatically picks up the latest pipeline run, so you can generate
multiple reports and always see the most recent one.

## Automatic updates with RunOutput

The `RunOutput` connection is evaluated at app startup. Each time the app
restarts or redeploys, it fetches the latest pipeline output.

For real-time updates without redeployment, you could:
1. Poll for new runs using the Flyte API
2. Implement a webhook that triggers app refresh
3. Use a database to track run status

## Complete example structure

Here's the full project structure:

```
feature-showcase/
├── generate.py    # Main pipeline with agentic refinement
├── prompts.py     # System prompts and Pydantic models
├── serve.py       # App deployment configuration
└── app.py         # Streamlit user interface
```

## Running the complete example

1. **Set up the secret**:
   ```bash
   flyte secret create openai-api-key
   ```

2. **Run the pipeline**:
   ```bash
   cd /path/to/unionai-examples/v2/user-guide/feature-showcase
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
| `ReusePolicy` | Keeps containers warm for cost-efficient LLM workloads |
| `@flyte.trace` | Checkpoints LLM calls for recovery and observability |
| `RetryStrategy` | Handles transient API failures gracefully |
| `flyte.group` | Organizes agentic iterations in the UI |
| `asyncio.gather` | Runs independent operations in parallel |
| `RunOutput` | Connects apps to pipeline outputs |

These patterns form the foundation for building production-grade AI workflows
that are resilient, observable, and cost-efficient.
