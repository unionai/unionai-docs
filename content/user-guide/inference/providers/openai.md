---
title: OpenAI
description: "Call the OpenAI API from Flyte tasks and apps: store your OpenAI API key as a secret and read it from the environment in your code."
icon: cloud
weight: 2
variants: +flyte +union
keywords:
  - OpenAI API
  - OpenAI Flyte
  - OpenAI Union.ai
  - OpenAI API key
  - OPENAI_API_KEY
  - OpenAI Python task
  - GPT
---

# OpenAI

A Flyte task or app can call the [OpenAI API](https://developers.openai.com/api/docs/quickstart) with the OpenAI SDK and a key from your own account.

| Setting | Value |
|---|---|
| Base URL | SDK default |
| API key | [API keys](https://platform.openai.com/settings/organization/api-keys) |
| Environment variable | `OPENAI_API_KEY` |

## Store your OpenAI API key

Run this command and paste the key at the prompt:

```bash
flyte create secret openai-api-key --project <your-project> --domain development
```

## Call OpenAI from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_openai.py" fragment="task" lang="python" >}}

## Call OpenAI from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the Inference Gateway

To add budgets, fallbacks, and guardrails, [add OpenAI to the Inference Gateway](../inference-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../inference-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
