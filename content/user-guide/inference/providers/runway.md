---
title: Use Runway with Flyte
linkTitle: Runway
description: "Generate video and images with the Runway API from Flyte tasks and apps: store your API key as a secret and use the runwayml Python SDK."
icon: cloud
weight: 21
variants: +flyte +union
keywords:
  - Runway API
  - Runway Flyte
  - Runway Union.ai
  - Runway API key
  - RUNWAYML_API_SECRET
  - Runway Python task
  - image to video
---

# Use Runway with Flyte

A Flyte task or app can call the [Runway API](https://docs.dev.runwayml.com/guides/using-the-api/) with its Python SDK and a key from your own account.

| Setting | Value |
|---|---|
| Python package | `runwayml` |
| API key | [Developer portal](https://dev.runway.com/) |
| Environment variable | `RUNWAYML_API_SECRET` |

## Store your Runway API key

Run this command and paste the key at the prompt:

```bash
flyte create secret runway-api-key --project <your-project> --domain development
```

## Generate video from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_runway.py" fragment="task" lang="python" >}}

## Call Runway from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add Runway to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
