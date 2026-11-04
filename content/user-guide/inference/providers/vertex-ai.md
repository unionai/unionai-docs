---
title: Google Vertex AI
description: "Call Google Vertex AI from Flyte tasks and apps with the OpenAI SDK: store a service account key as a secret and request an access token in the task."
icon: cloud
weight: 5
variants: +flyte +union
keywords:
  - Google Vertex AI API
  - Google Vertex AI Flyte
  - Google Vertex AI Union.ai
  - Vertex AI service account
  - Vertex AI Python task
  - OpenAI-compatible API
---

# Google Vertex AI

[Google Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/openai) has an OpenAI-compatible endpoint, but it takes a short-lived OAuth access token rather than a static API key. The token expires after 1 hour by default, so it doesn't fit a static secret.

Instead, store a service account key as a secret, and have the task request a token when it starts.

| Setting | Value |
|---|---|
| Base URL | `https://aiplatform.googleapis.com/v1/projects/<project>/locations/<location>/endpoints/openapi` |
| Credentials | Google Cloud service account key |
| Environment variable | None |

## Store your service account key

Create a [file secret](../../tasks/task-configuration/secrets#using-a-file-secret) from the key file:

```bash
flyte create secret vertex-service-account --from-file <path-to-key.json> --project <your-project> --domain development
```

## Call Vertex AI from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_vertex_ai.py" fragment="task" lang="python" >}}

Replace `<project>`, `<location>`, and `<model-id>` with your own values.

## Call Vertex AI from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the Inference Gateway

To add budgets, fallbacks, and guardrails, [add Google Vertex AI to the Inference Gateway](../inference-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../inference-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
