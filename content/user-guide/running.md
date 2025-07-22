---
title: Running
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Running

Flyte SDK lets you seamlessly switch between running your workflows locally on your machine and running them remotely on your Union/Flyte instance.

Furthermore, you perform these actions either programmatically from within Python code or from the command line using the `flyte` CLI.

## Running remotely

### From the command-line

To run your code on your Union/Flyte instance, you can use the `flyte run` command without the `--local` flag:

```shell
flyte run hello.py main --name "Ada"
```

### From Python

To run your workflow remotely from Python, use [`flyte.run()`](../api-reference/flyte-sdk/packages/flyte#run) by itself, like this:

```python
# hello.py

... # Your sub-task definitions here

@env.task
def main(name: str):
     ... # The main task logic here

if __name__ == "__main__":
    flyte.run(main, name="Ada")
```

This is the approach we use throughout our examples in this guide.
We execute the script, thus invoking the `flyte.run()` function, with the top-level task as a parameter.
The `flyte.run()` function then takes care of

* Bundles your code and sends to your Union/Flyte instance.
* Kicking off the execution of the top-level task.

## Running locally

### From the command-line

To run your code on your local machine, you can use the `flyte run` command with the `--local` flag:

```shell
flyte run --local hello.py main --name "Ada"
```

### From Python

To run your workflow locally from Python, you chain [`flyte.with_runcontext()`](../api-reference/flyte-sdk/packages/flyte#with_runcontext) with [`flyte.run()`](../api-reference/flyte-sdk/packages/flyte#run) and specify the run `mode="local"`, like this:

```python
# hello.py

... # Your sub-task definitions here

@env.task
def main(name: str):
     ... # The main task logic here

if __name__ == "__main__":
    flyte.with_runcontext(mode="local").run(main, name="Ada")
```

Running your workflow locally is useful for testing and debugging, as it allows you to run your code without deploying it to a remote instance.
It also lets you quickly iterate on your code without the overhead of deployment.

Obviously, if your code relies on remote resources or services, you will need to mock those in your local environment, or temporarily work around any missing functionality.
At the very least, local execution can be used to catch immediate syntax errors and other relatively simple issues before deploying your code to a remote instance.


<!-- TODO Add when supported

## Deploying to your Union/Flyte instance without running

You can also deploy your workflow to your Union/Flyte instance without running it immediately

### Deploying from the command-line

To deploy your workflow to your Union/Flyte instance without running it immediately, use the [`flyte deploy`]() command:

```shell
flyte [TOP_LEVEL_OPTIONS] deploy [SUB_COMMAND_OPTIONS] [FILE] [TASK_ENV_VAR]
```

* `TOP_LEVEL_OPTIONS`: Options that apply to the `flyte` command as a whole, such as `--config`, `--endpoint`, etc. See the [Flyte CLI documentation](../api-reference/flyte-cli#flyte) for more details.
* `SUB_COMMAND_OPTIONS`: Options that apply to the `deploy` sub-command. These are:
    * `--project | -p` `<string>`: The project to which this command applies.
    * `--domain | -d` `<string>`: The domain to which this command applies.
    * `--version | -v` `<string>`: The version of the deployment (optional).
    * `--dry-run`: Preview the deployment without actually deploying.
    * `--copy-style` `<option>`: The copy style to use when deploying the task. Options are `loaded_modules`, `inline`, or `none`.
* `FILE`: Path to the Python file containing the `TaskEnvironment` to deploy.
* `TASK_ENV_VAR`: The Python variable within the Python file to which the `TaskEnvironmewnt` object is assigned (often this is simply `env`).

For example:

```shell
flyte deploy --version "v1.0.0" hello.py env
```

### Deploying programmatically

You can also deploy your workflow programmatically using the [`flyte.deploy()`](../api-reference/flyte-sdk/packages/flyte#deploy) function:

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def my_task() -> str:
    return "Hello from my_task"

if __name__ == "__main__":
    flyte.init_from_config()
    d = flyte.deploy(env)
    print(d.summary_repr())
```

You can also deploy with additional options:

```python
deployment = flyte.deploy(
    env,
    dryrun=True,
    version="v1.0.0",
    copy_style="loaded_modules"
)
```

### Running a deployed workflow from the UI

Once your workflow is deployed, you can run it from the Union/Flyte web interface.

The UI will provide you with a live view of your workflow execution, including logs, task status, and outputs.

You can also get the direct URL to a running workflow programmatically:

```python
run = flyte.run(main, name="Ada")
print(f"View in UI: {run.url}")
```

### Running a deployed workflow from the CLI

After deploying your workflow, you can run it using the same [`flyte run`](../api-reference/flyte-cli#flyte-run) command:

```shell
flyte run hello.py main --name "Ada"
```

You can also follow the logs in real-time:

```shell
flyte run --follow hello.py main --name "Ada"
```

To check the status of your runs:

```shell
# List all runs
flyte get run

# Get details of a specific run
flyte get run "run-name"

# Get logs from a run
flyte get logs "run-name"
```

### Running a deployed workflow programmatically

There are several ways to run a deployed workflow programmatically:

#### Using flyte.run() with a deployed task

```python
import flyte

# Initialize your Flyte client
flyte.init_from_config("config.yaml")

# Run the deployed task
run = flyte.run(main, name="Ada")
print(f"Run URL: {run.url}")

# Wait for completion
run.wait()
print(f"Run completed with status: {run.phase}")
```

#### Using flyte.remote.Task.get() for reference tasks

For running tasks that are already deployed and versioned:

```python
import flyte.remote

# Get a deployed task by name and version
deployed_task = flyte.remote.Task.get("main", version="v1.0.0")

# Or get the latest version
deployed_task = flyte.remote.Task.get("main", auto_version="latest")

# Run the deployed task
result = await deployed_task(name="Ada")
```

#### Using run context for more control

```python
run = flyte.with_runcontext(
    name="my-custom-run",
    project="my-project",
    domain="development",
    env={"MY_VAR": "value"},
    labels={"team": "data-science"}
).run(main, name="Ada")
```
-->