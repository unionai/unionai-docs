---
title: App usage patterns
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# App usage patterns

Apps and tasks can interact in various ways: calling each other via HTTP, webhooks, WebSockets, or direct browser usage. This page describes the different patterns and when to use them.

## Patterns overview

1. [Call app from task](#call-app-from-task): A task makes HTTP requests to an app
2. [Call task from app (webhooks / APIs)](#call-task-from-app-webhooks--apis): An app triggers task execution via the Flyte SDK
3. [Call app from app](#call-app-from-app): One app makes HTTP requests to another app
4. [WebSocket-based interaction](#websocket-based-patterns): Real-time, bidirectional communication
5. **Browser-based access**: Users access apps directly through the browser

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

## Call task from app (webhooks / APIs)

Apps can trigger task execution using the Flyte SDK. This is useful for:

- Webhooks that trigger workflows
- APIs that need to run batch jobs
- Services that need to execute tasks asynchronously

Webhooks are HTTP endpoints that trigger actions in response to external events. Flyte apps can serve as webhook endpoints that trigger task runs, workflows, or other operations.

### Example: Basic webhook app

Here's a simple webhook that triggers Flyte tasks:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/webhook/basic_webhook.py" lang=python >}}

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

### Advanced webhook patterns

**Webhook with validation**

Use Pydantic for input validation:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/webhook_validation.py" fragment=validation-model lang=python >}}

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/webhook_validation.py" fragment=validated-webhook lang=python >}}

**Webhook with response waiting**

Wait for task completion:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/webhook_wait.py" fragment=wait-webhook lang=python >}}

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

### Webhook security and best practices

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

### Example: GitHub webhook

Here's an example webhook that triggers tasks based on GitHub events:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/github_webhook.py" fragment=github-webhook lang=python >}}

## Call app from app

Apps can call other apps by making HTTP requests. This is useful for:
- Microservice architectures
- Proxy/gateway patterns
- A/B testing setups
- Service composition

### Example: App calling another app

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/app_calling_app.py" lang=python >}}

Key points:
- Use `depends_on=[env1]` to ensure dependencies are deployed first
- Access the app endpoint via `env1.endpoint`
- Use HTTP clients (like `httpx`) to make requests between apps

### Using AppEndpoint parameter

You can pass app endpoints as parameters for more flexibility:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/app_calling_app_endpoint.py" fragment=using-app-endpoint lang=python >}}

## WebSocket-based patterns

WebSockets enable bidirectional, real-time communication between clients and servers. Flyte apps can serve WebSocket endpoints for real-time applications like chat, live updates, or streaming data.

### Example: Basic WebSocket app

Here's a simple FastAPI app with WebSocket support:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/websocket/basic_websocket.py" lang=python >}}

### WebSocket patterns

**Echo server**

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/websocket/websocket_patterns.py" fragment=echo-server lang=python >}}

**Broadcast server**

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/websocket/websocket_patterns.py" fragment=broadcast-server lang=python >}}

**Real-time data streaming**

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/websocket/websocket_patterns.py" fragment=streaming-server lang=python >}}

**Chat application**

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/websocket/websocket_patterns.py" fragment=chat-room lang=python >}}

### Using WebSockets with Flyte tasks

You can trigger Flyte tasks from WebSocket messages:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/websocket/task_runner_websocket.py" fragment=task-runner-websocket lang=python >}}

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
5. **Endpoint access**: Use `app_env.endpoint` or `AppEndpoint` parameter for accessing app URLs.
6. **Authentication**: Consider authentication when apps call each other (set `requires_auth=True` if needed).
7. **Webhook security**: Secure webhooks with auth, validation, and HTTPS.
8. **WebSocket robustness**: Implement connection management, heartbeats, and rate limiting.

## Summary

| Pattern | Use Case | Implementation |
|---------|----------|----------------|
| Task → App | Batch processing using inference services | HTTP requests from task |
| App → Task | Webhooks, APIs triggering workflows | Flyte SDK in app |
| App → App | Microservices, proxies, agent routers, LLM routers | HTTP requests between apps |
| Browser → App | User-facing dashboards | Direct browser access |

Choose the pattern that best fits your architecture and requirements.

