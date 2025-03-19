# Union CLI

The `union` CLI is the main tool developers use to interact with Union on the command line.

## Installation

The recommended way to install the union CLI outside a workflow project is to use [`uv`](https://docs.astral.sh/uv/):

```{code-block} shell
$ uv tool install union
```

This will install the `union` CLI globally on your system [as a `uv` tool](https://docs.astral.sh/uv/concepts/tools/).


## Configure the `union` CLI

To configure the `union` CLI to connect to Union Serverless, run the following command:

```{code-block} shell
$ union create login --serverless
```

To configure the `union` CLI to connect to you Union BYOC instance, run the following command:

```{code-block} shell
$ union create login --host <union-host-url>
```

where `<union-host-url>` is the URL of your Union instance.

These command will create the file `~/.union/config.yaml` with the configuration information to connect to the desired Union instance (Serverless or your own specific BYOC).

See [Quick start](../quick-start.md) for more details.

## Overriding the configuration file location

By default, the `union` CLI will look for a configuration file at `~/.union/config.yaml`.

You can override this behavior to specify a different configuration file by setting the `UNION_CONFIG` environment variable:

```{code-block} shell
export UNION_CONFIG=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `union` by using the `--config` flag:

```{code-block} shell
$ union --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

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

```{eval-rst}

.. click:: union.cli._main:main
    :prog: union
    :nested: full

```