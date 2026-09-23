---
title: Deploy and manage triggers
description: Deploy triggers with their task, activate or deactivate them, and delete them.
icon: toggles
weight: 8
variants: +flyte +union
---

# Deploy and manage triggers

Triggers are deployed with their task, and you can switch them off without deleting them. To pause a nightly job during a data migration, deactivate its trigger and reactivate it afterwards.

## Deploying a task with triggers

We recommend that you define your triggers in code together with your tasks and deploy them together.

The Union UI displays:

* `Owner` - who last deployed the trigger.

* `Last updated` - who last activated or deactivated the trigger and when. Note: If you deploy a trigger with `auto_activate=True`(default), this will match the `Owner`.

* `Last Run` - when was the last run created by this trigger.

For development and debugging purposes, you can adjust and deploy individual triggers from the UI.

To deploy a task with its triggers:

{{< tabs "deploy" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
flyte.deploy(env)
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte deploy -p <project> -d <domain> <file_with_tasks_and_triggers.py> env
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Upon deploy, all triggers that are associated with a given task `T` will be automatically switched to apply to the latest version of that task. Triggers on task `T` which are defined elsewhere (i.e. in the UI) will be deleted unless they have been referenced in the task definition of `T`

<!-- TODO
Add link to workflow deployment docs when available.
-->

## Activating and deactivating triggers

By default, triggers are automatically activated upon deployment (`auto_activate=True`).
Alternatively, you can set `auto_activate=False` to deploy inactive triggers.
An inactive trigger will not create runs until activated.

{{< code file="/unionai-examples/v2/user-guide/task-configuration/triggers/triggers.py" fragment="auto-activate-false" lang="python">}}

This trigger won't create runs until it is explicitly activated.
Activate it, or deactivate a trigger to stop it from creating new runs:

{{< tabs "activate" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
# Activate
flyte.remote.Trigger.update("custom_cron", "my_task_env.custom_task", active=True)

# Deactivate
flyte.remote.Trigger.update("custom_cron", "my_task_env.custom_task", active=False)
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
# Activate
flyte update trigger custom_cron my_task_env.custom_task --activate --project <project> --domain <domain>

# Deactivate
flyte update trigger custom_cron my_task_env.custom_task --deactivate --project <project> --domain <domain>
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

You can also view and manage your deployed triggers in the Union UI.

## Deleting triggers

If you decide that you don't need a trigger anymore, you can remove the trigger from the task definition and deploy the task again.

Alternatively, delete it directly:

{{< tabs "delete" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
flyte.remote.Trigger.delete("custom_cron", "my_task_env.custom_task")
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}

```bash
flyte delete trigger custom_cron my_task_env.custom_task --project <project> --domain <domain>
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}
