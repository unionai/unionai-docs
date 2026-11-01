---
title: Use OpenRouter with Flyte
linkTitle: OpenRouter
description: "Call the OpenRouter API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 15
variants: +flyte +union
keywords:
  - OpenRouter API
  - OpenRouter Flyte
  - OpenRouter Union.ai
  - OpenRouter API key
  - OPENROUTER_API_KEY
  - OpenRouter Python task
  - OpenAI-compatible API
---

# Use OpenRouter with Flyte

[OpenRouter](https://openrouter.ai/docs/quickstart) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://openrouter.ai/api/v1` |
| API key | [API keys](https://openrouter.ai/keys) |
| Environment variable | `OPENROUTER_API_KEY` |

## Store your OpenRouter API key

Run this command and paste the key at the prompt:

```bash
flyte create secret openrouter-api-key --project <your-project> --domain development
```

## Call OpenRouter from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_openrouter.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [OpenRouter docs](https://openrouter.ai/docs/quickstart).

## Call OpenRouter from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add OpenRouter to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
