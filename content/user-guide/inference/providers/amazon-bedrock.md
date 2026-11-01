---
title: AWS Bedrock
description: "Call the Amazon Bedrock API from Flyte tasks and apps with the OpenAI SDK: store your API key as a secret and set the base URL."
icon: cloud
weight: 4
variants: +flyte +union
keywords:
  - Amazon Bedrock API
  - AWS Bedrock
  - Amazon Bedrock Flyte
  - Amazon Bedrock Union.ai
  - Bedrock API key
  - AWS_BEARER_TOKEN_BEDROCK
  - Bedrock Python task
  - OpenAI-compatible API
---

# AWS Bedrock

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-chat-completions.html) has an OpenAI-compatible API, so a Flyte task or app can call it with the OpenAI SDK by changing the base URL.

| Setting | Value |
|---|---|
| Base URL | `https://bedrock-runtime.<region>.amazonaws.com/openai/v1` |
| API key | Bedrock console, **API keys** |
| Environment variable | `AWS_BEARER_TOKEN_BEDROCK` |

## Store your Bedrock API key

Run this command and paste the key at the prompt:

```bash
flyte create secret amazon-bedrock-api-key --project <your-project> --domain development
```

## Call Bedrock from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_amazon_bedrock.py" fragment="task" lang="python" >}}

Replace `<model-id>` with a model from the [Bedrock docs](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-chat-completions.html).

## Call Bedrock from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

## Use a Bedrock API key

Pass a Bedrock API key to the OpenAI SDK as `api_key`. AWS recommends short-term keys for production, which you'd need to refresh in the secret before they expire.

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Amazon Bedrock to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
