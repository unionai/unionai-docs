---
title: Use Nebius Token Factory with Flyte
linkTitle: Nebius Token Factory
description: "Call the Nebius Token Factory API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 14
variants: +flyte +union
keywords:
  - Nebius Token Factory API
  - Nebius Token Factory Flyte
  - Nebius Token Factory Union.ai
  - Nebius API key
  - NEBIUS_API_KEY
  - Nebius Python task
  - OpenAI-compatible API
---

# Use Nebius Token Factory with Flyte

[Nebius Token Factory](https://docs.tokenfactory.nebius.com/quickstart) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://api.tokenfactory.nebius.com/v1/` |
| API key | Token Factory console |
| Environment variable | `NEBIUS_API_KEY` |

## Store your Nebius API key

Run this command and paste the key at the prompt:

```bash
flyte create secret nebius-api-key --project <your-project> --domain development
```

## Call Nebius from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_nebius.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Nebius docs](https://docs.tokenfactory.nebius.com/quickstart).

## Call Nebius from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Nebius Token Factory to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
