---
title: Use Sarvam AI with Flyte
linkTitle: Sarvam AI
description: "Call the Sarvam AI API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 17
variants: +flyte +union
keywords:
  - Sarvam AI API
  - Sarvam AI Flyte
  - Sarvam AI Union.ai
  - Sarvam API key
  - SARVAM_API_KEY
  - Sarvam Python task
  - OpenAI-compatible API
---

# Use Sarvam AI with Flyte

[Sarvam AI](https://docs.sarvam.ai/api/getting-started/models/openweight) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://api.sarvam.ai/v2` |
| API key | [Key management](https://indus.sarvam.ai/key-management) |
| Environment variable | `SARVAM_API_KEY` |

## Store your Sarvam API key

Run this command and paste the key at the prompt:

```bash
flyte create secret sarvam-api-key --project <your-project> --domain development
```

## Call Sarvam from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_sarvam.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Sarvam docs](https://docs.sarvam.ai/api/getting-started/models/openweight).

## Call Sarvam from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Sarvam AI to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
