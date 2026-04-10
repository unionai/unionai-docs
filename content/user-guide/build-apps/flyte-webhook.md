---
title: Flyte webhook
weight: 13
variants: +flyte +union
---

# Flyte webhook

`FlyteWebhookAppEnvironment` is a pre-built `FastAPIAppEnvironment` that exposes
HTTP endpoints for common {{< key product_name >}} operations. Instead of writing
your own FastAPI routes to interact with the control plane, you get a
ready-to-deploy webhook service with a single constructor call.

## Available endpoints

The webhook provides endpoints for the following operations:

| Group | Endpoints | Description |
|---|---|---|
| **core** | `GET /health`, `GET /me` | Health check and authenticated user info |
| **task** | `POST /run-task/{domain}/{project}/{name}`, `GET /task/{domain}/{project}/{name}` | Run tasks and retrieve task metadata |
| **run** | `GET /run/{name}`, `GET /run/{name}/io`, `POST /run/{name}/abort` | Get run status, inputs/outputs, and abort runs |
| **app** | `GET /app/{name}`, `POST /app/{name}/activate`, `POST /app/{name}/deactivate`, `POST /app/{name}/call` | Manage apps and call other app endpoints |
| **trigger** | `POST /trigger/{task_name}/{trigger_name}/activate`, `POST /trigger/{task_name}/{trigger_name}/deactivate` | Activate and deactivate triggers |
| **build** | `POST /build-image` | Build container images |
| **prefetch** | `POST /prefetch/hf-model`, `GET /prefetch/hf-model/{run_name}`, `GET /prefetch/hf-model/{run_name}/io`, `POST /prefetch/hf-model/{run_name}/abort` | Prefetch HuggingFace models |

All endpoints except `/health`, `/docs`, and `/openapi.json` use passthrough
authentication, forwarding the caller's credentials to the
{{< key product_name >}} control plane.

## Basic usage

Create a webhook with all endpoints enabled:

{{< code file="/unionai-examples/v2/user-guide/build-apps/flyte_webhook_examples.py" fragment=basic-webhook lang=python >}}

Deploy and activate it:

{{< code file="/unionai-examples/v2/user-guide/build-apps/flyte_webhook_examples.py" fragment=deploy-webhook lang=python >}}

Once running, the webhook exposes OpenAPI docs at `{endpoint}/docs` (Swagger UI)
and `{endpoint}/redoc`.

## Filtering endpoints

You can restrict which endpoints the webhook exposes using either **endpoint
groups** or **individual endpoints**.

### Endpoint groups

Enable groups of related endpoints with `endpoint_groups`:

{{< code file="/unionai-examples/v2/user-guide/build-apps/flyte_webhook_examples.py" fragment=endpoint-groups lang=python >}}

Available groups: `all`, `core`, `task`, `run`, `app`, `trigger`, `build`, `prefetch`.

### Individual endpoints

For finer control, specify exact endpoints with `endpoints`:

{{< code file="/unionai-examples/v2/user-guide/build-apps/flyte_webhook_examples.py" fragment=individual-endpoints lang=python >}}

> [!NOTE]
> You cannot specify both `endpoint_groups` and `endpoints` at the same time. Use
> one or the other.

## Allow-listing

Restrict which resources the webhook can access using allow-lists.

### Task allow-list

Limit which tasks can be run or queried through the webhook:

{{< code file="/unionai-examples/v2/user-guide/build-apps/flyte_webhook_examples.py" fragment=task-allowlist lang=python >}}

Task identifiers support three formats:
- `domain/project/name` — exact match
- `project/name` — matches any domain
- `name` — matches any domain and project

### App allow-list

Limit which apps can be managed through the webhook:

{{< code file="/unionai-examples/v2/user-guide/build-apps/flyte_webhook_examples.py" fragment=app-allowlist lang=python >}}

### Trigger allow-list

Limit which triggers can be activated or deactivated:

{{< code file="/unionai-examples/v2/user-guide/build-apps/flyte_webhook_examples.py" fragment=trigger-allowlist lang=python >}}

Trigger identifiers support two formats:
- `task_name/trigger_name` — exact match
- `trigger_name` — matches any task

## Calling the webhook

Authenticate requests with a {{< key product_name >}} API key passed as a Bearer
token:

{{< code file="/unionai-examples/v2/user-guide/build-apps/flyte_webhook_examples.py" fragment=call-webhook lang=python >}}

## Authentication

`FlyteWebhookAppEnvironment` uses `FastAPIPassthroughAuthMiddleware`, which
extracts the caller's auth token from the `Authorization` header and sets up
a {{< key product_name >}} context so that every control-plane call (e.g.
`remote.Task.get`, `flyte.run`) runs with the caller's identity.

The `/health`, `/docs`, `/openapi.json`, and `/redoc` endpoints are excluded
from authentication.

## Self-reference protection

App endpoints (`get_app`, `activate_app`, `deactivate_app`, `call_app`) prevent
the webhook from targeting itself. Attempting to activate, deactivate, or call
the webhook's own name returns a `400 Bad Request` error.
