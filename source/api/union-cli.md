# union CLI

The `union` CLI is the main tool developers use to interact with Union on the command line.

## Installation

To install the latest version of the `union` CLI, run the following command:

{@@ if serverless @@}

```{code-block} shell
$ pip install -U union
```

:::{note}
These directions are for Union Serverless.

If you are using Union BYOC, you should [install `union` with the `[byoc]` extra package](https://docs.union.ai/byoc/quick-start#install-the-union-package).
:::

{@@ elif byoc @@}

```{code-block} shell
pip install -U "union[byoc]"
```

:::{note}
The `[byoc]` extra package includes configuration defaults specific to Union BYOC that differ from those needed for Union Serverless.

If you are using Union Serverless, you should [install `union` without the `[byoc]` extra package](https://docs.union.ai/serverless/quick-start#install-the-union-package).

You can tell whether you have the `byoc` extra package installed by running `pip list` and checking for the package `unionmeta-byoc`.
:::

{@@ endif @@}

This will install:
* The `union` command line tool
* The [`union` SDK](./sdk/index)
* The [`flytekit` SDK](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html)

## `union` CLI configuration search path

{@@ if serverless @@}

The `union` CLI installed in the plain `union` package (not the `union[byoc]` package) will automatically connect to `serverless.union.ai` if no other configuration files exist.

More precisely the CLI will check for configuration files as follows:

First, if a `--config` option is used, it will use the specified config file.

Second, the config files pointed to by the following environment variables (in this order):

* `UNION_CONFIG`
* `UNIONAI_CONFIG`
* `UCTL_CONFIG`

Third, the following hard-coded locations (in this order):

* `~/.union/config.yaml`
* `~/.uctl/config.yaml`

If none of these are present, the CLI will connect to `serverless.union.ai`.

{@@ elif byoc @@}

The `union` CLI installed in the `union[byoc]` package (not the plain `union` package),  will check for configuration files as follows:

First, if a `--config` option is used, it will use the specific file.

Second, the config files pointed to by the following environment variables (in this order):

* `UNION_CONFIG`
* `UNIONAI_CONFIG`
* `UCTL_CONFIG`

Third, the following hard-coded locations (in this order):

* `~/.union/config.yaml`
* `~/.uctl/config.yaml`

If none of these are present, the CLI will raise an error.

{@@ endif @@}

## `union` CLI commands

```{eval-rst}

.. click:: flytekit.clis.sdk_in_container.pyflyte:main
    :prog: union
    :nested: full
    :commands: backfill, build, create, delete, execution, fetch, get, info, init, launchplan, local-cache, metrics, package, register, run, serialize, serve, update

```