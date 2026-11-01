---
title: Use Cohere with Flyte
linkTitle: Cohere
description: "Call the Cohere API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 7
variants: +flyte +union
keywords:
  - Cohere API
  - Cohere Flyte
  - Cohere Union.ai
  - Cohere API key
  - CO_API_KEY
  - Cohere Python task
  - OpenAI-compatible API
---

# Use Cohere with Flyte

[Cohere](https://docs.cohere.com/docs/compatibility-api) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://api.cohere.ai/compatibility/v1` |
| API key | [API keys](https://dashboard.cohere.com/api-keys) |
| Environment variable | `CO_API_KEY` |

## Store your Cohere API key

Run this command and paste the key at the prompt:

```bash
flyte create secret cohere-api-key --project <your-project> --domain development
```

## Call Cohere from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_cohere.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Cohere docs](https://docs.cohere.com/docs/compatibility-api).

## Call Cohere from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Cohere to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
