# Getting started

In this section, we give a quick introduction to writing and running Union workflows on your local machine.

To get started with **Union.ai**, you will need to do the following:

* Install [Python 3.8 or higher](https://www.python.org/downloads/)
* Install [Flytekit](https://github.com/flyteorg/flytekit) with `pip install -U flytekit`.

## Create a "Hello, world!" workflow

To create an example workflow file, copy the following into a file called `example.py`:

```{code-block} python
from flytekit import task, workflow

@task
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@workflow
def hello_world_wf(name: str = 'world') -> str:
    res = say_hello(name=name)
    return res
```

## Tasks and workflows

In this example, the file `example.py` contains a task and a workflow.
These are simply Python functions decorated with the `@task` and `@workflow` decorators, respectively.
The workflow is the top-level construct which you run. The workflow, in turn, invokes the task.

### Run the example workflow in a local Python environment

Run the workflow with `pyflyte run`. The syntax is:

```{code-block} shell
$ pyflyte run <script_path> <task_or_workflow_name>
```

In this case:

```{code-block} shell
$ pyflyte run example.py hello_world_wf
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, world!
```

Since the `@workflow` function takes an argument called `name`, you can also pass that in:

```{code-block} shell
$ pyflyte run example.py hello_world_wf --name Ada
```

Then, you should see the following output:

```{code-block} shell
Running Execution on local.
Hello, Ada!
```

## Next steps

In the following sections, we will walk through setting up a simple but production-level Union project and deploying it to your Union instance in the cloud.

```{toctree}
:maxdepth: 2
:hidden:

installing-development-tools
creating-the-project
looking-at-the-dependencies
looking-at-the-workflow-code
running-in-a-local-python-environment
running-in-a-local-cluster
setting-up-the-project-on-union
deploying-the-project-on-union
more-resources
```
