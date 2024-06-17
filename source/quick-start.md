# Quick start

In this section, we give a quick introduction to writing and running Union workflows.

{@@ if serverless @@}

## Sign up for Union Serverless

First, sign up for Union Serverless:

:::{button-link} https://signup.union.ai/
:color: secondary

Create an account
:::

Once you've received confirmation that your sign up succeeded, navigate to
the Union console at [serverless.union.ai](https://serverless.union.ai).
This is where you will be able to see your workflow executions and manage your projects:

![Union console](/_static/images/dashboard.png)

{@@ elif byoc@@}

## Gather your credentials

After your administrator has onboarded you to Union, you should have the following at hand:

* Your Union credentials.
* The URL of your Union instance. We will refer to this as `<union-host-url>` below.

## Log into Union

Navigate to the web console at `<union-host-url>` and log in with your credentials.
Once you have logged in you should see the Union console.
This is where you will be able to see your workflow executions and and manage your projects:

![Union console](/_static/images/union-byoc-home.png)

{@@ endif @@}

## Set up your Python environment

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

## Install the `unionai` package

After setting up your virtual environment and activating it, install the `unionai` Python package:

{@@ if serverless @@}

```{code-block} shell
$ pip install -U unionai
```

{@@ elif byoc @@}

::::{tab-set}

:::{tab-item} Unix/macOS

```{code-block} shell
pip install -U 'unionai[byoc]'
```

:::


:::{tab-item} Windows

```{code-block} shell
pip install -U "unionai[byoc]"
```

:::
::::

:::{note}
The `[byoc]` extra package includes configuration defaults specific to Union BYOC that differ from those needed for Serverless.
:::

{@@ endif @@}

This will install:
* The [`unionai` command-line tool](../api/unionai-cli)
* The [`unionai` SDK](../api/sdk/index)
* The [`flytekit` SDK](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html)

{@@ if serverless @@}

```{warning}
If you have previously used Union BYOC or Flyte,
you may have configuration files left over that will interfere with access to Union Serverless through the `unionai` CLI tool.
Make sure to remove any files in `~/.flyte/` or `~/.unionai/` and unset the environment variables `FLYTECTL_CONFIG` and `UNIONAI_CONFIG` to avoid conflicts.
```

{@@ endif @@}

{@@ if byoc @@}

## Set up configuration for the `unionai` CLI

To run and register tasks, workflows, and launch plans from your local machine to your Union instance, you will need to create a Union connection configuration file that contains your Union host domain.

Your Union host domain is the part of your `<union-host-url>` after the `https://`.
For example, if your `<union-host-url>` is `https://my-union-instance.com`, then your Union host domain is `my-union-instance.com`. We will refer to this as `<union-host-domain>` below.

Create your configuration file at `~/.unionai/config.yaml` as below, with `<union-host-domain>` substituted appropriately.
Note that there are two `host` values to substitute and the resulting URLs are prefixed with `dns:///` (with three slashes):

```{code-block} yaml
:emphasize-lines: 3,8

union:
  connection:
    host: dns:///<union-host-domain>
    insecure: true
  auth:
    type: Pkce
admin:
  endpoint: dns:///<union-host-domain>
  insecure: true
  authType: Pkce
```

:::{note}

By default, the `unionai` CLI will look for a configuration file at `~/.unionai/config.yaml`.
You can override this behavior to specify a different configuration file by setting the `UNIONAI_CONFIG` environment variable:

```{code-block} shell
export UNIONAI_CONFIG=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `unionai` by using the `--config` flag:

```{code-block} shell
$ unionai --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```
:::

```{warning}
If you have previously used Flyte, you may have configuration files left over that will interfere with access to Union BYOC through the `unionai` CLI tool.
Make sure to remove any files in `~/.flyte/` or unset the environment variable `FLYTECTL_CONFIG` to avoid conflicts.
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

The "Hello, world!" code contains a task and a workflow, which are Python functions decorated with the `@task` and `@workflow` decorators, respectively.
For more information, see the [task](../core-concepts/tasks/index) and [workflow](../core-concepts/workflows/index) documentation.

## Run the workflow locally in Python

You can run the workflow in your local Python environment with the [`unionai run` command](../api/unionai-cli.md#unionai-run):

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

## Run the workflow remotely on Union

To run the workflow remotely on Union, add the [`--remote` flag](../api/unionai-cli.md#cmdoption-unionai-run-r):

```{code-block} shell
$ unionai run --remote hello.py hello_world_wf --name "Ada"
```

The output displays a URL that links to the workflow execution on the Union web console:

{@@ if serverless @@}

```{code-block} shell
[✔] Go to https://serverless.union.ai/org/... to see execution in the console.
```

Go to the Union console to see the execution:

![Dashboard](/_static/images/first-execution.png)

{@@ elif byoc @@}

```{code-block} shell
[✔] Go to https://<union-host-url>/org/... to see execution in the console.
```

Go to the Union console to see the execution:

![Dashboard](/_static/images/first-execution-byoc.png)

{@@ endif @@}
