---
title: Flyte 2
weight: 10
variants: +flyte -serverless +byoc +selfmanaged
---

# Flyte 2

{{< variant flyte >}}
{{< markdown >}}

Flyte 2 represents a fundamental shift in how workflows are written and executed in Flyte.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

Flyte 2 and Union 2 represent a fundamental shift in how workflows are written and executed in Union.

{{< /markdown >}}
{{< /variant >}}

### Simplified API

* The new API is more intuitive, with fewer abstractions and a focus on simplicity.
* There is no `@workflow` decorator. Instead, "workflows" are authored through a pattern of tasks calling tasks.
* Tasks are defined within environments, which encapsulate the context and resources needed for execution.

### Pure Python execution

* Workflows are written in pure Python, removing the constraints of a domain-specific language (DSL) and enabling full use of Python's capabilities.
* Workflows can be constructed at runtime, allowing for more flexible and adaptive behavior.
* Python's asynchronous programming model can be used to express parallelism.
* Standard Python error handling patterns (try/except) can be used to retry executions with changed parameters (like additional resources).
* Predefined static workflows are still supported when needed.

### Fine-grained reproducibility and recoverability

* Tracing augments task level-caching to enable reproducibility and recovery at the sub-task function level.

### Improved remote functionality

* Full management of the workflow lifecycle through both CLI and Python (programmatically).
* Fetch and run remote (previously deployed) tasks within the course of a running workflow.
* Author and run workflows and fetch workflow metadata (I/O and logs) directly from Jupyter notebooks.

{{< variant byoc selfmanaged >}}
{{< markdown >}}

### High performance engine

* Schedule tasks in milliseconds with reusable containers.
* Workflows can span multiple clusters, clouds, and regions

### Enhanced UI

* New UI with a streamlined and user-friendly experience for authoring and managing workflows.
* Improved visualization of workflow execution and monitoring.
* Simplified access to logs, metadata, and other important information.

{{< /markdown >}}
{{< /variant >}}