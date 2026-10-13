---
title: Jira
description: Receive Jira Cloud webhooks as Flyte runs, authenticated with a shared token.
icon: journal-text
weight: 5
variants: +flyte +union
---

# Jira

Receive [Jira Cloud](https://developer.atlassian.com/cloud/jira/platform/webhooks/) webhooks in Flyte and turn them into runs.

Jira Cloud doesn't sign its webhooks. This plugin authenticates deliveries with a shared token instead, which requires a proxy or a Jira Automation rule to add the token. Read [Authentication](#authentication) before you expose the route.

## Installation

```bash
pip install "flyteplugins-jira[app]"
```

Requires Python 3.10 or later. The `app` extra adds `fastapi` and `uvicorn` for serving the receiver.

## Authentication

The provider checks for a shared token in the `X-Webhook-Token` header, using a constant-time comparison. `JiraProvider` reports `signed=False`, and the setup dashboard shows that the route isn't signature-verified.

A shared token is weaker than a signature:

- The same token is sent with every request. Anyone who obtains it can forge deliveries.
- It doesn't cover the body. Anything between Jira and the app can change the payload undetected.

Jira webhooks can't send custom headers, so you need one of these to add `X-Webhook-Token`:

- An API gateway or ingress rule in front of the app that adds the header to requests from Jira's IP ranges.
- A Jira Automation rule that uses the **Send web request** action, which can set custom headers. This is the simpler option if your events are available as Automation triggers.

Without the header, the app rejects every delivery, because `require_signature` defaults to `True`.

> [!WARNING] Don't disable verification in production
> Setting `require_signature=False` makes the route launch runs for any request. Use it only for local development.

Set a narrow `scopes` allowlist as well.

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/jira/jira_webhooks.py" fragment=app lang=python >}}

The provider reads the token from `JIRA_WEBHOOK_TOKEN`, which the app mounts automatically. Jira doesn't issue this token, so generate one yourself:

```bash
flyte create secret jira-webhook-token --value "$(openssl rand -hex 32)"
```

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/jira/jira_webhooks.py" fragment=handler lang=python >}}

### Set up the webhook in Jira

Go to **Settings → System → Webhooks → Create a WebHook** and set:

1. **URL**: the `/webhook/jira` URL from the app's dashboard.
2. **Events**: the events your handlers match. Optionally, add a JQL filter.

Then configure your proxy or Automation rule to add `X-Webhook-Token`.

## Events

Constants live in `flyteplugins.jira.events`. Jira prefixes some event names (`jira:issue_created`) but not others (`comment_created`); the constants handle both.

| Class | Members |
|---|---|
| `Issue` | `CREATED`, `UPDATED`, `DELETED` |
| `Comment` | `CREATED`, `UPDATED`, `DELETED` |
| `Worklog` | `CREATED`, `UPDATED`, `DELETED` |
| `Project` | `CREATED`, `UPDATED`, `DELETED` |
| `Version` | `CREATED`, `UPDATED`, `RELEASED`, `UNRELEASED`, `DELETED` |
| `Sprint` | `CREATED`, `UPDATED`, `STARTED`, `CLOSED`, `DELETED` |

### Scope and deduplication

`scope` is the project key, such as `PROJ`. `resource_id` is the issue key, such as `PROJ-1`. `occurred_at` is Jira's `timestamp` field.

## The task it launches

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/jira/jira_tasks.py" fragment=task lang=python >}}

The example looks up transitions by name rather than by ID. Transition IDs differ between workflows, so a hard-coded ID breaks when someone edits the project's workflow.

The `jira` client is synchronous, so the example calls it through `asyncio.to_thread` to avoid blocking the event loop.

Authenticate with an Atlassian account email and an [API token](https://id.atlassian.com/manage-profile/security/api-tokens), using HTTP basic auth.

## Test without a Jira site

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/jira/jira_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local jira_tasks.py replay_sample_delivery
```

In this replay, `verify` compares the shared token; there's no signature to check. The output's `provider_signs_deliveries` is `False`.

## Examples

Both files are in [`v2/integrations/flyte-plugins/jira`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/jira):

- `jira_webhooks.py`: the receiver and an issue-created handler.
- `jira_tasks.py`: commenting, transitioning, and the offline replay.

## See also

- [Software development tools](./_index) for the event model, `run_once`, and scopes.
- [Event-driven automation](../../user-guide/software-development-lifecycle/event-driven-automation) for the pattern across Linear, Jira, and ClickUp.
- [Jira API reference](../../api-reference/integrations/software-development-tools/jira/_index).
