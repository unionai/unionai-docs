# Actors

Actors allow you to reuse a container and environment between tasks that need to maintain state. To create an actor, instantiate the [`ActorEnvironment`](../../api/union-sdk/actor.actorenvironment.md) class, then add the instance as a decorator to the task that requires that environment.

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

## Examples

### Hello world

The following example shows how to create a basic `ActorEnvironment` and use it for one task:

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/fd53b707f3158bce13746c0c68f67d27ad2f6d34/guides/02_core_concepts/actors/serverless/hello_world.py
:caption: hello_world.py

```
{@@ elif byoc @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/fd53b707f3158bce13746c0c68f67d27ad2f6d34/guides/02_core_concepts/actors/byoc/hello_world.py
:caption: hello_world.py

```
{@@ endif @@}

### Multiple instances of the same task

In this example, the `actor.task`-decorated task is invoked multiple times in one workflow, and will use the same `ActorEnvironment` on each invocation:

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/fd53b707f3158bce13746c0c68f67d27ad2f6d34/guides/02_core_concepts/actors/serverless/plus_one.py
:caption: hello_world.py

```
{@@ elif byoc @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/fd53b707f3158bce13746c0c68f67d27ad2f6d34/guides/02_core_concepts/actors/byoc/plus_one.py
:caption: hello_world.py

```
{@@ endif @@}

### Multiple tasks

Every task execution in the following example will execute in the same `ActorEnvironment`. You can use the same environment for multiple tasks in the same workflow and tasks across workflow definitions, using both subworkflows and launchplans:

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/fd53b707f3158bce13746c0c68f67d27ad2f6d34/guides/02_core_concepts/actors/serverless/multiple_tasks.py
:caption: hello_world.py

```
{@@ elif byoc @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/fd53b707f3158bce13746c0c68f67d27ad2f6d34/guides/02_core_concepts/actors/byoc/multiple_tasks.py
:caption: hello_world.py

```
{@@ endif @@}
