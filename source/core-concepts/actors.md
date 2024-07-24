# Actors

Actors allow you to reuse a container and environment between tasks that need to maintain state. To create an actor, instantiate the [`ActorEnvironment`](../api/sdk/actor.actorenvironment) class, then add the instance as a decorator to the task that requires that environment.

## `ActorEnvironment` parameters

* **backlog_length:** The number of tasks to keep in the worker queue on the backend. Setting `backlog_length` ensures that the worker executing actor tasks immediately executes the next task after completing the previous one instead of waiting for the scheduler to complete other operations before scheduling the next task.
{@@ if serverless @@}
* **container_image:** The container image to use for the task. Defaults to `cr.union.ai/union/unionai:py3.11-latest`.
{@@ elif byoc @@}
* **container_image:** The container image to use for the task. Defaults to `cr.flyte.org/flyteorg/flytekit:py3.9-latest`.
{@@ endif @@}
* **environment:** Environment variables as key, value pairs in a Python dictionary.
* **limits:** Compute resource limits.
* **parallelism:** The number of tasks that can execute in parallel, per worker.
* **replica_count:** The number of workers to provision that are able to accept tasks.
* **requests:** Compute resource requests per task.
* **secret_requests:** Keys (ideally descriptive) that can identify the secrets supplied at runtime. For more information, see [Managing secrets](../development-cycle/managing-secrets).
* **ttl_seconds:** How long to keep the Actor alive while no tasks are being run.

## Examples

### Hello world

The following example shows how to create a basic `ActorEnvironment` and use it for one task:

```{rli} https://raw.githubusercontent.com/unionai/examples/e8e8fb29470e5237089182048092b96f16d0fdc3/guides/02_core_concepts/actors/hello_world.py
:caption: hello_world.py

```

### Multiple instances of the same task

In this example, the `actor.task`-decorated task is invoked multiple times in one workflow, and will use the same `ActorEnvironment` on each invocation:

```{rli} https://raw.githubusercontent.com/unionai/examples/e8e8fb29470e5237089182048092b96f16d0fdc3/guides/02_core_concepts/actors/plus_one.py
:caption: plus_one.py

```

### Multiple tasks

Every task execution in the following example will execute in the same `ActorEnvironment`. You can use the same environment for multiple tasks in the same workflow and tasks across workflow definitions, using both subworkflows and launchplans:

```{rli} https://raw.githubusercontent.com/unionai/examples/e8e8fb29470e5237089182048092b96f16d0fdc3/guides/02_core_concepts/actors/multiple_tasks.py
:caption: multiple_entities.py

```