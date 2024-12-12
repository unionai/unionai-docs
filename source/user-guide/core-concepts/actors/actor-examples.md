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

### Refactoring from Regular Tasks to Actors

Notice that converting a non-actor workflow to use actors is as simple as replacing the @flytekit.task decorator with the @actor_env.task decorator. Additionally, task decorator arguments can be moved either to the actor environment or the actor task decorator, depending on whether they apply to the entire environment (e.g., resource specifications) or to a single task execution (e.g., caching arguments).

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/refs/heads/danielsola/se-297-actors-docs-for-customer-push/user_guide/core_concepts/actors/byoc/diff.py
:emphasize-lines: 2,3,4,5,6,7,8,9,10,11,13,18,24
:language: diff
```

