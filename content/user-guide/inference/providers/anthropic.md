---
title: Anthropic
description: "Call the Anthropic API and Claude models from Flyte tasks and apps: store your API key as a secret and use the anthropic Python SDK."
icon: cloud
weight: 3
variants: +flyte +union
keywords:
  - Anthropic API
  - Anthropic Flyte
  - Anthropic Union.ai
  - Anthropic API key
  - ANTHROPIC_API_KEY
  - Anthropic Python task
  - Claude
  - Claude API
---

# Anthropic

A Flyte task or app can call the [Anthropic API](https://platform.claude.com/docs/en/get-started) with the `anthropic` Python SDK and a key from your own account.

| Setting | Value |
|---|---|
| Python package | `anthropic` |
| API key | [API keys](https://platform.claude.com/settings/keys) |
| Environment variable | `ANTHROPIC_API_KEY` |

## Store your Anthropic API key

Run this command and paste the key at the prompt:

```bash
flyte create secret anthropic-api-key --project <your-project> --domain development
```

## Call Anthropic from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_anthropic.py" fragment="task" lang="python" >}}

## Call Anthropic from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

Anthropic also has an OpenAI-compatible endpoint, which its docs describe as being for testing and comparing models, not production.

{{< variant union >}}
{{< markdown >}}

## Route calls through the Inference Gateway

To add budgets, fallbacks, and guardrails, [add Anthropic to the Inference Gateway](../inference-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../inference-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
