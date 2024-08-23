# union CLI

The `union` CLI is the main tool developers use to interact with Union on the command line. It is a Python program that provides commands for developing, testing, and deploying workflows.

:::{note}
If you are a Union administrator or if you need to interact with Union in a CI/CD environment, you may want to use the [`uctl` CLI](uctl-cli/index) instead. The `uctl` CLI is a binary executable that provides system management functions, along with much of the functionality of the `union` CLI, but in a package that doesn't require a Python environment to run.
:::

## Installation

To install the latest version of the `union` CLI, run the following command:

{@@ if serverless @@}

```{code-block} shell
$ pip install -U union
```

{@@ elif byoc @@}

```{code-block} shell
pip install -U "union[byoc]"
```

{@@ endif @@}

This will install:
* The `union` command line tool
* The [`union` SDK](./sdk/index)
* The [`flytekit` SDK](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html)

{@@ if serverless @@}

:::{note}
These directions are for Union Serverless.

If you are using Union BYOC, you should [install `union` with the `[byoc]` extra package](https://docs.union.ai/byoc/api/union-cli).
:::

{@@ elif byoc @@}

:::{note}
The `[byoc]` extra package includes configuration defaults specific to Union BYOC that differ from those needed for Union Serverless.

If you are using Union Serverless, you should [install `union` without the `[byoc]` extra package](https://docs.union.ai/serverless/api/union-cli).

You can tell whether you have the `byoc` extra package installed by running `pip list` and checking for the package `unionmeta-byoc`.
:::

{@@ endif @@}

## Configuration

{@@ if serverless @@}

`union` will automatically connect to Union Serverless. You do not need to create a configuration file.

```{warning}
If you have previously used Union, you may have existing configuration files that will interfere with command line access to Union Serverless.

To avoid connection errors, remove any configuration files in the `~/.unionai/` or `~/.union/` directories and unset the environment variables `UNIONAI_CONFIG` and `UNION_CONFIG`.
```

{@@ elif byoc @@}

To create a configuration file that contains your Union connection information, run the following command, replacing `<union-host-url>` with the URL of your Union instance:

```{code-block} shell
$ union create login --host <union-host-url>
```

This will create a configuration file at `~/.union/config.yaml`.

```{note}
PKCE is the default authentication type. To specify a different authentication type in the configuration file, see [CLI authentication types](../../administration/cli-authentication-types).
```

### Configuration file location hierarchy

By default, the `union` CLI will use the configuration file at `~/.union/config.yaml` to connect to your Union instance unless you override it with the `--config` flag or by setting an environment variable that points to a configuration file. `union` searches for configuration files in the following order:

* `--config <path-to-config>` flag
* `UNION_CONFIG` environment variable
* `UNIONAI_CONFIG` environment variable
* `UCTL_CONFIG` environment variable
* `~/.union/config.yaml` file
* `~/.uctl/config.yaml` file

{@@ endif @@}

## Commands

```{eval-rst}

.. click:: flytekit.clis.sdk_in_container.pyflyte:main
    :prog: union
    :nested: full
    :commands: backfill, build, create, delete, execution, fetch, get, info, init, launchplan, local-cache, metrics, package, register, run, serialize, serve, update

```