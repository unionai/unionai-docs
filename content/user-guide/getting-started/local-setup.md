---
title: Local setup
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Local setup

In this section we will explain the options for configuring the `flyte` CLI and SDK to connect to your Union/Flyte instance.

Before proceeding, make sure you have completed the steps in [Getting started](../getting-started).
You will need to have the `uv` tool and the `flyte` Python package installed.

## Setting up a configuration file

In [Getting started](../getting-started) we used the `flyte create config` command to create a configuration file at `./.flyte/config.yaml`.

{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}
```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --project my-project \
    --domain development \
    --builder remote
```
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --project my-project \
    --domain development \
    --builder local
```
{{< /markdown >}}
{{< /variant >}}

This command creates a file called `./flyte/config.yaml` in your current working directory:

{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}
```yaml
admin:
  endpoint: dns:///my-org.my-company.com
image:
  builder: remote
task:
  domain: development
  org: my-org
  project: my-project
```
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
```yaml
admin:
  endpoint: dns:///my-org.my-company.com
image:
  builder: local
task:
  domain: development
  org: my-org
  project: my-project
```
{{< /markdown >}}
{{< /variant >}}

{{< dropdown title="💡 See full example using all available options" >}}

{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}
The example below creates a configuration file called `my-config.yaml` in the current working directory with all of the available options
```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --insecure \
    --builder remote \
    --domain development \
    --org my-org \
    --project my-project \
    --output my-config.yaml \
    --force
```
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
The example below creates a configuration file called `my-config.yaml` in the current working directory.
```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --insecure \
    --builder local \
    --domain development \
    --org my-org \
    --project my-project \
    --output my-config.yaml \
    --force
```
{{< /markdown >}}
{{< /variant >}}

{{< markdown >}}
See the [Reference](../../api-reference/flyte-cli#flyte-create-config) section for details on the available parameters.
{{< /markdown >}}

{{< /dropdown >}}

{{< dropdown title="ℹ️ Notes about the properties in the config file" >}}
{{< markdown >}}

**`admin` section**: contains the connection details for your Union/Flyte instance.

* `admin.endpoint` is the URL (always with `dns:///` prefix) of your Union/Flyte instance.
If your instance UI is found at https://my-org.my-company.com, the actual endpoint used in this file would be `dns:///my-org.my-company.com`.

* `admin.insecure` indicates whether to use an insecure connection (without TLS) to the Union/Flyte instance.
A setting of `true` is almost always only used for connecting to a local instance on your own machine.

**`image` section**: contains the configuration for building Docker images for your tasks.

* `image.builder` specifies the image builder to use for building Docker images for your tasks.
  * For Union instances this is usually set to `remote`, which means that the images will be built on Union's infrastructure using the Union `ImageBuilder`.
  * For Flyte OSS instances, `ImageBuilder` is not available, so this property must be set to `local`.
    This means that the images will be built locally on your machine.
    You need to have Docker installed and running for this to work.
    See [Image building](../task-configuration/container-images#image-building) for details.

**`task` section**: contains the configuration for running tasks on your Union/Flyte instance.

* `task.domain` specifies the domain in which the tasks will run.
Domains are used to separate different environments, such as `development`, `staging`, and `production`.

* `task.org` specifies the organization in which the tasks will run. The organization is usually synonymous with the name of the Union instance you are using, which is usually the same as the first part of the `admin.endpoint` URL.

* `task.project` specifies the project in which the tasks will run. The project you specify here will be the default project to which tasks are deployed if no other project is specified. The project you specify must already exist on your Union/Flyte instance (it will not be auto-created on first deploy).

<!-- TODO: add link to project creation when available -->
{{< /markdown >}}
{{< /dropdown >}}

## Using the configuration file

You can use the configuration file either explicitly by referencing it directly from a CLI or Python command, or implicitly by placing it in a specific location or setting an environment variable.

### Specify a configuration file explicitly

When using the `flyte` CLI, you can specify the configuration file explicitly by using the `--config` or `-c` parameter.

You can explicitly specify the configuration file when running a `flyte` CLI command by using the `--config` parameter, like this:

```shell
flyte --config my-config.yaml run hello.py main
```

or just using the `-c` shorthand:

```shell
flyte -c my-config.yaml run hello.py main
```

When invoking flyte commands programmatically, you have to first initialize the Flyte SDK with the configuration file.

To initialize with an explicitly specified configuration file, use [`flyte.init_from_config`](../../api-reference/flyte-sdk/packages/flyte#init_from_config):

```python
flyte.init_from_config("my-config.yaml")
```

Then you can continue with other `flyte` commands, such as running the main task:

```python
run = flyte.run(main)
```

### Use the configuration file implicitly

You can also use the configuration file implicitly by placing it in a specific location or setting an environment variable.

You can use the `flyte CLI` without an explicit `--config` like this:

```shell
flyte run hello.py main
```

You can also initializing the Flyte SDK programmatically without specifying a configuration file, like this:

```python
flyte.init_from_config()
```

In these cases, the SDK will search in the following order until it finds a configuration file:

* `./config.yaml` (i.e., in the current working directory).
* `./flyte/config.yaml` (i.e., in the `.flyte` directory in the current working directory).
* `UCTL_CONFIG` (a file pointed to by this environment variable).
* `FLYTECTL_CONFIG` (a file pointed to by this environment variable)
* `~/.union/config.yaml`
* `~/.flyte/config.yaml`

### Checking your configuration

You can check your current configuration by running the following command:

```shell
flyte get config
```

This will return the current configuration as a serialized Python object. For example

```shell
CLIConfig(
    Config(
        platform=PlatformConfig(endpoint='dns:///my-org.my-company.com', scopes=[]),
        task=TaskConfig(org='my-org', project='my-project', domain='development'),
        source=PosixPath('/Users/me/.flyte/config.yaml')
    ),
    <rich_click.rich_context.RichContext object at 0x104fb57f0>,
    log_level=None,
    insecure=None
)
```

## Inline configuration

### With `flyte` CLI

You can also use Flyte SDK with inline configuration parameters, without using a configuration file.

When using the `flyte` CLI, some parameters are specified after the top level command (i.e., `flyte`) while other are specified after the sub-command (for example, `run`).

For example, you can run a workflow using the following command:

```shell
flyte \
    --endpoint my-org.my-company.com \
    --org my-org \
    run \
    --domain development \
    --project my-project
    hello.py \
    main
```

See the [Flyte CLI reference](../../api-reference/flyte-cli) for details.

When using the Flyte SDK programmatically, you can use the [`flyte.init`](../../api-reference/flyte-sdk/packages/flyte#init) function to specify the backend endpoint and other parameters directly in your code.

### With `flyte` SDK

To initialize the Flyte SDK with inline parameters, you can use the [`flyte.init`](../../api-reference/flyte-sdk/packages/flyte#init) function like this:

```python
flyte.init(
    endpoint="dns:///my-org.my-company.com",
    org="my-org",
    project="my-project",
    domain="development",
)
```

See the [`flyte.init` reference](../../api-reference/flyte-sdk/packages/flyte#init) for details.
