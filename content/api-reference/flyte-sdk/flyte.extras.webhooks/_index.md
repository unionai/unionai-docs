---
title: flyte.extras.webhooks
description: "Receive SaaS webhooks in Flyte, and turn them into runs."
icon: box-seam
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# flyte.extras.webhooks

Receive SaaS webhooks in Flyte, and turn them into runs.

This package holds the product-agnostic machinery, so each
`flyteplugins-<product>` plugin stays thin and consistent:

- `WebhookAppEnvironment` — one app serving a dashboard and a verified receiver
  at `/webhook/{provider}`, for whichever providers you hand it.
- `Provider` — the contract a plugin implements: which env var holds its secret
  (`default_secret_env`, which the app mounts for you), how to verify a
  delivery, how to parse one into an event.
- `WebhookEvent` — the normalized event every provider parses into, so handlers
  and dedupe keys work the same regardless of which product sent it.
- `run_once` — launch a run once per event key. Webhook senders retry on
  any non-2xx and operators re-trigger by hand; this makes that safe.
- `EventType` — base for the typed event constants each plugin ships.
- `flyte.extras.webhooks.testing` — `assert_provider_conforms`, the
  CI-enforced conformance check every plugin runs.

Serving the app needs `fastapi` and `uvicorn`, which flyte keeps as the `app`
extra rather than as runtime dependencies — importing this package never
requires them; only building the app does.

The division of labor: core owns the app, dispatch, dedupe, and the verification
primitives that are easy to get subtly wrong; a plugin owns only what is
specific to its product.

```python
import flyte
from flyte.extras.webhooks import WebhookAppEnvironment, run_once
from flyteplugins.github import GitHubProvider
from flyteplugins.github import events

app_env = WebhookAppEnvironment(name="saas-webhooks", providers=[GitHubProvider()])


@app_env.on_event(events.PullRequest.OPENED)
async def triage(event):
    import flyte.remote as remote

    task = remote.Task.get(name="github-triage.triage_pr", auto_version="latest")
    result = await run_once.aio(task, key=event.dedupe_key(), repo=event.scope)
    if not result.created:
        return {"skipped": result.run.name, "url": result.run.url}
    return {"run": result.run.name}
```
## Directory

### Classes

| Class | Description |
|-|-|
| [`EventType`](../flyte.extras.webhooks/eventtype) | Base for event constants: a real `str`, usable anywhere a pattern is. |
| [`Provider`](../flyte.extras.webhooks/provider) | Everything core needs to accept one product's webhooks. |
| [`RunOnceResult`](../flyte.extras.webhooks/runonceresult) | The run covering a dedupe key, and whether this call created it. |
| [`WebhookAppEnvironment`](../flyte.extras.webhooks/webhookappenvironment) | Dashboard plus a verified webhook receiver for one or more providers. |
| [`WebhookEvent`](../flyte.extras.webhooks/webhookevent) | One inbound webhook, normalized across providers. |

### Errors

| Exception | Description |
|-|-|
| [`SignatureError`](../flyte.extras.webhooks/signatureerror) | Raised when an inbound delivery fails verification or cannot be parsed. |
| [`WebhookPluginError`](../flyte.extras.webhooks/webhookpluginerror) | Base class for all errors raised by this plugin. |

### Methods

| Method | Description |
|-|-|
| [`blocking_run()`](#blocking_run) | Return the run that blocks this key, or None. |
| [`constant_time_equals()`](#constant_time_equals) | Compare two credentials in constant time, without raising. |
| [`hex_hmac_sha256()`](#hex_hmac_sha256) | Hex HMAC-SHA256 of the raw body — the scheme most products use. |
| [`json_body()`](#json_body) | Parse a JSON body into a dict, raising `SignatureError` when it is not one. |
| [`lower_headers()`](#lower_headers) | Lowercase header keys, since HTTP header names are case-insensitive. |
| [`run_once()`](#run_once) | Launch `task` once for `key`, returning the run that covers it. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DUPE_LABEL_KEY` | `str` |  |

## Methods

#### blocking_run()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await blocking_run.aio()`.
```python
def blocking_run(
    key: str,
) -> Any
```
Return the run that blocks this key, or None.

A key is blocked while any run carrying its label is live or succeeded.

Call `blocking_run(key)` from sync code, or `await blocking_run.aio(key)`
from an async handler.



| Parameter | Type | Description |
|-|-|-|
| `key` | `str` | The dedupe key to look up. |

**Returns:** The blocking `flyte.remote.Run`, or None when the key is free.

#### constant_time_equals()

```python
def constant_time_equals(
    a: str,
    b: str,
) -> bool
```
Compare two credentials in constant time, without raising.

Always compares bytes. `hmac.compare_digest` raises `TypeError` on `str`
operands containing non-ASCII, and these values come off the wire — ASGI
servers hand Starlette raw header bytes, which it decodes as latin-1, so a
crafted header would otherwise turn a clean 401 into a 500.


| Parameter | Type | Description |
|-|-|-|
| `a` | `str` | |
| `b` | `str` | |

#### hex_hmac_sha256()

```python
def hex_hmac_sha256(
    secret: str,
    body: bytes,
) -> str
```
Hex HMAC-SHA256 of the raw body — the scheme most products use.


| Parameter | Type | Description |
|-|-|-|
| `secret` | `str` | |
| `body` | `bytes` | |

#### json_body()

```python
def json_body(
    body: bytes,
) -> dict[str, Any]
```
Parse a JSON body into a dict, raising `SignatureError` when it is not one.


| Parameter | Type | Description |
|-|-|-|
| `body` | `bytes` | |

#### lower_headers()

```python
def lower_headers(
    headers: Mapping[str, str],
) -> dict[str, str]
```
Lowercase header keys, since HTTP header names are case-insensitive.


| Parameter | Type | Description |
|-|-|-|
| `headers` | `Mapping[str, str]` | |

#### run_once()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await run_once.aio()`.
```python
def run_once(
    task: Any,
    key: str,
    copy_style: CopyFiles | None = None,
    runcontext_kwargs: dict[str, Any] | None = None,
    **inputs: Any,
) -> RunOnceResult
```
Launch `task` once for `key`, returning the run that covers it.

**Use `await run_once.aio(...)` inside an async handler.** The
synchronous form blocks the calling thread until the launch completes; on an
app's event loop that stalls every other in-flight request, and webhook
senders time deliveries out in seconds.



| Parameter | Type | Description |
|-|-|-|
| `task` | `Any` | The task to launch — either a `flyte.remote.Task` looked up by name, or a local `TaskEnvironment` task object. |
| `key` | `str` | Stable dedupe key for the triggering event. Any string works: the key *is* the dedupe scope, so choose it to match what "the same event" means for your workflow. |
| `copy_style` | `CopyFiles \| None` | Pass `"all"` when `task` is a local task object so the whole module tree is bundled. Leave as None when launching a `remote.Task` by name, which needs no bundle. |
| `runcontext_kwargs` | `dict[str, Any] \| None` | Forwarded to `flyte.with_runcontext`, for anything else the run needs — `env_vars`, `queue`, `interruptible`, `service_account`, `notifications`, and so on: ```python await run_once.aio(     task,     key=event.dedupe_key(),     runcontext_kwargs={"queue": "webhooks", "labels": {"team": "platform"}}, ) ``` Labels merge with the `dedupe` label rather than replacing it, so extra labels are fine — but setting `dedupe` yourself is not, since it is what makes the launch unique. |
| `**inputs` | `Any` | |

**Returns**

A `RunOnceResult` pairing the run that covers `key` with a `created`
flag: True when this call launched it, False when a live or succeeded
run already carried the key and is returned instead. Names of launched
runs are assigned by the control plane.


**Raises**

| Exception | Description |
|-|-|
| `ValueError` | when `runcontext_kwargs` sets `dedupe` to something other than `key`, or passes `copy_style` alongside the argument. |

