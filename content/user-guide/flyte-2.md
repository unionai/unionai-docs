---
title: Flyte 2
weight: 10
variants: +flyte +serverless +byoc +selfmanaged
---

# Flyte 2

With Flyte 2, we introduce a new SDK that simplifies workflow authoring and execution and a new UI that support the new capabilities of the SDK and enhances the user experience.

## What has changed?

Flyte 2 introduce several key improvements:

### Pure Python execution

* Write workflows in pure Python, enabling a more natural and flexible development experience.
* Cleanly express loops, conditionals via if-then statements, and error handling with try-catch statements.
* Dynamically apply overrides at runtime (i.e. catch OOM errors and retry with more memory).

### Simplified data model and API

* The new API is more intuitive, with fewer abstractions and a focus on simplicity.
* There are no Workflows. Instead, "workflows" are authored through a pattern of Tasks calling Tasks.
* Tasks are defined within Environments, which encapsulate the context and resources needed for execution.

### Robust support for reliable execution

* Caching at the task level, allowing for efficient reuse of previously computed results.
* Tracing and checkpointing at the level of individual functions within tasks,
  enabling retries and recovery from failures at a finer granularity.

### Improved Remote functionality

* Run workflows either through the CLI (i.e., `flyte run ...`) or programmatically (i.e., `flyte.run(my_task)`).
* Fetch and run remote (previously-deployed) Tasks within the course of a running workflow.
* Author, run, and fetch metadata (i.e. I/O and logs) from workflows directly from Jupyter notebooks.

### Enhanced UI

* The new UI provides a more streamlined and user-friendly experience for authoring and managing workflows.
* Improved visualization of workflow execution and monitoring.
* Simplified access to logs, metadata, and other important information.