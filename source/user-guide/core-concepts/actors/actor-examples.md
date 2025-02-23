# Actor examples

### Refactoring from Regular Tasks to Actors

Notice that converting a non-actor workflow to use actors is as simple as replacing the `@flytekit.task` decorator with the `@actor_env.task` decorator. Additionally, task decorator arguments can be moved either to the actor environment or the actor task decorator, depending on whether they apply to the entire environment (e.g. resource specifications) or to a single task execution (e.g. caching arguments).

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/refs/heads/danielsola/se-297-actors-docs-for-customer-push/user_guide/core_concepts/actors/byoc/diff.py
:emphasize-lines: 2,3,4,5,6,7,8,9,10,11,13,18,24
:language: diff
```

```{note}
The `union` package is a superset of `flytekit` and the following examples use `union` to define Flyte tasks, workflows, resources, etc. Though actors require `union`, you may use `flytekit` for the remaining Flyte constructs of you so desire.
```

## Multiple instances of the same task

In this example, the `actor.task`-decorated task is invoked multiple times in one workflow, and will use the same `ActorEnvironment` on each invocation:

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/serverless/plus_one.py
:caption: plus_one.py

```
{@@ elif byoc or byok @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/byoc/plus_one.py
:caption: plus_one.py

```
{@@ endif @@}

## Multiple tasks

Every task execution in the following example will execute in the same `ActorEnvironment`. You can use the same environment for multiple tasks in the same workflow and tasks across workflow definitions, using both subworkflows and launchplans:

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/serverless/multiple_tasks.py
:caption: multiple_tasks.py

```
{@@ elif byoc or byok @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/byoc/multiple_tasks.py
:caption: multiple_tasks.py

```
{@@ endif @@}

## Custom PodTemplates

Both tasks in the following example will be executed in the same `ActorEnvironment`, which is created with a `PodTemplate` for additional configuration.

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/pod_template.py
:caption: pod_template.py
:language: python
```

## Example: `@actor_cache` with `map_task`

With map tasks, each task is executed within the same environment, making actors a natural fit for this pattern. If a task has an expensive operation, like model loading, caching it with `@actor_cache` can improve performance. This example shows how to cache model loading in a mapped task to avoid redundant work and save resources.

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/serverless/caching_map_task.py
:caption: caching_map_task.py

```
{@@ elif byoc or byok @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/byoc/caching_map_task.py
:caption: caching_map_task.py

```
{@@ endif @@}

## Example: Caching with Custom Objects

Finally, we can cache custom objects by defining the `__hash__` and `__eq__` methods. These methods allow `@actor_cache` to determine if an object is the same between runs, ensuring that expensive operations are skipped if the object hasn’t changed.

{@@ if serverless @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/serverless/caching_custom_object.py
:caption: caching_custom_object.py

```
{@@ elif byoc or byok @@}
```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/actors/byoc/caching_custom_object.py
:caption: caching_custom_object.py

```
{@@ endif @@}

