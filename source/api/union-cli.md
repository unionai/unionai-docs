# union CLI

The `union` CLI is the main tool developers use to interact with Union on the command line.

## Installation

To install the latest version of the `union` CLI, run the following command:

```{code-block} shell
$ pip install -U union
```

This will install:
* The `union` command line tool
* The [`union` SDK](./sdk/index)
* The [`flytekit` SDK](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html)

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

See [Quick start](../index.md#quick-start) for more details.

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

.. click:: flytekit.clis.sdk_in_container.pyflyte:main
    :prog: union
    :nested: full
    :commands: backfill, build, create, delete, execution, fetch, get, info, init, launchplan, local-cache, metrics, package, register, run, serialize, serve, update

```