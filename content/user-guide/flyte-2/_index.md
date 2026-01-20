---
title: From Flyte 1 to Flyte 2
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# From Flyte 1 to Flyte 2

{{< variant flyte >}}
{{< markdown >}}

Flyte 2 represents a fundamental shift in how workflows are written and executed in Flyte.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

Flyte 2 and Union 2 represent a fundamental shift in how workflows are written and executed in Union.

{{< /markdown >}}
{{< /variant >}}

{{< note title="New to Flyte?" >}}
If you're new to Flyte, start with [Why Flyte?](../why-flyte) and the [Quickstart](../quickstart) guide instead. This section is for users migrating from Flyte 1.
{{< /note >}}

## Simplified API

The new API is more intuitive, with fewer abstractions to learn and a focus on simplicity.

| Use case                      | Flyte 1                     | Flyte 2                                 |
| ----------------------------- | --------------------------- | --------------------------------------- |
| Environment management        | `N/A`                       | `TaskEnvironment`                       |
| Perform basic computation     | `@task`                     | `@env.task`                             |
| Combine tasks into a workflow | `@workflow`                 | `@env.task`                             |
| Create dynamic workflows      | `@dynamic`                  | `@env.task`                             |
| Fanout parallelism            | `flytekit.map`              | Python `for` loop with `asyncio.gather` |
| Conditional execution         | `flytekit.conditional`      | Python `if-elif-else`                   |
| Catching workflow failures    | `@workflow(on_failure=...)` | Python `try-except`                     |

There is no `@workflow` decorator. Instead, "workflows" are authored through a pattern of tasks calling tasks.
Tasks are defined within environments, which encapsulate the context and resources needed for execution.

For details on the pure Python model and async support, see [Pure Python](pure-python) and [Asynchronous model](async).

## Improved remote functionality

Flyte 2 provides full management of the workflow lifecycle through a standardized API through the CLI and the Python SDK.

| Use case      | CLI                | Python SDK          |
| ------------- | ------------------ | ------------------- |
| Run a task    | `flyte run ...`    | `flyte.run(...)`    |
| Deploy a task | `flyte deploy ...` | `flyte.deploy(...)` |

You can also fetch and run remote (previously deployed) tasks within the course of a running workflow.

{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/remote.py" fragment="all" lang="python" >}}

## Native Notebook support

Author and run workflows and fetch workflow metadata (I/O and logs) directly from Jupyter notebooks.

![Native Notebook](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/user-guide/notebook.png)

{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

## High performance engine

Schedule tasks in milliseconds with reusable containers, which massively increases the throughput of containerized tasks.

{{< /markdown >}}
{{< code file="/external/unionai-examples/v2/user-guide/task-configuration/reusable-containers/reuse.py" fragment="env" lang="python" >}}
{{< markdown >}}

Coupled with multi-cluster, multi-cloud, and multi-region support, Flyte 2 can scale to handle even the most demanding
workflows.

{{< /markdown >}}
{{< /variant >}}

## Enhanced UI

New UI with a streamlined and user-friendly experience for authoring and managing workflows.

![New UI](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/user-guide/v2ui.png)

This UI improves the visualization of workflow execution and monitoring, simplifying access to logs, metadata, and other important information.
