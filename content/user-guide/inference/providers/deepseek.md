---
title: Use DeepSeek with Flyte
linkTitle: DeepSeek
description: "Call the DeepSeek API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 8
variants: +flyte +union
keywords:
  - DeepSeek API
  - DeepSeek Flyte
  - DeepSeek Union.ai
  - DeepSeek API key
  - DEEPSEEK_API_KEY
  - DeepSeek Python task
  - OpenAI-compatible API
---

# Use DeepSeek with Flyte

[DeepSeek](https://api-docs.deepseek.com/) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://api.deepseek.com` |
| API key | DeepSeek platform, **API keys** |
| Environment variable | `DEEPSEEK_API_KEY` |

## Store your DeepSeek API key

Run this command and paste the key at the prompt:

```bash
flyte create secret deepseek-api-key --project <your-project> --domain development
```

## Call DeepSeek from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_deepseek.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [DeepSeek docs](https://api-docs.deepseek.com/).

## Call DeepSeek from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add DeepSeek to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
