---
title: Task configuration
weight: 5
variants: +flyte +union
---

# Task configuration

In Flyte 1, image, resources, caching, secrets, and scheduling were configured per-task on the `@task` decorator or per-workflow on a `LaunchPlan`. In Flyte 2 most of this moves to the `flyte.TaskEnvironment`, so it's declared once and shared. See [Migration](./migration) for the overall approach.

## Image, resources, and caching

Image, resources, and caching move from the `@task` decorator to the `TaskEnvironment`. Per-task settings like `retries` and `timeout` stay on `@env.task`. Note that `mem` is renamed to `memory`, and there are no separate `requests`/`limits` — a single `Resources` value serves as both.

{{< tabs "migration-task-config" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/task_config_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/task_config_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

For the complete parameter mapping, see [Tasks and workflows](../../../api-reference/migration/tasks-and-workflows) and [Container images](../../../api-reference/migration/images) in the reference.

## Secrets

Secrets move from `secret_requests` on the task to `secrets` on the `TaskEnvironment`, and you read them from environment variables instead of `current_context().secrets` — for example, an API key for a model registry or hosted LLM.

{{< tabs "migration-secrets" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/secrets_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/secrets_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

See [Secrets](../../task-configuration/secrets) for more.

## Scheduling

A `LaunchPlan` with a `CronSchedule` (say, a nightly retraining job) becomes a `flyte.Trigger` attached directly to the task. Use `flyte.TriggerTime` to bind the scheduled fire time to an input, and deploy the trigger with `flyte deploy`.

{{< tabs "migration-scheduling" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/scheduling_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/scheduling_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

See [Triggers](../../task-configuration/triggers) and [Triggers and dynamic workflows](../../../api-reference/migration/triggers-and-dynamic) for more.

## Next

- [Control flow](./control-flow) — conditionals, dynamic behavior, and error handling
- [Data types and I/O](./data-io) — files, DataFrames, and dataclasses
