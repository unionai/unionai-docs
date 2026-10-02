---
title: GitHub
description: Receive GitHub webhooks as Flyte runs, gate a merge on a human decision, and mint short-lived GitHub App tokens.
icon: github
weight: 1
variants: +flyte +union
---

# GitHub

Receive [GitHub webhooks](https://docs.github.com/en/webhooks) in Flyte and turn them into runs. The plugin also provides a human review gate for pull requests and GitHub App token minting.

## Installation

```bash
pip install "flyteplugins-github[app]"
```

Requires Python 3.10 or later. Install only the extras you use:

| Extra | Adds | Needed for |
|---|---|---|
| `app` | `fastapi`, `uvicorn` | Serving the receiver |
| `review` | `PyGithub` | `review_pr` and `collect_review_context` |
| `auth` | `PyJWT[crypto]` | `mint_installation_token` |

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=app lang=python >}}

The provider reads its secret from `GITHUB_WEBHOOK_SECRET`, which the app mounts automatically.

Register a handler against an event constant, and launch a run with `run_once`:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=handler lang=python >}}

Serve the app, then copy the payload URL from the dashboard:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_webhooks.py" fragment=serve lang=python >}}

### Set up the webhook in GitHub

In the repository, go to **Settings → Webhooks → Add webhook** and set:

1. **Payload URL**: the `/webhook/github` URL from the app's dashboard.
2. **Secret**: the value you stored as the `github-webhook-secret` Flyte secret.
3. **Content type**: either option works. The provider handles `application/json` and the default `application/x-www-form-urlencoded` identically.
4. **Events**: the events your handlers match.

GitHub sends a `ping` event when you create the webhook. The provider answers it, so a successful first delivery confirms the URL is reachable.

## Events

Constants live in `flyteplugins.github.events`. Use `.ANY` to match every action on a type, or a specific member to match one action. For an event the constants don't cover, pass the raw string.

| Class | Members |
|---|---|
| `PullRequest` | `ANY`, `OPENED`, `CLOSED`, `REOPENED`, `EDITED`, `ASSIGNED`, `UNASSIGNED`, `LABELED`, `UNLABELED`, `SYNCHRONIZE`, `READY_FOR_REVIEW`, `CONVERTED_TO_DRAFT`, `REVIEW_REQUESTED`, `REVIEW_REQUEST_REMOVED`, `LOCKED`, `UNLOCKED` |
| `Issues` | `ANY`, `OPENED`, `CLOSED`, `REOPENED`, `EDITED`, `ASSIGNED`, `UNASSIGNED`, `LABELED`, `UNLABELED`, `MILESTONED`, `DEMILESTONED`, `PINNED`, `UNPINNED`, `LOCKED`, `UNLOCKED`, `TRANSFERRED`, `DELETED` |
| `IssueComment` | `ANY`, `CREATED`, `EDITED`, `DELETED` |
| `PullRequestReview` | `ANY`, `SUBMITTED`, `EDITED`, `DISMISSED` |
| `PullRequestReviewComment` | `ANY`, `CREATED`, `EDITED`, `DELETED` |
| `Push`, `Create`, `Delete`, `Fork` | `ANY` only. GitHub sends no action for these. |
| `Release` | `ANY`, `PUBLISHED`, `UNPUBLISHED`, `CREATED`, `EDITED`, `DELETED`, `PRERELEASED`, `RELEASED` |
| `WorkflowRun` | `ANY`, `REQUESTED`, `IN_PROGRESS`, `COMPLETED` |
| `CheckRun` | `ANY`, `CREATED`, `COMPLETED`, `REREQUESTED`, `REQUESTED_ACTION` |
| `CheckSuite` | `ANY`, `COMPLETED`, `REQUESTED`, `REREQUESTED` |
| `Installation` | `ANY`, `CREATED`, `DELETED`, `SUSPEND`, `UNSUSPEND`, `NEW_PERMISSIONS_ACCEPTED` |
| `InstallationRepositories` | `ANY`, `ADDED`, `REMOVED` |
| `Star` | `ANY`, `CREATED`, `DELETED` |

`Issues` is plural to match GitHub's event name.

`PullRequest.CLOSED` fires both when a pull request is merged and when it's closed without merging. Check `event.payload["pull_request"]["merged"]` to tell them apart.

### Scope and deduplication

`scope` is the repository's `full_name`, such as `octo/repo`. `resource_id` is `owner/repo#number`, with the comment or review ID appended when there is one, so separate comments on one issue get separate dedupe keys.

## The tasks it launches

Call GitHub from a task with `PyGithub`:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=task lang=python >}}

The token the task uses to read the pull request is a separate credential from the webhook secret. Mount it on the task environment, not the app.

## Human review gates

`review_pr` pauses a run until a person reviews a pull request in the Flyte UI, then returns their decision. It creates a `flyte.new_condition` carrying the pull request's metadata and waits on it.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=review-gate lang=python >}}

The condition is stored on the backend, so the run can wait for days and survives restarts.

`review_pr` returns a `ReviewDecision`:

| Field | Type | Description |
|---|---|---|
| `verdict` | `"approve" \| "request_changes" \| "comment"` | The reviewer's verdict |
| `summary` | `str` | The reviewer's summary |
| `comments` | `list[ReviewComment]` | Each has `path`, `line`, `body`, and a `severity` of `info`, `warning`, or `blocking` |
| `reviewer` | `str \| None` | Who reviewed |
| `is_approved` | `bool` | `True` when `verdict == "approve"` |
| `blocking_comments` | `list[ReviewComment]` | Comments with `blocking` severity |

`review_pr` also accepts:

- `condition_name`: defaults to a name derived from the repository and pull request number.
- `instructions`: replaces the default reviewer prompt.
- `timeout`: passed to `flyte.new_condition`. On expiry, `wait()` raises `flyte.errors.ConditionTimedoutError`.
- `max_files`: the maximum number of changed files to include.
- `token`: the GitHub token used to read the pull request.

`review_pr` reads the pull request with `PyGithub`, so it requires the `review` extra.

## GitHub App tokens

To clone, push, or open pull requests from a task, authenticate as a GitHub App rather than with a personal access token. `mint_installation_token` creates an installation token that expires after one hour.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=app-token lang=python >}}

Store three values as Flyte secrets:

| Secret | Where to find it |
|---|---|
| `github-app-id` | The app's **General** tab, under **App ID**. Not the Client ID. |
| `github-app-installation-id` | The URL after you install the app: `.../settings/installations/<id>` |
| `github-app-private-key` | The `.pem` file from **Generate a private key**. GitHub shows it only once. |

```bash
flyte create secret github-app-id --value 1234567
flyte create secret github-app-installation-id --value 87654321
flyte create secret github-app-private-key --from-file ~/Downloads/app.private-key.pem
```

Use `--from-file` for the private key. Passing the multi-line PEM through `--value` can lose its newlines, and the mint then fails.

Each secret's key maps to the environment variable the function reads, so you don't need `as_env_var=`. If the App secrets aren't set, the function falls back to `GITHUB_TOKEN` or `GH_TOKEN`.

`mint_installation_token` returns `None` instead of raising when credentials are missing, so check the result before using it. It's synchronous; call it through `asyncio.to_thread` from async code, as in the example.

## Test without a GitHub account

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/github/github_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local github_tasks.py replay_sample_delivery
```

## Examples

Both files are in [`v2/integrations/flyte-plugins/github`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/github):

- `github_webhooks.py`: the receiver, its handler, and serving it.
- `github_tasks.py`: size labeling with `PyGithub`, the `review_pr` gate, App token minting, and the offline replay.

## See also

- [Software development tools](./_index) for the event model, `run_once`, and scopes.
- [Review and release gates](../../user-guide/software-development-lifecycle/review-and-release-gates) for what to build on top of this.
- [GitHub API reference](../../api-reference/integrations/software-development-tools/github/_index).
