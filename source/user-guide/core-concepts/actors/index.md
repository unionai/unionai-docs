# Actors

Actors allow you to reuse a container and environment between tasks, avoiding the cost of starting a new container for each task. This can be useful when you have a task that requires a lot of setup or has a long startup time.

To create an actor, instantiate the [`ActorEnvironment`](../../api-reference/union-sdk/actor.actorenvironment.md) class, then add the instance as a decorator to the task that requires that environment.

### `ActorEnvironment` parameters

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


You can learn more about the tradeoffs between actors and regular tasks, as well as the efficiency gains you can expect [here](actors-and-regular-tasks.md).

## Caching on Actor Replicas

The `@actor.cache` decorator provides a powerful mechanism to cache the results of Python callables on individual actor replicas. This is particularly beneficial for workflows involving repetitive tasks, such as data preprocessing, model loading, or initialization of shared resources, where caching can minimize redundant operations and improve overall efficiency. This avoids repetitive computation or loading processes, particularly useful for workflows that involve expensive operations like loading large datasets or initializing machine learning models. Once a callable is cached on a replica, subsequent tasks that use the same actor can access the cached result, significantly improving performance and efficiency.

### When to Use `actor.cache`

- **Shared Initialization Costs:**  
  For expensive, shared initialization processes that multiple tasks rely on.

- **Repetitive Task Execution:**  
  When tasks repeatedly require the same resource or computation on the same actor replica.

- **Complex Object Caching:**  
  Use custom Python objects as keys to define unique cache entries.

- **Avoiding Resource Contention:**  
  Ensure some tasks are explicitly run to initialize shared resources, avoiding race conditions.

Below is a simplified example showcasing the use of `@actor.cache` for caching repetitive tasks. This dummy example demonstrates caching model that is loaded by the `load_model` task.

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/serverless/caching_basic.py
:caption: caching_basic.py

```
{@@ elif byoc @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/byoc/caching_basic.py
:caption: caching_basic.py
```
```{note}
In order to get the `@actor.cache` functionality, you must pin `union` to at least `0.1.121`.
```
{@@ endif @@}

![Actor caching example 1](/_static/images/user-guide/core-concepts/actors/caching/actor-cache-example-1.png)

You can see that the first call of `evaluate` took considerable time as it involves allocating a node for the task, creating a container, and loading the model. The subsequent calls of `evaluate` execute in a fraction of the time. 

You can see examples of more advanced actor usage [here](actor-examples.md).