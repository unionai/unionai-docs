---
title: Single-script apps
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Single-script apps

The simplest way to build and deploy an app with Flyte is to write everything in a single Python script. This approach is perfect for:

- **Quick prototypes**: Rapidly test ideas and concepts
- **Simple services**: Basic HTTP servers, APIs, or dashboards
- **Learning**: Understanding how Flyte apps work without complexity
- **Minimal examples**: Demonstrating core functionality

All the code for your app—the application logic, the app environment configuration, and the deployment code—lives in one file. This makes it easy to understand, share, and deploy.

## Plain Python HTTP server

The simplest possible app is a plain Python HTTP server using Python's built-in `http.server` module. This requires no external dependencies beyond the Flyte SDK.

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/plain_python_server.py" lang=python >}}

### Key points

- **No external dependencies**: Uses only Python's standard library
- **Simple handler**: Define request handlers as Python classes
- **Basic command**: Run the server with a simple Python command
- **Minimal resources**: Requires only basic CPU and memory

## Streamlit app

Streamlit makes it easy to build interactive web dashboards. Here's a complete single-script Streamlit app:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit_single_script.py" lang=python >}}

### Key points

- **Interactive UI**: Streamlit provides widgets and visualizations out of the box
- **Single file**: All UI logic and deployment code in one script
- **Simple deployment**: Just specify the Streamlit command and port
- **Rich ecosystem**: Access to Streamlit's extensive component library

## FastAPI app

FastAPI is a modern, fast web framework for building APIs. Here's a minimal single-script FastAPI app:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi_single_script.py" lang=python >}}

### Key points

- **FastAPIAppEnvironment**: Automatically configures uvicorn and FastAPI
- **Type hints**: FastAPI uses Python type hints for automatic validation
- **Auto docs**: Interactive API documentation at `/docs` endpoint
- **Async support**: Built-in support for async/await patterns

## Running single-script apps

To run any of these examples:

1. **Save the script** to a file (e.g., `my_app.py`)
2. **Ensure you have a config file** (`config.yaml` or `config.json`) in the same directory
3. **Run the script**:

```bash
python my_app.py
```

Or using `uv`:

```bash
uv run my_app.py
```

The script will:
- Initialize Flyte from your config
- Deploy the app to your Union/Flyte instance
- Print the app URL

## When to use single-script apps

**Use single-script apps when:**
- ✅ Building prototypes or proof-of-concepts
- ✅ Creating simple services with minimal logic
- ✅ Learning how Flyte apps work
- ✅ Sharing complete, runnable examples
- ✅ Building demos or tutorials

**Consider multi-script apps when:**
- Your app grows beyond a few hundred lines
- You need to organize code into modules
- You want to reuse components across apps
- You're building production applications

See [**Multi-script apps**](./multi-script-apps) for examples of organizing apps across multiple files.

## Next steps

- [**Multi-script apps**](./multi-script-apps): Organize your app across multiple files
- [**Streamlit app**](./streamlit-app): Learn more about building Streamlit dashboards
- [**FastAPI app**](./fastapi-app): Explore FastAPI features and patterns
- [**Configuring apps**](../configure-apps/): Customize app environments and resources

