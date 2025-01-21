# Local setup

In [Getting started](./index.md) we showed you how to run your first workflow right in the Union interface, in the browser.

Now we will move on to setting up an actual project, which will allow you to run workflows on Union from your local machine.

The first step is to set up your local environment.


## A note on best practices

Union supports the full flexibility of the Python ecosystem in structuring your projects and in the choice of tools used to manage those projects.

However, in this guide we will be opinionated about some aspects of tooling, project structure and project management, in order to streamline the experience and guide users toward established best practices.

The essential guidelines are:

1. Use the [`uv` package and project manager](https://docs.astral.sh/uv/).

2. Structure your project source according to our established patterns (see [Project structure](./project-structure.md)).

3. Use a source code management system for your code. In this guide we assume you are using Git (and in some examples, specifically GitHub).


## Install uv

First, [install `uv`](https://docs.astral.sh/uv/#getting-started).
The `uv` tool is our recommended package and project manager.
It replaces `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and more.

You can, of course, use other tools, but all discussion in these pages will use `uv`,
so you will have to adapt the directions as appropriate.


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
