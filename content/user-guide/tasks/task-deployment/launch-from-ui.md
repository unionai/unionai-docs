---
title: Launch deployed tasks from the UI
description: Find a deployed task in the Tasks list and start a run with the launch form.
icon: play
weight: 12
variants: -flyte +union
---

# Launch deployed tasks from the UI

Once you [deploy a task environment](./_index#persistent-deployment), each of its tasks appears in the **Tasks** list in the {{< key product_name >}} UI.
From there you can open a task, pick a version, fill in its inputs, and start a run without writing any code.

## Find a deployed task

Select **Tasks** in the navigation panel to open the **Tasks** list for the current project and domain.
Each row shows the task's **Name**, **Trigger type**, **Last run**, **Last deployed** time, and **Deployed by** user.

To narrow the list:

- **Search tasks**: type part of a task name. The match is case-insensitive.
- **Last updated**: show tasks updated in the last hour, past 24 hours, past week, past month, or past year.
- **Trigger type**: show tasks with a **Schedule** trigger, an **Artifact** trigger, or **No automation**.
- **Environment type**: show tasks that run in a **Reusable** or **Non-reusable** environment.
- **Deployed by**: show tasks deployed by specific users.
- **All tasks** / **Entry points**: switch to **Entry points** to show only tasks marked with `entrypoint=True`. See [Entrypoint tasks](./entrypoints).

Use **Clear all** to reset the filters.

Click a task to open its details page. The details page opens on the latest version.
Its tabs are:

- **Runs**: the task's runs. When you are viewing a specific version, a toggle switches between runs of that version only and runs of all versions.
- **Task**: the task's definition.
- **Triggers**: the task's triggers.
- **Versions**: every deployed version, with when and by whom it was deployed and its last run.

To view another version, use the version picker under the task name, or click a row on the **Versions** tab.

## Launch a run

On the task details page, click **Run**.
You can also open the launch form straight from the **Tasks** list: open a task row's menu and choose **Run task**. On the **Versions** tab, a version row's menu has **Run this version**.

The launch form opens on the version you are viewing, or on the latest version.
To launch a different version, use the version selector under the task name at the top of the form.
The selector lists versions newest first, marks the latest one **Latest**, and has a search box for long version lists.

The form has these tabs:

| Tab | What you set |
|---|---|
| **Inputs** | The task's inputs. |
| **Context** | Run context values. |
| **Settings** | Run name, queue, and other run settings. |
| **Env vars** | Environment variables for the run. |
| **Secrets** | Overrides for the secrets the task declares. Shown only when the task declares secrets. |
| **Labels** | Labels for the run. |
| **Annotations** | Annotations for the run. |
| **Notifications** | Notification rules for the run. |

Click **Run** at the bottom of the form to start the run.

### Enter inputs

The **Inputs** tab shows one field for each task input, filled with the task's defaults. Required inputs are marked with `*`.
Each field matches the input's type:

| Input type | How you enter it |
|---|---|
| `str`, `int`, `float` | A text or number field. |
| `bool` | A checkbox. |
| `Enum` | A drop-down of the enum's values. |
| `datetime.datetime`, `datetime.date` | A date and time picker. |
| `datetime.timedelta` | A text field that takes a duration such as `1h 30m`. |
| `flyte.io.File`, `flyte.io.Dir` | Enter a URI, or upload a file or directory from your machine. |
| `list` | Add elements with **Add to** followed by the input's name, for example **Add to numbers**. |
| `dict` | Add key-value pairs with **Add to** followed by the input's name. |
| Dataclass or Pydantic model | A nested group of fields, one per attribute. |

To edit all inputs as JSON instead, switch the toggle at the top right of the tab from the form view to the raw view.
**Reset inputs** restores the defaults.

### Choose a queue

On the **Settings** tab, **Queue override** picks the queue the run is routed to.
Leave it empty to use the default routing.
For how queues route work, see [Managing queues](../../clusters-and-queues/queues).

The same tab sets the **Run name**. Leave it empty to have one generated.
A run name must be unique in the project and domain; the form reports a name that is already taken.

## Find the run

When the run is created, the UI opens the new run's details page.
The run also appears in the **Runs** list and on the **Runs** tab of the task's details page.
