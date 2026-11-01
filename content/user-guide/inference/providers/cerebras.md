---
title: Use Cerebras with Flyte
linkTitle: Cerebras
description: "Call the Cerebras API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 6
variants: +flyte +union
keywords:
  - Cerebras API
  - Cerebras Flyte
  - Cerebras Union.ai
  - Cerebras API key
  - CEREBRAS_API_KEY
  - Cerebras Python task
  - OpenAI-compatible API
---

# Use Cerebras with Flyte

[Cerebras](https://inference-docs.cerebras.ai/resources/openai) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://api.cerebras.ai/v1` |
| API key | Cerebras Cloud console, **API Keys** |
| Environment variable | `CEREBRAS_API_KEY` |

## Store your Cerebras API key

Run this command and paste the key at the prompt:

```bash
flyte create secret cerebras-api-key --project <your-project> --domain development
```

## Call Cerebras from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_cerebras.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Cerebras docs](https://inference-docs.cerebras.ai/resources/openai).

## Call Cerebras from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Cerebras to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
