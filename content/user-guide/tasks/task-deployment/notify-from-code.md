---
title: Send notifications from your code
description: Post a message when a run succeeds or fails, from the run's own driver task, with the destination read from a secret at runtime.
icon: bell
weight: 13
variants: +flyte +union
---

# Send notifications from your code

To report a run's outcome, wrap the work in the driver task in `try`/`except`, post the message, and re-raise.
The notification is ordinary code, so it reads its destination from a secret when the task runs.
The same deployment can then post to a different webhook on each cluster.

{{< variant flyte >}}
{{< markdown >}}
Open-source Flyte doesn't deliver built-in notifications yet, so use this pattern to notify on run outcomes.
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
[Built-in notifications](./run-with-notifications) need no code, but their delivery details are fixed when you submit the run.
Use this pattern when the destination must be chosen at runtime, or when the message needs results the run computed.
{{< /markdown >}}
{{< /variant >}}

{{< code file="/unionai-examples/v2/user-guide/task-deployment/notify-from-code/notify_from_code.py" fragment="notify-from-code" lang="python">}}

Create the secret before you run the task:

```bash
flyte create secret SLACK_WEBHOOK_URL --value <your-webhook-url>
```

{{< variant flyte >}}
{{< markdown >}}
Each cluster has its own secret store. Create `SLACK_WEBHOOK_URL` on each cluster, with that cluster's webhook.
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
Each [cluster pool](../../cluster-workload-management/cluster-pools) has its own secret store. To post to a different webhook from each pool, create `SLACK_WEBHOOK_URL` in each one with `--cluster-pool`. See [Secrets](../task-configuration/secrets).
{{< /markdown >}}
{{< /variant >}}

## Notify once per run

Three details keep the message from being sent more than once:

- **Put retries on the child tasks, not the driver.** `train` retries up to three times, and the driver sees the exception only after the last attempt fails, so it posts once. If the driver had `retries`, each driver attempt would post again.
- **Make the post a [traced function](../task-programming/traces).** A completed trace is a checkpoint. If the driver resumes after an interruption, it doesn't send the message again.
- **Re-raise after posting.** The run still ends as failed, and the error stays in the run.

The exception from a failed child task reaches the driver as `flyte.errors.RuntimeUserError`, with the original error message. The example catches `Exception` so that system errors notify too.

## Limitations

The driver sends the notification, so nothing is sent if the driver itself doesn't reach the `except` block. This happens when:

- The driver task runs out of memory, times out, or crashes.
- The run is aborted.
