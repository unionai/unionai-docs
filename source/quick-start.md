# Quick start

This section gives you a quick introduction to writing and running Union workflows.

{@@ if serverless @@}

## Sign up for Union Serverless

First, sign up for Union Serverless:

:::{button-link} https://signup.union.ai/
:color: secondary

Create an account
:::

Once you've received confirmation that your sign up succeeded, navigate to
the UI at [serverless.union.ai](https://serverless.union.ai).

To get started, try selecting the default project, called `flytesnacks`, from the list of projects.
This will take you to `flytesnacks` project dashboard:

![Union UI](/_static/images/quick-start/serverless-dashboard.png)


{@@ elif byoc @@}

## Gather your credentials

After your administrator has onboarded you to Union, you should have the following at hand:

* Your Union credentials.
* The URL of your Union instance. We will refer to this as `<union-host-url>` below.

## Log into Union

Navigate to the UI at `<union-host-url>` and log in with your credentials.
Once you have logged in you should see the Union UI.

To get started, try selecting the default project, called `flytesnacks`, from the list of projects.
This will take you to `flytesnacks` project dashboard:

![Union UI](/_static/images/quick-start/byoc-dashboard.png)

{@@ endif @@}

{@@ if serverless @@}

## Run your first workflow

Run your first workflow on a Union Workspace.

```{note}
See the [local development](user-guide/first-workflow/index) guide to run your
first workflow in your local machine instead.
```

::::{tab-set}

:::{tab-item} {octicon}`play` Start workspace

Go to the Workspaces page by clicking on the `Workspaces` button on the
left-hand navigation bar.

Start the default workspace by clicking on the `default` workspace item.

![Start workspace](/_static/gifs/start-workspace.gif)

:::

:::{tab-item} {octicon}`book` Open workspace
When the `Status` is `Active` on the `default` workspace, you can click on it
again to open the workspace.

*It will take a few moments to load the VSCode interface.*

![Open workspace](/_static/gifs/open-workspace.gif)

:::

:::{tab-item} {octicon}`check-circle-fill` Complete walkthrough
Once the workspace is open, you should see a VSCode interface in your browser.

![Workspace VSCode](/_static/images/quick-start/serverless-workspace-vscode.png)

In the walkthrough, you'll learn how to:

1. 🤖 Train a model
2. 🔀 Parallelize model training
3. 📘 Iterate on a Jupyter Notebook

:::

:::{tab-item} {octicon}`stop` Stop workspace
The workspace will terminate after 20 minutes of idle time, but you can also
stop it manually on the Workspaces page.

![Open workspace](/_static/gifs/stop-workspace.gif)
:::

::::

## Next steps

Once you've completed the walkthrough, run more examples in the [User Guide](user-guide/index)
and [Tutorials](tutorials/index) in the workspace.


{@@ elif byoc @@}

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
Install Python using your package manager or from [Python.org](https://www.python.org/downloads/), then run the following to create a virtual environment:

```{code-block} shell
$ python -m venv .venv
$ source .venv/bin/activate
```
:::

::::

## Install the `union` package

After setting up your virtual environment and activating it, install the `union` Python package:

```{code-block} shell
$ pip install -U union
```

This will install:
* The [`union` command-line tool](api-reference/union-cli)
* The [`union` SDK](api-reference/union-sdk)
* The [`flytekit` SDK](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html)

## Configure the `union` CLI

To register and run workflows on your Union instance using the `union` CLI, you will need to create a configuration file that contains your Union connection information.
To do this, run the following command:

{@@ if serverless @@}

```{code-block} shell
$ union create login --serverless
```
This will create the `~/.union/config.yaml` with the configuration information to connect to Union Serverless.

:::{note}
These directions apply to Union Serverless. To configure a connection to your Union instance in Union BYOC, see the [BYOC version of this page](https://docs.union.ai/byoc/quick-start#configure-the-union-cli).
:::

{@@ elif byoc @@}

```{code-block} shell
$ union create login --host <union-host-url>
```

where `<union-host-url>` is the URL of your Union instance, mentioned above.

This will create the `~/.union/config.yaml` with the configuration information to connect to your Union instance.

:::{note}
These directions apply to Union BYOC, where you connect to your own dedicated Union instance. To configure a connection to Union Serverless, see the [Serverless version of this page](https://docs.union.ai/serverless/quick-start#configure-the-union-cli).
:::

{@@ endif @@}

By default, the `union` CLI will look for a configuration file at `~/.union/config.yaml`. (See [union CLI](../api-reference/union-cli) for more details.)
You can override this behavior to specify a different configuration file by setting the `UNION_CONFIG` environment variable:

```{code-block} shell
export UNION_CONFIG=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `union` by using the `--config` flag:

```{code-block} shell
$ union --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

```{warning}
If you have previously used Union, you may have configuration files left over that will interfere with access to Union Serverless through the `union` CLI tool.
Make sure to remove any files in `~/.unionai/` or `~/.union/` and unset the environment variables `UNIONAI_CONFIG` and `UNION_CONFIG` to avoid conflicts.
```

{@@ if byoc @@}
For more details on connection configuration see [CLI authentication types](guide/administration/cli-authentication-types).
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
For more information, see the [task](guide/core-concepts/tasks/index) and [workflow](guide/core-concepts/workflows/index) documentation.

## Run the workflow locally in Python

You can run the workflow in your local Python environment with the [`union run` command](../api-reference/union-cli.md#union-cli-commands):

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

To run the workflow remotely on Union, add the [`--remote` flag](../api-reference/union-cli.md#union-cli-commands):

```{code-block} shell
$ union run --remote hello.py hello_world_wf --name "Ada"
```

The output displays a URL that links to the workflow execution in the UI:

{@@ if serverless @@}

```{code-block} shell
[✔] Go to https://serverless.union.ai/org/... to see execution in the UI.
```

{@@ elif byoc @@}

```{code-block} shell
[✔] Go to https://<union-host-url>/org/... to see execution in the UI.
```

{@@ endif @@}

Click the link to see the execution in the UI.

{@@ endif @@}