# Local setup

{@@ if serverless @@}

In [Getting started](./index.md) we showed you how to run your first workflow right in the Union.ai interface, in the browser.

{@@ endif @@}

In this section we will set up your local environment so that you can start building and deploying Union.ai workflows from your local machine.


## Install `uv`

First, [install `uv`](https://docs.astral.sh/uv/#getting-started).

:::{admonition} Using `uv` as best practice
The `uv` tool is our [recommended package and project manager](https://docs.astral.sh/uv/).
It replaces `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and more.

You can, of course, use other tools,
but all discussion in these pages will use `uv`,
so you will have to adapt the directions as appropriate.
:::

## Ensure the correct version of Python is installed

Union.ai requires Python `>=3.9,<3.13`.
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


## Install the `union` CLI

Once `uv` is installed, use it to install the `union` CLI:

```{code-block} shell
$ uv tool install union
```

This will install the `union` CLI as a globally available tool on your system.

:::{admonition} Add the install location to your PATH
`uv` installs tools in `~/.local/bin` by default.
Make sure this location is in your `PATH`, so you can run the `union` command from anywhere.
`uv` provides a convenience command to do this: `uv tool update-shell`.

Note that later in this guide we will be running the `union` CLI to run your workflows.
In those cases you will be running `union` within the Python virtual environment of your workflow project.
You will not be using this globally installed instance of `union`.
This instance of `union` is only used during the configuration step, below, when no projects yet exist.
:::

## Configure the `union` CLI

Next, you need to create a configuration file that contains your Union.ai connection information.
To do this, run the following command:

{@@ if serverless @@}

```{code-block} shell
$ union create login --serverless
```
This will create the `~/.union/config.yaml` with the configuration information to connect to Union.ai Serverless.

:::{note}
These directions apply to Union.ai Serverless.
To configure a connection to your Union.ai instance in Union.ai BYOC, see the [BYOC version of this page](https://docs.union.ai/byoc/quick-start#configure-the-union-cli).
:::

{@@ elif byoc @@}

```{code-block} shell
$ union create login --host <union-host-url>
```

`<union-host-url>` is the URL of your Union.ai instance, mentioned in [Getting started](./index.md#gather-your-credentials).

This will create the `~/.union/config.yaml` with the configuration information to connect to your Union.ai instance.

:::{note}
These directions apply to Union.ai BYOC, where you connect to your own dedicated Union.ai instance.
To configure a connection to Union.ai Serverless, see the [Serverless version of this page](https://docs.union.ai/serverless/quick-start#configure-the-union-cli).
:::

{@@ endif @@}

By default, the `union` CLI will look for a configuration file at `~/.union/config.yaml`. (See [Union.ai CLI](../../api-reference/union-cli.md) for more details.)
You can override this behavior to specify a different configuration file by setting the `UNION_CONFIG` environment variable:

```{code-block} shell
export UNION_CONFIG=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `union` by using the `--config` flag.
For example:

```{code-block} shell
$ union --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

```{warning}
If you have previously used Union.ai, you may have configuration files left over that will interfere with access to Union.ai Serverless through the `union` CLI tool.
Make sure to remove any files in `~/.unionai/` or `~/.union/` and unset the environment variables `UNIONAI_CONFIG` and `UNION_CONFIG` to avoid conflicts.
```

## Check your `union` CLI configuration

To check your `union` CLI configuration, run:

```{code-block} shell
$ union info
```

You should get a response like this:

{@@ if byoc @@}

```{code-block} shell
$ union info
╭────────────────────────────────────────────────────────── Union.ai CLI Info ─────────────────────────────────────────────────────────────╮
│                                                                                                                                       │
│ union is the CLI to interact with Union.ai. Use the CLI to register, create and track task and workflow executions locally and remotely. │
│                                                                                                                                       │
│ Union.ai Version    : 0.1.132                                                                                                            │
│ Flytekit Version : 1.14.3                                                                                                             │
│ Union.ai Endpoint   : <union-host-url>                                                                                                   │
│ Config Source    : <path-to-config> file                                                                                              │
│                                                                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

For more details on connection configuration see [CLI authentication types](../administration/cli-authentication-types.md).

{@@ elif serverless @@}

```{code-block} shell
$ union info
╭────────────────────────────────────────────────────────── Union.ai CLI Info ─────────────────────────────────────────────────────────────╮
│                                                                                                                                       │
│ union is the CLI to interact with Union.ai. Use the CLI to register, create and track task and workflow executions locally and remotely. │
│                                                                                                                                       │
│ Union.ai Version    : 0.1.132                                                                                                            │
│ Flytekit Version : 1.14.3                                                                                                             │
│ Union.ai Endpoint   : serverless-1.us-east-2.s.union.ai                                                                                  │
│ Config Source    : <path-to-config> file                                                                                              │
│                                                                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

{@@ endif @@}
