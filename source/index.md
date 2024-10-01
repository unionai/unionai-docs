# Union

Union AI orchestrator empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience.

* Run complex AI workloads with unparalleled performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale or compliance.

## Deployment models

Union is available in two deployment options: **Serverless** and **BYOC** (Bring Your Own Cloud).

{@@ if serverless @@}

* **Union Serverless** is a turnkey solution that takes care of all the infrastructure for you.
  All you need to do is sign up through your GitHub account and start running your workflows.<br/>
  **You are currently in the Union Serverless docs**.<br/>
  To get started, follow the [quick start guide](#quick-start) below.

* **Union BYOC** lets you keep your data and workflow code on your infrastructure, but has Union manage it for you.
  It also offers more control over your hardware and other advanced features.<br/>
  Switch to the Union BYOC docs [here](https://docs.union.ai/byoc).

{@@ elif byoc @@}

* **Union BYOC** lets you keep your data and workflow code on your infrastructure, but has Union manage it for you.
  It also offers more control over your hardware and other advanced features.<br/>
  **You are currently in the Union BYOC docs**.<br/>
  To get started, follow the [quick start guide](#quick-start) below.

* **Union Serverless** is a turnkey solution that takes care of all the infrastructure for you.
  All you need to do is sign up through your GitHub account and start running your workflows.<br/>
  Switch to the Union Serverless docs [here](https://docs.union.ai/serverless).

{@@ endif @@}

## Quick start

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

```{code-block} shell
$ pip install -U union
```

This will install:
* The [`union` command-line tool](api/union-cli)
* The [`union` SDK](api/union-sdk)
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
These directions apply to Union Serverless. To configure a connection to your Union instance in Union BYOC, see the [BYOC version of this page](https://docs.union.ai/byoc/index.html#configure-the-union-cli).
:::

{@@ elif byoc @@}

```{code-block} shell
$ union create login --host <union-host-url>
```

where `<union-host-url>` is the URL of your Union instance, mentioned above.

This will create the `~/.union/config.yaml` with the configuration information to connect to your Union instance.

:::{note}
These directions apply to Union BYOC, where you connect to your own dedicated Union instance. To configure a connection to Union Serverless, see the [Serverless version of this page](https://docs.union.ai/serverless/index.html#configure-the-union-cli).
:::

{@@ endif @@}

By default, the `union` CLI will look for a configuration file at `~/.union/config.yaml`. (See [union CLI](../api/union-cli) for more details.)
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
For more information, see the [task](./core-concepts/tasks/index) and [workflow](./core-concepts/workflows/index) documentation.

## Run the workflow locally in Python

You can run the workflow in your local Python environment with the [`union run` command](../api/union-cli.md#union-cli-commands):

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

To run the workflow remotely on Union, add the [`--remote` flag](../api/union-cli.md#union-cli-commands):

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

:::{note}
When you use `union create login --host <union-host-url>` to configure the `union` CLI, this creates a `config.yaml` file
configured for a Proof Key of Code Exchange (PKCE) mechanism. This is one of three authentication options, including DeviceFlow and
ClientSecret. In short, PKCE opens a browser window allowing you to login, DeviceFlow returns a URL you can navigate to,
and ClientSecret authenticates via a pre-configured secret. If you are using Union in a headless fashion, either on a
VM, connecting to a machine via SSH, in CI/CD, etc., DeviceFlow and ClientSecret should be considered.
See [CLI authentication](administration/cli-authentication.md) for more information.
:::