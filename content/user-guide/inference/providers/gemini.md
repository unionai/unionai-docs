---
title: Use the Gemini API with Flyte
linkTitle: Gemini API
description: "Call the Gemini API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 9
variants: +flyte +union
keywords:
  - Gemini API
  - Gemini API Flyte
  - Gemini API Union.ai
  - Gemini API key
  - GEMINI_API_KEY
  - Gemini Python task
  - OpenAI-compatible API
---

# Use the Gemini API with Flyte

[Gemini API](https://ai.google.dev/gemini-api/docs/openai) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://generativelanguage.googleapis.com/v1beta/openai/` |
| API key | [Google AI Studio](https://aistudio.google.com/apikey) |
| Environment variable | `GEMINI_API_KEY` |

## Store your Gemini API key

Run this command and paste the key at the prompt:

```bash
flyte create secret gemini-api-key --project <your-project> --domain development
```

## Call Gemini from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_gemini.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Gemini docs](https://ai.google.dev/gemini-api/docs/openai).

## Call Gemini from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Gemini API to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
