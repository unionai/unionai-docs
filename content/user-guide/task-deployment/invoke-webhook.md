---
title: Running Tasks via Webhooks
weight: 5
variants: -flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Running Tasks via Webhooks

On Union, you can deploy apps (see [Apps documentation](../../configure-apps/)) that can run any deployed Flyte tasks. These apps can be REST API services, like FastAPI, that accept HTTP requests and run tasks on behalf of the caller.

A key feature of this approach is **passthrough authentication** - the app can carry forward the identity of the caller and use their credentials to run the task. This ensures proper authorization and audit trails, as tasks are executed with the permissions of the actual user making the request.

## How passthrough authentication works

When you deploy a webhook service on Union:

1. The caller sends an HTTP request with their authentication token (typically in the `Authorization` header)
2. Your webhook app extracts the authentication headers from the request
3. The app forwards these headers to the Flyte control plane when running the task
4. The task executes with the caller's identity and permissions

This is different from using a service API key, where all tasks would run with the same service account permissions regardless of who made the request.

## Setting up passthrough authentication

### Initialize with `flyte.init_passthrough()`

To enable passthrough authentication, initialize your app using `flyte.init_passthrough()`:

```python
import flyte

# Initialize Flyte with passthrough authentication
await flyte.init_passthrough.aio(
    endpoint="dns:///your-endpoint.hosted.unionai.cloud",
    project="my-project",      # Optional: default project
    domain="development",       # Optional: default domain
)
```

The `init_passthrough()` function configures the Flyte SDK to accept authentication metadata from the request context rather than using a static token or interactive authentication flow.

**Parameters:**

- `endpoint`: **Required**. The Flyte control plane endpoint URL
- `project`: Optional. Default project to use if not specified per request
- `domain`: Optional. Default domain to use if not specified per request
- `org`: Optional. Organization name
- `insecure`: Optional. Whether to use an insecure connection (default: `False`)

> [!IMPORTANT]
> The `endpoint` parameter is required when using passthrough authentication. Unlike other authentication modes, passthrough cannot infer the endpoint from environment variables or config files since it needs explicit initialization.

### Passing authentication metadata

Once initialized, you need to provide the caller's authentication headers when making requests to the Flyte control plane. There are two approaches:

#### Option 1: Using FastAPI middleware (recommended if using fastapi)

For FastAPI applications, Flyte provides a convenient middleware that automatically extracts authentication headers from incoming requests and sets them in the Flyte context:

```python
from fastapi import FastAPI
from flyte.app.extras import FastAPIPassthroughAuthMiddleware

app = FastAPI()

# Add the middleware - automatically handles auth for all endpoints
app.add_middleware(
    FastAPIPassthroughAuthMiddleware,
    excluded_paths={"/health"}  # Optional: skip auth for specific paths
)

@app.post("/run-task")
async def run_task():
    # No need to manually extract headers!
    # The middleware automatically sets auth context
    task = remote.Task.get(project="my-project", domain="development", name="my_task")
    run = await flyte.run.aio(task, x=42)
    return {"run_url": run.url}
```

**Middleware features:**

- **Automatic header extraction**: Extracts `Authorization` and `Cookie` headers by default
- **Path exclusions**: Skip auth for specific endpoints like `/health` or `/metrics`
- **Custom extractors**: Add custom header extraction logic
- **Thread-safe**: Properly isolates authentication per request using context variables

**Middleware parameters:**

- `excluded_paths`: Set of URL paths that bypass authentication extraction
- `header_extractors`: Custom list of header extractor functions (optional)

**Custom header extractors:**

```python
from flyte.app.extras import FastAPIPassthroughAuthMiddleware

app.add_middleware(
    FastAPIPassthroughAuthMiddleware,
    header_extractors=[
        FastAPIPassthroughAuthMiddleware.extract_authorization_header,
        FastAPIPassthroughAuthMiddleware.extract_custom_header("x-api-key"),
    ],
    excluded_paths={"/health", "/metrics"},
)
```

#### Option 2: Using the `auth_metadata()` context manager (any script, web serving framework)

The `flyte.remote.auth_metadata()` context manager allows you to explicitly set authentication headers for a block of code:

```python
import flyte.remote as remote

@app.post("/run-task")
async def run_task(request: Request):
    # Extract authentication from the request
    auth_header = request.headers.get("authorization")

    # Use auth_metadata to forward the caller's credentials
    with remote.auth_metadata(("authorization", auth_header)):
        # Get and run the task with the caller's identity
        task = remote.Task.get(project="my-project", domain="development", name="my_task")
        run = await flyte.run.aio(task, x=42)
        return {"run_url": run.url}
```

The `auth_metadata()` context manager accepts one or more tuples of `(header_name, header_value)`:

```python
with remote.auth_metadata(
    ("authorization", auth_header),
    ("cookie", cookie_header),
):
    # All Flyte API calls within this block use these headers
    ...
```



## Complete example

Here's a complete FastAPI webhook service that runs Flyte tasks with passthrough authentication:

```python
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from starlette import status

import flyte
import flyte.remote as remote
from flyte.app.extras import FastAPIAppEnvironment, FastAPIPassthroughAuthMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize Flyte with passthrough auth on startup."""
    endpoint = os.getenv("FLYTE_ENDPOINT")
    if not endpoint:
        raise RuntimeError("FLYTE_ENDPOINT environment variable not set")

    await flyte.init_passthrough.aio(
        endpoint=endpoint,
        project=os.getenv("FLYTE_INTERNAL_EXECUTION_PROJECT"),
        domain=os.getenv("FLYTE_INTERNAL_EXECUTION_DOMAIN"),
    )
    yield


app = FastAPI(
    title="Flyte Webhook Runner",
    description="A webhook service that runs Flyte tasks",
    lifespan=lifespan,
)

# Add passthrough auth middleware
app.add_middleware(FastAPIPassthroughAuthMiddleware, excluded_paths={"/health"})


@app.get("/health")
async def health_check():
    """Health check endpoint (no auth required)."""
    return {"status": "healthy"}


@app.get("/me")
async def get_current_user():
    """Get information about the authenticated user."""
    user = await remote.User.get.aio()
    return {
        "subject": user.subject(),
        "name": user.name(),
    }


@app.post("/run-task/{project}/{domain}/{name}")
async def run_task(
    project: str,
    domain: str,
    name: str,
    inputs: dict,
    version: str | None = None,
):
    """
    Run a Flyte task with the caller's credentials.

    Args:
        project: Flyte project name
        domain: Flyte domain (e.g., development, staging, production)
        name: Task name
        inputs: Dictionary of input parameters for the task
        version: Task version (optional, defaults to "latest")

    Returns:
        Dictionary containing the run information
    """
    try:
        # Get the task
        task = remote.Task.get(
            project=project,
            domain=domain,
            name=name,
            version=version,
            auto_version="latest" if version is None else None,
        )

        # Run the task with the caller's identity
        run = await flyte.run.aio(task, **inputs)

        return {"url": run.url, "name": run.name}

    except flyte.errors.RemoteTaskError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )


# Configure the app deployment
image = flyte.Image.from_debian_base().with_pip_packages("fastapi", "uvicorn")

app_env = FastAPIAppEnvironment(
    name="webhook-runner",
    app=app,
    description="A webhook service that runs Flyte tasks with passthrough auth",
    image=image,
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=True,  # Platform handles auth at gateway
    env_vars={
        "FLYTE_ENDPOINT": "your-endpoint.hosted.unionai.cloud",
    },
)
```

For a complete working example, see [`examples/apps/run_webhook.py`](https://github.com/unionai/flyte-sdk/blob/main/examples/apps/run_webhook.py) in the Flyte SDK repository.

## Calling the webhook

Once deployed, you can call your webhook using standard HTTP tools:

```bash
# Get API key for authentication
flyte get api-key my-webhook-key

# Call the webhook to run a task
curl -X POST \
  -H "Authorization: Bearer <your-api-key>" \
  -H "Content-Type: application/json" \
  -d '{"x": 42, "y": "hello"}' \
  https://your-app.apps.unionai.cloud/run-task/my-project/development/my_task
```

The task will execute with the permissions associated with the API key used in the request.

## Best practices

1. **Always set an endpoint**: The `endpoint` parameter is required for `init_passthrough()`

2. **Use middleware for FastAPI**: The `FastAPIPassthroughAuthMiddleware` eliminates boilerplate and ensures consistent auth handling

3. **Exclude public endpoints**: Use `excluded_paths` to skip auth for health checks and public endpoints

4. **Set default project/domain**: If most requests target the same project/domain, set them during initialization to simplify your endpoint handlers

5. **Handle errors gracefully**: Catch `RemoteTaskError` and other exceptions to return appropriate HTTP status codes

6. **Validate inputs**: Always validate task inputs before passing them to `flyte.run()`

7. **Use the caller's identity**: Passthrough auth ensures proper authorization and audit trails - avoid using static service credentials when possible

## Troubleshooting

### "FLYTE_ENDPOINT environment variable not set"

Ensure you set the `FLYTE_ENDPOINT` environment variable in your app configuration, or pass it explicitly to `init_passthrough()`.

### "Authentication credentials required"

The middleware returns this error when no authentication headers are found. Ensure:
- The client includes an `Authorization` header with a valid token
- The endpoint is not in the `excluded_paths` set
- Header extractors are configured correctly

### "Task not found"

Verify:
- The task exists in the specified project/domain
- The task name is correct (use the fully qualified name: `package.module.task_name`)
- The caller has permission to view the task

### Tasks run with wrong permissions

If tasks aren't respecting the caller's permissions:
- Verify `init_passthrough()` is called with `auth_type="Passthrough"`
- Ensure auth headers are being extracted and forwarded correctly
- Check that the middleware is added before route handlers