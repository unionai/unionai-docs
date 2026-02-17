---
title: Migration from Flyte 1
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
llm_readable_bundle: true
---

# Migration from Flyte 1 to Flyte 2

{{< note >}}
An LLM-readable bundle of this entire section is available at [`section.md`](section.md).
This single file contains all pages in this section, optimized for AI coding agent context.
{{< /note >}}

This section provides a comprehensive reference for migrating Flyte 1 (flytekit) workflows to Flyte 2 (flyte SDK).

For a quick-start overview of the migration process, see [Migration](../../user-guide/flyte-2/migration) in the User Guide.

## Key API changes at a glance

| Use case                      | Flyte 1                     | Flyte 2                                 |
| ----------------------------- | --------------------------- | --------------------------------------- |
| Environment management        | N/A                         | `TaskEnvironment`                       |
| Perform basic computation     | `@task`                     | `@env.task`                             |
| Combine tasks into a workflow | `@workflow`                 | `@env.task`                             |
| Create dynamic workflows      | `@dynamic`                  | `@env.task`                             |
| Fanout parallelism            | `flytekit.map`              | Python `for` loop with `asyncio.gather` |
| Conditional execution         | `flytekit.conditional`      | Python `if-elif-else`                   |
| Catching workflow failures    | `@workflow(on_failure=...)` | Python `try-except`                     |

## Topics

{{< grid >}}

{{< link-card target="overview" icon="lightbulb" title="Philosophy and imports" >}}
Key paradigm shifts and package import mapping from flytekit to flyte.
{{< /link-card >}}

{{< link-card target="images" icon="deployed_code" title="Container images" >}}
Migrate from ImageSpec to flyte.Image with the fluent builder API.
{{< /link-card >}}

{{< link-card target="configuration-and-cli" icon="terminal" title="Configuration and CLI" >}}
Config file format changes and CLI command mapping.
{{< /link-card >}}

{{< link-card target="tasks-and-workflows" icon="workflow" title="Tasks and workflows" >}}
Migrate @task, @workflow, and @dynamic to TaskEnvironment and @env.task.
{{< /link-card >}}

{{< link-card target="secrets-resources-caching" icon="settings" title="Secrets, resources, and caching" >}}
Updated patterns for secrets access, resource configuration, and caching.
{{< /link-card >}}

{{< link-card target="parallelism-and-async" icon="call_split" title="Parallelism and async" >}}
Migrate map_task to flyte.map and asyncio.gather patterns.
{{< /link-card >}}

{{< link-card target="triggers-and-dynamic" icon="schedule" title="Triggers and dynamic workflows" >}}
Migrate LaunchPlan schedules to Triggers and @dynamic to regular tasks.
{{< /link-card >}}

{{< link-card target="examples-and-gotchas" icon="code" title="Examples and common gotchas" >}}
Complete migration examples and common pitfalls to avoid.
{{< /link-card >}}

{{< /grid >}}
