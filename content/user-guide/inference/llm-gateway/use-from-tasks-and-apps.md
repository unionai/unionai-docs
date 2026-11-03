---
title: Use from tasks and apps
description: Call models through the LLM Gateway from tasks and apps running on Union.
icon: braces
weight: 4
variants: -flyte +union
---

# Use from tasks and apps

Tasks and apps on any of your Union clusters call the gateway like any OpenAI-compatible API: set the base URL to the gateway's endpoint and pass a virtual key as the API key. A summarization task, a RAG app, and an agent all share one endpoint, and each gets its own budget through its own key.

## Prerequisites

- A deployed gateway and its endpoint, from **Settings → LLM Gateway**. See [Deploy the gateway](./deploy-gateway).
- A [virtual key](./virtual-keys) for the task or app, stored as a Union secret:

  ```bash
  flyte create secret llm-gateway-key sk-un-...
  ```

## Call the gateway from a task

Mount the secret on the environment:

{{< code file="/unionai-examples/v2/user-guide/llm-gateway/call_from_task.py" fragment=env lang=python >}}

Then point the client at the gateway. Address models as `provider/model`:

{{< code file="/unionai-examples/v2/user-guide/llm-gateway/call_from_task.py" fragment=task lang=python >}}

The `fallbacks` list is optional. If `openai/gpt-4.1-mini` fails, the gateway retries the call on `anthropic/claude-haiku-4-5`. See [Fallbacks](./virtual-keys#fallbacks).

## Call the gateway from an app

Apps use the same pattern. This FastAPI app has its own key, so its budget and allowed models are separate from every task's. The `x-un-dim-app` header tags its requests for [spend attribution](./virtual-keys#attribute-spend-with-custom-dimensions):

{{< code file="/unionai-examples/v2/user-guide/llm-gateway/call_from_app.py" fragment=app lang=python >}}

## Use other clients

Any client that speaks the OpenAI API works against the gateway's `/v1` base URL:

- **Anthropic models through the OpenAI SDK.** Use `model="anthropic/<model>"`. The gateway translates the request.
- **LiteLLM.** Use the `openai/` prefix so LiteLLM sends an OpenAI-format request, set `api_base` to the gateway's `/v1` URL, and pass the virtual key as `api_key`.
- **LangChain.** Use `ChatOpenAI(base_url=..., api_key=..., model="provider/model")`.
- **curl.**

  ```bash
  curl https://<your-gateway-endpoint>/v1/chat/completions \
    -H "Authorization: Bearer $LLM_GATEWAY_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model": "openai/gpt-4.1-mini", "messages": [{"role": "user", "content": "Hello"}]}'
  ```

List the models a key can reach with `GET /v1/models`.
