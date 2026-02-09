---
title: Basic project
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Basic project: RAG

This example demonstrates a two-stage RAG (Retrieval-Augmented Generation) pattern:
an offline embedding pipeline that processes and stores quotes, followed by an online
serving application that enables semantic search.

## Concepts covered

- `TaskEnvironment` for defining task execution environments
- `Dir` artifacts for passing directories between tasks
- `AppEnvironment` for serving applications
- `Parameter` and `RunOutput` for connecting apps to task outputs
- Semantic search with sentence-transformers and ChromaDB

## Part 1: The embedding pipeline

The embedding pipeline fetches quotes from a public API, creates vector embeddings
using sentence-transformers, and stores them in a ChromaDB database.

### Setting up the environment

The `TaskEnvironment` defines the execution environment for all tasks in the pipeline.
It specifies the container image, required packages, and resource allocations:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/embed.py" lang="python" fragment="embedding-env" >}}

The environment uses:
- `Image.from_debian_base()` to create a container with Python 3.12
- `with_pip_packages()` to install sentence-transformers and ChromaDB
- `Resources` to request 2 CPUs and 4GB of memory
- `cache="auto"` to enable automatic caching of task outputs

### Fetching data

The `fetch_quotes` task retrieves quotes from a public API:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/embed.py" lang="python" fragment="fetch-quotes" >}}

This task demonstrates:
- Async task definition with `async def`
- Returning structured data (`list[dict]`) from a task
- Using the `@embedding_env.task` decorator to associate the task with its environment

### Creating embeddings

The `embed_quotes` task creates vector embeddings and stores them in ChromaDB:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/embed.py" lang="python" fragment="embed-quotes" >}}

Key points:
- Uses the `all-MiniLM-L6-v2` model from sentence-transformers (runs on CPU)
- Creates a persistent ChromaDB database with cosine similarity
- Returns a `Dir` artifact that captures the entire database directory
- The `await Dir.from_local()` call uploads the directory to artifact storage

### Orchestrating the pipeline

The main pipeline task composes the individual tasks:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/embed.py" lang="python" fragment="embedding-pipeline" >}}

### Running the pipeline

To run the embedding pipeline:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/embed.py" lang="python" fragment="main" >}}

```bash
uv run embed.py
```

The pipeline will:
1. Fetch 100 quotes from the API
2. Create embeddings using sentence-transformers
3. Store everything in a ChromaDB database
4. Return the database as a `Dir` artifact

## Part 2: The serving application

The serving application provides a Streamlit web interface for searching quotes
using the embeddings created by the pipeline.

### App environment configuration

The `AppEnvironment` defines how the application runs:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/serve.py" lang="python" fragment="app-env" >}}

Key configuration:
- `args` specifies the command to run the Streamlit app
- `port=8080` exposes the application on port 8080
- `parameters` defines inputs to the app:
  - `RunOutput` connects to the embedding pipeline's output
  - `download=True` downloads the directory to local storage
  - `env_var="QUOTES_DB_PATH"` makes the path available to the app
- `include=["app.py"]` bundles the Streamlit app with the deployment

### The Streamlit application

The app loads the ChromaDB database using the path from the environment variable:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/app.py" lang="python" fragment="load-db" >}}

The search interface provides a text input and result count slider:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/app.py" lang="python" fragment="search-ui" >}}

When the user searches, the app encodes the query and finds similar quotes:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/app.py" lang="python" fragment="search-logic" >}}

The app also includes a random quote feature:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/app.py" lang="python" fragment="random-quote" >}}

### Deploying the app

To deploy the quote search application:

{{< code file="/external/unionai-examples/v2/user-guide/basic-project/serve.py" lang="python" fragment="main" >}}

```bash
uv run serve.py
```

The app will be deployed and automatically connected to the embedding pipeline's
output through the `RunOutput` parameter.

## Key takeaways

1. **Two-stage RAG pattern**: Separate offline embedding creation from online serving
   for better resource utilization and cost efficiency.

2. **Dir artifacts**: Use `Dir` to pass entire directories (like databases) between
   tasks and to serving applications.

3. **RunOutput**: Connect applications to task outputs declaratively, enabling
   automatic data flow between pipelines and apps.

4. **CPU-friendly embeddings**: The `all-MiniLM-L6-v2` model runs efficiently on CPU,
   making this pattern accessible without GPU resources.
