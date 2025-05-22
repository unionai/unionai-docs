---
title: Local setup
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Local setup

{{< variant serverless >}}
{{< markdown >}}

In [Getting started](./_index) we showed you how to run your first workflow right in the {{< key product_name >}} interface, in the browser.

{{< /markdown >}}
{{< /variant >}}

In this section we will set up your local environment so that you can start building and deploying {{< key product_name >}} workflows from your local machine.

## Install `uv`

First, [install `uv`](https://docs.astral.sh/uv/#getting-started).

> [!NOTE] Using `uv` as best practice
> The `uv` tool is our [recommended package and project manager](https://docs.astral.sh/uv/).
> It replaces `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and more.
>
> You can, of course, use other tools,
> but all discussion in these pages will use `uv`,
> so you will have to adapt the directions as appropriate.

## Ensure the correct version of Python is installed

{{< key kit_name >}} requires Python `>=3.9,<3.13`.
We recommend using `3.12`.
You can install it with:

```shell
$ uv python install 3.12
```

> [!NOTE] Uninstall higher versions of Python
> When installing Python packages "as tools" (as we do below with the `{{< key kit >}}`),
> `uv` will default to the latest version of Python available on your system.
> If you have a version `>=3.13` installed, you will need to uninstall it since `{{< key kit >}}` requires `>=3.9,<3.13`.

## Install the `{{< key cli >}}` CLI

Once `uv` is installed, use it to install the `{{< key cli >}}` CLI by installing the `{{< key kit >}}` Python package:

```shell
$ uv tool install {{< key kit >}}
```

This will make the `{{< key cli >}}` CLI globally available on your system.

> [!NOTE] Add the installation location to your PATH
> `uv` installs tools in `~/.local/bin` by default.
> Make sure this location is in your `PATH`, so you can run the `{{< key cli >}}` command from anywhere.
> `uv` provides a convenience command to do this: `uv tool update-shell`.
>
> Note that later in this guide we will be running the `{{< key cli >}}` CLI to run your workflows.
> In those cases you will be running `{{< key cli >}}` within the Python virtual environment of your workflow project.
> You will not be using this globally installed instance of `{{< key cli >}}`.
> This instance of `{{< key cli >}}` is only used during the configuration step, below, when no projects yet exist.

{{< variant flyte >}}
{{< markdown >}}

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

## Install `flytectl` to set up a local cluster

For production use you will need to install Flyte in your cloud infrastructure (see [Deployment](../../deployment)).
Here we are using a local cluster for experimentation and demonstration purposes.

To set up a local cluster you must first install the `flytectl` CLI.

> [!NOTE] Flytectl vs Pyflyte
> `flytectl` is different from the `pyflyte`.
>
> `pyflyte` is a Python program and part of the `flytekit` SDK
> It is the primary command-line tool used during Flyte development.
>
> `flytectl` is a compiled binary (written in Go) and used for performing certain administrative tasks.
> (see [Flytectl](../../api-reference/uctl-cli) for details)

To install `flytectl`, follow these instructions:


{{< /markdown >}}
{{< tabs >}}
{{< tab "macOS" >}}
{{< markdown >}}

To install `flytectl` on a Mac, use [Homebrew](https://brew.sh/), `curl`, or download the binary manually.

**Homebrew**

```shell
$ brew tap flyteorg/homebrew-tap
$ brew install flytectl
```

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://ctl.flyte.org/install | sudo bash -s -- -b /usr/local/bin
```

**Manual download**

To download manually, see the [`flytectl` releases](https://github.com/flyteorg/flytectl/releases).

{{< /markdown >}}
{{< /tab >}}

{{< tab "Linux" >}}
{{< markdown >}}

To install `flytectl` on Linux, use `curl` or download the binary manually.

**curl**

To use `curl`, set `BINDIR` to the installation location (it defaults to `./bin`) and run the following command
(note that [jq](https://jqlang.org/) needs to be installed to run this script):

```shell
$ curl -sL https://ctl.flyte.org/install | sudo bash -s -- -b /usr/local/bin
```

**Manual download**

To download manually, see the [`flytectl` releases](https://github.com/flyteorg/flytectl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< tab "Windows" >}}
{{< markdown >}}

To install `flytectl` on Windows, use `curl` , or download the binary manually.

**curl**

To use `curl`, in a Linux shell (such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)), set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://ctl.flyte.org/install | sudo bash -s -- -b /usr/local/bin
```

**Manual download**

To download manually, see the [`flytectl` releases](https://github.com/flyteorg/flytectl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}
{{< markdown >}}

## Start Docker and the local cluster

Once you have installed Docker and `flytectl`, do the following:

1. Start the Docker daemon.

2. Use `flytectl` to set up a local Flyte cluster by running:

```shell
$ flytectl demo start
```

This will start a local Flyte cluster on your machine and place a configuration file in `~/.flyte/config-sandbox.yaml`
that contains the connection information to connect `pyflyte` (and `flytectl`) to that cluster.

The local Flyte cluster will be available at `localhost:30080`.

> [!NOTE] Try Flyte technology through {{< key product_name >}} Serverless
> Alternatively, you can try using Flyte technology through {{< key product_name >}} Serverless.
> With {{< key product_name >}} Serverless you do not need to install a local cluster and can start
> experimenting immediately on a full cloud deployment.
> You can even use the Workspaces in-browser IDE to quickly iterate on code.
> See [{{< key product_name >}} Serverless > Getting started]({{< docs_home serverless >}}/user-guide/getting-started) for more details.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}

## Configure the connection to your cluster

Next, you need to create a configuration file that contains your {{< key product_name >}} connection information:

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless >}}
{{< markdown >}}

```shell
$ {{< key cli >}} create login --serverless
```

This will create the `~/.union/config.yaml` with the configuration information to connect to {{< key product_name >}} Serverless.

> [!NOTE] These directions apply to {{< key product_name >}} Serverless
> To configure a connection to your {{< key product_name >}} instance in {{< key product_name >}} BYOC, see the
> [BYOC version of this page]({{< docs_home byoc >}}/user-guide/getting-started/local-setup#configure-the-connection-to-your-cluster).
> To configure a connection to your {{< key product_name >}} instance in {{< key product_name >}} Self-managed, see the
> [Self-managed version of this page]({{< docs_home selfmanaged >}}/user-guide/getting-started/local-setup#configure-the-connection-to-your-cluster).

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

```shell
$ {{< key cli >}} create login --host <union-host-url>
```

`<union-host-url>` is the URL of your {{< key product_name >}} instance, mentioned in [Getting started](.#gather-your-credentials).

This will create the `~/.union/config.yaml` with the configuration information to connect to your {{< key product_name >}} instance.

> [!NOTE]
> These directions apply to {{< key product_name >}} BYOC and Self-managed, where you connect to your own dedicated {{< key product_name >}} instance.
> To configure a connection to {{< key product_name >}} Serverless, see the
> [Serverless version of this page]({{< docs_home serverless >}}/user-guide/getting-started/local-setup#configure-the-connection-to-your-cluster).

See [Running in a local cluster](../development-cycle/running-in-a-local-cluster) for more details on the format of the `yaml` file.
<!-- TODO: Fix this target page to have a more generic title (it applies to all clusters) and fix its content -->

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

By default, the {{< key cli_name >}} CLI will look for a configuration file at `~/.union/config.yaml`. (See [{{< key cli_name >}} CLI](../../api-reference/union-cli) for more details.)
You can override this behavior to specify a different configuration file by setting the `{{< key config_env >}}` environment variable:

```shell
$ export {{< key config_env >}}=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `{{< key cli >}}` by using the `--config` flag.
For example:

```shell
$ {{< key cli >}} --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

> [!WARNING]
> If you have previously used {{< key product_name >}}, you may have configuration files left over that will interfere with
> access to {{< key product_name >}} Serverless through the {{< key cli_name >}} CLI tool.
> Make sure to remove any files in `~/.unionai/` or `~/.union/` and unset the environment
> variables `UNIONAI_CONFIG` and `UNION_CONFIG` to avoid conflicts.

See [Running in a local cluster](../development-cycle/running-in-a-local-cluster) for more details on
the format of the `yaml` file.
<!-- TODO: Fix this target page to have a more generic title (it applies to all clusters) and fix its content -->

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

## Configure the connection to your cluster

To configure the connection from `pyflyte` and `flytectl` to your Flyte instance, set the `FLYTECTL_CONFIG` environment variable to point to the configuration file that `flytectl` created:

```shell
$ export FLYTECTL_CONFIG=~/.flyte/config-sandbox.yaml
```

This will allow you to interact with your local Flyte cluster.

To interact with a Flyte cluster in the cloud you will need to adjust the configuration
and point the environment variable to the new configuration file.

Alternatively, you can always specify the configuration file on the command line when invoking `pyflyte` or `flytectl` by using the `--config` flag.
For example:

```shell
$ pyflyte --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

See [Running in a local cluster](../development-cycle/running-in-a-local-cluster) for more details on the format of the `yaml` file.
<!-- TODO: Fix this target page to have a more generic title (it applies to all clusters) and fix its content -->

{{< /markdown >}}
{{< /variant >}}

## Check your CLI configuration

To check your CLI configuration, run:

```shell
$ {{< key cli >}} info
```

You should get a response like this:

{{< variant byoc selfmanaged >}}
{{< markdown >}}

```shell
$ {{< key cli >}} info
╭────────────────────────────────────────────────────────── {{< key product_name >}} CLI Info ─────────────────────────────────────────────────────────────╮
│                                                                                                                                       │
│ {{< key cli >}} is the CLI to interact with {{< key product_name >}}. Use the CLI to register, create and track task and workflow executions locally and remotely. │
│                                                                                                                                       │
│ {{< key product_name >}} Version    : 0.1.132                                                                                                            │
│ Flytekit Version : 1.14.3                                                                                                             │
│ {{< key product_name >}} Endpoint   : <union-host-url>                                                                                                   │
│ Config Source    : <path-to-config> file                                                                                              │
│                                                                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

For more details on connection configuration see [Authentication](../development-cycle/authentication).

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless >}}
{{< markdown >}}

```shell
$ {{< key cli >}} info
╭────────────────────────────────────────────────────────── {{< key product_name >}} CLI Info ─────────────────────────────────────────────────────────────╮
│                                                                                                                                       │
│ {{< key cli >}} is the CLI to interact with {{< key product_name >}}. Use the CLI to register, create and track task and workflow executions locally and remotely. │
│                                                                                                                                       │
│ {{< key product_name >}} Version    : 0.1.132                                                                                                            │
│ Flytekit Version : 1.14.3                                                                                                             │
│ {{< key product_name >}} Endpoint   : serverless-1.us-east-2.s.union.ai                                                                                  │
│ Config Source    : <path-to-config> file                                                                                              │
│                                                                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

```shell
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

{{< /markdown >}}
{{< /variant >}}
