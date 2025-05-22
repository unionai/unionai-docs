---
title: Flytectl CLI
weight: 4
variants: +flyte -serverless -byoc -selfmanaged
sidebar_expanded: true
---

# {{< key ctl_name >}} CLI

The `{{< key ctl >}}` CLI provides functionality for Union administrators to manage Union-specific entities like users, roles, and Union configuration.

It also includes much of the functionality of the [`{{< key cli >}}` CLI](../union-cli), but since it is a compiled binary (written in Go), it is faster and more efficient than the Python-based `{{< key cli >}}` CLI and more suitable for situations like running in a CI/CD environment where you might want to avoid the overhead of large Python dependencies.

> [!NOTE]
> If you are not a Union administrator, or if you will be interacting with Union in an environment where
> Python is installed, you should use the [`{{< key cli >}}` CLI](../union-cli) instead.

## Installation

{{< variant serverless byoc selfmanaged >}}
{{< tabs >}}
{{< tab "macOS" >}}
{{< markdown >}}

To install `uctl` on a Mac, use [Homebrew](https://brew.sh/), `curl`, or manually download the binary.

**Homebrew**

```shell
$ brew tap unionai/homebrew-tap
$ brew install uctl
```

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

**Manual download**

To download the binary manually, see the [`uctl` releases page](https://github.com/unionai/uctl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< tab "Linux" >}}
{{< markdown >}}

To install `uctl` on Linux, use `curl` or manually download the binary.

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

**Manual download**

To download the binary manually, see the [`uctl` releases page](https://github.com/unionai/uctl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< tab "Windows" >}}
{{< markdown >}}

To install `uctl` on Windows, use `curl` or manually download the binary.

**curl**

To use `curl`, in a Linux shell (such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)), set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

**Manual download**

To download the binary manually, see the [`uctl` releases page](https://github.com/unionai/uctl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}
{{< /variant >}}
{{< variant flyte >}}
{{< tabs >}}
{{< tab "macOS" >}}
{{< markdown >}}

To install `flytectl` on a Mac, use [Homebrew](https://brew.sh/), `curl`, or manually download the binary.

**Homebrew**

```shell
$ brew tap flyteorg/homebrew-tap
$ brew install flytectl
```

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://ctl.flyte.org/install | bash
```

**Manual download**

To download the binary manually, see the [`flytectl` releases page](https://github.com/flyteorg/flytectl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< tab "Linux" >}}
{{< markdown >}}

To install `flytectl` on Linux, use `curl` or manually download the binary.

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://ctl.flyte.org/install | bash
```

**Manual download**

To download the binary manually, see the [`flytectl` releases page](https://github.com/flyteorg/flytectl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< tab "Windows" >}}
{{< markdown >}}

To install `flytectl` on Windows, use `curl` or manually download the binary.

**curl**

To use `curl`, in a Linux shell (such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)), set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://ctl.flyte.org/install | bash
```

**Manual download**

To download the binary manually, see the [`flytectl` releases page](https://github.com/flyteorg/flytectl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}
{{< /variant >}}


## Configuration

{{< variant serverless >}}
{{< markdown >}}

`uctl` will automatically connect to Union Serverless. You do not need to create a configuration file.

> [!WARNING]
> If you have previously used Union, you may have existing configuration files that will interfere with command line access to Union Serverless.
>
> To avoid connection errors, remove any configuration files in the `~/.unionai/` or `~/.union/` directories and unset the environment variables `UNIONAI_CONFIG` and `UNION_CONFIG`.

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}

To create a configuration file that contains your Union connection information, run the following command, replacing `<union-host-url>` with the URL of your Union instance:

```shell
$ {{< key ctl >}} config init --host <{{< key product>}}-host-url>
```

This will create a new configuration file at `~/.{{< key product>}}/config.yaml`:

```yaml
admin:
  endpoint: dns:///<{{< key product>}}-host-url>
  insecure: false
  authType: Pkce
```

> [!NOTE]
> PKCE is the default authentication type. To specify a different authentication type in the configuration file,
> see [Authentication](../../user-guide/development-cycle/authentication).

### Configuration file location hierarchy

By default, the `{{< key ctl >}}` CLI will use the configuration file at `~/.{{< key product >}}/config.yaml` to connect to your Union instance unless you override it. `{{< key ctl >}}` searches for configuration files in the following order:

{{< /markdown >}}
{{< /variant >}}

{{< variant byoc selfmanaged >}}
{{< markdown >}}

* `--config <path-to-config>` flag
* `UNION_CONFIG` environment variable
* `UCTL_CONFIG` environment variable
* `~/.union/config.yaml` file
* `~/.uctl/config.yaml` file

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

* `--config <path-to-config>` flag
* `FLYTECTL_CONFIG` environment variable
* `~/.flyte/config.yaml` file

{{< /markdown >}}
{{< /variant >}}

## Options

| Option | Type | Description |
|--------|------|-------------|
| `--admin.audience` | string | Audience to use when initiating OAuth2 authorization requests. |
| `--admin.authType` | string | Type of OAuth2 flow used for communicating with admin.ClientSecret, Pkce, ExternalCommand are valid values (default "ClientSecret") |
| `--admin.authorizationHeader` | string | Custom metadata header to pass JWT |
| `--admin.authorizationServerUrl` | string | This is the URL to your IdP's authorization server. It'll default to Endpoint |
| `--admin.caCertFilePath` | string | Use specified certificate file to verify the admin server peer. |
| `--admin.clientId` | string | Client ID (default "flytepropeller") |
| `--admin.clientSecretEnvVar` | string | Environment variable containing the client secret |
| `--admin.clientSecretLocation` | string | File containing the client secret (default "/etc/secrets/client_secret") |
| `--admin.command` | strings | Command for external authentication token generation |
| `--admin.defaultServiceConfig` | string  |
| `--admin.deviceFlowConfig.pollInterval` | string | amount of time the device flow would poll the token endpoint if auth server doesn't return a polling interval. Okta and google IDP do return an interval' (default "5s") |
| `--admin.deviceFlowConfig.refreshTime` | string | grace period from the token expiry after which it would refresh the token. (default "5m0s") |
| `--admin.deviceFlowConfig.timeout` | string | amount of time the device flow should complete or else it will be cancelled. (default "10m0s") |
| `--admin.endpoint` | string | For admin types,  specify where the uri of the service is located. |
| `--admin.httpProxyURL` | string | OPTIONAL: HTTP Proxy to be used for OAuth requests. |
| `--admin.insecure` | | Use insecure connection. |
| `--admin.insecureSkipVerify` | | InsecureSkipVerify controls whether a client verifies the server's certificate chain and host name. Caution : shouldn't be use for production usecases' |
| `--admin.maxBackoffDelay` | string | Max delay for grpc backoff (default "8s") |
| `--admin.maxRetries` | int | Max number of gRPC retries (default 4) |
| `--admin.perRetryTimeout` | string | gRPC per retry timeout (default "15s") |
| `--admin.pkceConfig.refreshTime` | string | grace period from the token expiry after which it would refresh the token. (default "5m0s") |
| `--admin.pkceConfig.timeout` | string | Amount of time the browser session would be active for authentication from client app. (default "2m0s") |
| `--admin.scopes` | strings | List of scopes to request |
| `--admin.tokenRefreshWindow` | string  | Max duration between token refresh attempt and token expiry. (default "0s") |
| `--admin.tokenUrl` | string | OPTIONAL: Your IdP's token endpoint. It'll be discovered from flyte admin's OAuth Metadata endpoint if not provided. |
| `--admin.useAudienceFromAdmin` | | Use Audience configured from admins public endpoint config. |
| `--admin.useAuth` | | Deprecated: Auth will be enabled/disabled based on admin's dynamically discovered information. |
| `-c`, `--config` | string | config file (default is $HOME/.flyte/config.yaml) |
| `--console.endpoint` | string | Endpoint of console, if different than flyte admin |
| `-d`, `--domain` | string | Specifies the Flyte project's domain. |
| `--files.archive` | | Pass in archive file either an http link or local path. |
| `--files.assumableIamRole` | string | Custom assumable iam auth role to register launch plans with. |
| `--files.continueOnError` | | Continue on error when registering files. |
| `--files.destinationDirectory` | string | Location of source code in container. |
| `--files.dryRun` | | Execute command without making any modifications. |
| `--files.enableSchedule` | | Enable the schedule if the files contain schedulable launchplan. |
| `--files.force` | | Force use of version number on entities registered with flyte. |
| `--files.k8ServiceAccount` | string | Deprecated. Please use `--K8sServiceAccount` |
| `--files.k8sServiceAccount` | string | Custom kubernetes service account auth role to register launch plans with. |
| `--files.outputLocationPrefix` | string | Custom output location prefix for offloaded types (files/schemas). |
| `--files.sourceUploadPath` | string | Deprecated: Update flyte admin to avoid having to configure storage access from {{< key ctl >}}. |
| `--files.version` | string | Version of the entity to be registered with flyte which are un-versioned after serialization.
| `-h`, `--help` | | help for {{< key ctl >}} |
| `--logger.formatter.type` | string | Sets logging format type. (default "json") |
| `--logger.level` | int | Sets the minimum logging level. (default 3) |
| `--logger.mute` | | Mutes all logs regardless of severity. Intended for benchmarks/tests only. |
| `--logger.show-source` | | Includes source code location in logs. |
| `-o`, `--output` | string | Specifies the output type - supported formats [TABLE JSON YAML DOT DOTURL]. NOTE: dot, doturl are only supported for Workflow (default "TABLE") |
| `-p`, `--project` | string | Specifies the Flyte project.
| `--storage.cache.max_size_mbs` | int | Maximum size of the cache where the Blob store data is cached in-memory. If not specified or set to 0,  cache is not used |
| `--storage.cache.target_gc_percent` | int | Sets the garbage collection target percentage. |
| `--storage.connection.access-key` | string | Access key to use. Only required when authtype is set to accesskey. |
| `--storage.connection.auth-type` | string | Auth Type to use [iam, accesskey]. (default "iam") |
| `--storage.connection.disable-ssl` | | Disables SSL connection. Should only be used for development. |
| `--storage.connection.endpoint` | string | URL for storage client to connect to. |
| `--storage.connection.region` | string | Region to connect to. (default "us-east-1") |
| `--storage.connection.secret-key` | string | Secret to use when accesskey is set. |
| `--storage.container` | string | Initial container (in s3 a bucket) to create -if it doesn't exist-.' |
| `--storage.defaultHttpClient.timeout` | string | Sets time out on the http client. (default "0s") |
| `--storage.enable-multicontainer` | | If this is true,  then the container argument is overlooked and redundant. This config will automatically open new connections to new containers/buckets as they are encountered |
| `--storage.limits.maxDownloadMBs` | int | Maximum allowed download size (in MBs) per call. (default 2) |
| `--storage.stow.config` | stringToString | Configuration for stow backend. Refer to github/flyteorg/stow (default []) |
| `--storage.stow.kind` | string | Kind of Stow backend to use. Refer to github/flyteorg/stow |
| `--storage.type` | string | Sets the type of storage to configure [s3/minio/local/mem/stow]. (default "s3") |


## Commands

{{< variant byoc >}}
{{< markdown >}}
* `{{< key ctl >}} apply {{{< key ctl >}}-apply/index}` is used for updating various Union/Flyte resources, including cluster configs.
* `{{< key ctl >}} config {{{< key ctl >}}-config/index}` runs various config commands.
{{< /markdown >}}
{{< /variant >}}
* `{{< key ctl >}} create {{{< key ctl >}}-create/index}` creates various Flyte resources such as tasks, workflows, launch plans, executions, and projects.
* `{{< key ctl >}} delete {{{< key ctl >}}-delete/index}` terminates/deletes various Flyte resources, such as executions and resource attributes.
* `{{< key ctl >}} demo {{{< key ctl >}}-demo/index}` provides commands for starting and interacting with a standalone minimal
                                local environment for running Flyte.
* `{{< key ctl >}} get {{{< key ctl >}}-get/index}` fetches various Flyte resources such as tasks, workflows, launch plans, executions, and projects.
* `{{< key ctl >}} register {{{< key ctl >}}-register/index}` registers tasks, workflows, and launch plans from a list of generated serialized files.
* `{{< key ctl >}} update {{{< key ctl >}}-update/index}` update Flyte resources e.g., projects.
* `{{< key ctl >}} version {{{< key ctl >}}-version>` fetches `{{< key ctl >}}` version.


## Entities

| Entity | Commands |
|--------|----------|
| Cluster resource attribute | {{< multiline >}}
[`{{< key ctl >}} get cluster-resource-attribute`](./{{< key ctl >}}-get/{{< key ctl >}}-get-cluster-resource-attribute)
[`{{< key ctl >}} update cluster resource attribute`](./{{< key ctl >}}-update/{{< key ctl >}}-update-cluster-resource-attribute)
[`{{< key ctl >}} delete cluster resource attribute`](./{{< key ctl >}}-delete/{{< key ctl >}}-delete-cluster-resource-attribute)
{{< /multiline >}} |
| Config | {{< multiline>}}
[`{{< key ctl >}} config init`](./{{< key ctl >}}-config/{{< key ctl >}}-config-init)
[`{{< key ctl >}} config discover`](./{{< key ctl >}}-config/{{< key ctl >}}-config-discover)
[`{{< key ctl >}} config docs`](./{{< key ctl >}}-config/{{< key ctl >}}-config-docs)
[`{{< key ctl >}} config validate`](./{{< key ctl >}}-config/{{< key ctl >}}-config-validate)
{{< /multiline >}} |
| Demo | {{< multiline>}}
[`{{< key ctl >}} demo start`](./{{< key ctl >}}-demo/{{< key ctl >}}-demo-start)
[`{{< key ctl >}} demo status`](./{{< key ctl >}}-demo/{{< key ctl >}}-demo-status)
[`{{< key ctl >}} demo exec`](./{{< key ctl >}}-demo/{{< key ctl >}}-demo-exec)
[`{{< key ctl >}} demo reload`](./{{< key ctl >}}-demo/{{< key ctl >}}-demo-reload)
[`{{< key ctl >}} demo teardown`](./{{< key ctl >}}-demo/{{< key ctl >}}-demo-teardown)
{{< /multiline >}} |
| Execution | {{< multiline>}}
[`{{< key ctl >}} create execution`](./{{< key ctl >}}-create/{{< key ctl >}}-create-execution)
[`{{< key ctl >}} get execution`](./{{< key ctl >}}-get/{{< key ctl >}}-get-execution)
[`{{< key ctl >}} update execution`](./{{< key ctl >}}-update/{{< key ctl >}}-update-execution)
[`{{< key ctl >}} delete execution`](./{{< key ctl >}}-delete/{{< key ctl >}}-delete-execution)
{{< /multiline >}} |
| Execution cluster label | {{< multiline>}}
[`{{< key ctl >}} get execution-cluster-label`](./{{< key ctl >}}-get/{{< key ctl >}}-get-execution-cluster-label)
[`{{< key ctl >}} update execution-cluster-label`](./{{< key ctl >}}-update/{{< key ctl >}}-update-execution-cluster-label)
[`{{< key ctl >}} delete execution-cluster-label`](./{{< key ctl >}}-delete/{{< key ctl >}}-delete-execution-cluster-label)
{{< /multiline >}} |
| Execution queue attribute | {{< multiline>}}
[`{{< key ctl >}} get execution-queue-attribute`](./{{< key ctl >}}-get/{{< key ctl >}}-get-execution-queue-attribute)
[`{{< key ctl >}} update execution-queue-attribute`](./{{< key ctl >}}-update/{{< key ctl >}}-update-execution-queue-attribute)
[`{{< key ctl >}} delete execution-queue-attribute`](./{{< key ctl >}}-delete/{{< key ctl >}}-delete-execution-queue-attribute)
{{< /multiline >}} |
| Files |  [`{{< key ctl >}} regiser files`](./{{< key ctl >}}-register/{{< key ctl >}}-register-files) |
| Launch plan | {{< multiline>}}
[`{{< key ctl >}} get launchplan`](./{{< key ctl >}}-get/{{< key ctl >}}-get-launchplan)
[`{{< key ctl >}} update launchplan`](./{{< key ctl >}}-update/{{< key ctl >}}-update-launchplan)
[`{{< key ctl >}} update launchplan-meta`](./{{< key ctl >}}-update/{{< key ctl >}}-update-launchplan-meta)
{{< /multiline >}} |
| Plugin override | {{< multiline>}}
[`{{< key ctl >}} get plugin-override`](./{{< key ctl >}}-get/{{< key ctl >}}-get-plugin-override)
[`{{< key ctl >}} update plugin-override`](./{{< key ctl >}}-update/{{< key ctl >}}-update-plugin-override)
[`{{< key ctl >}} delete plugin-override`](./{{< key ctl >}}-delete/{{< key ctl >}}-delete-plugin-override)
{{< /multiline >}} |
| Project | {{< multiline>}}
[`{{< key ctl >}} create project`](./{{< key ctl >}}-create/{{< key ctl >}}-create-project)
[`{{< key ctl >}} get project`](./{{< key ctl >}}-get/{{< key ctl >}}-get-project)
[`{{< key ctl >}} update project`](./{{< key ctl >}}-update/{{< key ctl >}}-update-project)
{{< /multiline >}} |
| Task | {{< multiline>}}
[`{{< key ctl >}} get task`](./{{< key ctl >}}-get/{{< key ctl >}}-get-task)
[`{{< key ctl >}} update task-meta`](./{{< key ctl >}}-update/{{< key ctl >}}-update-task-meta)
{{< /multiline >}} |
| Task resource attribute | {{< multiline>}}
[`{{< key ctl >}} get task-resource-attribute`](./{{< key ctl >}}-get/{{< key ctl >}}-get-task-resource-attribute)
[`{{< key ctl >}} update task-resource-attribute`](./{{< key ctl >}}-update/{{< key ctl >}}-update-task-resource-attribute)
[`{{< key ctl >}} delete task-resource-attribute`](./{{< key ctl >}}-delete/{{< key ctl >}}-delete-task-resource-attribute)
{{< /multiline >}} |
| Workflow | {{< multiline>}}
[`{{< key ctl >}} get workflow`](./{{< key ctl >}}-get/{{< key ctl >}}-get-workflow)
[`{{< key ctl >}} update workflow-meta`](./{{< key ctl >}}-update/{{< key ctl >}}-update-workflow-meta)
{{< /multiline >}} |
| Workflow execution config | {{< multiline>}}
[`{{< key ctl >}} get workflow-execution-config`](./{{< key ctl >}}-get/{{< key ctl >}}-get-workflow-execution-config)
[`{{< key ctl >}} update workflow-execution-config`](./{{< key ctl >}}-update/{{< key ctl >}}-update-workflow-execution-config)
[`{{< key ctl >}} delete workflow-execution-config`](./{{< key ctl >}}-delete/{{< key ctl >}}-delete-workflow-execution-config)
{{< /multiline >}} |
