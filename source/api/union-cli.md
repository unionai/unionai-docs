# union CLI

The `union` CLI is the main tool developers use to interact with Union.

## `union` CLI configuration search path

{@@ if serverless @@}

When using Union Serverless, you should always install the plain `union` package and not the `union[byoc]` package, which is configured for [Union BYOC](../byoc/quick-start.md#install-the-union-package).

This will ensure that the CLI will automatically connect to `serverless.union.ai`, assuming no other configurations are set up.

More precisely the CLI will check for configuration files as follows:

First, if a `--config` option is specified on the command line, it will use the file specified there.

Second, the locations pointed to by the following environment variables (in this order):

* `UNION_CONFIG`
* `UNIONAI_CONFIG`
* `UCTL_CONFIG`

Third, the following hard-coded locations (in this order):

* `~/.union/config.yaml`
* `~/.uctl/config.yaml`

If none of these are present, it will connect to `serverless.union.ai`.

{@@ elif byoc @@}

When using Union BYOC, you should always install the `union[byoc]` package and not the plain `union` package, which is is configured for [Union Serverless](../serverless/quick-start).

This will ensure that the CLI will check for configuration files as follows (if no `--config` option is specified on the command line):

First, if a `--config` option is specified on the command line, it will use the file specified there.

Second, the locations pointed to by the following environment variables (in this order):

* `UNION_CONFIG`
* `UNIONAI_CONFIG`
* `UCTL_CONFIG`

Third, the following hard-coded locations  (in this order):

* `~/.union/config.yaml`
* `~/.uctl/config.yaml`

If none of these are present, it will raise an error. It will not attempt to connect to  `serverless.union.ai`, as the Serverless version of the CLI would.

{@@ endif @@}

```{eval-rst}

.. click:: flytekit.clis.sdk_in_container.pyflyte:main
    :prog: union
    :nested: full
    :commands: backfill, build, create, delete, execution, fetch, get, info, init, launchplan, local-cache, metrics, package, register, run, serialize, serve, update

```