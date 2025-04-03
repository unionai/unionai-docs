---
title: Union CLI
weight: 3
variants: -flyte +serverless +byoc +byok
---

# {{< key cli_name >}} CLI

The `{{< key cli >}}` CLI is the main tool developers use to interact with {{< key product_name >}} on the command line.

## Installation

The recommended way to install the union CLI outside a workflow project is to use [`uv`](https://docs.astral.sh/uv/):

```shell
$ uv tool install {{< key kit >}}
```

This will install the `{{< key cli >}}` CLI globally on your system [as a `uv` tool](https://docs.astral.sh/uv/concepts/tools/).


## Configure the `{{< key cli >}}` CLI

{{< variant serverless >}}
{{< markdown >}}
To configure the `{{< key cli >}}` CLI to connect to {{< key product_name >}} Serverless, run the following command:

```shell
$ {{< key cli >}} create login --serverless
```

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc byok >}}
{{< markdown >}}

To configure the `{{< key cli >}}` CLI to connect to you {{< key product_name >}}  BYOC or BYOK instance, run the following command:

```shell
$ {{< key cli >}} create login --host <{{< key product >}}-host-url>
```

where `<{{< key cli >}}-host-url>` is the URL of your {{< key product_name >}}  instance.

{{< /markdown >}}
{{< /variant >}}

These command will create the file `~/.{{< key product >}}/config.yaml` with the configuration information to connect to the {{< key product_name >}}  instance.

See [Getting started > Local setup](../user-guide/getting-started/local-setup) for more details.

## Overriding the configuration file location

By default, the `{{< key cli >}}` CLI will look for a configuration file at `~/.{{< key product >}}/config.yaml`.

You can override this behavior to specify a different configuration file by setting the `{{< key config_env >}} ` environment variable:

```shell
export {{< key config_env >}}=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `{{< key cli >}}` by using the `--config` flag:

```shell
$ {{< key cli >}} --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

## `{{< key cli >}}` CLI configuration search path

The `{{< key cli >}}` CLI will check for configuration files as follows:

First, if a `--config` option is used, it will use the specified config file.

{{< variant serverless byoc byok >}}
{{< markdown >}}

Second, the config files pointed to by the following environment variables (in this order):

* `UNION_CONFIG`
* `UNIONAI_CONFIG`
* `UCTL_CONFIG`

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

Second, the config file pointed to by the `FLYTECTL_CONFIG` environment variable.

{{< /markdown >}}
{{< /variant >}}

Third, the following hard-coded locations (in this order):

{{< variant serverless byoc byok >}}
{{< markdown >}}

Third, the following hard-coded locations (in this order):

* `~/.union/config.yaml`
* `~/.uctl/config.yaml`

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

Third, the hard-coded location `~/.flyte/config.yaml`.

{{< /markdown >}}
{{< /variant >}}

If none of these are present, the CLI will raise an error.

## `{{< key cli >}}` CLI commands
