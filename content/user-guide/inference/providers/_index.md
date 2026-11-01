---
title: Providers
description: "Call hosted LLM and model APIs such as Fireworks AI, OpenAI, and Anthropic from Flyte tasks and apps, with API keys stored as secrets."
icon: cloud
weight: 1
variants: +flyte +union
keywords:
  - inference providers
  - hosted LLM API
  - model provider API key
  - OpenAI-compatible API
  - Fireworks AI
  - OpenAI
  - Anthropic
  - Flyte secrets
---

# Providers

Tasks and apps can call a hosted model API using a key from your own provider account. Billing, rate limits, and data handling stay under your agreement with the provider. You store the key as a secret, and your code reads it from an environment variable at runtime.

{{< variant union >}}
{{< markdown >}}

This works on both BYOC and Self-managed deployments. To add budgets, fallbacks, and guardrails, route the same calls through the [LLM Gateway](#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}

## Supported providers

These guides cover setup and a complete task for the most common providers:

{{< subpage-cards >}}

### Other OpenAI-compatible providers

These providers work with the OpenAI SDK by changing the base URL. Start from the [Fireworks AI task](./fireworks#call-fireworks-from-a-task), and change the base URL, the secret, the environment variable, and the model.

| Provider | Get an API key | Base URL | Conventional variable |
|---|---|---|---|
| [Azure OpenAI](https://learn.microsoft.com/en-us/azure/foundry/openai/api-version-lifecycle) | Your Azure resource | `https://<your-resource>.openai.azure.com/openai/v1/` | `AZURE_OPENAI_API_KEY` |
| [Gemini API](https://ai.google.dev/gemini-api/docs/openai) | [Google AI Studio](https://aistudio.google.com/apikey) | `https://generativelanguage.googleapis.com/v1beta/openai/` | `GEMINI_API_KEY` |
| [Mistral AI](https://docs.mistral.ai/resources/sdks) | Mistral console, **API Keys** | `https://api.mistral.ai/v1` | `MISTRAL_API_KEY` |
| [Cohere](https://docs.cohere.com/docs/compatibility-api) | [API keys](https://dashboard.cohere.com/api-keys) | `https://api.cohere.ai/compatibility/v1` | `CO_API_KEY` |
| [Groq](https://console.groq.com/docs/quickstart) | [API keys](https://console.groq.com/keys) | `https://api.groq.com/openai/v1` | `GROQ_API_KEY` |
| [DeepSeek](https://api-docs.deepseek.com/) | DeepSeek platform, **API keys** | `https://api.deepseek.com` | `DEEPSEEK_API_KEY` |
| [Grok API](https://docs.x.ai/docs/tutorial) | xAI console, **API Keys** | `https://api.x.ai/v1` | `XAI_API_KEY` |
| [Perplexity](https://docs.perplexity.ai/docs/agent-api/openai-compatibility) | [API keys](https://console.perplexity.ai/project/keys) | `https://api.perplexity.ai/v1` | `PERPLEXITY_API_KEY` |
| [Cerebras](https://inference-docs.cerebras.ai/resources/openai) | Cerebras Cloud console, **API Keys** | `https://api.cerebras.ai/v1` | `CEREBRAS_API_KEY` |
| [OpenRouter](https://openrouter.ai/docs/quickstart) | [API keys](https://openrouter.ai/keys) | `https://openrouter.ai/api/v1` | `OPENROUTER_API_KEY` |
| [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers/index) | [Access tokens](https://huggingface.co/settings/tokens) | `https://router.huggingface.co/v1` | `HF_TOKEN` |
| [Nebius Token Factory](https://docs.tokenfactory.nebius.com/quickstart) | Token Factory console | `https://api.tokenfactory.nebius.com/v1/` | `NEBIUS_API_KEY` |
| [Sarvam AI](https://docs.sarvam.ai/api/getting-started/models/openweight) | [Key management](https://indus.sarvam.ai/key-management) | `https://api.sarvam.ai/v2` | `SARVAM_API_KEY` |
| [Wafer](https://docs.wafer.ai/serverless) | Wafer dashboard | `https://pass.wafer.ai/v1` | Your choice |

Two of these differ from the task:

- **Azure OpenAI:** Set `model` to the name of your deployment, not the name of the underlying model.
- **Perplexity:** Its Agent API uses OpenAI's Responses format, so call `client.responses.create()` instead of `client.chat.completions.create()`. Support for its earlier Sonar Chat Completions API has ended.

### Providers with their own SDK

These providers don't document an OpenAI-compatible endpoint for production use. Add the SDK to the image and pass it the key from the environment. See the [Anthropic guide](./anthropic) for the pattern.

| Provider | Get an API key | Python package | Conventional variable | Models |
|---|---|---|---|---|
| [Anthropic](./anthropic) | [API keys](https://platform.claude.com/settings/keys) | `anthropic` | `ANTHROPIC_API_KEY` | Chat |
| [ElevenLabs](https://elevenlabs.io/docs/quickstart) | [API keys](https://elevenlabs.io/app/api/api-keys) | `elevenlabs` | `ELEVENLABS_API_KEY` | Speech |
| [Runway](https://docs.dev.runwayml.com/guides/using-the-api/) | [Developer portal](https://dev.runway.com/) | `runwayml` | `RUNWAYML_API_SECRET` | Video and image |
| [TypeSafe](https://docs.typesafe.ai/introduction/quickstart.md) | TypeSafe console | `typesafe-sdk` | `TYPESAFE_API_KEY` | Typed answers |

## Store the API key as a secret

Run this command without `--value` and paste the key at the prompt, which keeps it out of your shell history:

```bash
flyte create secret fireworks-api-key --project <your-project> --domain development
```

Leave out `--project` and `--domain` to make the secret available across your organization. Prefer a project and domain, so that one team's tasks can't use another team's key.

Check that the secret exists:

```bash
flyte get secret --project <your-project> --domain development
```

The output lists metadata such as the name and scope. It never includes the value.

{{< variant union >}}
{{< markdown >}}

Each cluster pool has its own secret store. If your organization has more than one pool, an organization-wide secret needs `--cluster-pool`. See [Org-wide secrets in a multi-cluster deployment](../../tasks/task-configuration/secrets#org-wide-secrets-in-a-multi-cluster-deployment).

Secret values stay in your own infrastructure and no API returns them. See [Secrets management](../../../security/data-protection/secrets).

{{< /markdown >}}
{{< /variant >}}

## Call the provider from a task

Declare the secret on the environment and read it from the environment variable. This task calls Fireworks AI through the OpenAI SDK:

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_fireworks.py" fragment="task" lang="python" >}}

A task can only read a secret whose scope covers the project and domain it runs in. Provider model IDs change often, so check the provider's model catalog for current names.

## Call the provider from an app

`AppEnvironment` takes the same `secrets` argument, and the app reads the same environment variable:

{{< code file="/unionai-examples/v2/user-guide/inference/providers/call_from_app.py" fragment="app-env" lang="python" >}}

## Use a different key for one call

Override the secret for a single invocation when the same task needs different credentials, for example per team:

{{< code file="/unionai-examples/v2/user-guide/inference/providers/override_key.py" fragment="override" lang="python" >}}

The override replaces the environment's secrets for that call. On a [reusable container](../../tasks/task-configuration/reusable-containers) it raises an error unless you also pass `reusable="off"`. See [Overriding secrets](../../tasks/task-configuration/overrides#overriding-secrets).

{{< variant union >}}
{{< markdown >}}

## Choose direct calls or the gateway

Calling a provider directly needs the fewest moving parts. The [LLM Gateway](../../llm-gateway/_index) supports all of the providers above, including Fireworks, behind one endpoint.

| | Direct call | LLM Gateway |
|---|---|---|
| **Key your code holds** | The provider's API key | A virtual key with its own budget and rate limit |
| **Change provider** | Change the base URL, key, and model | Change the model name |
| **Provider outage** | Handle it in your code | Fall back to another model |
| **Prompt and answer checks** | Write them into each task or app | Global guardrails on every call |
| **Spend across teams** | One view per provider account | One view per virtual key |

To move to the gateway, [add the provider](../../llm-gateway/providers#add-a-hosted-provider) using the same secret, then [point your client at the gateway](../../llm-gateway/use-from-tasks-and-apps).

{{< /markdown >}}
{{< /variant >}}

## Keep keys safe

- **Never return a key from a task.** Task outputs are written in plaintext to your object store and appear in the UI and in downstream tasks.
- **Keep keys out of code, task inputs, and `flyte.run()` arguments.** Inputs are stored and displayed the same way as outputs.
- **Rotate without downtime.** Create a key at the provider, delete and re-create the secret with the new value, redeploy apps that use it, and then revoke the old key.

## Troubleshooting

**The provider returns 401:**
The key is invalid, revoked, or was stored with a typo. Test it outside Flyte with the provider's REST API, then re-create the secret.

**The task fails before it runs, with a secret not found error:**
The secret's scope doesn't cover the task's project and domain. List secrets with the same `--project` and `--domain` the task uses.

**The provider returns 429:**
You've reached a rate limit on your provider account. Check its limits and your usage in the provider's console.
