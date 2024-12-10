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

## Examples

### Hello world

The following example shows how to create a basic `ActorEnvironment` and use it for one task:

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/serverless/hello_world.py
:caption: hello_world.py

```
{@@ elif byoc @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/byoc/hello_world.py
:caption: hello_world.py

```
{@@ endif @@}

### Multiple instances of the same task

In this example, the `actor.task`-decorated task is invoked multiple times in one workflow, and will use the same `ActorEnvironment` on each invocation:

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/serverless/plus_one.py
:caption: plus_one.py

```
{@@ elif byoc @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/byoc/plus_one.py
:caption: plus_one.py

```
{@@ endif @@}

### Multiple tasks

Every task execution in the following example will execute in the same `ActorEnvironment`. You can use the same environment for multiple tasks in the same workflow and tasks across workflow definitions, using both subworkflows and launchplans:

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/serverless/multiple_tasks.py
:caption: multiple_tasks.py

```
{@@ elif byoc @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/byoc/multiple_tasks.py
:caption: multiple_tasks.py

```
{@@ endif @@}

### Custom PodTemplates

Both tasks in the following example will be executed in the same `ActorEnvironment`, which is created with a `PodTemplate` for additional configuration.

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/pod_template.py
:caption: pod_template.py
:language: python
```

```{code-block} diff
--- lao	2002-02-21 23:30:39.942229878 -0800
+++ tzu	2002-02-21 23:30:50.442260588 -0800
@@ -1,7 +1,6 @@
-The Way that can be told of is not the eternal Way;
-The name that can be named is not the eternal name.
 The Nameless is the origin of Heaven and Earth;
-The Named is the mother of all things.
+The named is the mother of all things.
+
 Therefore let there always be non-being,
   so we may see their subtlety,
 And let there always be being,
@@ -9,3 +8,6 @@
 The two are the same,
 But after they are produced,
   they have different names.
+They both may be called deep and profound.
+Deeper and more profound,
+The door of all subtleties!
```
