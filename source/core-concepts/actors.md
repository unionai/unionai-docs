# Actors

Actors allow you to reuse containers between tasks that need to maintain state. You can create an actor by instantiating the [`ActorEnvironment`](../api/sdk/actor.actorenvironment) class, then add the `@actor` decorator to thet task that requires a stateful environment every time it's invoked.

## `ActorEnvironment` parameters

* **backlog_length:**
{@@ if serverless @@}
* **container_image:** The container image to use for the task. Defaults to `cr.union.ai/union/unionai:py3.11-latest`.
{@@ elif byoc @@}
* **container_image:** The container image to use for the task. Defaults to `cr.flyte.org/flyteorg/flytekit:py3.9-latest`.
{@@ endif @@}
* **environment:**
* **limits:** Compute resource limits.
* **parallelism:** The number of tasks that can execute in parallel, per worker.
* **replica_count:** The number of workers to provision that are able to accept tasks.
* **requests:** Compute resource requests per task.
* **secret_requests:** Keys (ideally descriptive) that can identify the secrets supplied at runtime. For more information, see [Managing secrets](../getting-started/managing-secrets).
* **ttl_seconds:** How long to keep the Actor alive while no tasks are being run.

## Examples

### Hello world

```{rli} https://raw.githubusercontent.com/unionai/examples/nikki/add-actors-example/guides/02_core_concepts/actors/hello_world.py
:caption: hello_world.py

```

### Addition

```{rli} https://raw.githubusercontent.com/unionai/examples/nikki/add-actors-example/guides/02_core_concepts/actors/plus_one.py
:caption: plus_one.py

```
