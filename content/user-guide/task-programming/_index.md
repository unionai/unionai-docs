---
title: Build tasks
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Build tasks

This section covers the essential programming patterns and techniques for developing robust Flyte workflows. Once you understand the basics of task configuration, these guides will help you build sophisticated, production-ready data pipelines and machine learning workflows.

## What you'll learn

The task programming section covers key patterns for building effective Flyte workflows:

**Data handling and types**
- [**Files and directories**](./files-and-directories): Work with large datasets using Flyte's efficient file and directory types that automatically handle data upload, storage, and transfer between tasks.
- [**DataFrames**](./dataframes): Pass DataFrames between tasks without downloading data into memory, with support for Pandas, Polars, PyArrow, Dask, and other DataFrame backends.
- [**Data classes and structures**](./dataclasses-and-structures): Use Python data classes and Pydantic models as task inputs and outputs to create well-structured, type-safe workflows.
- [**Custom context**](./custom-context): Use custom context to pass metadata through your task execution hierarchy without adding parameters to every task.

**Execution patterns**
- [**Fanout**](./fanout): Scale your workflows by running many tasks in parallel, perfect for processing large datasets or running hyperparameter sweeps.
- [**Grouping actions**](./grouping-actions): Organize related task executions into logical groups for better visualization and management in the UI.
- [**Container tasks**](./container-tasks): Run arbitrary containers in any language without the Flyte SDK installed, using Flyte's copilot sidecar for seamless data flow.
- [**Remote tasks**](./remote-tasks): Use previously deployed tasks without importing their code or dependencies, enabling team collaboration and task reuse.
- [**Pod templates**](../task-configuration/pod-templates): Extend tasks with Kubernetes pod templates to add sidecars, volume mounts, and advanced Kubernetes configurations.
- [**Abort and cancel actions**](./abort-tasks): Stop in-progress actions automatically, programmatically, or manually via the CLI and UI.
- [**Other features**](./other-features): Advanced patterns like task forwarding and other specialized task execution techniques.

**Development and debugging**
- [**Notebooks**](./notebooks): Write and iterate on workflows directly in Jupyter notebooks for interactive development and experimentation.
- [**Unit testing**](./unit-testing): Test your Flyte tasks using direct invocation for business logic or `flyte.run()` for Flyte-specific features.
- [**Reports**](./reports): Generate custom HTML reports during task execution to display progress, results, and visualizations in the UI.
- [**Traces**](./traces): Add fine-grained observability to helper functions within your tasks for better debugging and resumption capabilities.
- [**Error handling**](./error-handling): Implement robust error recovery strategies, including automatic resource scaling and graceful failure handling.

## When to use these patterns

These programming patterns become essential as your workflows grow in complexity:

- Use **fanout** when you need to process multiple items concurrently or run parameter sweeps.
- Implement **error handling** for production workflows that need to recover from infrastructure failures.
- Apply **grouping** to organize complex workflows with many task executions.
- Leverage **files and directories** when working with large datasets that don't fit in memory.
- Use **DataFrames** to efficiently pass tabular data between tasks across different processing engines.
- Choose **container tasks** when you need to run code in non-Python languages, use legacy containers, or execute AI-generated code in sandboxes.
- Use **remote tasks** to reuse tasks deployed by other teams without managing their dependencies.
- Apply **pod templates** when you need advanced Kubernetes features like sidecars or specialized storage configurations.
- Use **traces** to debug non-deterministic operations like API calls or ML inference.
- Create **reports** to monitor long-running workflows and share results with stakeholders.
- Use **custom context** when you need lightweight, cross-cutting metadata to flow through your task hierarchy without becoming part of the task's logical inputs.
- Write **unit tests** to validate your task logic and ensure type transformations work correctly before deployment.
- Use **abort and cancel** to stop unnecessary actions when conditions change, such as early convergence in HPO or manual intervention.

Each guide includes practical examples and best practices to help you implement these patterns effectively in your own workflows.
