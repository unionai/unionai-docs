---
title: Tasks
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Tasks

Tasks are the fundamental units of compute in {{< key product_name >}}.
They are independently executable, strongly typed, and containerized building blocks that make up workflows.
Workflows are constructed by chaining together tasks, with the output of one task feeding into the input of the next to form a directed acyclic graph.

## Tasks are independently executable

Tasks are designed to be independently executable, meaning that they can be run in isolation from other tasks.
And since most tasks are just Python functions, they can be executed on your local machine, making it easy to unit test and debug tasks locally before deploying them to {{< key product_name >}}.

Because they are independently executable, tasks can also be shared and reused across multiple workflows and, as long as their logic is deterministic, their input and outputs can be [cached](../caching) to save compute resources and execution time.

## Tasks are strongly typed

Tasks have strongly typed inputs and outputs, which are validated at deployment time.
This helps catch bugs early and ensures that the data passing through tasks and workflows is compatible with the explicitly stated types.

Under the hood, {{< key product_name >}} uses the [Flyte type system]() and translates between the Flyte types and the Python types.
Python type annotations make sure that the data passing through tasks and workflows is compatible with the explicitly stated types defined through a function signature.
The {{< key product_name >}} type system is also used for caching, data lineage tracking, and automatic serialization and deserialization of data as it’s passed from one task to another.

## Tasks are containerized

While (most) tasks are locally executable, when a task is deployed to {{< key product_name >}} as part of the registration process it is containerized and run in its own independent Kubernetes pod.

{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

This allows tasks to have their own independent set of [software dependencies](./task-software-environment/_index) and [hardware requirements](./task-hardware-environment/_index).
For example, a task that requires a GPU can be deployed to {{< key product_name >}} with a GPU-enabled container image, while a task that requires a specific version of a software library can be deployed with that version of the library installed.

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless >}}
{{< markdown >}}

This allows tasks to have their own independent set of [software dependencies](../../core-concepts/image-spec) and [hardware requirements](./task-hardware-environment/_index).
For example, a task that requires a GPU can be deployed to {{< key product_name >}} with a GPU-enabled container image, while a task that requires a specific version of a software library can be deployed with that version of the library installed.

{{< /markdown >}}
{{< /variant >}}

## Tasks are named, versioned, and immutable

The fully qualified name of a task is a combination of its project, domain, and name. To update a task, you change it and re-register it under the same fully qualified name. This creates a new version of the task while the old version remains available. At the version level task are, therefore, immutable. This immutability is important for ensuring that workflows are reproducible and that the data lineage is accurate.

## Tasks are (usually) deterministic and cacheable

When deciding if a unit of execution is suitable to be encapsulated as a task, consider the following questions:

* Is there a well-defined graceful/successful exit criteria for the task?
    * A task is expected to exit after completion of input processing.
* Is it deterministic and repeatable?
    * Under certain circumstances, a task might be cached or rerun with the same inputs.
      It is expected to produce the same output every time.
      You should, for example, avoid using random number generators with the current clock as seed.
* Is it a pure function? That is, does it have side effects that are unknown to the system?
    * It is recommended to avoid side effects in tasks.
    * When side effects are unavoidable, ensure that the operations are idempotent.

For details on task caching, see [Caching](../caching).

{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}
## Workflows can contain many types of tasks

One of the most powerful features of {{< key product_name >}} is the ability to run widely differing computational workloads as tasks with a single workflow.

Because of the way that {{< key product_name >}} is architected, tasks within a single workflow can differ along many dimensions. While the total number of ways that tasks can be configured is quite large, the options fall into three categories:

* **Task type**: These include standard Python tasks, map tasks, raw container tasks, and many specialized plugin tasks. For more information, see [Task types](./task-types).
* **Software environment**: Define the task container image, dependencies, and even programming language. For more information, see [Task software environment](./task-software-environment/_index).
* **Hardware environment**: Define the resource requirements (processor numbers, storage amounts) and machine node characteristics (CPU and GPU type). For more information, see [Task hardware environment](./task-hardware-environment/_index).

### Mix and match task characteristics

Along these three dimensions, you can mix and match characteristics to build a task definition that performs exactly the job you want, while still taking advantage of all the features provided at the workflow level like output caching, versioning, and reproducibility.

Tasks with diverse characteristics can be combined into a single workflow.
For example, a workflow might contain:

* A **Python task running on your default container image** with default dependencies and a default resource and hardware profile.
* A **Python task running on a container image with additional dependencies** configured to run on machine nodes with a specific type of GPU.
* A **raw container task** running a Java process.
* A **plugin task** running a Spark job that spawns its own cluster-in-a-cluster.
* A **map task** that runs multiple copies of a Python task in parallel.

The ability to build workflows from such a wide variety of heterogeneous tasks makes {{< key product_name >}} uniquely flexible.

> [!NOTE]
> Not all parameters are compatible. For example, with specialized plugin task types, some configurations are
> not available (this depends on task plugin details).

## Task configuration

The `@{{< key kit_as >}}.task` decorator can take a number of parameters that allow you to configure the task's behavior.
For example, you can specify the task's software dependencies, hardware requirements, caching behavior, retry behavior, and more.
For more information, see [Task parameters](./task-parameters).
{{< /markdown >}}
{{< /variant >}}