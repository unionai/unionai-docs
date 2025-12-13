---
title: App calling patterns
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# App calling patterns

Apps and tasks can call each other in various patterns. This page describes the different patterns and when to use them.

## Patterns overview

1. **Call app from task**: A task makes HTTP requests to an app
2. **Call task from app**: An app triggers task execution via the Flyte SDK
3. **Call app from app**: One app makes HTTP requests to another app

## Call app from task

Tasks can call apps by making HTTP requests to the app's endpoint. This is useful when:
- You need to use a long-running service during task execution
- You want to call a model serving endpoint from a batch processing task
- You need to interact with an API from a workflow

### Example: Task calling an app

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/task_calling_app.py" lang=python >}}

Key points:
- The task environment uses `depends_on=[app_env]` to ensure the app is deployed first
- Access the app endpoint via `app_env.endpoint`
- Use standard HTTP client libraries (like `httpx`) to make requests

### Using AppEndpoint input

For more dynamic scenarios, you can pass the app endpoint as an input:

```python
@task_env.task
async def call_app_task(app_url: str, data: dict) -> dict:
    """Task that calls an app with a dynamic endpoint."""
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{app_url}/process", json=data)
        response.raise_for_status()
        return response.json()
```

## Call task from app

Apps can trigger task execution using the Flyte SDK. This is useful for:
- Webhooks that trigger workflows
- APIs that need to run batch jobs
- Services that need to execute tasks asynchronously

### Example: Webhook app calling a task

```python
from fastapi import FastAPI
import flyte
from flyte.app.extras import FastAPIAppEnvironment
import flyte.remote as remote

app = FastAPI(title="Webhook Runner")

env = FastAPIAppEnvironment(
    name="webhook-runner",
    app=app,
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
        "fastapi", "uvicorn"
    ),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
)

# Define a task environment for the task to be called
task_env = flyte.TaskEnvironment(
    name="processing-env",
    image=flyte.Image.from_debian_base(python_version=(3, 12)),
    resources=flyte.Resources(cpu=2, memory="4Gi"),
)

@task_env.task
async def process_data(data: dict) -> dict:
    """Task that processes data."""
    # ... processing logic ...
    return {"result": "processed"}

@app.post("/run-task")
async def run_task_webhook(data: dict):
    """Webhook endpoint that triggers a task."""
    # Initialize Flyte in the app
    await flyte.init_in_cluster.aio()
    
    # Fetch the task
    task = await remote.TaskDetails.fetch(
        project="flytesnacks",
        domain="development",
        name="process_data",
        version="v1",
    )
    
    # Run the task
    run = await flyte.run.aio(task, **data)
    
    return {
        "run_id": run.id,
        "url": run.url,
        "status": "started",
    }
```

### Using lifecycle initialization

For apps that need to call tasks, initialize Flyte in the app's startup:

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize Flyte before accepting requests."""
    await flyte.init_in_cluster.aio()
    yield
    # Cleanup if needed

app = FastAPI(
    title="Task Runner API",
    lifespan=lifespan,
)

@app.post("/execute")
async def execute_task(task_input: dict):
    """Execute a task from the app."""
    task = await remote.TaskDetails.fetch(...)
    run = await flyte.run.aio(task, **task_input)
    return {"run_id": run.id, "url": run.url}
```

## Call app from app

Apps can call other apps by making HTTP requests. This is useful for:
- Microservice architectures
- Proxy/gateway patterns
- A/B testing setups
- Service composition

### Example: App calling another app

```python
import httpx
from fastapi import FastAPI
import flyte
from flyte.app.extras import FastAPIAppEnvironment

# Backend app
app1 = FastAPI(title="Backend API")
env1 = FastAPIAppEnvironment(
    name="backend-api",
    app=app1,
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
        "fastapi", "uvicorn", "httpx"
    ),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
)

@app1.get("/greeting/{name}")
async def greeting(name: str) -> str:
    return f"Hello, {name}!"

# Frontend app that calls the backend
app2 = FastAPI(title="Frontend API")
env2 = FastAPIAppEnvironment(
    name="frontend-api",
    app=app2,
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
        "fastapi", "uvicorn", "httpx"
    ),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
    depends_on=[env1],  # Ensure backend is deployed first
)

@app2.get("/greeting/{name}")
async def greeting_proxy(name: str):
    """Proxy that calls the backend app."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{env1.endpoint}/greeting/{name}")
        response.raise_for_status()
        return response.json()
```

Key points:
- Use `depends_on=[env1]` to ensure dependencies are deployed first
- Access the app endpoint via `env1.endpoint`
- Use HTTP clients (like `httpx`) to make requests between apps

### Using AppEndpoint input

You can pass app endpoints as inputs for more flexibility:

```python
env2 = FastAPIAppEnvironment(
    name="frontend-api",
    app=app2,
    inputs=[
        flyte.app.Input(
            name="backend_url",
            value=flyte.app.AppEndpoint(app_name="backend-api"),
        ),
    ],
    # ...
)

@app2.get("/greeting/{name}")
async def greeting_proxy(name: str):
    backend_url = os.getenv("BACKEND_URL")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{backend_url}/greeting/{name}")
        return response.json()
```

## Browser-based apps

For browser-based apps (like Streamlit), users interact directly through the web interface. The app URL is accessible in a browser, and users interact with the UI directly - no API calls needed from other services.

To access a browser-based app:
1. Deploy the app
2. Navigate to the app URL in a browser
3. Interact with the UI directly

## Best practices

1. **Use `depends_on`**: Always specify dependencies to ensure proper deployment order
2. **Handle errors**: Implement proper error handling for HTTP requests
3. **Use async clients**: Use async HTTP clients (`httpx.AsyncClient`) in async contexts
4. **Initialize Flyte**: For apps calling tasks, initialize Flyte in the app's startup
5. **Endpoint access**: Use `app_env.endpoint` or `AppEndpoint` input for accessing app URLs
6. **Authentication**: Consider authentication when apps call each other (set `requires_auth=True` if needed)

## Summary

| Pattern | Use Case | Implementation |
|---------|----------|----------------|
| Task → App | Batch processing using services | HTTP requests from task |
| App → Task | Webhooks, APIs triggering workflows | Flyte SDK in app |
| App → App | Microservices, proxies | HTTP requests between apps |
| Browser → App | User-facing dashboards | Direct browser access |

Choose the pattern that best fits your architecture and requirements.

