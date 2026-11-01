---
title: Use the Grok API with Flyte
linkTitle: Grok API
description: "Call the Grok API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 10
variants: +flyte +union
keywords:
  - Grok API
  - Grok API Flyte
  - Grok API Union.ai
  - Grok API key
  - XAI_API_KEY
  - Grok Python task
  - OpenAI-compatible API
---

# Use the Grok API with Flyte

[Grok API](https://docs.x.ai/docs/tutorial) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://api.x.ai/v1` |
| API key | xAI console, **API Keys** |
| Environment variable | `XAI_API_KEY` |

## Store your Grok API key

Run this command and paste the key at the prompt:

```bash
flyte create secret grok-api-key --project <your-project> --domain development
```

## Call Grok from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_grok.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Grok docs](https://docs.x.ai/docs/tutorial).

## Call Grok from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Grok API to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
