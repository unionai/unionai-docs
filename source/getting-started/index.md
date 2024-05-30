# Getting started

In this section, we give a quick introduction to writing and running Union workflows on your local machine.

To get started with **Union.ai**, you will need to do the following:

* Install [Python 3.8 or higher](https://www.python.org/downloads/)
* Install [`unionai`](https://pypi.org/project/unionai/) with `pip install -U unionai`

```{note}
Installing `unionai` will install both the `unionai` and `flytekit` SDKs, along with the `unionai` command-line tool.
```

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

Run the workflow with `unionai run`. The syntax is:

```{code-block} shell
$ unionai run <script_path> <task_or_workflow_name>
```

In this case:

```{code-block} shell
$ unionai run example.py hello_world_wf
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, world!
```

Since the `@workflow` function takes an argument called `name`, you can also pass that in:

```{code-block} shell
$ unionai run example.py hello_world_wf --name Ada
```

Then, you should see the following output:

```{code-block} shell
Running Execution on local.
Hello, Ada!
```

## Next steps

In the following sections, we will walk through setting up a simple but production-level Union project and deploying it to your Union instance in the cloud.
