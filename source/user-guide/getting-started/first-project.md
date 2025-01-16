# First project

In this section we will:

* Install and configure the tools you need to work with Union.
* Set up a Union project on your local machine.
* Run the project code locally.
* Deploy the project to your Union instance in the cloud and run it there.


## A note on best practices

Union supports the full flexibility of the Python ecosystem in structuring your projects and in the choice of tools used to manage those projects.

However, in this guide we will be opinionated about some aspects of tooling, project structure and project management, in order to streamline the experience and guide users toward established best practices.

The essential guidelines are:

1. Use the [`uv` package and project manager](https://docs.astral.sh/uv/).
   You can, of course, use other tools, but all discussion in these pages will use `uv`, so you will have to adapt the directions as appropriate
   (if you are reluctant to switch to `uv`, just try it, we strongly recommend it!)

2. Structure your project source according to our established patterns (see [Project structure](./project-structure.md)).
   After years of experience we have come up with some good organizing principles that will make your life easier. Follow them.

3. Use a source code management system for your code. In this guide we assume you are using Git (and in some examples, specifically GitHub).


## Install uv

First, [install `uv`](https://docs.astral.sh/uv/#getting-started).


## Ensure the correct version of Python is installed

Union requires Python `>=3.9,<3.13`.
We recommend using `3.12`.
You can install it with:

```{code-block} shell
$ uv python install 3.12
```

:::{admonition} Uninstall higher versions of Python
When installing Python packages "as tools" (as we do below with the `union` CLI),
`uv` will default to the latest version of Python available on your system.
If you have a version `>=3.13` installed, you will need to uninstall it since `union` requires `>=3.9,<3.13`.
:::


## Install union CLI

Once `uv` is installed, use it to install the `union` CLI:

```{code-block} shell
$ uv tool install union
```

This will install the `union` CLI as a globally available tool on your system.

:::{admonition} Add the install location to your PATH
`uv` installs tools in `~/.local/bin` by default.
Make sure this location is in your `PATH`, so you can run the `union` command from anywhere.
`uv` provides a convenience command to do this: `uv tool update-shell`.
:::


## Configure the `union` CLI

To register and run workflows on your Union instance using the `union` CLI,
you will need to create a configuration file that contains your Union connection information.
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

`<union-host-url>` is the URL of your Union instance, mentioned in [Getting started](./index.md#gather-your-credentials).

This will create the `~/.union/config.yaml` with the configuration information to connect to your Union instance.

:::{note}
These directions apply to Union BYOC, where you connect to your own dedicated Union instance. To configure a connection to Union Serverless, see the [Serverless version of this page](https://docs.union.ai/serverless/quick-start#configure-the-union-cli).
:::

{@@ endif @@}

By default, the `union` CLI will look for a configuration file at `~/.union/config.yaml`. (See [Union CLI](../../api-reference/union-cli.md) for more details.)
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

For more details on connection configuration see [CLI authentication types](../administration/cli-authentication-types.md).

{@@ endif @@}


## Initialize a new project

To create a new project, run the following command:

```{code-block} shell
$ union init first-project
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
For more information, see the [tasks](./user-guide/core-concepts/tasks/index.md) and [workflows](./user-guide/core-concepts/workflows/index.md) documentation.

## Run the workflow locally in Python

You can run the workflow in your local Python environment with the [`union run` command](./api-reference/union-cli.md#union-cli-commands):

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

To run the workflow remotely on Union, add the [`--remote` flag](./api-reference/union-cli.md#union-cli-commands):

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




## Next step

{@@ if serverless @@}

The next step is [Running the workflow](./running-the-workflow.md).

{@@ elif byoc @@}

The next step is [Setting up container image handling](./setting-up-container-image-handling.md).

{@@ endif @@}
