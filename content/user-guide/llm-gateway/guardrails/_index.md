---
title: Guardrails
description: Check every prompt before it reaches a model, and every answer before it reaches the caller, with your own code.
icon: shield-check
weight: 6
variants: -flyte +union
---

# Guardrails

A guardrail is your own code, run by the gateway around every model call. Use one to keep personal data out of third-party models, to withhold answers that leak credentials, to refuse off-limits topics, or to answer common questions from your own cache without paying for a model call.

Guardrails are global. One guardrail applies to every virtual key on the gateway, so a new team or app is covered from its first request.

## How guardrails work

A gateway has at most two guardrails:

- **Pre-call**, run before the model. It sees the prompt and returns one of three verdicts:
  - **pass**: the call goes to the model.
  - **fail**: the call is refused, and the model is never called.
  - **cache hit**: the guardrail supplies the answer itself, and the model is never called.
- **Post-call**, run after the model. It sees the answer and returns one of two verdicts:
  - **pass**: the answer goes to the caller.
  - **fail**: the answer is withheld.

A refused call returns `403` with error type `guardrail_blocked` and the message your guardrail chose. A refused call is never retried on a [fallback](../virtual-keys#fallbacks).

A guardrail can't rewrite a prompt or an answer. To redact rather than refuse, have the pre-call guardrail fail with a message that tells the caller what to remove.

Each guardrail is a Union app of type `Guardrail`, running on the gateway's cluster. The gateway calls it over the cluster-local network with a plain HTTP request, so you can write it in any language:

- **Python:** use `GuardrailAppEnvironment` from `flyteplugins-union`. Write a function that returns a verdict; the class handles the HTTP side. See [Python guardrails](./python-guardrails).
- **Any other language:** implement two HTTP endpoints. See [Guardrail protocol](./protocol).

## Register a guardrail

1. Deploy the guardrail app on the gateway's cluster.
2. Open **Settings → LLM Gateway → Guardrails**, and choose the pre-call or post-call stage.
3. Fill in the guardrail:

   | Field | Meaning |
   |---|---|
   | **Guardrail app** | The app to call. Only running apps of type `Guardrail` on the gateway's cluster are listed. |
   | **Timeout (ms)** | How long the gateway waits for a verdict. Defaults to 5,000. At most 30,000. |
   | **Fail open** | What happens when the guardrail can't answer. See [When a guardrail fails](#when-a-guardrail-fails). |

The gateway picks up the guardrail in under a second. To use one app for both stages, register it under each stage.

## When a guardrail fails

A guardrail *fails* when it times out, returns a status other than `200`, or returns a body the gateway can't read. What happens next depends on **Fail open**:

| Fail open | Effect | Use it when |
|---|---|---|
| Off (default) | The call is refused with `503` `guardrail_unavailable`. | The guardrail enforces a rule you can't break, such as keeping personal data in-house. |
| On | The call proceeds as if the guardrail returned pass. The failure is recorded. | The guardrail is advisory, and availability matters more. |

Every guardrail outcome other than pass is recorded with the request's usage, with the `reason` your guardrail returned, so blocks per key show up in the console.

## What guardrails see

- **Request types.** Chat completions, text completions, the Responses API, and, on the pre-call stage only, decisions. Embeddings, audio, and image requests are never sent to a guardrail.
- **Messages.** The pre-call stage gets the conversation as a flat list of text messages. The post-call stage gets the answer text, and not the prompt. If a post-call check needs the prompt, look it up by `request_id` from state your pre-call check saved.
- **Caller context.** The virtual key's ID and name, the provider and model, and the caller's [custom dimensions](../virtual-keys#attribute-spend-with-custom-dimensions).

## Streaming

For a streamed answer, the post-call check runs once, on the full text, after the last chunk. Chunks already sent to the caller can't be recalled: a fail ends the stream with an error event, after the text that was already delivered. If your post-call guardrail must stop text from ever reaching the caller, have callers turn off streaming.

The gateway buffers at most 1 MiB of text per stream and 64 MiB across all streams on a replica. Change both limits under **Stream buffering** on the **Guardrails** tab. Past either limit, the check sees a prefix of the answer with `truncated` set.

A cache hit on a streamed request is delivered as a single chunk.

## Keep guardrails fast

Every guarded call waits for the guardrail, so its latency adds to every request. Keep checks in memory where you can, keep at least one replica running so calls never wait for a cold start, and set the timeout close to your guardrail's real worst case.

{{< subpage-cards >}}
