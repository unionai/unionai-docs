---
title: Run and deploy tasks
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Run and deploy tasks

You have seen how to configure and build the tasks that compose your project.
Now you need to decide how to execute them on your Flyte backend.

Flyte offers two distinct approaches for getting your tasks onto the backend:

**Use `flyte run` when you're iterating and experimenting:**
- Quickly test changes during development
- Try different parameters or code modifications
- Debug issues without creating permanent artifacts
- Prototype new ideas rapidly

**Use `flyte deploy` when your project is ready to be formalized:**
- Freeze a stable version of your tasks for repeated use
- Share tasks with team members or across environments
- Move from experimentation to a more structured workflow
- Create a permanent reference point (not necessarily production-ready)

This section explains both approaches and when to use each one.

## Ephemeral deployment and immediate execution

The `flyte run` CLI command and the `flyte.run()` SDK function are used to **ephemerally deploy** and **immediately execute** a task on the backend in a single step.
The task can be re-run and its execution and outputs can be observed in the **Runs list** UI, but it is not permanently added to the **Tasks list** on the backend.

Let's say you have the following file called `greeting.py`:

```python
# greeting.py

import flyte

env = flyte.TaskEnvironment(name="greeting_env")

@env.task
async def greet(message: str) -> str:
    return f"{message}!"
```

### With the `flyte run` CLI command

The general form of the command for running a task from a local file is:

```bash
flyte run <file_path> <task_name> <args>
```

So, to run the `greet` task defined in the `greeting.py` file, you would run:

```bash
flyte run greeting.py greet --message "Good morning!"
```

This command:
1. **Temporarily deploys** the task environment named `greeting_env` (held by the variable `env`) that contains the `greet` task.
2. **Executes** the `greet` function with argument `message` set to `"Good morning!"`. Note that `message` is the actual parameter name defined in the function signature.
3. **Returns** the execution results and displays them in the terminal.

### With the `flyte.run()` SDK function

You can also do the same thing programmatically using the `flyte.run()` function:

```python
# greeting.py

import flyte

env = flyte.TaskEnvironment(name="greeting_env")

@env.task
async def greet(message: str) -> str:
    return f"{message}!"

if __name__ == "__main__":
    flyte.init_from_config()
    result = flyte.run(greet, message="Good morning!")
    print(f"Result: {result}")
```

Here we add a `__main__` block to the `greeting.py` file that initializes the Flyte SDK from the configuration file and then calls `flyte.run()` with the `greet` task and its argument.
Now you can run the `greet` task on the backend just by executing the `greeting.py` file locally as a script:

```bash
python greeting.py
```

For more details on how `flyte run` and `flyte.run()` work under the hood, see [How Run Works](./how-task-run-works).

## Persistent deployment

The `flyte deploy` CLI command and the `flyte.deploy()` SDK function are used to **persistently deploy** a task environment (and all its contained tasks) to the backend.
The tasks within the deployed environment will appear in the **Tasks list** UI on the backend and can then be executed multiple times without needing to redeploy them.

### With the `flyte deploy` CLI command

The general form of the command for running a task from a local file is:

```bash
flyte deploy <file_path> <task_environment_variable>
```

So, using the same `greeting.py` file as before, you can deploy the `greeting_env` task environment like this:

```bash
flyte deploy greeting.py env
```

This command deploys the task environment *assigned to the variable `env`* in the `greeting.py` file, which is the `TaskEnvironment` named `greeting_env`.

Notice that you must specify the *variable* to which the `TaskEnvironment` is assigned (`env` in this case), not the name of the environment itself (`greeting_env`).

Deploying a task environment deploys all tasks defined within it. Here, that means all functions decorated with `@env.task`.
In this case there is just one: `greet()`.

### With the `flyte.deploy()` SDK function

You can also do the same thing programmatically using the `flyte.deploy()` function:

```python
# greeting.py

import flyte

env = flyte.TaskEnvironment(name="greeting_env")

@env.task
async def greet(message: str) -> str:
    return f"{message}!"

if __name__ == "__main__":
    flyte.init_from_config()
    deployments = flyte.deploy(env)
    print(deployments[0].summary_repr())
```

Now you can deploy the `greeting_env` task environment (and therefore the `greet()` task) just by executing the `greeting.py` file locally as a script.

```bash
python greeting.py
```

For more details on how `flyte deploy` and `flyte.deploy()` work under the hood, see [How Deployment Works](./how-task-deployment-works).

## Running already deployed tasks

If you have already deployed your task environment, you can run its tasks without redeploying by using the `flyte run` CLI command or the `flyte.run()` SDK function in a slightly different way. Alternatively, you can always initiate execution of a deployed task from the UI.

### With the `flyte run` CLI command

To run a permanently deployed task using the `flyte run` CLI command, use the special `deployed-task` keyword followed by the task reference in the format `{environment_name}.{task_name}`. For example, to run the previously deployed `greet` task from the `greeting_env` environment, you would run:

```bash
flyte run deployed-task greeting_env.greet --message "World"
```

Notice that now that the task environment is deployed, you use its name (`greeting_env`), not by the variable name to which it was assigned in source code (`env`).
The task environment name plus the task name (`greet`) are combined with a dot (`.`) to form the full task reference: `greeting_env.greet`.
The special `deployed-task` keyword tells the CLI that you are referring to a task that has already been deployed. In effect, it replaces the file path argument used for ephemeral runs.

When executed, this command will run the already-deployed `greet` task with argument `message` set to `"World"`. You will see the result printed in the terminal. You can also, of course, observe the execution in the **Runs list** UI.

### With the `flyte.run()` SDK function

You can also run already-deployed tasks programmatically using the `flyte.run()` function.
For example, to run the previously deployed `greet` task from the `greeting_env` environment, you would do:

```python
# greeting.py

import flyte

env = flyte.TaskEnvironment(name="greeting_env")

@env.task
async def greet(message: str) -> str:
    return f"{message}!"

if __name__ == "__main__":
    flyte.init_from_config()
    flyte.deploy(env)
    task = flyte.remote.Task.get("greeting_env.greet", auto_version="latest")
    result = flyte.run(task, message="Good morning!")
    print(f"Result: {result}")
```

When you execute this script locally, it will:

- Deploy the `greeting_env` task environment as before.
- Retrieve the already-deployed `greet` task using `flyte.remote.Task.get()`, specifying its full task reference as a string: `"greeting_env.greet"`.
- Call `flyte.run()` with the retrieved task and its argument.

For more details on how running already-deployed tasks works, see [How task Run works > SDK: Running deployed tasks](./how-task-run-works#running-deployed-tasks).

<!--
TODO: Add link to Flyte remote documentation when available
For details on Flyte remote functionality, see the [Flyte remote]().
-->
