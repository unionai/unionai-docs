---
title: GitLab
description: Receive GitLab webhooks as Flyte runs, authenticated with a shared token.
icon: git
weight: 6
variants: +flyte +union
---

# GitLab

Receive GitLab webhooks in Flyte and turn them into runs.

The plugin authenticates deliveries with the webhook's secret token, a shared token rather than a signature. Read [Authentication](#authentication) before you expose the route.

## Installation

```bash
pip install "flyteplugins-gitlab[app]"
```

Requires Python 3.10 or later. The `app` extra adds `fastapi` and `uvicorn` for serving the receiver. The `gitlab` extra adds `python-gitlab` for calling the GitLab API from your tasks; the plugin itself doesn't use it.

## Authentication

The provider compares the `X-Gitlab-Token` header against the stored token, using a constant-time comparison. A delivery with a missing or wrong token is rejected with a 401. `GitLabProvider` reports `signed=False`, and the setup dashboard shows the route as verified by a shared token, not a signature.

A shared token is weaker than a signature:

- The same token is sent with every request. Anyone who obtains it can forge deliveries.
- It doesn't cover the body. Anything between GitLab and the app can change the payload undetected.

This plugin doesn't support GitLab's signing-token mode. Set a secret token on the webhook instead.

> [!WARNING] Don't disable verification in production
> Setting `require_signature=False` makes the route launch runs for any request. Use it only for local development.

Set a narrow `scopes` allowlist as well.

## The receiver

Pass `GitLabProvider()` to a `WebhookAppEnvironment`, as in the [quick start](./_index#quick-start), and register handlers with the constants in `flyteplugins.gitlab.events`.

The provider reads the token from `GITLAB_WEBHOOK_TOKEN`, which the app mounts automatically. Generate a token and store it under that name:

```bash
flyte create secret GITLAB_WEBHOOK_TOKEN --value "$(openssl rand -hex 32)"
```

### Set up the webhook in GitLab

In your GitLab project's webhook settings, add a webhook with:

1. The URL: the `/webhook/gitlab` URL from the app's dashboard.
2. The secret token: the token you stored in `GITLAB_WEBHOOK_TOKEN`.
3. The events your handlers match.

## Events

Constants live in `flyteplugins.gitlab.events`. The event type is the payload's `object_kind`. The action is `object_attributes.action`, except for pipelines and deployments, where it is the `status`. Release and deployment hooks have no `object_attributes`: GitLab sends their fields at the top level of the payload.

| Class | Members |
|---|---|
| `MergeRequest` | `OPEN`, `CLOSE`, `REOPEN`, `UPDATE`, `APPROVAL`, `APPROVED`, `UNAPPROVAL`, `UNAPPROVED`, `MERGE` |
| `Issue` | `OPEN`, `CLOSE`, `REOPEN`, `UPDATE` |
| `Note` | `ANY` only. Comments carry no action |
| `Push` | `ANY` only |
| `TagPush` | `ANY` only |
| `Pipeline` | `CREATED`, `WAITING_FOR_RESOURCE`, `PREPARING`, `PENDING`, `RUNNING`, `SUCCESS`, `FAILED`, `CANCELED`, `SKIPPED`, `MANUAL`, `SCHEDULED` |
| `Release` | `CREATE`, `UPDATE` |
| `Deployment` | `RUNNING`, `SUCCESS`, `FAILED`, `CANCELED` |

Every class also has `ANY`, which matches all actions of that type. For example, `MergeRequest.OPEN` is `merge_request.open`, and `Pipeline.SUCCESS` is `pipeline.success`.

`flyteplugins.gitlab.payloads` has `TypedDict` views of the payloads, for editor autocomplete in handlers.

### Scope and deduplication

`scope` is the project's `path_with_namespace`, such as `octo/repo`. `resource_id` follows GitLab's own notation:

| Event | `resource_id` |
|---|---|
| Merge request | `octo/repo!7` |
| Issue | `octo/repo#7` |
| Comment | On a merge request or issue, the parent's ID plus the note ID, such as `octo/repo!7:5` or `octo/repo#7:5`, so two comments on one thread get different keys. On a commit or snippet, `None`, so it deduplicates on `X-Gitlab-Event-UUID` |
| Pipeline | `octo/repo/-/pipelines/42` |
| Deployment | `octo/repo/-/deployments/3` |
| Release | `octo/repo/-/releases/v1.0` |
| Push, tag push | `None`, so `event.dedupe_key()` uses the delivery's `X-Gitlab-Event-UUID` |

For a comment, `title` is the parent merge request's or issue's title. For a release it's the release name, and for a deployment it's the environment.

## Test without a GitLab account

`flyteplugins.gitlab` exports a `SAMPLE_DELIVERY`, a recorded merge-request delivery. The plugin's [`gitlab_webhooks.py`](https://github.com/flyteorg/flyte-sdk/blob/v2.11.4/plugins/gitlab/examples/gitlab_webhooks.py) example replays it through the app in-process:

```bash
python gitlab_webhooks.py --local
```

The replay posts the sample twice, showing the same `dedupe_key` both times, and then posts it with a wrong token, which the app refuses with a 401.

## See also

- [Software development tools](./_index) for the event model, `run_once`, and scopes.
- [Event-driven automation](../../user-guide/software-development-lifecycle/event-driven-automation) for the pattern across ticketing and source-control events.
