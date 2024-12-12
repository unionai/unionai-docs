# Actors

Actors allow you to reuse a container and environment between tasks, avoiding the cost of starting a new container for each task. This can be useful when you have a task that requires a lot of setup or has a long startup time.

To create an actor, instantiate the [`ActorEnvironment`](../../api-reference/union-sdk/actor.actorenvironment.md) class, then add the instance as a decorator to the task that requires that environment.

## `ActorEnvironment` parameters

{@@ if serverless @@}
* **container_image:** The container image to use for the task. Defaults to `cr.union.ai/union/unionai:py3.11-latest`.
{@@ elif byoc @@}
* **container_image:** The container image to use for the task. Defaults to `cr.flyte.org/flyteorg/flytekit:py3.11-latest`.
{@@ endif @@}
* **environment:** Environment variables as key, value pairs in a Python dictionary.
* **limits:** Compute resource limits.
* **replica_count:** The number of workers to provision that are able to accept tasks.
* **requests:** Compute resource requests per task.
* **secret_requests:** Keys (ideally descriptive) that can identify the secrets supplied at runtime. For more information, see [Managing secrets](../development-cycle/managing-secrets).
* **ttl_seconds:** How long to keep the Actor alive while no tasks are being run.


