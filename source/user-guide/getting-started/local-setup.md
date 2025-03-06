# Local setup

{@@ if serverless @@}

In [Getting started](./index.md) we showed you how to run your first workflow right in the Union interface, in the browser.

{@@ endif @@}

In this section we will set up your local environment so that you can start building and deploying {@= Product =@} workflows from your local machine.


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

{@= Kit =@} requires Python `>=3.9,<3.13`.
We recommend using `3.12`.
You can install it with:

```{code-block} shell
$ uv python install 3.12
```

:::{admonition} Uninstall higher versions of Python
When installing Python packages "as tools" (as we do below with the `{@= kit =@}`),
`uv` will default to the latest version of Python available on your system.
If you have a version `>=3.13` installed, you will need to uninstall it since `{@= kit =@}` requires `>=3.9,<3.13`.
:::


## Install the `{@= cli =@}` CLI

Once `uv` is installed, use it to install the `{@= cli =@}` CLI by installing the `{@= kit =@}` Python package:

```{code-block} shell
$ uv tool install {@= kit =@}
```

This will make the `{@= cli =@}` CLI globally available on your system.

:::{admonition} Add the install location to your PATH
`uv` installs tools in `~/.local/bin` by default.
Make sure this location is in your `PATH`, so you can run the `union` command from anywhere.
`uv` provides a convenience command to do this: `uv tool update-shell`.

Note that later in this guide we will be running the `{@= cli =@}` CLI to run your workflows.
In those cases you will be running `{@= cli =@}` within the Python virtual environment of your workflow project.
You will not be using this globally installed instance of `{@= cli =@}`.
This instance of `{@= cli =@}` is only used during the configuration step, below, when no projects yet exist.
:::

{@@ if flyte @@}

## Install Docker and get access to a container registry

Flyte tasks are run in containers. Every container requires a container image that defines its software environment.
When developing and running Flyte tasks and workflows, an important part of the process is building those images and pushing them to a container registry.
Your Flyte installation then pulls down these images when it spins up the containers that run your tasks.

To build and push the images you need to have Docker (or an equivalent container runtime) installed on your local machine.

Go to [the Docker website](https://docs.docker.com/get-docker/) for installation directions.

You will also need access to a container registry where you can push your images.
Furthermore, the pushed images will need to be accessible to the Flyte installation you are using
(The registry must be accessible and the images themselves must also have the appropriate permissions.
For example, a public registry like `ghcr.io` with the images set to public, would work).

:::{admonition} Union simplifies image building and registry
With Union you do not need to install Docker, build images, or deal with container registries.
Union offers an in-cloud image builder and registry service that greatly simplifies this part of the development process.
See [Union image builder]() for more details.
{@# TODO: Add link #@}
:::

## Install `flytectl` to set up a local cluster

For production use you will need to install Flyte in your cloud infrastructure (see [Deployment](../../deployment/index.md)).
Here we are using a local cluster for experimentation and demonstration purposes.

To set up a local cluster you must first install the `flytectl` CLI.

:::{admonition} Flytectl vs Pyflyte
`flytectl` is different from the `pyflyte`.

`pyflyte` is a Python program and part of the `flytekit` SDK
It is the primary command-line tool used during Flyte development.

`flytectl` is a compiled binary (written in Go) and used for performing certain administrative tasks.
(see [Flytectl](../../api-reference/uctl-cli/index.md) for details)
:::

To install `flytectl`, follow these instructions:

::::{tab-set}

:::{tab-item} macOS
To install `flytectl` on a Mac, use [Homebrew](https://brew.sh/), `curl`, or download the binary manually.

**Homebrew**

```{code-block} shell
$ brew tap flyteorg/homebrew-tap
$ brew install flytectl
```

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```{code-block} shell
$ curl -sL https://ctl.flyte.org/install | sudo bash -s -- -b /usr/local/bin
```

**Manual download**

To download manually, see the [`flytectl` releases](https://github.com/flyteorg/flytectl/releases).
:::

:::{tab-item} Linux
To install `flytectl` on Linux, use `curl` or download the binary manually.

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command
(note that [jq](https://jqlang.org/) needs to be installed to run this script):

```{code-block} shell
$ curl -sL https://ctl.flyte.org/install | sudo bash -s -- -b /usr/local/bin
```

**Manual download**

To download manually, see the [`flytectl` releases](https://github.com/flyteorg/flytectl/releases).
:::

:::{tab-item} Windows
To install `flytectl` on Windows, use `curl` , or download the binary manually.

**curl**

To use `curl`, in a Linux shell (such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)), set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```{code-block} shell
$ curl -sL https://ctl.flyte.org/install | sudo bash -s -- -b /usr/local/bin
```

**Manual download**

To download manually, see the [`flytectl` releases](https://github.com/flyteorg/flytectl/releases).
:::

::::

## Start Docker and the local cluster

Once you have installed Docker and `flytectl`, do the following:

1. Start the Docker daemon.

2. Use `flytectl` to set up a local Flyte cluster by running:

```{code-block} shell
$ flytectl demo start
```

This will start a local Flyte cluster on your machine and place a configuration file in `~/.flyte/config-sandbox.yaml`
that contains the connection information to connect `pyflyte` (and `flytectl`) to that cluster.

The local Flyte cluster will be available at `localhost:30080`.

:::{admonition} Union simplifies the development cycle
With Union you do not need to install a local cluster.
You can start experimenting immediately on a full cloud deployment by connecting to Union Serverless.
You can even use the Union Workspaces in-browser IDE to quickly iterate on code.
See [Union Serverless > Getting started](https://docs.union.ai/serverless/user-guide/getting-started/index.html) for more details.
:::

{@@ elif serverless @@}

## Configure the connection to your Union Serverless instance

Next, you need to create a configuration file that contains your {@= Product =@} connection information:

```{code-block} shell
$ union create login --serverless
```

This will create the `~/.union/config.yaml` with the configuration information to connect to Union Serverless.

:::{note}
These directions apply to Union Serverless.
To configure a connection to your Union instance in Union BYOC, see the [BYOC version of this page](https://docs.union.ai/byoc/quick-start#configure-the-union-cli).
To configure a connection to your Union instance in Union BYOK, see the [BYOK version of this page](https://docs.union.ai/byok/quick-start#configure-the-union-cli).
:::

{@@ elif byoc or byok @@}

## Configure the connection to your {@= Product_full =@} instance

```{code-block} shell
$ union create login --host <union-host-url>
```

`<union-host-url>` is the URL of your Union instance, mentioned in [Getting started](./index.md#gather-your-credentials).

This will create the `~/.union/config.yaml` with the configuration information to connect to your Union instance.

:::{note}
These directions apply to Union BYOC, where you connect to your own dedicated Union instance.
To configure a connection to Union Serverless, see the [Serverless version of this page](https://docs.union.ai/serverless/quick-start#configure-the-union-cli).
:::

{@@ endif @@}

{@@ if serverless or byoc or byok @@}

By default, the `union` CLI will look for a configuration file at `~/.union/config.yaml`. (See [Union CLI](../../api-reference/union-cli.md) for more details.)
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
If you have previously used Union, you may have configuration files left over that will interfere with access to Union Serverless through the `union` CLI tool.
Make sure to remove any files in `~/.unionai/` or `~/.union/` and unset the environment variables `UNIONAI_CONFIG` and `UNION_CONFIG` to avoid conflicts.
```

{@@ elif flyte @@}

By default, the `pyflyte` and `flytectl` CLIs will look for a configuration file at `~/.union/config-sandbox.yaml`. (See [Pyflyte CLI](../../api-reference/union-cli.md) and [Flytectl CLI](../../api-reference/uctl-cli/index.md) for more details.)

You can override this behavior to specify a different configuration file by setting the `FLYTECTL_CONFIG` environment variable:

```{code-block} shell
export FLYTECTL_CONFIG=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `pyflyte` or `flytectl` by using the `--config` flag.
For example:

```{code-block} shell
$ pyflyte --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

{@@ endif}

## Check your CLI configuration

To check your CLI configuration, run:

```{code-block} shell
$ {@= cli =@} info
```

You should get a response like this:

{@@ if byoc or byok @@}

```{code-block} shell
$ union info
╭────────────────────────────────────────────────────────── Union CLI Info ─────────────────────────────────────────────────────────────╮
│                                                                                                                                       │
│ union is the CLI to interact with Union. Use the CLI to register, create and track task and workflow executions locally and remotely. │
│                                                                                                                                       │
│ Union Version    : 0.1.132                                                                                                            │
│ Flytekit Version : 1.14.3                                                                                                             │
│ Union Endpoint   : <union-host-url>                                                                                                   │
│ Config Source    : <path-to-config> file                                                                                              │
│                                                                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

For more details on connection configuration see [CLI authentication types](../administration/cli-authentication-types.md).

{@@ elif serverless @@}

```{code-block} shell
$ union info
╭────────────────────────────────────────────────────────── Union CLI Info ─────────────────────────────────────────────────────────────╮
│                                                                                                                                       │
│ union is the CLI to interact with Union. Use the CLI to register, create and track task and workflow executions locally and remotely. │
│                                                                                                                                       │
│ Union Version    : 0.1.132                                                                                                            │
│ Flytekit Version : 1.14.3                                                                                                             │
│ Union Endpoint   : serverless-1.us-east-2.s.union.ai                                                                                  │
│ Config Source    : <path-to-config> file                                                                                              │
│                                                                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

{@@ elif flyte @@}

```{code-block} shell
$ pyflyte info
╭────────────────────────────────────────────────────────── Flytekit CLI Info ──────────────────────────────────────────────────────────╮
│                                                                                                                                       │
│ This CLI is meant to be used within a virtual environment that has Flytekit installed. Ideally it is used to iterate on your Flyte    │
│ workflows and tasks.                                                                                                                  │
│                                                                                                                                       │
│ Flytekit Version: 1.15.0                                                                                                              │
│ Flyte Backend Version: <flyte-backend-version>                                                                                        │
│ Flyte Backend Endpoint: <flyte-host-url>                                                                                              │
│                                                                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

{@@ endif @@}
