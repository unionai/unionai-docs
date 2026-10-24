---
title: Providers
description: Add hosted model providers and self-hosted vLLM or SGLang models to the LLM Gateway.
icon: cloud
weight: 2
variants: -flyte +union
---

# Providers

A provider is a source of models behind the gateway: a hosted API such as OpenAI or Anthropic, or a model you serve yourself on Union with vLLM or SGLang. Callers address every model as `provider/model`, for example `openai/gpt-4.1-mini` or `anthropic/claude-sonnet-4-5`, so moving a workload between providers means changing one string.

## Add a hosted provider

1. Store the provider's API key as a Union secret:

   ```bash
   flyte create secret openai-api-key <your-openai-api-key>
   ```

2. Open **Settings → LLM Gateway → Providers** and click **Add provider**.
3. Fill in the provider:

   | Field | Meaning |
   |---|---|
   | **Provider** | One of the supported providers listed below. |
   | **API key secret** | The Union secret that holds the API key, for example `openai-api-key`. |
   | **Models** | A comma-separated allowlist, for example `gpt-4.1, gpt-4.1-mini`. Leave it empty to allow every model. |
   | **Weight** | The load-balancing weight among providers. Defaults to `1`. |

4. Redeploy the gateway so it mounts the new secret. The provider shows **Pending** until then, and **Deployed** after.

The secret is mounted on the gateway and stays in your data plane. The control plane never reads it, and the gateway's policy refers to it only by name.

The gateway meters hosted providers from its built-in price catalog, so budgets count their spend without any setup.

### Supported providers

`openai`, `anthropic`, `azure`, `bedrock`, `vertex`, `gemini`, `mistral`, `cohere`, `groq`, `deepseek`, `xai`, `perplexity`, `cerebras`, `fireworks`, `openrouter`, `huggingface`, `nebius`, `sarvam`, `elevenlabs`, `runway`, `wafer`, `typesafe`.

The console lists the providers your gateway supports when you add one.

## Add a self-hosted model

You can put a model you serve on Union behind the gateway, next to hosted providers. Callers reach it with the same client, the same virtual keys, and the same guardrails.

1. Deploy the model as a [vLLM](../user-guide/apps/native-app-integrations/vllm-app) or [SGLang](../user-guide/apps/native-app-integrations/sglang-app) app on the gateway's cluster.
2. In **Settings → LLM Gateway → Providers**, click **Add provider** and choose the vLLM or SGLang provider type.
3. Fill in the provider:

   | Field | Meaning |
   |---|---|
   | **Serving app** | The vLLM or SGLang app. Only apps on the gateway's cluster are listed. |
   | **Model id** | The model the app serves (its `--served-model-name`). Filled in from the app when it records one. |
   | **Name** | The provider name, which callers use as the model prefix. |
   | **Cost** | USD per 1 million input tokens and per 1 million output tokens. |
   | **Answers decisions** | Lets callers send this app `POST /v1/decisions`. The model must support tool calling. |
   | **Weight** | The load-balancing weight among providers. Defaults to `1`. |

A provider named `qwen` whose app serves `qwen3-8b` is called as `qwen/qwen3-8b`.

The gateway reaches the app over its cluster-local address, so no API key or public URL is involved. The app must be running when you add it.

> [!WARNING] Set a cost for self-hosted models you want to budget
> A self-hosted provider with no cost is treated as free: its calls never count against any virtual key's budget. To change the cost later, remove the provider and add it again.

## Remove a provider

Delete the provider in **Settings → LLM Gateway → Providers**. Virtual keys that list it can no longer reach its models; requests to them fail, or go to a fallback if the request names one.
