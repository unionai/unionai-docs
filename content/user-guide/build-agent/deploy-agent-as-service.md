---
title: Deploy an agent as a service
weight: 10
variants: +flyte +serverless +union
mermaid: true
---

# Deploy an agent as a service

Once you've built an agent — with [pure Python](./python-agents), the [`Agent` harness](./flyte-agents), or a [third-party framework](../agent-framework-integrations/_index) — *how* you run it is an independent choice. The same agent object can be deployed in several ways:

| Pattern | When to use it | What invokes the agent |
|---------|----------------|------------------------|
| **As a task** | On-demand runs from the CLI, a notebook, or another service | `flyte.run(...)` |
| **As a scheduled task** | Recurring autonomous wakeups (triage, monitoring, reports) | A `flyte.Trigger` (cron or fixed-rate) |
| **Behind a webhook** | React to external events (GitHub, paging tools, CI) | An HTTP `POST` to an `AppEnvironment` |

All three wrap the agent loop in a regular Flyte task, so every run is durable, retryable, and observable in the {{< key product_name >}} dashboard. The examples below use the `Agent` harness, but the pattern is identical for any agent — just call your agent's entry point inside the task.

## As a task

The simplest deployment: put the agent loop in an `@env.task` and invoke it on demand. This works for any agent.

```python
import flyte
from flyte.ai.agents import Agent

env = flyte.TaskEnvironment(
    name="concierge-agent",
    image=flyte.Image.from_debian_base().with_pip_packages("litellm"),
    secrets=[flyte.Secret(key="internal-anthropic-api-key", as_env_var="ANTHROPIC_API_KEY")],
)

agent = Agent(
    name="customer-concierge",
    instructions="You are a customer-service concierge.",
    tools=[...],
)


@env.task(report=True)
async def concierge(request: str) -> str:
    """Run the agent for a single request."""
    result = await agent.run.aio(request)
    return result.summary or result.error
```

Run it on demand:

```bash
flyte run agent.py concierge --request "Refund order #12345 to the customer."
```

Or from Python with `flyte.run(concierge, request="...")`. To register a stable, deployed version of the task, use `flyte deploy agent.py env`.

## As a scheduled task (via `Trigger`)

To run an agent autonomously on a schedule, attach a `flyte.Trigger` to the task. The "wakeup" is a regular Flyte task — the agent loop runs inside it, so every tool call is durable, observable, and retryable. Pair this with [agent memory](./agent-memory) so the agent resumes prior context on each wakeup.

{{< code file="/unionai-examples/v2/user-guide/build-agent/deploy/scheduled_triage_agent.py" fragment="scheduled" lang="python" >}}

The agent's tools (`list_open_issues`, `classify_issue`, `post_digest`) are durable `@env.task`s; see the [full example](https://github.com/unionai/unionai-examples/tree/main/v2/user-guide/build-agent/deploy/scheduled_triage_agent.py) for their definitions.

Deploying the task registers the trigger; from then on {{< key product_name >}} wakes the agent on schedule. Use `flyte.Cron(...)` for calendar schedules or `flyte.FixedRate(...)` for fixed intervals. The `flyte.TriggerTime` input is filled with the scheduled fire time. See [Triggers](../task-configuration/triggers) for the full schedule reference.

## Behind a webhook (`AppEnvironment`)

To kick off an agent run in response to an external event, deploy a small FastAPI app via an `AppEnvironment` that exposes an HTTP endpoint. The endpoint launches the agent task with `flyte.run.aio(...)`, so the long-running agent loop executes durably in the background while the webhook returns immediately with a run URL.

{{< code file="/unionai-examples/v2/user-guide/build-agent/deploy/webhook_agent.py" fragment="webhook" lang="python" >}}

The agent and its tools (`fetch_pr`, `post_comment`) are defined in the [full example](https://github.com/unionai/unionai-examples/tree/main/v2/user-guide/build-agent/deploy/webhook_agent.py).

Once deployed, point your external system at the `/trigger` URL:

```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"repository": "flyteorg/flyte", "pull_request": {"number": 123}, "action": "opened"}' \
    https://<subdomain>.apps.<endpoint>/trigger
```

> [!NOTE]
> When the webhook app submits runs on behalf of incoming requests, it needs valid {{< key product_name >}} credentials. Use passthrough auth (a `FastAPIPassthroughAuthMiddleware` and `flyte.init_passthrough`) so the run is submitted with the caller's identity. See [FastAPI apps](../native-app-integrations/fastapi-app).

## Chat and other app patterns

- **Chat UI:** To let users converse with the agent in a browser, serve it behind a chat interface. See [Add a chat UI](./agent-chat-ui).
- **FastAPI endpoint:** For API-first agents, expose your agent behind a REST endpoint with `FastAPIAppEnvironment` so other services or agents can call it programmatically.
- **Model serving:** [Serve open-weight LLMs](../native-app-integrations/vllm-app) on GPUs behind an OpenAI-compatible API with `VLLMAppEnvironment` or `SGLangAppEnvironment`.

> [!TIP]
> See [Build Apps](../build-apps/_index) and [Configure Apps](../configure-apps/_index) for more details on hosting services on {{< key product_name >}}.
