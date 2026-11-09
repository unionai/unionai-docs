---
title: Decisions
description: Send a state and named questions to the Inference Gateway's POST /v1/decisions endpoint and get a typed answer to each.
icon: sliders
weight: 7
variants: -flyte +union
---

# Decisions

`POST /v1/decisions` asks a model several typed questions about one piece of state in a single call. Each named question gets its own answer: a probability, a chosen option, or a score. Use it for the narrow judgments described in [Decision models](../decision-models/_index), such as routing, moderation, and guards, through the same endpoint and virtual keys as the rest of your model traffic.

## Call the endpoint

```bash
curl https://<your-gateway-endpoint>/v1/decisions \
  -H "Authorization: Bearer sk-un-..." \
  -H "Content-Type: application/json" \
  -d '{
  "model": "typesafe/<model>",
  "state": "Customer: I was charged twice for one order.",
  "questions": {
    "is_billing": {
      "kind": "noul",
      "instructions": "Is this a billing issue?"
    },
    "urgency": {
      "kind": "choice",
      "instructions": "How urgent is it?",
      "criteria": {
        "low": "can wait",
        "high": "reply today"
      }
    }
  }
}'
```

If the gateway is behind Union sign-in, run `flyte proxy app` first and call `http://127.0.0.1:8600/v1/decisions` instead. See [Use from your laptop](./use-from-laptop).

Replace `<your-gateway-endpoint>` with your gateway's endpoint from **Settings → Inference Gateway**, `sk-un-...` with a virtual key, and `<model>` with a model your `typesafe` provider allows.

When the gateway has a deployed `typesafe` provider, or a vLLM or SGLang provider with **Answers decisions** on, the gateway's overview in **Settings → Inference Gateway** shows this command with your endpoint and a model filled in.

## The request

| Field | Meaning |
|---|---|
| `model` | The `provider/model` that answers, for example `typesafe/<model>` or `qwen/qwen3-8b`. The provider must answer decisions; see [Which providers answer decisions](#which-providers-answer-decisions). |
| `state` | The text the questions are about. |
| `questions` | The questions, keyed by name. |

Each question has a `kind` and `instructions`, the question itself:

| `kind` | Answer | `criteria` |
|---|---|---|
| `noul` | A probability. | Not needed. |
| `choice` | One of the options. | A mapping of each option to a description of when it applies. |

## Which providers answer decisions

| Provider | Answers decisions |
|---|---|
| `typesafe` | Yes. TypeSafe's decision models answer decisions only, not chat or completions. |
| Hosted LLM providers | Chat models that support tool calling. The gateway asks the model through one forced tool call. |
| vLLM and SGLang apps | Only when the provider was added with **Answers decisions** on. The gateway asks the model through one forced tool call on chat completions, so the model must support tool calling. With the setting off, the gateway refuses decision requests for that provider. See [Add a self-hosted model](./providers#add-a-self-hosted-model). |

A gateway on an older image may not serve `/v1/decisions`. If the gateway's overview shows an update available, redeploy the gateway.
