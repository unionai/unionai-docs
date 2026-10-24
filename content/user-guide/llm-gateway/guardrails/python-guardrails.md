---
title: Python guardrails
description: Write an LLM Gateway guardrail as a Python function with GuardrailAppEnvironment.
icon: code
weight: 1
variants: -flyte +union
---

# Python guardrails

`GuardrailAppEnvironment` turns a Python function into a guardrail app. You write a function that takes the request and returns a verdict. The class serves the HTTP endpoints the gateway calls, and gives the app the `Guardrail` type the console looks for.

## Install

```bash
pip install 'flyteplugins-union[guardrails]'
```

The `guardrails` extra adds FastAPI and uvicorn.

## Write a pre-call guardrail

This guardrail refuses prompts that contain a Social Security number or an email address, and answers one known question from a cache:

{{< code file="/unionai-examples/v2/user-guide/llm-gateway/pii_guardrail.py" fragment=checks lang=python >}}

A check receives a `GuardrailRequest` and returns a `Verdict`:

| Return | Effect |
|---|---|
| `Verdict.allow()` | The call proceeds. |
| `Verdict.block(message, reason)` | The caller gets `403` `guardrail_blocked` with `message`. `reason` is a short label recorded with the request's usage. |
| `Verdict.cached(content)` | The caller gets `content` as the model's answer, and the model is never called. Pre-call stage only. |

`reason` must be lowercase letters, digits, `_`, or `-`, up to 64 characters, for example `pii_ssn`. It is recorded, so it must never contain user content. `Verdict.block()` raises `ValueError` for any other value. `message` is shown to the caller and is not recorded.

`GuardrailRequest` carries the fields described in the [guardrail protocol](./protocol#request), plus two helpers:

- `last_user_message()` returns the most recent `user` message.
- `text()` returns the text the stage is about: all message content on the pre-call stage, the model's answer on the post-call stage.

## Deploy it

Wrap the check in a `GuardrailAppEnvironment`:

{{< code file="/unionai-examples/v2/user-guide/llm-gateway/pii_guardrail.py" fragment=env lang=python >}}

`GuardrailAppEnvironment` accepts every `flyte.app.AppEnvironment` option, such as `resources`, `scaling`, `secrets`, and `image`. The default image installs `flyteplugins-union[guardrails]`. If your checks need more packages, pass your own image and include `flyteplugins-union[guardrails]` in it.

Deploy it on the gateway's cluster:

```bash
flyte deploy pii_guardrail.py env
```

Then [register it](./_index#register-a-guardrail) in **Settings → LLM Gateway → Guardrails** as the pre-call guardrail.

Leave `requires_auth` at its default. The gateway reaches the app over the cluster-local network and never goes through the app's public endpoint.

## Check answers after the model

Pass a `post` function to check the model's answer. One app can serve both stages. Checks can be `async`:

{{< code file="/unionai-examples/v2/user-guide/llm-gateway/post_guardrail.py" fragment=checks lang=python >}}

Register the app under both stages to use both checks. A stage with no function returns pass.

## Add guardrail routes to an existing FastAPI app

If you already run a FastAPI app, mount the guardrail routes on it with `guardrail_router()`, and give the environment the `Guardrail` type:

{{< code file="/unionai-examples/v2/user-guide/llm-gateway/fastapi_guardrail.py" fragment=router lang=python >}}

`GuardrailAppEnvironment` also accepts an existing app, as `app=`, and adds the routes to it.

## Test locally

The guardrail is an ordinary FastAPI app, so you can test it without deploying, using FastAPI's test client:

```python
from fastapi.testclient import TestClient

from pii_guardrail import env

client = TestClient(env.app)
verdict = client.post(
    "/guardrail/pre",
    json={"stage": "pre", "input": {"messages": [{"role": "user", "content": "My SSN is 123-45-6789"}]}},
).json()
assert verdict["decision"] == "fail"
```
