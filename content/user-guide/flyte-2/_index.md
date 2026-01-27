---
title: From Flyte 1 to Flyte 2
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# From Flyte 1 to Flyte 2

Flyte 2 represents a fundamental shift in how Flyte workflows are written and executed.

## Pure Python execution

Write workflows in pure Python, enabling a more natural development experience and removing the constraints of a
domain-specific language (DSL).

{{< tabs "flyte-2-python" >}}
{{< tab "Sync Python" >}}
{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/sync_example.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< tab "Async Python" >}}
{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/async_example.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

As you can see in the hello world example, workflows can be constructed at runtime, allowing for more flexible and
adaptive behavior. Flyte 2 supports:

- Python's asynchronous programming model to express parallelism.
- Python's native error handling with `try-except` to overridden configurations, like resource requests.
- Predefined static workflows when compile-time safety is critical.

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

## Fine-grained reproducibility and recoverability

As in Flyte 1, Flyte 2 supports caching at the task level (via `@env.task(cache=...)`), but it further enables recovery at the finer-grained, sub-task level through a feature called tracing (via `@flyte.trace`).

{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/trace.py" fragment="all" lang="python" >}}

Here `call_llm` runs in the same container as `main` and acts as an automated checkpoint with full observability in the UI.
If the task fails due to a system error (e.g., node preemption or infrastructure failure), Flyte can recover and replay from the
last successful trace rather than restarting from the beginning.

Note that tracing is distinct from caching: traces are recovered only if there is a system failure
whereas with cached outputs are persisted for reuse across separate runs.

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

When running on a Union.ai backend, Flyte 2 enables you to schedule tasks in milliseconds with reusable containers, which massively increases the throughput of containerized tasks.

{{< /markdown >}}
{{< code file="/external/unionai-examples/v2/user-guide/flyte-2/reuse.py" fragment="env" lang="python" >}}
{{< markdown >}}

Coupled with multi-cluster, multi-cloud, and multi-region support, Flyte 2 on Union.ai can scale to handle even the most demanding workflows.

## Enhanced UI

The Union.ai backend also offers a new UI with a streamlined and user-friendly experience for authoring and managing workflows.

![New UI](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/user-guide/v2ui.png)

This UI improves the visualization of workflow execution and monitoring, simplifying access to logs, metadata, and other important information.

{{< /markdown >}}
{{< /variant >}}
