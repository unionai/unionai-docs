---
title: Anatomy of a run
weight: 50
variants: +flyte +serverless +byoc +selfmanaged
---

# Anatomy of a run

To understand how Flyte 2 works, it helps to establish a few definitions and concepts.

* **Workflow**: A collection of tasks linked by invocation, with a top-most task that is the entry point of the workflow.
  We sometime refer to this as the "parent", "driver" or "top-most" task.
  Unlike in Flyte 1, there is no explicit `@workflow` decorator; instead, the workflow is defined implicitly by the structure of the code.
  Nonetheless, you will often see the assemblage of tasks referred to as a "workflow".

* **TaskEnvironment**: A `TaskEnvironment` object is the abstraction that defines the hardware and software environment in which one or more tasks are executed.
    * The hardware environment is specified by parameters that define the type of compute resources (e.g., CPU, memory) allocated to the task.
    * The software environment is specified by parameters that define the container image, including dependencies, required to run the task.

* **Task**: A Python function.
  * Tasks are defined using the `@env.task` decorator, where the `env` refers to a `TaskEnvironment` object.
  * Tasks can involve invoking helper functions as well as other tasks and assembling outputs from those invocations.

* **Run**: A run is the execution of a task directly initiated by a user and all its descendant tasks, considered together.

* **Action**: An action is the execution of a single task, considered independently. A run consists of one or more actions.


<!-- included info on what you see in the UI including runs, actions, task info, logs, external log links (action links)
-->
