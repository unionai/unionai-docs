---
title: Running tasks
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Running tasks

Flyte SDK lets you seamlessly switch between running your workflows locally on your machine and running them remotely on your Union/Flyte instance.

Furthermore, you perform these actions either programmatically from within Python code or from the command line using the `flyte` CLI.

## Running remotely

### From the command-line

To run your code on your Union/Flyte instance, you can use the `flyte run` command without the `--local` flag:

```shell
flyte run hello.py main
```

This deploys your code to the configured Union/Flyte instance and runs it immediately (Since no explicit `--config` is specified, the configuration found according to the [default configuration search](../local-setup#use-the-configuration-file-implicitly) will be used).

### From Python

To run your workflow remotely from Python, use [`flyte.run()`](../../api-reference/flyte-sdk/packages/flyte#run) by itself, like this:

{{< code file="/external/unionai-examples/v2/user-guide/getting-started/running/run_from_python.py" lang="python" >}}

This is the approach we use throughout our examples in this guide.
We execute the script, thus invoking the `flyte.run()` function, with the top-level task as a parameter.
The `flyte.run()` function then deploys and runs the code in that file itself on your remote Union/Flyte instance.

## Running locally

### From the command-line

To run your code on your local machine, you can use the `flyte run` command with the `--local` flag:

```shell
flyte run --local hello.py main
```

### From Python

To run your workflow locally from Python, you chain [`flyte.with_runcontext()`](../../api-reference/flyte-sdk/packages/flyte#with_runcontext) with [`flyte.run()`](../../api-reference/flyte-sdk/packages/flyte#run) and specify the run `mode="local"`, like this:

{{< code file="/external/unionai-examples/v2/user-guide/getting-started/running/run_local_from_python.py" lang="python" >}}

Running your workflow locally is useful for testing and debugging, as it allows you to run your code without deploying it to a remote instance.
It also lets you quickly iterate on your code without the overhead of deployment.

Obviously, if your code relies on remote resources or services, you will need to mock those in your local environment, or temporarily work around any missing functionality.
At the very least, local execution can be used to catch immediate syntax errors and other relatively simple issues before deploying your code to a remote instance.

<!--


Usages as intended in final design:

# Deploy a specific environment from a file
flyte deploy examples/hello.py my_env

# Deploy all environments in a file
flyte deploy examples/hello.py

# Deploy all environments in a directory
flyte deploy examples/

# Recursively deploy all environments in a directory and its subdirectories
flyte deploy --recursive examples/

# Other options
--project -p
--domain -d
--version
--dry-run,--dryrun
--copy-style [loaded_modules|all|none]
--ignore-load-errors
--help






TODO: Add back when properly available

## Deploying to your Union/Flyte instance without running

You can also deploy your workflow to your Union/Flyte instance without running it immediately
### Deploying from the command-line

To deploy your workflow to your Union/Flyte instance without running it immediately, use the [`flyte deploy`]() command:

```shell
flyte [TOP_LEVEL_OPTIONS] deploy [SUB_COMMAND_OPTIONS] [FILE] [TASK_ENV_VAR]
```

* `TOP_LEVEL_OPTIONS`: Options that apply to the `flyte` command as a whole, such as `--config`, `--endpoint`, etc. See the [Flyte CLI documentation](../../api-reference/flyte-cli#flyte) for more details.
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

You can also deploy your workflow programmatically using the [`flyte.deploy()`](../../api-reference/flyte-sdk/packages/flyte#deploy) function:

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

After deploying your workflow, you can run it using the same [`flyte run`](../../api-reference/flyte-cli#flyte-run) command:

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
result = flyte.run(deployed_task, name="Ada")
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
<!--
TODO: Check this code for accuracy, relevance
This was generated by an LLM doc writer




## Managing Remote Executions

Once your workflows are running, you can connect to and manage them remotely from anywhere. This includes monitoring active executions, accessing completed runs, and retrieving results.

### Accessing Existing Runs

#### Get Run by Name

```python
import flyte.remote

# Connect to a specific run
run = flyte.remote.Run.get("my-run-name")

print(f"Status: {run.phase}")
print(f"URL: {run.url}")

# Wait for completion if still running
if not run.done():
    run.wait()

print(f"Final status: {run.phase}")
```

#### List Recent Runs

```python
# List all recent runs
async for run in flyte.remote.Run.listall():
    print(f"Run: {run.name}, Status: {run.phase}")

# Filter by project/domain
async for run in flyte.remote.Run.listall(
    filters="project=my-project AND domain=production"
):
    print(f"Production run: {run.name}")
```

### Monitoring Running Executions

#### Real-time Log Streaming

```python
# Connect to running execution
run = flyte.remote.Run.get("training-run-12345")

# Stream logs in real-time
run.show_logs(follow=True)

# Get specific log lines
logs = run.show_logs(max_lines=100, show_ts=True)
print(logs)
```

#### Watching Execution Progress

```python
# Monitor execution status changes
async for details in run.watch():
    print(f"Status: {details.phase}")
    if details.has_logs():
        recent_logs = details.logs()[-10:]  # Last 10 lines
        print(f"Recent logs: {recent_logs}")

    if details.done():
        break
```

#### Getting Execution Details

```python
# Get comprehensive run information
run = flyte.remote.Run.get("my-run")

print(f"Created: {run.created_at}")
print(f"Duration: {run.duration}")
print(f"Resources used: {run.resources}")

# Get task-level details
for node in run.node_executions:
    print(f"Task: {node.display_name}, Status: {node.phase}")
```

### Cross-Environment Management

#### Multi-Environment Monitoring

```python
# Monitor production from development environment
prod_config = {
    "endpoint": "https://prod-cluster.com",
    "project": "my-project",
    "domain": "production"
}

dev_config = {
    "endpoint": "https://dev-cluster.com",
    "project": "my-project",
    "domain": "development"
}

# Check production status
flyte.init(**prod_config)
prod_runs = [run async for run in flyte.remote.Run.listall()]
print(f"Production runs: {len(prod_runs)}")

# Switch to development
flyte.init(**dev_config)
dev_runs = [run async for run in flyte.remote.Run.listall()]
print(f"Development runs: {len(dev_runs)}")
```

#### Environment Comparison

```python
# Compare same workflow across environments
def get_workflow_runs(endpoint, domain, workflow_name):
    flyte.init(endpoint=endpoint, domain=domain)
    return [
        run async for run in flyte.remote.Run.listall()
        if workflow_name in run.name
    ]

prod_runs = get_workflow_runs("prod-cluster.com", "production", "ml-pipeline")
staging_runs = get_workflow_runs("staging-cluster.com", "staging", "ml-pipeline")

print(f"Production: {len(prod_runs)} runs")
print(f"Staging: {len(staging_runs)} runs")
```

### Accessing Results and Data

#### Retrieving Outputs

```python
# Get outputs from completed run
run = flyte.remote.Run.get("completed-run")

if run.done() and run.phase == "SUCCEEDED":
    outputs = run.outputs()
    print(f"Results: {outputs}")
else:
    print(f"Run not completed: {run.phase}")
```

#### Downloading Artifacts

```python
# Download files produced by remote execution
run = flyte.remote.Run.get("data-processing-run")
outputs = run.outputs()

# Download specific output files
if "processed_data_path" in outputs:
    local_path = flyte.remote.download_file(
        outputs["processed_data_path"],
        local_path="./downloaded_data.csv"
    )
    print(f"Downloaded to: {local_path}")
```

## Common Remote Management Use Cases

### Production Monitoring

```python
# Monitor critical production workflows
import asyncio
from datetime import datetime, timedelta

async def monitor_production():
    flyte.init_from_config("prod-config.yaml")

    while True:
        # Check for failed runs in last hour
        recent_runs = [
            run async for run in flyte.remote.Run.listall()
            if run.created_at > datetime.now() - timedelta(hours=1)
        ]

        failed_runs = [run for run in recent_runs if run.phase == "FAILED"]

        if failed_runs:
            for run in failed_runs:
                print(f"ALERT: Failed run {run.name}")
                # Get error details
                logs = run.show_logs(max_lines=50)
                print(f"Error logs: {logs}")

        await asyncio.sleep(300)  # Check every 5 minutes

# Run monitoring
asyncio.run(monitor_production())
```

### Debugging Failed Executions

```python
# Investigate failed runs
def debug_failed_run(run_name):
    run = flyte.remote.Run.get(run_name)

    print(f"Run: {run.name}")
    print(f"Status: {run.phase}")
    print(f"Error: {run.error}")

    # Get detailed logs
    logs = run.show_logs(max_lines=1000)
    print("Full logs:")
    print(logs)

    # Check individual task failures
    for node in run.node_executions:
        if node.phase == "FAILED":
            print(f"Failed task: {node.display_name}")
            task_logs = node.show_logs()
            print(f"Task logs: {task_logs}")

debug_failed_run("failed-training-run-456")
```

### Result Comparison

```python
# Compare results across different runs
def compare_model_runs(run_names):
    results = {}

    for run_name in run_names:
        run = flyte.remote.Run.get(run_name)
        if run.done() and run.phase == "SUCCEEDED":
            outputs = run.outputs()
            results[run_name] = outputs.get("model_accuracy", 0)

    print("Model comparison:")
    for run_name, accuracy in results.items():
        print(f"{run_name}: {accuracy:.3f}")

    best_run = max(results.items(), key=lambda x: x[1])
    print(f"Best model: {best_run[0]} with accuracy {best_run[1]:.3f}")

compare_model_runs([
    "model-v1-run-123",
    "model-v2-run-124",
    "model-v3-run-125"
])
```

## Best Practices for Remote Management

### Connection Management

```python
# Use context managers for connection handling
class RemoteConnection:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        flyte.init(**self.config)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup if needed
        pass

# Usage
with RemoteConnection(prod_config) as conn:
    runs = [run async for run in flyte.remote.Run.listall()]
    print(f"Found {len(runs)} runs")
```

### Error Handling

```python
import flyte.errors

def safe_remote_access(run_name):
    try:
        run = flyte.remote.Run.get(run_name)
        return run.outputs() if run.done() else None
    except flyte.errors.NotFoundError:
        print(f"Run {run_name} not found")
        return None
    except flyte.errors.RuntimeSystemError as e:
        print(f"System error: {e}")
        return None
```

### Efficient Querying

```python
# Use filters to reduce network overhead
async def get_recent_failed_runs():
    # More efficient than fetching all runs
    async for run in flyte.remote.Run.listall(
        filters="phase=FAILED AND created_at>2024-01-01",
        sort_by=("created_at", "desc"),
        limit=50
    ):
        yield run
```
-->