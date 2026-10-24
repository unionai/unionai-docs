---
title: Guardrail protocol
description: The HTTP contract between the LLM Gateway and a guardrail, for writing guardrails in any language.
icon: braces
weight: 2
variants: -flyte +union
---

# Guardrail protocol

A guardrail is an HTTP server with two endpoints. The gateway sends each one a JSON description of the call and reads back a JSON verdict. Implement this contract in any language: reuse a Go policy engine your security team already runs, or a Node service that calls a moderation model.

For Python, `GuardrailAppEnvironment` implements this contract for you. See [Python guardrails](./python-guardrails).

## Endpoints

| Method and path | Called |
|---|---|
| `POST /guardrail/pre` | Before the model, if the app is the pre-call guardrail. |
| `POST /guardrail/post` | After the model, if the app is the post-call guardrail. |
| `GET /guardrail/health` | Optional. The gateway never calls it. Use it for your own probes. |

The gateway sends `Content-Type: application/json` and no credentials. It reaches the app over the cluster-local network, never through the app's public endpoint.

Return `200` with a verdict for every check, including a block. Any other status is a [guardrail failure](./_index#when-a-guardrail-fails), not a block.

## Request

Both endpoints receive the same envelope. Ignore fields you don't recognize, because the gateway may add new ones.

| Field | Type | Meaning |
|---|---|---|
| `request_id` | string | The gateway's ID for the call. The same on the pre-call and post-call checks of one call. |
| `stage` | string | `pre` or `post`. |
| `virtual_key` | object | `{"id": ..., "name": ...}` of the caller's virtual key. |
| `provider` | string | The provider the call is routed to, for example `openai`. |
| `model` | string | The model, without the provider prefix, for example `gpt-4.1-mini`. |
| `request_type` | string | `chat_completion`, `text_completion`, `responses`, or, on the pre-call stage only, `decisions`. |
| `stream` | boolean | Whether the caller asked for a streamed answer. |
| `input.messages` | array | The conversation as `{"role", "content"}` objects, with `content` flattened to text. Empty on the post-call stage. |
| `output` | object | The model's answer. Post-call stage only. See below. |
| `metadata` | object | The caller's `x-un-dim-<name>` header values, keyed by `<name>`. |

`output` has these fields:

| Field | Type | Meaning |
|---|---|---|
| `content` | string | The answer text. For a streamed answer, the full accumulated text. |
| `finish_reason` | string | The model's finish reason, for example `stop`. |
| `response` | object | The full OpenAI `chat.completion` object. Non-streamed chat completions only. |
| `truncated` | boolean | `true` if a streamed answer outgrew the gateway's buffer and `content` is a prefix. |

How inputs become messages:

- Chat content blocks are joined with newlines.
- A text completion becomes one `user` message.
- A Responses API input maps each item's text to a message.
- A decision becomes a `system` message holding its questions as JSON, followed by a `user` message holding its state.

A pre-call request:

```json
{
  "request_id": "b3f4c2d1",
  "stage": "pre",
  "virtual_key": {"id": "vk_7d2a", "name": "support-bot"},
  "provider": "openai",
  "model": "gpt-4.1-mini",
  "request_type": "chat_completion",
  "stream": false,
  "input": {
    "messages": [
      {"role": "system", "content": "You are a support assistant."},
      {"role": "user", "content": "What is our refund window?"}
    ]
  },
  "metadata": {"team": "support"}
}
```

A post-call request:

```json
{
  "request_id": "b3f4c2d1",
  "stage": "post",
  "virtual_key": {"id": "vk_7d2a", "name": "support-bot"},
  "provider": "openai",
  "model": "gpt-4.1-mini",
  "request_type": "chat_completion",
  "stream": true,
  "input": {"messages": []},
  "output": {"content": "Refunds are accepted within 30 days.", "finish_reason": "stop"},
  "metadata": {"team": "support"}
}
```

## Verdict

| Field | Type | Meaning |
|---|---|---|
| `decision` | string | `pass`, `fail`, or, on the pre-call stage only, `cache_hit`. Required. |
| `message` | string | On `fail`, the message shown to the caller. Not recorded. Defaults to `Request blocked by guardrail`. |
| `reason` | string | On `fail`, a short label recorded with the request's usage. Must match `^[a-z0-9_-]{1,64}$`. Any other value is dropped. Never put user content in it. |
| `response` | object | On `cache_hit`, the answer to return, as an OpenAI `chat.completion` object. |

```json
{"decision": "pass"}
```

```json
{"decision": "fail", "message": "Remove the email address and try again.", "reason": "pii_email"}
```

```json
{
  "decision": "cache_hit",
  "response": {
    "choices": [
      {"index": 0, "finish_reason": "stop", "message": {"role": "assistant", "content": "Refunds are accepted within 30 days."}}
    ]
  }
}
```

The gateway fills in `id`, `object`, `model`, `created`, and an empty `usage` if the `cache_hit` response leaves them out, so `choices[0].message` is the minimum.

Rules:

- `cache_hit` is honored for chat completions only. For other request types it counts as `pass`.
- A `cache_hit` response the gateway can't use is ignored, and the call proceeds to the model.
- A missing, empty, or unknown `decision` is a guardrail failure.
- The response body may be at most 4 MiB.
- The gateway waits for the registered timeout: 5 seconds by default, at most 30 seconds.

## Example: a guardrail in Go

This guardrail refuses prompts that contain an AWS access key ID:

```go
package main

import (
	"encoding/json"
	"net/http"
	"regexp"
)

var awsKey = regexp.MustCompile(`\bAKIA[0-9A-Z]{16}\b`)

type message struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

type request struct {
	Stage string `json:"stage"`
	Input struct {
		Messages []message `json:"messages"`
	} `json:"input"`
}

type verdict struct {
	Decision string `json:"decision"`
	Message  string `json:"message,omitempty"`
	Reason   string `json:"reason,omitempty"`
}

func pre(w http.ResponseWriter, r *http.Request) {
	var req request
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	v := verdict{Decision: "pass"}
	for _, m := range req.Input.Messages {
		if awsKey.MatchString(m.Content) {
			v = verdict{Decision: "fail", Message: "Prompts may not contain AWS keys.", Reason: "aws_key"}
			break
		}
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(v)
}

func main() {
	http.HandleFunc("POST /guardrail/pre", pre)
	http.HandleFunc("GET /guardrail/health", func(w http.ResponseWriter, _ *http.Request) {
		w.Write([]byte(`{"status":"ok"}`))
	})
	http.ListenAndServe(":8080", nil)
}
```

## Deploy a guardrail in any language

Build the server into a container image, then deploy it as an app of type `Guardrail`. The type is what makes the app selectable as a guardrail in the console:

```python
import flyte
import flyte.app

env = flyte.app.AppEnvironment(
    name="aws-key-guardrail",
    type="Guardrail",
    image="<your-registry>/aws-key-guardrail:1.0.0",
    # The server's start command inside the image. Set it, because the image doesn't contain flyte.
    command=["/usr/local/bin/aws-key-guardrail"],
    port=8080,
    scaling=flyte.app.Scaling(replicas=(1, 4)),
)
```

```bash
flyte deploy guardrail_app.py env
```

Deploy it on the gateway's cluster, then [register it](./_index#register-a-guardrail).
