---
title: Fireworks
description: "Call the Fireworks AI API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret, set the base URL, and use serverless or on-demand model"
icon: cloud
weight: 1
variants: +flyte +union
keywords:
  - Fireworks AI API
  - Fireworks AI Flyte
  - Fireworks AI Union.ai
  - Fireworks API key
  - FIREWORKS_API_KEY
  - Fireworks Python task
  - OpenAI-compatible API
  - Fireworks on-demand deployment
---

# Fireworks

[Fireworks AI](https://docs.fireworks.ai/getting-started/quickstart) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://api.fireworks.ai/inference/v1` |
| API key | [API keys](https://app.fireworks.ai/settings/users/api-keys) |
| Environment variable | `FIREWORKS_API_KEY` |

## Store your Fireworks API key

Run this command and paste the key at the prompt:

```bash
flyte create secret fireworks-api-key --project <your-project> --domain development
```

## Call Fireworks from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_fireworks.py" fragment="task" lang="python" >}}

Models on Fireworks' serverless tier use the name `accounts/fireworks/models/<model>`. Some catalog models aren't available on that tier and need a dedicated deployment.

## Call Fireworks from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

## Use an on-demand deployment

An on-demand deployment runs a model on dedicated GPUs. To use one, change only the model name. The base URL, the key, and the secret stay the same:

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_fireworks.py" fragment="on-demand" lang="python" >}}

A deployment that has scaled to zero returns a 503 while it scales up, so give the task [retries](../../tasks/task-configuration/retries-and-timeouts).

## Handle rate limits

A 429 means you've reached a rate limit on your Fireworks account. You can move to an on-demand deployment, but its requests still count toward account-wide limits, and a 429 there usually means the GPUs are saturated.

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Fireworks AI to the LLM Gateway](../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
