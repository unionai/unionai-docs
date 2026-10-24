---
title: Virtual keys
description: Issue LLM Gateway keys with budgets, rate limits, model allowlists, and fallbacks.
icon: key
weight: 3
variants: -flyte +union
---

# Virtual keys

A virtual key (`sk-un-...`) is the credential every caller presents to the gateway. Give each team, app, or developer their own key. For example, the support bot gets a key limited to `claude-sonnet-4-5` with a $200 monthly budget, and the research team gets a key for any model with $2,000 a month. Neither ever sees a provider API key, and revoking one key affects no one else.

## Issue a key

1. Open **Settings → LLM Gateway → Virtual keys** and issue a new key.
2. Fill in the key:

   | Field | Meaning |
   |---|---|
   | **Name** | Who or what the key is for, for example `ml-platform-team`. |
   | **Description** | Optional. |
   | **Providers** | The providers this key may use. Selecting none allows all of them. |
   | **Allowed models** | A comma-separated allowlist, for example `gpt-4.1-mini, claude-sonnet-4-5`. Leave it empty to allow every model. |
   | **Fallbacks** | An ordered list of provider and model pairs to try when the primary fails. See [Fallbacks](#fallbacks). |
   | **Budget (USD)** | The most the key may spend per day, week, or month. Empty means unlimited. |
   | **Rate limit (req/min)** | The most requests the key may send per minute. Empty means unlimited. |

3. Copy the key value from the confirmation dialog and store it where the caller reads it, for example as a Union secret:

   ```bash
   flyte create secret support-bot-llm-key sk-un-...
   ```

Callers send the key the way any OpenAI-compatible client sends an API key, as `Authorization: Bearer sk-un-...`.

## Budgets

A budget is a dollar ceiling per window: per day, per week, or per month. The gateway keeps a running total for each key and rejects calls with `402` as soon as the ceiling is reached. Enforcement happens in the gateway itself, so it keeps working when the control plane is unreachable. The total resets at the start of each window.

Spend is computed from token counts and each provider's price. A self-hosted provider with no cost set is not metered. See [Providers](./providers).

For how replicas and restarts affect the running total, see [Size the gateway](./deploy-gateway#size-the-gateway).

## Fallbacks

Fallbacks keep a caller working when its primary model fails. A request names an ordered list of `provider/model` strings. If the primary call fails, the gateway tries each fallback in turn until one succeeds.

The caller sends the list with each request, in the `fallbacks` field of the request body. With the OpenAI Python SDK:

```python
response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    messages=[{"role": "user", "content": "Summarize this ticket."}],
    extra_body={"fallbacks": ["anthropic/claude-haiku-4-5", "bedrock/amazon.nova-lite-v1:0"]},
)
```

The **Fallbacks** list on a key records the chain that key's callers should send. Each entry must use one of the key's providers. The gateway does not add the list to requests on its own.

Fallbacks cover:

- provider errors and outages, and
- rejections by the key's own policy, such as a primary model that is not on the key's allowlist.

A guardrail block is never retried on a fallback. A prompt your guardrail refuses is refused for every model.

## Attribute spend with custom dimensions

Add `x-un-dim-<name>` headers to tag requests, for example `x-un-dim-team: search` or `x-un-dim-customer: acme`. The gateway records the values with each request's usage and passes them to guardrails as `metadata`. Use them to break down the spend of one key, without issuing more keys.

## Errors

| Status | Meaning |
|---|---|
| `401` | The request has no virtual key, or the key is unknown or revoked. |
| `402` | The key has reached its budget for the current window. |
| `403` `model_blocked` | The model is not on the key's allowlist. |
| `403` `guardrail_blocked` | A guardrail refused the prompt or the answer. See [Guardrails](./guardrails/_index). |
| `503` `guardrail_unavailable` | A guardrail could not be reached and is set to block on failure. |

A request that exceeds the key's rate limit is rejected until the minute window resets.

## Change or revoke a key

Keys can't be edited. To change a key's providers, models, fallbacks, budget, or rate limit, issue a new key with the settings you want, update the callers' secret, then revoke the old key.

Revoking a key in **Settings → LLM Gateway → Virtual keys** takes effect on the gateway in under a second.
