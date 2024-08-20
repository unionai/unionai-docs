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
the UI at [serverless.union.ai](https://serverless.union.ai).
This is where you will be able to see your workflow executions and manage your projects:

![Union UI](/_static/images/dashboard.png)

{@@ elif byoc @@}

## Gather your credentials

After your administrator has onboarded you to Union, you should have the following at hand:

* Your Union credentials.
* The URL of your Union instance. We will refer to this as `<union-host-url>` below.

## Log into Union

Navigate to the UI at `<union-host-url>` and log in with your credentials.
Once you have logged in you should see the Union UI.
This is where you will be able to see your workflow executions and and manage your projects:

![Union UI](/_static/images/union-byoc-home.png)

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

## Install the `union` package

After setting up your virtual environment and activating it, install the `union` Python package:

{@@ if serverless @@}

```{code-block} shell
$ pip install -U union
```

:::{note}
These directions are for Union Serverless.

If you are using Union BYOC, you should [install `union` with the `[byoc]` extra package](https://docs.union.ai/byoc/quick-start#install-the-union-package).
:::

{@@ elif byoc @@}

```{code-block} shell
pip install -U "union[byoc]"
```

:::{note}
The `[byoc]` extra package includes configuration defaults specific to Union BYOC that differ from those needed for Union Serverless.

If you are using Union Serverless, you should [install `union` without the `[byoc]` extra package](https://docs.union.ai/serverless/quick-start#install-the-union-package).

You can tell whether you have the `byoc` extra package installed by running `pip list` and checking for the package `unionmeta-byoc`.
:::

{@@ endif @@}

This will install:
* The [`union` command-line tool](./api/union-cli)
* The [`union` SDK](./api/sdk/index)
* The [`flytekit` SDK](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html)

{@@ if byoc @@}

## Set up configuration for the `union` CLI

To register and run workflows on your Union instance using the `union` CLI, you will need to create a configuration file that contains your Union connection information. To do this, run the following command:

```{code-block} shell
$ union create login --host <union-host-url>
```

where `<union-host-url>` is the URL of your Union instance, mentioned above.

This will create a configuration file at `~/.union/config.yaml`.

By default, the `union` CLI will look for a configuration file at `~/.union/config.yaml`. (See [union CLI](./api/union-cli) for more details.)
You can override this behavior to specify a different configuration file by setting the `UNION_CONFIG` environment variable:

```{code-block} shell
export UNION_CONFIG=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `union` by using the `--config` flag:

```{code-block} shell
$ union --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

{@@ endif @@}

```{warning}
If you have previously used Union, you may have configuration files left over that will interfere with access to Union Serverless through the `union` CLI tool.
Make sure to remove any files in `~/.unionai/` or `~/.union/` and unset the environment variables `UNIONAI_CONFIG` and `UNION_CONFIG` to avoid conflicts.
```

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

You can run the workflow in your local Python environment with the [`union run` command](../api/union-cli.md#union-run):

```{code-block} shell
$ union run hello.py hello_world_wf
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, world!
```

Since the `@workflow` function takes an argument called `name`, you can also pass that in
as a command-line argument like this:

```{code-block} shell
$ union run hello.py hello_world_wf --name Ada
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, Ada!
```

## Run the workflow remotely on Union

To run the workflow remotely on Union, add the [`--remote` flag](../api/union-cli.md#cmdoption-union-run-r):

```{code-block} shell
$ union run --remote hello.py hello_world_wf --name "Ada"
```

The output displays a URL that links to the workflow execution in the UI:

{@@ if serverless @@}

```{code-block} shell
[✔] Go to https://serverless.union.ai/org/... to see execution in the UI.
```

Go to the UI to see the execution:

![Dashboard](/_static/images/first-execution.png)

{@@ elif byoc @@}

```{code-block} shell
[✔] Go to https://<union-host-url>/org/... to see execution in the UI.
```

Go to the UI to see the execution:

![Dashboard](/_static/images/first-execution-byoc.png)

{@@ endif @@}
