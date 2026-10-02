---
title: Slack
description: Receive Slack events, interactions, and slash commands as Flyte runs — and post, update, and gate a run on a button click.
icon: slack
weight: 2
variants: +flyte +union
---

# Slack

Receive [Slack](https://api.slack.com/apis/events-api) webhooks in Flyte, send messages back from tasks, and park a run on a button click. Slack is the broadest of the [SDLC integrations](./_index) in both directions: it delivers three different shapes to one route, and it is one of two plugins that also *send*.

## Installation

```bash
pip install "flyteplugins-slack[app]"
```

Requires Python 3.10 or later. The `app` extra pulls in `fastapi` and `uvicorn` for serving the receiver; `notify` and `approval` send over `httpx`, which Flyte already depends on, so they need no extra.

## Two credentials, and they are not interchangeable

This is the thing to get straight first, because conflating them produces errors that read like something else entirely.

| Credential | Where | Used by | Default env var |
|---|---|---|---|
| **Signing secret** | *Basic Information* | The receiver, to verify deliveries | `SLACK_SIGNING_SECRET` |
| **Bot token** (`xoxb-…`) | *OAuth & Permissions* | `notify` and `approval`, to call the Web API | `SLACK_BOT_TOKEN` |

The signing secret belongs to the app and is mounted automatically from the provider's `default_secret_env`. The bot token belongs on the **task** environment, and posting with it needs the `chat:write` scope plus a `/invite` of the bot into the channel.

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_webhooks.py" fragment=app lang=python >}}

`approval.register(app_env)` is one line that wires up the other half of the approval round trip — see [Approvals](#approvals).

### Three delivery shapes, one route

All three arrive at `/webhook/slack` and are signed the same way, so one provider verifies them all. `on_event` is what tells them apart:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_webhooks.py" fragment=handler lang=python >}}

| Shape | Body | `event_type` | `action` |
|---|---|---|---|
| Events API callback | JSON | The event's `type` — `message`, `app_mention` | The event's `subtype`, when it has one |
| Interactivity (buttons, shortcuts, modals) | form, JSON under `payload` | `block_actions`, `view_submission`, `shortcut`, … | The `action_id` or `callback_id` |
| Slash command | form fields | `command` | The command name, leading `/` dropped |

Because the action half of an interaction is the `action_id`, the bare constant matches every button and `action=` narrows it to one:

```python
# every Block Kit button in the workspace
@app_env.on_event(events.Interaction.BLOCK_ACTIONS)
async def any_button(event): ...

# exactly one button
@app_env.on_event(events.Interaction.BLOCK_ACTIONS, action="redeploy")
async def redeploy_button(event): ...
```

A leading `/` is dropped from slash commands, so `action="/deploy"` reads the way Slack displays it.

### Setting up the app in Slack

At [api.slack.com/apps](https://api.slack.com/apps), paste the `/webhook/slack` URL from the dashboard into **all three** places you use:

1. **Event Subscriptions → Request URL**, then subscribe to the bot events your handlers match.
2. **Interactivity & Shortcuts → Request URL**, if you use buttons, shortcuts, modals, or approvals.
3. **Slash Commands → Request URL**, per command.

The provider answers both of Slack's reachability probes automatically — the `url_verification` challenge on the Events API URL and the form-encoded `ssl_check` on the other two — so the URL should go green immediately.

Scopes: `app_mentions:read` to receive mentions, `chat:write` to post, `commands` for slash commands.

## Events

Constants live in `flyteplugins.slack.events`.

| Class | Members |
|---|---|
| `Message` | `ANY`, `CHANGED`, `DELETED`, `REPLIED`, `CHANNEL_JOIN`, `CHANNEL_LEAVE`, `BOT_MESSAGE`, `FILE_SHARE`, `THREAD_BROADCAST` |
| `AppMention` | `ANY` |
| `Reaction` | `ADDED`, `REMOVED` |
| `Channel` | `CREATED`, `DELETED`, `RENAME`, `ARCHIVE`, `UNARCHIVE` |
| `Member` | `JOINED_CHANNEL`, `LEFT_CHANNEL` |
| `Team` | `JOIN` |
| `File` | `CREATED`, `SHARED`, `DELETED` |
| `Pin` | `ADDED`, `REMOVED` |
| `AppHome` | `OPENED` |
| `Interaction` | `BLOCK_ACTIONS`, `VIEW_SUBMISSION`, `VIEW_CLOSED`, `SHORTCUT`, `MESSAGE_ACTION` |
| `Command` | `ANY` |

### How events are scoped and deduped

`scope` is the channel id, which is what `scopes=` matches. `resource_id` is `channel:ts` — **per message**. To collapse a whole thread onto one run, build your own key from `thread_ts` and pass it to `run_once` directly.

For interactions, `occurred_at` is the click's `action_ts`, so two clicks of one button get their own dedupe keys while a redelivery of either does not.

> [!NOTE] Slack is the one provider with a replay window
> Deliveries older than five minutes (`MAX_REQUEST_AGE_SECONDS`) are rejected, which is why the plugin's `SAMPLE_DELIVERY` signs at call time rather than carrying a fixed signature that would start failing the moment it aged out.

## Sending from tasks

Receiving is the app's job; sending is a task's. `notify` covers the sends every integration otherwise hand-rolls in fifty lines of HTTP and `ok`-checking.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=task lang=python >}}

| Function | Does |
|---|---|
| `post(channel, text, *, blocks, thread_ts, token)` | Posts a message; returns its `ts`, which both anchors a thread and addresses `update` |
| `update(channel, ts, text, *, blocks, token)` | Edits a posted message in place — progress counters, final status |
| `delete(channel, ts, *, token)` | Deletes one of the bot's own messages |
| `respond(response_url, text, *, blocks, replace_original, response_type)` | Answers an interaction or slash command. **No token needed** |

`respond` is the one to reach for from a handler: it posts to the `response_url` every interaction and slash command carries, valid for 30 minutes and five uses, which makes it the zero-setup way for a launched task to answer the click that launched it.

`SlackApiError` carries Slack's own code. The two worth knowing: `not_in_channel` means the bot needs a `/invite`, and `missing_scope` names the OAuth scope to add.

> [!NOTE] One place can hold the token
> `notify` ships a ready-made task environment with a `send` task. Deploy it once and only it holds the bot token; every other run posts through `flyte.run(notify.send, ...)` without mounting a secret.

## Approvals

`approval` is the round trip, and the reason it belongs in the plugin rather than in an example: posting buttons is Slack's job, but *parking a run until one is clicked* is Flyte's.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=approval lang=python >}}

The task half posts a Block Kit message and parks the run on a `flyte.new_condition`. The webhook half signals that condition when a button is clicked, then replaces the buttons with a "decided by" line so nobody clicks twice. The button's `value` carries the run, action, and condition names, so the app needs no configuration to answer — which is what `approval.register(app_env)` switches on.

`request` takes `options` (default `("approve", "reject")`), `thread_ts`, `timeout` (default one hour), `name`, and `token`. It is `syncify`'d: use `.aio(...)` from async tasks and the bare call from sync ones. It runs inside a task only, since the condition is registered against the running action.

`approval.blocks(...)` is exposed separately, so a richer message — context blocks, fields, images — can embed the same buttons in your own layout and still be answered by the registered handler.

> [!NOTE] An approval nobody clicks is not a stuck run
> The condition is equally answerable from the Flyte UI. If nobody clicks in Slack, the run shows the same prompt there and either path resolves it.

## Try it without a Slack workspace

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local slack_tasks.py replay_sample_delivery
```

## Examples

Both files live in [`v2/integrations/flyte-plugins/slack`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/slack):

- `slack_webhooks.py` — the receiver, a mention handler, a slash command, and `approval.register`.
- `slack_tasks.py` — `notify` post-then-update, the approval gate, and the offline replay.

## See also

- [SDLC integrations](./_index) for the shared model: the normalized event, `run_once`, and scoping.
- [Slack API reference](../../api-reference/integrations/sdlc-integrations/slack/_index).
