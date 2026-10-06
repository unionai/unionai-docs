---
title: GitHub
description: "GitHub webhooks for Flyte."
icon: book
version: 2.11.0
variants: +flyte +union
layout: py_api
---

# GitHub



GitHub webhooks for Flyte.

Hand a `GitHubProvider()` to a `WebhookAppEnvironment` and register handlers with the
typed constants in `events`:

```python
import flyte
from flyte.extras.webhooks import WebhookAppEnvironment, run_once
from flyteplugins.github import GitHubProvider, events

app_env = WebhookAppEnvironment(
    name="github-webhooks",
    providers=[GitHubProvider()],
    secrets=[flyte.Secret("GITHUB_WEBHOOK_SECRET", as_env_var="GITHUB_WEBHOOK_SECRET")],
)


@app_env.on_event(events.PullRequest.OPENED)
async def triage(event):
    import flyte.remote as remote

    task = remote.Task.get(name="github-triage.triage_pr", auto_version="latest")
    result = await run_once.aio(task, key=event.dedupe_key(), repo=event.scope)
    if not result.created:
        return {"skipped": result.run.name, "url": result.run.url}
    return {"run": result.run.name}
```

## Human review gates

`review_pr` parks a run on a `flyte.new_condition` carrying the pull request's
metadata as JSON, waits for a human to answer in the Flyte UI, and returns a
typed decision:

```python
from flyteplugins.github import review_pr


@env.task
async def gated_merge(repo: str, number: int) -> str:
    decision = await review_pr(repo, number)
    if decision.is_approved:
        ...  # merge, with PyGithub
    return f"blocked: {decision.summary}"
```

It lives here because the condition is the part only Flyte can do. Reading the
pull request is `PyGithub`'s job, and this calls it directly rather than
wrapping it — install `flyteplugins-github[review]` for that extra.

## GitHub App tokens

Agents that clone, push, or open PRs authenticate best as a GitHub App,
minting a short-lived installation token per operation instead of holding a
personal access token:

```python
from flyteplugins.github import clone_url, mint_installation_token

token = mint_installation_token()  # GITHUB_APP_ID / _INSTALLATION_ID / _PRIVATE_KEY
url = clone_url("octo/repo", token)
```

It lives here because every agent otherwise carries its own copy of the same
minting logic — install `flyteplugins-github[auth]` for that extra.

Wrapping the GitHub API for anything else is not this plugin's job; use
`PyGithub` from your tasks. See `examples/external_saas_integrations`.
## Directory

### Classes

| Class | Description |
|-|-|
| [`GitHubProvider`](./githubprovider) | GitHub's webhook provider, with its defaults pre-wired. |
| [`ReviewComment`](./reviewcomment) | A single inline review comment. |
| [`ReviewContext`](./reviewcontext) | Review metadata collected from a pull request. |
| [`ReviewDecision`](./reviewdecision) | Structured decision parsed from a reviewer's condition response. |

### Methods

| Method | Description |
|-|-|
| [`build_review_prompt()`](#build_review_prompt) | Build the markdown prompt shown to the reviewer in the Flyte UI. |
| [`clone_url()`](#clone_url) | An https clone URL for `repo` ("owner/name"), authenticated when a token is given. |
| [`collect_review_context()`](#collect_review_context) | Fetch a pull request and assemble the metadata a reviewer needs. |
| [`condition_name_for()`](#condition_name_for) | Derive a condition name from a pull request, within the length limit. |
| [`handshake()`](#handshake) | Answer the `ping` GitHub sends when a webhook is created. |
| [`mint_installation_token()`](#mint_installation_token) | A fresh installation token, or None with a logged reason. |
| [`parse()`](#parse) | Normalize a GitHub delivery — JSON or form-encoded — into a `WebhookEvent`. |
| [`parse_review_payload()`](#parse_review_payload) | Parse a reviewer's condition response into a `ReviewDecision`. |
| [`review_pr()`](#review_pr) | Park the run on a human review condition and return the decision. |
| [`verify()`](#verify) | Verify the `X-Hub-Signature-256` HMAC over the raw body. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_TOKEN_ENV_VAR` | `str` |  |
| `SAMPLE_DELIVERY` | `tuple` |  |

## Methods

#### build_review_prompt()

```python
def build_review_prompt(
    context: ReviewContext,
    instructions: str = '',
) -> str
```
Build the markdown prompt shown to the reviewer in the Flyte UI.

The metadata is embedded as a fenced JSON block so it renders verbatim and
can be machine-parsed downstream.


| Parameter | Type | Description |
|-|-|-|
| `context` | `ReviewContext` | |
| `instructions` | `str` | |

#### clone_url()

```python
def clone_url(
    repo: str,
    token: str | None = None,
) -> str
```
An https clone URL for `repo` ("owner/name"), authenticated when a token is given.


| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | |
| `token` | `str \| None` | |

#### collect_review_context()

```python
def collect_review_context(
    repo: str,
    number: int,
    max_files: int = 50,
    token: str | None = None,
) -> ReviewContext
```
Fetch a pull request and assemble the metadata a reviewer needs.



| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | Repository full name (`owner/repo`). |
| `number` | `int` | Pull request number. |
| `max_files` | `int` | Cap on how many changed files to include. |
| `token` | `str \| None` | Explicit token; otherwise read from `GITHUB_TOKEN`. |

#### condition_name_for()

```python
def condition_name_for(
    repo: str,
    number: int,
) -> str
```
Derive a condition name from a pull request, within the length limit.


| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | |
| `number` | `int` | |

#### handshake()

```python
def handshake(
    headers: Mapping[str, str],
    body: bytes,
) -> dict[str, Any] | None
```
Answer the `ping` GitHub sends when a webhook is created.


| Parameter | Type | Description |
|-|-|-|
| `headers` | `Mapping[str, str]` | |
| `body` | `bytes` | |

#### mint_installation_token()

```python
def mint_installation_token(
    app_id: str | None = None,
    installation_id: str | None = None,
    private_key: str | None = None,
) -> str | None
```
A fresh installation token, or None with a logged reason.

None means "proceed unauthenticated or not at all" — treat it the way a
missing token is treated today, so a half-configured deployment degrades
instead of crashing. Synchronous, one HTTPS round trip: call through
`asyncio.to_thread` from handlers and other async code.



| Parameter | Type | Description |
|-|-|-|
| `app_id` | `str \| None` | The app's numeric id; otherwise read from `GITHUB_APP_ID`. |
| `installation_id` | `str \| None` | The installation's numeric id; otherwise read from `GITHUB_APP_INSTALLATION_ID`. |
| `private_key` | `str \| None` | The app's PEM private key; otherwise read from `GITHUB_APP_PRIVATE_KEY`. |

#### parse()

```python
def parse(
    headers: Mapping[str, str],
    body: bytes,
) -> WebhookEvent
```
Normalize a GitHub delivery — JSON or form-encoded — into a `WebhookEvent`.


| Parameter | Type | Description |
|-|-|-|
| `headers` | `Mapping[str, str]` | |
| `body` | `bytes` | |

#### parse_review_payload()

```python
def parse_review_payload(
    payload: str,
) -> ReviewDecision
```
Parse a reviewer's condition response into a `ReviewDecision`.

Accepts raw JSON, JSON inside a fenced code block, or prose with a JSON
object somewhere in it — reviewers paste all three. Verdict synonyms
(`approved`, `changes_requested`, `lgtm`, ...) are normalized.



| Parameter | Type | Description |
|-|-|-|
| `payload` | `str` | |

**Raises**

| Exception | Description |
|-|-|
| `ValueError` | when no JSON object with a recognizable verdict can be extracted from the payload. |

#### review_pr()

```python
def review_pr(
    repo: str,
    number: int,
    condition_name: str | None = None,
    instructions: str = '',
    timeout: timedelta | int | float | None = None,
    max_files: int = 50,
    token: str | None = None,
) -> ReviewDecision
```
Park the run on a human review condition and return the decision.

Collects the pull request's metadata, raises a markdown condition carrying
it as JSON, waits for a human to respond in the Flyte UI, and parses the
response into a typed decision:

```python
@env.task
async def gated_merge(repo: str, number: int) -> str:
    decision = await review_pr(repo, number)
    if decision.is_approved:
        ...
    return f"blocked: {decision.summary}"
```



| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | Repository full name (`owner/repo`). |
| `number` | `int` | Pull request number. |
| `condition_name` | `str \| None` | Name of the condition action; defaults to one derived from the repo and number. |
| `instructions` | `str` | Override for the reviewer instructions in the prompt. |
| `timeout` | `timedelta \| int \| float \| None` | Forwarded to `flyte.new_condition`. On expiry `wait()` raises `flyte.errors.ConditionTimedoutError`. |
| `max_files` | `int` | Cap on how many changed files to include in the prompt. |
| `token` | `str \| None` | Explicit token; otherwise read from `GITHUB_TOKEN`. |

**Returns**

The parsed `ReviewDecision`.


**Raises**

| Exception | Description |
|-|-|
| `ValueError` | when the reviewer's response carries no recognizable verdict. |

#### verify()

```python
def verify(
    body: bytes,
    headers: Mapping[str, str],
    secret: str,
) -> bool
```
Verify the `X-Hub-Signature-256` HMAC over the raw body.


| Parameter | Type | Description |
|-|-|-|
| `body` | `bytes` | |
| `headers` | `Mapping[str, str]` | |
| `secret` | `str` | |

