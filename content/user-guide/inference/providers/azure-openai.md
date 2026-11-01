---
title: Use Azure OpenAI with Flyte
linkTitle: Azure OpenAI
description: "Call the Azure OpenAI API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 5
variants: +flyte +union
keywords:
  - Azure OpenAI API
  - Azure OpenAI Flyte
  - Azure OpenAI Union.ai
  - Azure OpenAI API key
  - AZURE_OPENAI_API_KEY
  - Azure OpenAI Python task
  - OpenAI-compatible API
---

# Use Azure OpenAI with Flyte

[Azure OpenAI](https://learn.microsoft.com/en-us/azure/foundry/openai/api-version-lifecycle) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://<your-resource>.openai.azure.com/openai/v1/` |
| API key | Your Azure resource |
| Environment variable | `AZURE_OPENAI_API_KEY` |

## Store your Azure OpenAI API key

Run this command and paste the key at the prompt:

```bash
flyte create secret azure-openai-api-key --project <your-project> --domain development
```

## Call Azure OpenAI from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_azure_openai.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Azure OpenAI docs](https://learn.microsoft.com/en-us/azure/foundry/openai/api-version-lifecycle).

## Call Azure OpenAI from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

## Use your deployment name

Set `model` to the name of your deployment, not the name of the underlying model.

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Azure OpenAI to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
