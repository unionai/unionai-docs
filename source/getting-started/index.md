# Getting started

In this section, we give a quick introduction to writing and running Union workflows.

{@@ if serverless @@}

## Sign up for Union Serverless

First, sign up for Union Serverless:

:::{button-link} https://signup.union.ai/
:color: secondary

Create an account
:::

Once you've received confirmation that your sign up succeeded, navigate to
the Union console at [serverless.union.ai](https://serverless.union.ai):

![Union console](/_static/images/dashboard.png)

{@@ elif byoc@@}

## Gather your credentials

After your administrator has onboarded you to Union, you should have the following at hand:

* Your Union credentials.
* The URL of your Union instance. We will refer to this as `<union-host-url>` below.

## Log into Union

Navigate to the Union console at `<union-host-url>` and log in with your credentials.
Once you have logged in you should see the Union console:

![Union console](/_static/images/union-byoc-home.png)

{@@ endif @@}

## Set up your local environment

### Set up your Python environment

Set up a Python virtual environment with `conda`, `venv` or a similar tool.

Python 3.8 or higher is required. Python 3.11 is the current recommended version.

::::{tab-set}

:::{tab-item} conda
Install `conda` using [Miniconda](https://docs.anaconda.com/free/miniconda/index.html), then run the following to create
a new Python environment:

```{code-block} shell
$ conda create -n union-env python=3.11
$ conda activate union-env
```
:::

:::{tab-item} venv
Install Python 3.11 from your package manager or from [Python.org](https://www.python.org/downloads/), then run the following to create a virtual environment:

```{code-block} shell
$ python -m venv .venv
$ source .venv/bin/activate
```
:::

::::

### Install the `unionai` Python package

After setting up your virtual environment and activating it, install the `unionai` Python package::

```{code-block} shell
$ pip install unionai
```

This will install:
* The `unionai` command-line tool
* The `unionai` SDK
* The `flytekit` SDK

{@@ if byoc @@}

### Set up configuration for the `unionai` CLI tool

In your home directory:

* Create a directory called `.unionai`
* Within that directory, create a file called `config.yaml` with the following content,
substituting `<union-host-url>` with the URL of your Union instance:

```{code-block} yaml
union:
  connection:
    host: <union-host-url>
    insecure: true
  auth:
    type: Pkce
admin:
  endpoint: <union-host-url>
  insecure: true
  authType: Pkce
```

Add the following environment variable export to your shell profile and make sure the profile takes effect:

```{code-block} shell
export UNIONAI_CONFIG=~/.unionai/config.yaml
```

{@@ endif @@}

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

The file `hello.py` contains a task and a workflow.
These are simply Python functions decorated with the `@task` and `@workflow` decorators, respectively.
The workflow is the top-level construct that, in turn, invokes the task.

## Run the workflow in Python locally

You can run the workflow in your local Python environment like this:

```{code-block} shell
$ unionai run hello.py hello_world_wf
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, world!
```

Since the `@workflow` function takes an argument called `name`, you can also pass that in
as a command-line argument like this:

```{code-block} shell
$ unionai run hello.py hello_world_wf --name Ada
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, Ada!
```

## Run the workflow on Union in the cloud

To run the workflow remotely on Union, add the `--remote` flag:

```{code-block} shell
$ unionai run --remote hello.py hello_world_wf --name "Ada"
```

The output displays a URL that links to the workflow execution on the Union web console:

```{code-block} shell
[✔] Go to https://serverless.union.ai/org/... to see execution in the console.
```

Go to the Union console to see the execution:

![Dashboard](/_static/images/first-execution.png)
