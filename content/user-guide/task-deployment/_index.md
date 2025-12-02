---
title: Task deployment and run
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Task deployment and run

You have seen how to configure and build the tasks that compose your project.
In this section we will explain how to deploy those tasks to the Flyte backend and execute them.

## Basic deployment

In Flyte, you move your code from your local machine to your Flyte backend by *deploying* the `TaskEnvironment`s that contain your tasks.

### With the `flyte deploy` CLI command

For example, let's say you have the following task environment and task defined in a file called `my_example.py`:

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def my_task(name: str) -> str:
    return f"Hello, {name}!"
```

Assuming you have a [valid Flyte configuration](../getting-started/local-setup) (a `config.yaml` that points to your Flyte backend and includes a default project and domain)
and the [`flyte` package installed](../getting-started/#install-the-flyte-package) in your prevailing Python `venv`, then you can deploy your `my_env` task environment like this:

```bash
flyte deploy my_example.py env
```

This command deploys the task environment *assigned to the variable `env`* in the `my_example.py` file to your Flyte backend.

Notice that you must specify the *variable* to which the `TaskEnvironment` is assigned (`env` in this case), not the name of the environment itself (`my_env`).

Deploying a task environment deploys all tasks defined within it. Here, that means all tasks decorated with `@env.task`. In this case there is just one: `my_task`.

### With the `flyte.deploy()` SDK function

You can also deploy a task environment programmatically using the `flyte.deploy()` function.

Let's add some code to our `my_example.py` file to deploy the `env` task environment when the file is run as a script:

```python
# my_example.py

import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def my_task(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    flyte.init_from_config()
    deployment = flyte.deploy(env)
    print(deployment[0].summary_repr())
```

Now you can deploy the `env` task environment by running the `my_example.py` as a script:

```bash
python my_example.py
```

The same deployment occurs: the `my_env` task environment is deployed to your Flyte backend, including its task `my_task`.

For a detailed explanation of what happens during deployment, see [How Deployment Works](./how-task-deployment-works).

## Deploy and run in one step

While `flyte deploy` only deploys your task environments to the backend, `flyte run` can both deploy and execute tasks in a single command, making it ideal for development and testing workflows.

### Running with automatic deployment

You can run a task directly from your local code without explicitly deploying first:

```bash
flyte run my_example.py my_task --name "World"
```

This command:
1. **Deploys** the task environment containing `my_task` (if not already deployed or if code has changed)
2. **Executes** the `my_task` function with the provided arguments
3. **Returns** the execution results

The deployment happens automatically behind the scenes using the same process as `flyte deploy`, but then immediately launches an execution.

### Running already deployed tasks

If you have already deployed your task environment, you can run tasks without redeploying by using the `deployed-task` syntax:

```bash
flyte run deployed-task my_env.my_task --name "World"
```

This approach:
- **Skips deployment** entirely, using the already-deployed task
- **Executes faster** since no deployment overhead is involved
- **Uses the deployed version** of your code, not your local changes

The task reference format is `{environment_name}.{task_name}` where:
- `environment_name` is the `name` property of your `TaskEnvironment` (`"my_env"` in our example)
- `task_name` is the function name of your task (`"my_task"` in our example)

### SDK execution with `flyte.run()`

You can also run tasks programmatically using the `flyte.run()` function:

```python
# my_example.py

import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def my_task(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    flyte.init_from_config()

    # Deploy and run in one step
    result = flyte.run(my_task, name="World")
    print(f"Result: {result}")

    # Or run an already deployed task
    result = flyte.run("my_env.my_task", name="World")
    print(f"Result: {result}")
```

For more details on how running works under the hood, see [How Run Works](./how-task-run-works).