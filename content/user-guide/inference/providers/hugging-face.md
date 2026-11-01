---
title: Use Hugging Face Inference Providers with Flyte
linkTitle: Hugging Face
description: "Call the Hugging Face Inference Providers API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 12
variants: +flyte +union
keywords:
  - Hugging Face Inference Providers API
  - Hugging Face Inference Providers Flyte
  - Hugging Face Inference Providers Union.ai
  - Hugging Face API key
  - HF_TOKEN
  - Hugging Face Python task
  - OpenAI-compatible API
---

# Use Hugging Face Inference Providers with Flyte

[Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers/index) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://router.huggingface.co/v1` |
| API key | [Access tokens](https://huggingface.co/settings/tokens) |
| Environment variable | `HF_TOKEN` |

## Store your Hugging Face API key

Run this command and paste the key at the prompt:

```bash
flyte create secret hugging-face-api-key --project <your-project> --domain development
```

## Call Hugging Face from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_hugging_face.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Hugging Face docs](https://huggingface.co/docs/inference-providers/index).

## Call Hugging Face from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Hugging Face Inference Providers to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
