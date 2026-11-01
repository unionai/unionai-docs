---
title: Use Groq with Flyte
linkTitle: Groq
description: "Call the Groq API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 11
variants: +flyte +union
keywords:
  - Groq API
  - Groq Flyte
  - Groq Union.ai
  - Groq API key
  - GROQ_API_KEY
  - Groq Python task
  - OpenAI-compatible API
---

# Use Groq with Flyte

[Groq](https://console.groq.com/docs/quickstart) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://api.groq.com/openai/v1` |
| API key | [API keys](https://console.groq.com/keys) |
| Environment variable | `GROQ_API_KEY` |

## Store your Groq API key

Run this command and paste the key at the prompt:

```bash
flyte create secret groq-api-key --project <your-project> --domain development
```

## Call Groq from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_groq.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Groq docs](https://console.groq.com/docs/quickstart).

## Call Groq from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Groq to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
