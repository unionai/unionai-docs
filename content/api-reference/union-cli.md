# Union CLI

The `union` CLI is the main tool developers use to interact with Union on the command line.

## Installation

The recommended way to install the union CLI outside a workflow project is to use [`uv`](https://docs.astral.sh/uv/):

{{< highlight shell >}}
$ uv tool install union
{{< /highlight >}}

This will install the `union` CLI globally on your system [as a `uv` tool](https://docs.astral.sh/uv/concepts/tools/).


## Configure the `union` CLI

To configure the `union` CLI to connect to Union Serverless, run the following command:

{{< highlight shell >}}
$ union create login --serverless
{{< /highlight >}}

To configure the `union` CLI to connect to you Union BYOC instance, run the following command:

{{< highlight shell >}}
$ union create login --host <union-host-url>
{{< /highlight >}}

where `<union-host-url>` is the URL of your Union instance.

These command will create the file `~/.union/config.yaml` with the configuration information to connect to the desired Union instance (Serverless or your own specific BYOC).

See [Quick start](../quick-start.md) for more details.

## Overriding the configuration file location

By default, the `union` CLI will look for a configuration file at `~/.union/config.yaml`.

You can override this behavior to specify a different configuration file by setting the `UNION_CONFIG` environment variable:

{{< highlight shell >}}
export UNION_CONFIG=~/.my-config-location/my-config.yaml
{{< /highlight >}}

Alternatively, you can always specify the configuration file on the command line when invoking `union` by using the `--config` flag:

{{< highlight shell >}}
$ union --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
{{< /highlight >}}

## `union` CLI configuration search path

The `union` CLI will check for configuration files as follows:

First, if a `--config` option is used, it will use the specified config file.

Second, the config files pointed to by the following environment variables (in this order):

* `UNION_CONFIG`
* `UNIONAI_CONFIG`
* `UCTL_CONFIG`

Third, the following hard-coded locations (in this order):

* `~/.union/config.yaml`
* `~/.uctl/config.yaml`

If none of these are present, the CLI will raise an error.

## `union` CLI commands

```--eval-rst--

.. click:: union.cli._main:main
    :prog: union
    :nested: full

```