---
title: Use TypeSafe with Flyte
linkTitle: TypeSafe
description: "Get typed answers from the TypeSafe API in Flyte tasks and apps: store your API key as a secret and use the typesafe-sdk Python package."
icon: cloud
weight: 22
variants: +flyte +union
keywords:
  - TypeSafe API
  - TypeSafe Flyte
  - TypeSafe Union.ai
  - TypeSafe API key
  - TYPESAFE_API_KEY
  - TypeSafe Python task
  - typed answers
---

# Use TypeSafe with Flyte

A Flyte task or app can call the [TypeSafe API](https://docs.typesafe.ai/introduction/quickstart.md) with its Python SDK and a key from your own account.

| Setting | Value |
|---|---|
| Python package | `typesafe-sdk` |
| API key | TypeSafe console |
| Environment variable | `TYPESAFE_API_KEY` |

## Store your TypeSafe API key

Run this command and paste the key at the prompt:

```bash
flyte create secret typesafe-api-key --project <your-project> --domain development
```

## Get typed answers from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_typesafe.py" fragment="task" lang="python" >}}

## Call TypeSafe from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add TypeSafe to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
