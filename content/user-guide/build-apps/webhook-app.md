---
title: Webhook app
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Webhook app

Webhooks are HTTP endpoints that trigger actions in response to external events. Flyte apps can serve as webhook endpoints that trigger task runs, workflows, or other operations.

## Basic webhook app

Here's a simple webhook that triggers Flyte tasks:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/webhook/basic_webhook.py" lang=python >}}

## Using the webhook

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

## Advanced webhook patterns

### Webhook with validation

Add input validation:

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

### Webhook with response waiting

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

### Webhook with secret management

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

## Best practices

1. **Authentication**: Always secure webhooks with authentication (API keys, tokens, etc.)
2. **Input validation**: Validate webhook inputs using Pydantic models
3. **Error handling**: Handle errors gracefully and return meaningful error messages
4. **Async operations**: Use async/await for I/O operations
5. **Health checks**: Include health check endpoints
6. **Logging**: Log webhook requests for debugging and auditing
7. **Rate limiting**: Consider implementing rate limiting for production

## Security considerations

1. **API keys**: Store API keys in Flyte secrets, not in code
2. **HTTPS**: Always use HTTPS in production
3. **Input validation**: Validate all inputs to prevent injection attacks
4. **Access control**: Implement proper access control mechanisms
5. **Audit logging**: Log all webhook invocations for security auditing

## Example: GitHub webhook

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

## Troubleshooting

**Authentication failing:**
- Verify API key matches
- Check that secrets are properly configured
- Review authentication logic

**Task not running:**
- Verify task exists at specified project/domain/name/version
- Check task inputs match expected format
- Review Flyte logs for task execution errors

**Slow responses:**
- Consider async task execution (don't wait for completion)
- Implement proper timeout handling
- Monitor webhook performance

