# Getting started

In this section, we give a quick introduction to writing and running Union workflows.

{@@ if serverless @@}

## Signing up for a Union Serverless account

First, sign up for Union Serverless:

:::{button-link} https://signup.union.ai/
:color: secondary

Create an account
:::

Once you've received confirmation that you're off the waitlist, navigate to
[serverless.union.ai](https://serverless.union.ai) to see the dashboard:

![Dashboard](/_static/images/dashboard.png)

{@@ endif @@}

## Setting up your local environment

Set up a Python virtual environment with `conda`, `venv` or a similar tool.

Python 3.8 or higher is required. Python 3.11 is the current recommended version.

::::{tab-set}

:::{tab-item} conda
Install `conda` using [Miniconda](https://docs.anaconda.com/free/miniconda/index.html), then run the following to create
a new Python environment:

```{code-block} shell
conda create -n quick-start python=3.11
conda activate quick-start
```
:::

:::{tab-item} venv
Install Python 3.11 from your package manager or from [Python.org](https://www.python.org/downloads/), then run the following to create a virtual environment:

```{code-block} shell
python -m venv .venv
source .venv/bin/activate
```
:::

::::

After setting up your virtual environment and activating it, install the `unionai` Python package::

```{code-block} shell
pip install unionai
```

This will install the `unionai` SDK, which ships with the `unionai` CLI tool,
and the `flytekit` SDK.

## Create a "Hello, world!" workflow

To create an example workflow file, copy the following into a file called `hello.py`:

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

In this example, the file `hello.py` contains a task and a workflow.
These are simply Python functions decorated with the `@task` and `@workflow` decorators, respectively.
The workflow is the top-level construct which you run. The workflow, in turn, invokes the task.

### Run the example workflow in your local Python environment

Run the workflow with `unionai run`. The syntax is:

```{code-block} shell
$ unionai run <script_path> <task_or_workflow_name>
```

In this case:

```{code-block} shell
$ unionai run hello.py hello_world_wf
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, world!
```

Since the `@workflow` function takes an argument called `name`, you can also pass that in:

```{code-block} shell
$ unionai run hello.py hello_world_wf --name Ada
```

Then, you should see the following output:

```{code-block} shell
Running Execution on local.
Hello, Ada!
```

{@@ if serverless @@}

To run the workflow remotely on Union:

```{code-block} shell
$ unionai run --remote hello.py hello_world_wf --name "Ada"
```

This command prints an URL that links to the execution on Union's web console:

```{code-block} shell
[✔] Go to https://serverless.union.ai/org/... to see execution in the console.
```

Congratulations, you have just run your first workflow on Union!

{@@ elif byoc @@}

## Next steps

In the following sections, we will walk through setting up a simple but production-level Union project and deploying it to your Union instance in the cloud.

{@@ endif @@}