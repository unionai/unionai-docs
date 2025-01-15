# UnionRemote examples

## Registering and running a workflow

In the following example we register and run a workflow and retrieve its output:

```{code-block} shell
:caption: A simple project

├── remote.py
└── workflow
    ├── __init__.py
    └── example.py
```

The workflow code that will be registered and run on Union resides in the `workflow` directory and consists of an empty `__init__.py` file and the workflow and task code in `example.py`:

```{code-block} python
:caption: example.py
import os
from union import task, workflow, FlyteFile


@task()
def create_file(message: str) -> FlyteFile:
    with open("data.txt", "w") as f:
        f.write(message)
    return FlyteFile(path="data.txt")

@workflow
def my_workflow(message: str) -> FlyteFile:
    f = create_file(message)
    return f
```

The file `remote.py` contains the `UnionRemote` logic. It is not part of the workflow code, and is meant to be run on your local machine.

```{code-block} python
:caption: remote.py
from union import UnionRemote
from workflow.example import my_workflow


def run_workflow():
    remote = UnionRemote()
    remote.fast_register_workflow(entity=my_workflow)
    execution = remote.execute(
        entity=my_workflow,
        inputs={"message": "Hello, world!"},
        wait=True)
    output = execution.outputs["o0"]
    print(output)
    with open(output, "r") as f:
        read_lines = f.readlines()
    print(read_lines)


if __name__ == "__main__":
    run_workflow()
```

You can run the code with:

```{code-block} shell
$ python remote.py
```

The `my_workflow` workflow and the `create_file` task is registered and run.
Once the workflow completes, the output is passed back to the `run_workflow` function and printed out.

The output is also be available via the UI, in the **Outputs** tab of the `create_file` task details view:

![Outputs](/_static/images/user-guide/development-cycle/union-remote/outputs.png)

The steps above demonstrates the simplest way of registering and running a workflow with `UnionRemote`.
For more options and details see [API reference > UnionRemote > Entrypoint](../../../api-reference/union-remote/entrypoint.md).

{@@ if byoc @@}

## Terminating all running executions for a workflow

This example shows how to terminate all running executions in a given workflow name.

```{code-block} python
from union.remote import UnionRemote
from dataclasses import dataclass
import json
from flytekit.configuration import Config
from flytekit.models.core.execution import NodeExecutionPhase

@dataclass
class Execution:
    name: str
    link: str

SOME_LARGE_LIMIT = 5000
PHASE = NodeExecutionPhase.RUNNING
WF_NAME = "your_workflow_name"
EXECUTIONS_TO_IGNORE = ["some_execution_name_to_ignore"]
PROJECT = "your_project"
DOMAIN = "production"
ENDPOINT = "union.example.com"

remote = UnionRemote(
    config=Config.for_endpoint(endpoint=ENDPOINT),
    default_project=PROJECT,
    default_domain=DOMAIN,
)

executions_of_interest = []

executions = remote.recent_executions(limit=SOME_LARGE_LIMIT)

for e in executions:
    if e.closure.phase == PHASE:
        if e.spec.launch_plan.name == WF_NAME:
            if e.id.name not in EXECUTIONS_TO_IGNORE:
                execution_on_interest = Execution(name=e.id.name, link=f"https://{ENDPOINT}/console/projects/{PROJECT}/domains/{DOMAIN}/executions/{e.id.name}")
                executions_of_interest.append(execution_on_interest)
                remote.terminate(e, cause="Terminated manually via script.")


with open('terminated_executions.json', 'w') as f:
    json.dump([{'name': e.name, 'link': e.link} for e in executions_of_interest], f, indent=2)

print(f"Terminated {len(executions_of_interest)} executions.")
```

## Rerunning all failed executions of a workflow

This example shows how to identify all failed executions from a given workflow since a certain time, and re-run them with the same inputs and a pinned workflow version.

```{code-block} python
import datetime
import pytz
from union.remote import UnionRemote
from flytekit.models.core.execution import NodeExecutionPhase

SOME_LARGE_LIMIT = 5000
WF_NAME = "your_workflow_name"
PROJECT = "your_project"
DOMAIN = "production"
ENDPOINT = "union.example.com"
VERSION = "your_target_workflow_version"

remote = UnionRemote(
    config=Config.for_endpoint(endpoint=ENDPOINT),
    default_project=PROJECT,
    default_domain=DOMAIN,
)

executions = remote.recent_executions(limit=SOME_LARGE_LIMIT)

failures = [
    NodeExecutionPhase.FAILED,
    NodeExecutionPhase.ABORTED,
    NodeExecutionPhase.FAILING,
]

# time of the last successful execution
date = datetime.datetime(2024, 10, 30, tzinfo=pytz.UTC)

# filter executions by name
filtered = [execution for execution in executions if execution.spec.launch_plan.name == WF_NAME]

# filter executions by phase
failed = [execution for execution in filtered if execution.closure.phase in failures]

# filter executions by time
windowed = [execution for execution in failed if execution.closure.started_at > date]

# get inputs for each execution
inputs = [remote.sync(execution).inputs for execution in windowed]

# get new workflow version entity
workflow = remote.fetch_workflow(name=WF_NAME, version=VERSION)

# execute new workflow for each failed previous execution
[remote.execute(workflow, inputs=X) for X in inputs]
```

{@@ endif @@}