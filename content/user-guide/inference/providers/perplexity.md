---
title: Use Perplexity with Flyte
linkTitle: Perplexity
description: "Call the Perplexity API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 16
variants: +flyte +union
keywords:
  - Perplexity API
  - Perplexity Flyte
  - Perplexity Union.ai
  - Perplexity API key
  - PERPLEXITY_API_KEY
  - Perplexity Python task
  - OpenAI-compatible API
---

# Use Perplexity with Flyte

[Perplexity](https://docs.perplexity.ai/docs/agent-api/openai-compatibility) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://api.perplexity.ai/v1` |
| API key | [API keys](https://console.perplexity.ai/project/keys) |
| Environment variable | `PERPLEXITY_API_KEY` |

## Store your Perplexity API key

Run this command and paste the key at the prompt:

```bash
flyte create secret perplexity-api-key --project <your-project> --domain development
```

## Call Perplexity from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_perplexity.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Perplexity docs](https://docs.perplexity.ai/docs/agent-api/openai-compatibility).

## Call Perplexity from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

## Use the Responses API

Perplexity's Agent API uses OpenAI's Responses format, so the example calls `client.responses.create()` instead of `client.chat.completions.create()`. Support for its earlier Sonar Chat Completions API has ended.

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Perplexity to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
