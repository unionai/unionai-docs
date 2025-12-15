---
title: App usage patterns
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# App usage patterns

Apps and tasks can interact in various ways: calling each other via HTTP, webhooks, WebSockets, or direct browser usage. This page describes the different patterns and when to use them.

## Patterns overview

1. **Call app from task**: A task makes HTTP requests to an app
2. **Call task from app (webhooks / APIs)**: An app triggers task execution via the Flyte SDK
3. **Call app from app**: One app makes HTTP requests to another app
4. **WebSocket-based interaction**: Real-time, bidirectional communication
5. **Browser → app**: Users access apps directly through the browser

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

## Call task from app (webhooks / APIs)

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

### Webhook usage and patterns

Webhooks are HTTP endpoints that trigger actions in response to external events. Flyte apps can serve as webhook endpoints that trigger task runs, workflows, or other operations.

#### Basic webhook app

Here's a simple webhook that triggers Flyte tasks:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/webhook/basic_webhook.py" lang=python >}}

#### Using the webhook

Once deployed, you can trigger tasks via HTTP POST:

```bash
curl -X POST "https://your-webhook-url/run-task/flytesnacks/development/my_task/v1" \
  -H "Authorization: Bearer test-api-key" \
  -H "Content-Type: application/json" \
  -d '{"input_key": "input_value"}'
```

Response:

```json
{
  "url": "https://console.union.ai/...",
  "id": "abc123",
  "status": "started"
}
```

#### Advanced webhook patterns

**Webhook with validation**

Use Pydantic for input validation:

```python
from pydantic import BaseModel

class TaskInput(BaseModel):
    data: dict
    priority: int = 0

@app.post("/run-task/{project}/{domain}/{name}/{version}")
async def run_task(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: TaskInput,  # Validated input
    credentials: HTTPAuthorizationCredentials = Security(verify_token),
):
    task = await remote.TaskDetails.fetch(
        project=project,
        domain=domain,
        name=name,
        version=version,
    )
    
    run = await flyte.run.aio(task, **inputs.dict())
    
    return {
        "run_id": run.id,
        "url": run.url,
    }
```

**Webhook with response waiting**

Wait for task completion:

```python
@app.post("/run-task-and-wait/{project}/{domain}/{name}/{version}")
async def run_task_and_wait(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: dict,
    credentials: HTTPAuthorizationCredentials = Security(verify_token),
):
    task = await remote.TaskDetails.fetch(
        project=project,
        domain=domain,
        name=name,
        version=version,
    )
    
    run = await flyte.run.aio(task, **inputs)
    run.wait()  # Wait for completion
    
    return {
        "run_id": run.id,
        "url": run.url,
        "status": run.status,
        "outputs": run.outputs(),
    }
```

**Webhook with secret management**

Use Flyte secrets for API keys:

```python
env = FastAPIAppEnvironment(
    name="webhook-runner",
    app=app,
    secrets=flyte.Secret(key="webhook-api-key", as_env_var="WEBHOOK_API_KEY"),
    # ...
)
```

Then access in your app:

```python
WEBHOOK_API_KEY = os.getenv("WEBHOOK_API_KEY")
```

#### Webhook security and best practices

- **Authentication**: Always secure webhooks with authentication (API keys, tokens, etc.).
- **Input validation**: Validate webhook inputs using Pydantic models.
- **Error handling**: Handle errors gracefully and return meaningful error messages.
- **Async operations**: Use async/await for I/O operations.
- **Health checks**: Include health check endpoints.
- **Logging**: Log webhook requests for debugging and auditing.
- **Rate limiting**: Consider implementing rate limiting for production.

Security considerations:

- Store API keys in Flyte secrets, not in code.
- Always use HTTPS in production.
- Validate all inputs to prevent injection attacks.
- Implement proper access control mechanisms.
- Log all webhook invocations for security auditing.

#### Example: GitHub webhook

Here's an example webhook that triggers tasks based on GitHub events:

```python
from fastapi import FastAPI, Request, Header
import hmac
import hashlib

app = FastAPI(title="GitHub Webhook Handler")

@app.post("/github-webhook")
async def github_webhook(
    request: Request,
    x_hub_signature_256: str = Header(None),
):
    """Handle GitHub webhook events."""
    body = await request.body()
    
    # Verify signature
    secret = os.getenv("GITHUB_WEBHOOK_SECRET")
    signature = hmac.new(
        secret.encode(),
        body,
        hashlib.sha256
    ).hexdigest()
    
    expected_signature = f"sha256={signature}"
    if not hmac.compare_digest(x_hub_signature_256, expected_signature):
        raise HTTPException(status_code=403, detail="Invalid signature")
    
    # Process webhook
    event = await request.json()
    event_type = request.headers.get("X-GitHub-Event")
    
    if event_type == "push":
        # Trigger deployment task
        task = await remote.TaskDetails.fetch(...)
        run = await flyte.run.aio(task, commit=event["after"])
        return {"run_id": run.id, "url": run.url}
    
    return {"status": "ignored"}
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

## WebSocket-based patterns

WebSockets enable bidirectional, real-time communication between clients and servers. Flyte apps can serve WebSocket endpoints for real-time applications like chat, live updates, or streaming data.

### Basic WebSocket app

Here's a simple FastAPI app with WebSocket support:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/websocket/basic_websocket.py" lang=python >}}

### WebSocket patterns

**Echo server**

```python
@app.websocket("/echo")
async def echo(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        pass
```

**Broadcast server**

```python
@app.websocket("/broadcast")
async def broadcast(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

**Real-time data streaming**

```python
@app.websocket("/stream")
async def stream_data(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Generate or fetch data
            data = {"timestamp": datetime.now().isoformat(), "value": random.random()}
            await websocket.send_json(data)
            await asyncio.sleep(1)  # Send update every second
    except WebSocketDisconnect:
        pass
```

**Chat application**

```python
class ChatRoom:
    def __init__(self, name: str):
        self.name = name
        self.connections: list[WebSocket] = []
    
    async def join(self, websocket: WebSocket):
        self.connections.append(websocket)
    
    async def leave(self, websocket: WebSocket):
        self.connections.remove(websocket)
    
    async def broadcast(self, message: str, sender: WebSocket):
        for connection in self.connections:
            if connection != sender:
                await connection.send_text(message)

rooms: dict[str, ChatRoom] = {}

@app.websocket("/chat/{room_name}")
async def chat(websocket: WebSocket, room_name: str):
    await websocket.accept()
    
    if room_name not in rooms:
        rooms[room_name] = ChatRoom(room_name)
    
    room = rooms[room_name]
    await room.join(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            await room.broadcast(data, websocket)
    except WebSocketDisconnect:
        await room.leave(websocket)
```

### Using WebSockets with Flyte tasks

You can trigger Flyte tasks from WebSocket messages:

```python
@app.websocket("/task-runner")
async def task_runner(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            # Receive task request
            message = await websocket.receive_text()
            request = json.loads(message)
            
            # Trigger Flyte task
            task = await remote.TaskDetails.fetch(
                project=request["project"],
                domain=request["domain"],
                name=request["task"],
                version=request["version"],
            )
            
            run = await flyte.run.aio(task, **request["inputs"])
            
            # Send run info back
            await websocket.send_json({
                "run_id": run.id,
                "url": run.url,
                "status": "started",
            })
            
            # Optionally stream updates
            async for update in run.stream():
                await websocket.send_json({
                    "status": update.status,
                    "message": update.message,
                })
    
    except WebSocketDisconnect:
        pass
```

### WebSocket client example

Connect from Python:

```python
import asyncio
import websockets
import json

async def client():
    uri = "ws://your-app-url/ws"
    async with websockets.connect(uri) as websocket:
        # Send message
        await websocket.send("Hello, Server!")
        
        # Receive message
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(client())
```

## Browser-based apps

For browser-based apps (like Streamlit), users interact directly through the web interface. The app URL is accessible in a browser, and users interact with the UI directly - no API calls needed from other services.

To access a browser-based app:
1. Deploy the app
2. Navigate to the app URL in a browser
3. Interact with the UI directly

## Best practices

1. **Use `depends_on`**: Always specify dependencies to ensure proper deployment order.
2. **Handle errors**: Implement proper error handling for HTTP requests.
3. **Use async clients**: Use async HTTP clients (`httpx.AsyncClient`) in async contexts.
4. **Initialize Flyte**: For apps calling tasks, initialize Flyte in the app's startup.
5. **Endpoint access**: Use `app_env.endpoint` or `AppEndpoint` input for accessing app URLs.
6. **Authentication**: Consider authentication when apps call each other (set `requires_auth=True` if needed).
7. **Webhook security**: Secure webhooks with auth, validation, and HTTPS.
8. **WebSocket robustness**: Implement connection management, heartbeats, and rate limiting.

## Summary

| Pattern | Use Case | Implementation |
|---------|----------|----------------|
| Task → App | Batch processing using services | HTTP requests from task |
| App → Task | Webhooks, APIs triggering workflows | Flyte SDK in app |
| App → App | Microservices, proxies | HTTP requests between apps |
| Browser → App | User-facing dashboards | Direct browser access |

Choose the pattern that best fits your architecture and requirements.

