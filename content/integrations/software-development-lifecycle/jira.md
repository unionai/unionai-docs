---
title: Jira
description: Receive Jira Cloud webhooks as Flyte runs — and what to put in front of them, since Jira does not sign.
icon: journal-text
weight: 5
variants: +flyte +union
---

# Jira

Receive [Jira Cloud](https://developer.atlassian.com/cloud/jira/platform/webhooks/) webhooks in Flyte and turn them into runs. See [Software development lifecycle](./_index) for the shared model this builds on.

Read the authentication section before exposing the route. Jira is the one provider in this family that does not sign its webhooks, and that changes what you have to do.

## Installation

```bash
pip install "flyteplugins-jira[app]"
```

Requires Python 3.10 or later. The `app` extra pulls in `fastapi` and `uvicorn` for serving the receiver.

## Authentication: Jira does not sign

Every other provider here signs its deliveries with an HMAC, so the receiver can prove a payload came from the product and was not altered. **Jira Cloud sends no signature at all.**

So this plugin authenticates with a shared token in an `X-Webhook-Token` header, compared in constant time. `JiraProvider` reports `signed=False`, which is what makes the setup dashboard say so plainly rather than implying a guarantee that is absent.

That substitution is weaker in two specific ways, and both are worth stating:

- **A shared token travels on every request** rather than signing one. Anything that has ever seen it can replay or forge a delivery.
- **It does not cover the body.** A proxy or anything in the path could alter the payload without detection.

> [!WARNING] Jira cannot send custom headers, so something in front must inject one
> A plain Jira webhook has no way to add `X-Webhook-Token`. You need one of:
>
> - **An API gateway or ingress rule** in front of the app that injects the header on requests from Jira's address range, or
> - **A Jira Automation rule** using *Send web request*, which **can** set custom headers — and is the simplest route if your events are expressible as automation triggers.
>
> Without one of these, deliveries will be refused ( is the default, and the right default). Do not reach for `require_signature=False` to make them flow — that turns the route into an unauthenticated run-launcher. It exists for local development.

Combine the token with a narrow `scopes` allowlist, and treat the proxy as part of the auth story rather than an extra.

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/jira/jira_webhooks.py" fragment=app lang=python >}}

`JIRA_WEBHOOK_TOKEN` is mounted for you from the provider's `default_secret_env`. Generate a long random value yourself — unlike the other providers, there is nothing on Jira's side that issues it:

```bash
flyte create secret jira-webhook-token --value "$(openssl rand -hex 32)"
```

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/jira/jira_webhooks.py" fragment=handler lang=python >}}

### Setting up the webhook in Jira

**Settings → System → Webhooks → Create a WebHook**:

1. **URL** — the `/webhook/jira` URL from the app's dashboard.
2. **Events** — select the events your handlers match, and optionally a JQL filter.
3. Configure whatever sits in front of the app to inject `X-Webhook-Token`.

## Events

Constants live in `flyteplugins.jira.events`. Note that Jira namespaces some event names (`jira:issue_created`) and not others (`comment_created`) — the constants hide that inconsistency.

| Class | Members |
|---|---|
| `Issue` | `CREATED`, `UPDATED`, `DELETED` |
| `Comment` | `CREATED`, `UPDATED`, `DELETED` |
| `Worklog` | `CREATED`, `UPDATED`, `DELETED` |
| `Project` | `CREATED`, `UPDATED`, `DELETED` |
| `Version` | `CREATED`, `UPDATED`, `RELEASED`, `UNRELEASED`, `DELETED` |
| `Sprint` | `CREATED`, `UPDATED`, `STARTED`, `CLOSED`, `DELETED` |

### How events are scoped and deduped

`scope` is the **project key** (`PROJ`), which is what `scopes=` matches. `resource_id` is the **issue key** (`PROJ-1`) — the stable handle the Jira API takes, and unlike the numeric id, the one a human reads too. `occurred_at` is Jira's own `timestamp`.

## The task it launches

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/jira/jira_tasks.py" fragment=task lang=python >}}

Two things generalize here:

- **Transitions are resolved by name, not by a hard-coded id.** Transition ids are per-workflow, so a hard-coded one breaks the first time somebody edits the project's workflow — in a way that surfaces as a confusing API error rather than as "the workflow changed".
- **The `jira` client is synchronous**, so it runs through `asyncio.to_thread` to stay off the event loop.

Credentials are an Atlassian account email plus an [API token](https://id.atlassian.com/manage-profile/security/api-tokens), used as HTTP basic auth.

## Try it without a Jira site

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/jira/jira_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local jira_tasks.py replay_sample_delivery
```

Note what `verify` is doing in that replay: comparing a shared token, not checking a signature. The returned `provider_signs_deliveries` is `False`.

## Examples

Both files live in [`v2/integrations/flyte-plugins/jira`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/jira):

- `jira_webhooks.py` — the receiver and an issue-created handler.
- `jira_tasks.py` — commenting and transitioning, and the offline replay.

## See also

- [Software development lifecycle](./_index) for the shared model: the normalized event, `run_once`, and scoping.
- [Jira API reference](../../api-reference/integrations/software-development-lifecycle/jira/_index).
