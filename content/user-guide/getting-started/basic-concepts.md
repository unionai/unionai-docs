---
title: Basic concepts
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Basic concepts

To understand how Flyte 2 works, it helps to establish a few definitions and concepts.

* **Workflow**: A collection of tasks linked by invocation, with a top-most task that is the entry point of the workflow.
  We sometime refer to this as the "parent", "driver" or "top-most" task.
  Unlike in Flyte 1, there is no explicit `@workflow` decorator; instead, the workflow is defined implicitly by the structure of the code.
  Nonetheless, you will often see the assemblage of tasks referred to as a "workflow".

* `TaskEnvironment`: A `[[TaskEnvironment]]` object is the abstraction that defines the hardware and software environment in which one or more tasks are executed.
    * The hardware environment is specified by parameters that define the type of compute resources (e.g., CPU, memory) allocated to the task.
    * The software environment is specified by parameters that define the container image, including dependencies, required to run the task.

* **Task**: A Python function.
  * Tasks are defined using the `[[TaskEnvironment.task]]` decorator.
  * Tasks can involve invoking helper functions as well as other tasks and assembling outputs from those invocations.

* **Run**: A `[[Run]]` is the execution of a task directly initiated by a user and all its descendant tasks, considered together.

* **Action**: An `[[Action]]` is the execution of a single task, considered independently. A run consists of one or more actions.

* **AppEnvironment**: An `[[AppEnvironment]]` object is the abstraction that defines the hardware and software environment in which an app runs.
    * The hardware environment is specified by parameters that define the type of compute resources (e.g., CPU, memory, GPU) allocated to the app.
    * The software environment is specified by parameters that define the container image, including dependencies, required to run the app.
    * Apps have additional configuration options specific to services, such as port configuration, scaling behavior, and domain settings.

* **App**: A long-running service that provides functionality via HTTP endpoints. Unlike tasks, which run to completion, apps remain active and can handle multiple requests over time.

* **App vs Task**: The fundamental difference is that apps are services that stay running and handle requests, while tasks are functions that execute once and complete.
  - Apps are suited for short running API calls that need low latency and durability is not required.
  - Apps may expose one or more endpoints, which Tasks consist of one function entrypoint.
  - Every invocation of a Task is durable and can run for long periods of time.
  - In Flyte, durability means that inputs and outputs are recorded in an object store, are visible in the UI, can be cached. In multi-step tasks, durability provides the ability to resume the execution from where it left off without re-computing the output of a task



<!-- included info on what you see in the UI including runs, actions, task info, logs, external log links (action links)
-->
