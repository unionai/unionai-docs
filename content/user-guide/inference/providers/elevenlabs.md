---
title: Use ElevenLabs with Flyte
linkTitle: ElevenLabs
description: "Generate speech with the ElevenLabs API from Flyte tasks and apps: store your API key as a secret and use the elevenlabs Python SDK."
icon: cloud
weight: 20
variants: +flyte +union
keywords:
  - ElevenLabs API
  - ElevenLabs Flyte
  - ElevenLabs Union.ai
  - ElevenLabs API key
  - ELEVENLABS_API_KEY
  - ElevenLabs Python task
  - text to speech
---

# Use ElevenLabs with Flyte

A Flyte task or app can call the [ElevenLabs API](https://elevenlabs.io/docs/quickstart) with its Python SDK and a key from your own account.

| Setting | Value |
|---|---|
| Python package | `elevenlabs` |
| API key | [API keys](https://elevenlabs.io/app/api/api-keys) |
| Environment variable | `ELEVENLABS_API_KEY` |

## Store your ElevenLabs API key

Run this command and paste the key at the prompt:

```bash
flyte create secret elevenlabs-api-key --project <your-project> --domain development
```

## Generate speech from a task

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_elevenlabs.py" fragment="task" lang="python" >}}

Replace `<voice-id>` with a voice from your ElevenLabs account.

## Call ElevenLabs from an app

An `AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable. See [Call the provider from an app](./_index#call-the-provider-from-an-app).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

To add budgets, fallbacks, and guardrails, [add ElevenLabs to the LLM Gateway](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps). See [Choose direct calls or the gateway](./_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}
