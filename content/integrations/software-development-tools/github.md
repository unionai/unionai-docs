---
title: GitHub
description: Receive GitHub webhooks as Flyte runs, gate a merge on a human decision, and mint short-lived GitHub App tokens.
icon: github
weight: 1
variants: +flyte +union
---

# GitHub

Receive [GitHub webhooks](https://docs.github.com/en/webhooks) in Flyte and turn them into runs. This is the richest of these integrations because it carries two things beyond the webhook provider — a human review gate and GitHub App authentication — both in places where Flyte can do something `PyGithub` cannot.

## Installation

```bash
pip install "flyteplugins-github[app]"
```

Requires Python 3.10 or later. Three extras, kept apart so a webhook-only install stays lean:

| Extra | Pulls in | Needed for |
|---|---|---|
| `app` | `fastapi`, `uvicorn` | Serving the receiver app |
| `review` | `PyGithub` | `review_pr` and `collect_review_context` |
| `auth` | `PyJWT[crypto]` | `mint_installation_token` |

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=app lang=python >}}

`GITHUB_WEBHOOK_SECRET` is mounted for you from the provider's `default_secret_env`, so it does not need naming again in `secrets=`.

Register a handler against a typed constant, and launch a run with `run_once`:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=handler lang=python >}}

Then serve it and copy the payload URL off the dashboard:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=serve lang=python >}}

### Setting up the webhook in GitHub

Go to the repository's **Settings → Webhooks → Add webhook**, then:

1. **Payload URL** — the `/webhook/github` URL from the app's dashboard.
2. **Secret** — the same value you stored as the `github-webhook-secret` Flyte secret.
3. **Content type** — either works. `application/json` and the default `application/x-www-form-urlencoded` (which wraps the JSON in a `payload=` form field) normalize identically, because the HMAC signs the raw body regardless of encoding. A webhook left on the default is not a bug you need to find.
4. **Events** — choose individual events matching the handlers you registered.

GitHub sends a `ping` when the webhook is created. The provider answers it automatically, so a green first delivery means verification is working.

## Events

Constants live in `flyteplugins.github.events`. Use `.ANY` to match every action on a type, or a specific member to match one.

| Class | Members |
|---|---|
| `PullRequest` | `ANY`, `OPENED`, `CLOSED`, `REOPENED`, `EDITED`, `ASSIGNED`, `UNASSIGNED`, `LABELED`, `UNLABELED`, `SYNCHRONIZE`, `READY_FOR_REVIEW`, `CONVERTED_TO_DRAFT`, `REVIEW_REQUESTED`, `REVIEW_REQUEST_REMOVED`, `LOCKED`, `UNLOCKED` |
| `Issues` | `ANY`, `OPENED`, `CLOSED`, `REOPENED`, `EDITED`, `ASSIGNED`, `UNASSIGNED`, `LABELED`, `UNLABELED`, `MILESTONED`, `DEMILESTONED`, `PINNED`, `UNPINNED`, `LOCKED`, `UNLOCKED`, `TRANSFERRED`, `DELETED` |
| `IssueComment` | `ANY`, `CREATED`, `EDITED`, `DELETED` |
| `PullRequestReview` | `ANY`, `SUBMITTED`, `EDITED`, `DISMISSED` |
| `PullRequestReviewComment` | `ANY`, `CREATED`, `EDITED`, `DELETED` |
| `Push`, `Create`, `Delete`, `Fork` | `ANY` only — GitHub sends no action for these |
| `Release` | `ANY`, `PUBLISHED`, `UNPUBLISHED`, `CREATED`, `EDITED`, `DELETED`, `PRERELEASED`, `RELEASED` |
| `WorkflowRun` | `ANY`, `REQUESTED`, `IN_PROGRESS`, `COMPLETED` |
| `CheckRun` | `ANY`, `CREATED`, `COMPLETED`, `REREQUESTED`, `REQUESTED_ACTION` |
| `CheckSuite` | `ANY`, `COMPLETED`, `REQUESTED`, `REREQUESTED` |
| `Installation` | `ANY`, `CREATED`, `DELETED`, `SUSPEND`, `UNSUSPEND`, `NEW_PERMISSIONS_ACCEPTED` |
| `InstallationRepositories` | `ANY`, `ADDED`, `REMOVED` |
| `Star` | `ANY`, `CREATED`, `DELETED` |

Note `Issues` is plural, because GitHub's event type is. A raw string still works for anything the constants do not cover yet.

> [!NOTE] `PullRequest.CLOSED` fires on merge *and* on close-without-merge
> Check `event.payload["pull_request"]["merged"]` to tell them apart. This is the single most common surprise in GitHub webhook handling.

### How events are scoped and deduped

`scope` is the repository's `full_name`, which is what `scopes=` matches. `resource_id` is `owner/repo#number`, extended with the comment or review id when there is one — so two comments on one issue do not collapse onto a single dedupe key.

## The tasks it launches

There is no Flyte wrapper around the GitHub API, and that is deliberate: `PyGithub` is the maintained client, and a task is just a function that calls it.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=task lang=python >}}

The PR-reading token is a different credential from the webhook signing secret, and lives on the task environment rather than the app. The app never needs it; the task never needs the signing secret.

## Human review gates

`review_pr` is the one place a plugin beats the vendor SDK outright, because the thing it adds is Flyte's, not GitHub's: it parks a run on a `flyte.new_condition` carrying the pull request's metadata as JSON, waits for a human to answer in the Flyte UI, and returns a typed decision.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=review-gate lang=python >}}

The run survives restarts while it waits, because the condition is durable state on the backend rather than a held-open process. A gate can wait days without holding anything open.

`ReviewDecision` carries:

| Field | Type | Notes |
|---|---|---|
| `verdict` | `"approve" \| "request_changes" \| "comment"` | |
| `summary` | `str` | The reviewer's prose |
| `comments` | `list[ReviewComment]` | Each with `path`, `line`, `body`, and a `severity` of `info`, `warning`, or `blocking` |
| `reviewer` | `str \| None` | |
| `is_approved` | `bool` | Convenience for `verdict == "approve"` |
| `blocking_comments` | `list[ReviewComment]` | Just the `blocking` ones |

`review_pr` also takes `condition_name` (defaults to one derived from the repo and number), `instructions` (overrides the reviewer prompt), `timeout` (forwarded to `flyte.new_condition`; on expiry `wait()` raises `flyte.errors.ConditionTimedoutError`), `max_files`, and `token`.

Reading the pull request is `PyGithub`'s job, and `review_pr` calls it directly rather than wrapping it — hence the `[review]` extra.

## GitHub App tokens

An agent that clones, pushes, or opens pull requests authenticates best as a GitHub App: mint a short-lived installation token per operation instead of holding a personal access token. Tokens live one hour — plenty for a clone or a `gh pr create`, useless to anyone who later finds one in a log.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=app-token lang=python >}}

Three inputs, all injected as Flyte secrets:

| Secret | Where to find it |
|---|---|
| `github-app-id` | The app's **General** tab — *App ID*, not the Client ID beside it |
| `github-app-installation-id` | The URL you land on after installing the app: `.../settings/installations/<id>` |
| `github-app-private-key` | The `.pem` from *Generate a private key*, which GitHub shows exactly once |

```bash
flyte create secret github-app-id --value 1234567
flyte create secret github-app-installation-id --value 87654321
flyte create secret github-app-private-key --from-file ~/Downloads/app.private-key.pem
```

Use `--from-file` for the key. A PEM is multi-line, and a shell that eats the newlines yields a key that parses fine nowhere and fails at mint time, which is a long way from the mistake.

A kebab-case secret key upper-cases into the environment variable the function reads, so no `as_env_var=` is needed. `GITHUB_TOKEN` and `GH_TOKEN` are honored as fallbacks, so a deployment can migrate one secret at a time.

> [!NOTE] `mint_installation_token` returns `None` rather than raising
> `None` means "proceed unauthenticated or not at all", so a half-configured deployment degrades instead of crashing. It is also synchronous — one HTTPS round trip — so call it through `asyncio.to_thread` from async code, as above.

## Try it without a GitHub account

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local github_tasks.py replay_sample_delivery
```

## Examples

Both files live in [`v2/integrations/flyte-plugins/github`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/github):

- `github_webhooks.py` — the receiver app, its handler, and serving it.
- `github_tasks.py` — size labelling with `PyGithub`, the `review_pr` gate, App-token minting, and the offline replay.

## See also

- [Software development tools](./_index) for the shared model: the normalized event, `run_once`, and scoping.
- [Review and release gates](../../user-guide/software-development-lifecycle/review-and-release-gates) for what to build on top of this.
- [GitHub API reference](../../api-reference/integrations/software-development-tools/github/_index).
