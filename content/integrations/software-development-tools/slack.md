---
title: Slack
description: Receive Slack events, interactions, and slash commands as Flyte runs, and post messages and approval buttons from tasks.
icon: slack
weight: 2
variants: +flyte +union
---

# Slack

Receive [Slack](https://api.slack.com/apis/events-api) events, interactions, and slash commands in Flyte and turn them into runs. From tasks, the plugin can post and update messages, and pause a run until someone clicks an approval button.

## Installation

```bash
pip install "flyteplugins-slack[app]"
```

Requires Python 3.10 or later. The `app` extra adds `fastapi` and `uvicorn` for serving the receiver. The `notify` and `approval` modules need no extra.

## Credentials

The plugin uses two Slack credentials. They aren't interchangeable.

| Credential | Where to find it | Used by | Environment variable |
|---|---|---|---|
| Signing secret | **Basic Information** | The receiver, to verify deliveries | `SLACK_SIGNING_SECRET` |
| Bot token (`xoxb-…`) | **OAuth & Permissions** | `notify` and `approval`, to call the Web API | `SLACK_BOT_TOKEN` |

The app mounts the signing secret automatically. Mount the bot token on the task environment. Posting requires the `chat:write` scope, and the bot must be invited to the channel with `/invite`.

## The receiver

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_webhooks.py" fragment=app lang=python >}}

`approval.register(app_env)` adds the handler that receives approval button clicks. See [Approvals](#approvals).

### Delivery types

Slack sends three kinds of delivery to `/webhook/slack`. All three are signed the same way, and `on_event` tells them apart:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_webhooks.py" fragment=handler lang=python >}}

| Delivery | Body | `event_type` | `action` |
|---|---|---|---|
| Events API callback | JSON | The event's `type`, such as `message` or `app_mention` | The event's `subtype`, if any |
| Interactivity (buttons, shortcuts, modals) | Form, with JSON in `payload` | `block_actions`, `view_submission`, `shortcut`, … | The `action_id` or `callback_id` |
| Slash command | Form | `command` | The command name, without the leading `/` |

For interactions, the action is the `action_id`. A bare constant matches every button; add `action=` to match one:

```python
# Every Block Kit button in the workspace
@app_env.on_event(events.Interaction.BLOCK_ACTIONS)
async def any_button(event): ...

# One button
@app_env.on_event(events.Interaction.BLOCK_ACTIONS, action="redeploy")
async def redeploy_button(event): ...
```

For slash commands, you can write `action="/deploy"` or `action="deploy"`. The leading `/` is dropped.

### Set up the app in Slack

At [api.slack.com/apps](https://api.slack.com/apps), paste the `/webhook/slack` URL from the dashboard into each of these that you use:

1. **Event Subscriptions → Request URL**. Then subscribe to the bot events your handlers match.
2. **Interactivity & Shortcuts → Request URL**, for buttons, shortcuts, modals, or approvals.
3. **Slash Commands → Request URL**, for each command.

The provider answers Slack's `url_verification` challenge and `ssl_check` probe, so each URL verifies as soon as you save it.

Required scopes: `app_mentions:read` to receive mentions, `chat:write` to post, `commands` for slash commands.

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

### Scope and deduplication

`scope` is the channel ID. `resource_id` is `channel:ts`, which identifies a single message. To launch one run per thread instead, build a key from `thread_ts` and pass it to `run_once` as `key=`.

For interactions, `occurred_at` is the click's `action_ts`. Two clicks on one button launch two runs; a redelivery of either click doesn't.

The provider rejects deliveries more than five minutes old (`MAX_REQUEST_AGE_SECONDS`). For this reason, `SAMPLE_DELIVERY` signs its payload when called rather than carrying a fixed signature.

## Send messages from tasks

The `notify` module posts, edits, and deletes messages through the Slack Web API.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=task lang=python >}}

| Function | Description |
|---|---|
| `post(channel, text, *, blocks, thread_ts, token)` | Posts a message and returns its `ts`. Use the `ts` to reply in a thread or to `update` the message. |
| `update(channel, ts, text, *, blocks, token)` | Edits a posted message, for example to show progress or a final status |
| `delete(channel, ts, *, token)` | Deletes a message the bot posted |
| `respond(response_url, text, *, blocks, replace_original, response_type)` | Replies to an interaction or slash command. Needs no token. |

`respond` posts to the `response_url` that each interaction and slash command carries. The URL is valid for 30 minutes and five uses, so a task launched by a click can reply to that click without a bot token.

Failed calls raise `SlackApiError` with Slack's error code. `not_in_channel` means the bot needs to be invited to the channel. `missing_scope` names the OAuth scope to add.

To keep the bot token in one place, deploy `notify.env`. It provides a `send` task that holds the token, and other runs post through `flyte.run(notify.send, ...)` without mounting the secret themselves.

## Approvals

`approval.request` posts a message with buttons and pauses the run until someone clicks one.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=approval lang=python >}}

The task posts a Block Kit message and waits on a `flyte.new_condition`. When someone clicks a button, the handler added by `approval.register(app_env)` resolves the condition and replaces the buttons with a line showing who decided. Each button carries the run, action, and condition names, so the handler needs no other configuration.

`request` accepts:

- `options`: the button labels. Defaults to `("approve", "reject")`.
- `thread_ts`: posts into an existing thread.
- `timeout`: defaults to one hour.
- `name` and `token`.

Call `request.aio(...)` from async tasks and `request(...)` from sync tasks. It works only inside a task, because the condition belongs to the running action.

To embed the buttons in your own message layout, build them with `approval.blocks(...)`. The registered handler answers them the same way.

The condition can also be resolved from the Flyte UI, which shows the same prompt.

## Test without a Slack workspace

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/slack/slack_tasks.py" fragment=replay lang=python >}}

```bash
flyte run --local slack_tasks.py replay_sample_delivery
```

## Examples

Both files are in [`v2/integrations/flyte-plugins/slack`](https://github.com/unionai/unionai-examples/tree/main/v2/integrations/flyte-plugins/slack):

- `slack_webhooks.py`: the receiver, a mention handler, a slash command, and `approval.register`.
- `slack_tasks.py`: posting and updating with `notify`, the approval gate, and the offline replay.

## See also

- [Software development tools](./_index) for the event model, `run_once`, and scopes.
- [Slack API reference](../../api-reference/integrations/software-development-tools/slack/_index).
