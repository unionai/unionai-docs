---
title: Flyte v2 SDK
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Flyte v2 SDK

The Flyte v2 SDK is the new toolkit for authoring workflows in Union and Flyte v2.

## What has changed?

The SDK introduces several key improvements:

### Pure Python execution

* Write workflows in pure Python, enabling a more natural and flexible development experience.
* Cleanly express loops, conditionals via if-then statements, and error handling with try-catch statements.
* Dynamically apply overrides at runtime (i.e. catch OOM errors and retry with more memory).

### Simplified data model and API

* The new API is more intuitive, with fewer abstractions and a focus on simplicity.
* There are no Workflows. Instead, "workflows" are authored through a pattern of Tasks calling Tasks.
* Tasks are defined within Environments, which encapsulate the context and resources needed for execution.

### Improved Remote functionality

* Run workflows either through the CLI (i.e., `flyte run ...`) or programmatically (i.e., `flyte.run(my_task)`).
* Fetch and run remote (previously-deployed) Tasks within the course of a running workflow.
* Author, run, and fetch metadata (i.e. I/O and logs) from workflows directly from Jupyter notebooks.