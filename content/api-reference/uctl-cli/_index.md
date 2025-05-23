---
title: Uctl CLI
weight: 4
variants: -flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Uctl CLI

The `uctl` CLI provides functionality for Union administrators to manage Union-specific entities like users, roles, and Union configuration.

It also includes much of the functionality of the [`union` CLI](../union-cli), but since it is a compiled binary (written in Go), it is faster and more efficient than the Python-based `union` CLI and more suitable for situations like running in a CI/CD environment where you might want to avoid the overhead of large Python dependencies.

> [!NOTE]
> If you are not a Union administrator, or if you will be interacting with Union in an environment where
> Python is installed, you should use the [`union` CLI](../union-cli) instead.

## Installation

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
{{< variant byoc selfmanaged >}}
{{< markdown >}}

To create a configuration file that contains your Union connection information, run the following command, replacing `<union-host-url>` with the URL of your Union instance:

```shell
$ uctl config init --host <union-host-url>
```

This will create a new configuration file at `~/.union/config.yaml`:

```yaml
admin:
  endpoint: dns:///<union-host-url>
  insecure: false
  authType: Pkce
```

> [!NOTE]
> PKCE is the default authentication type. To specify a different authentication type in the configuration file,
> see [Authentication](../../user-guide/development-cycle/authentication).

### Configuration file location hierarchy

By default, the `uctl` CLI will use the configuration file at `~/.union/config.yaml` to connect to your Union instance unless you override it. `uctl` searches for configuration files in the following order:

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
| `--admin.insecureSkipVerify` | | InsecureSkipVerify controls whether a client verifies the server's certificate chain and host name.Caution: shouldn't be use for production usecases' |
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
| `--files.sourceUploadPath` | string | Deprecated: Update flyte admin to avoid having to configure storage access from uctl. |
| `--files.version` | string | Version of the entity to be registered with flyte which are un-versioned after serialization.
| `-h`, `--help` | | help for uctl |
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
* `uctl apply {uctl-apply/index}` is used for updating various Union/Flyte resources, including cluster configs.
* `uctl config {uctl-config/index}` runs various config commands.
{{< /markdown >}}
{{< /variant >}}
* `uctl create {uctl-create/index}` creates various Flyte resources such as tasks, workflows, launch plans, executions, and projects.
* `uctl delete {uctl-delete/index}` terminates/deletes various Flyte resources, such as executions and resource attributes.
* `uctl demo {uctl-demo/index}` provides commands for starting and interacting with a standalone minimal
                                local environment for running Flyte.
* `uctl get {uctl-get/index}` fetches various Flyte resources such as tasks, workflows, launch plans, executions, and projects.
* `uctl register {uctl-register/index}` registers tasks, workflows, and launch plans from a list of generated serialized files.
* `uctl update {uctl-update/index}` update Flyte resources e.g., projects.
* `uctl version {uctl-version>` fetches `uctl` version.


## Entities

| Entity | Commands |
|--------|----------|
| Cluster resource attribute | {{< multiline >}}
[`uctl get cluster-resource-attribute`](./uctl-get/uctl-get-cluster-resource-attribute)
[`uctl update cluster resource attribute`](./uctl-update/uctl-update-cluster-resource-attribute)
[`uctl delete cluster resource attribute`](./uctl-delete/uctl-delete-cluster-resource-attribute)
{{< /multiline >}} |
| Config | {{< multiline>}}
[`uctl config init`](./uctl-config/uctl-config-init)
[`uctl config discover`](./uctl-config/uctl-config-discover)
[`uctl config docs`](./uctl-config/uctl-config-docs)
[`uctl config validate`](./uctl-config/uctl-config-validate)
{{< /multiline >}} |
| Demo | {{< multiline>}}
[`uctl demo start`](./uctl-demo/uctl-demo-start)
[`uctl demo status`](./uctl-demo/uctl-demo-status)
[`uctl demo exec`](./uctl-demo/uctl-demo-exec)
[`uctl demo reload`](./uctl-demo/uctl-demo-reload)
[`uctl demo teardown`](./uctl-demo/uctl-demo-teardown)
{{< /multiline >}} |
| Execution | {{< multiline>}}
[`uctl create execution`](./uctl-create/uctl-create-execution)
[`uctl get execution`](./uctl-get/uctl-get-execution)
[`uctl update execution`](./uctl-update/uctl-update-execution)
[`uctl delete execution`](./uctl-delete/uctl-delete-execution)
{{< /multiline >}} |
| Execution cluster label | {{< multiline>}}
[`uctl get execution-cluster-label`](./uctl-get/uctl-get-execution-cluster-label)
[`uctl update execution-cluster-label`](./uctl-update/uctl-update-execution-cluster-label)
[`uctl delete execution-cluster-label`](./uctl-delete/uctl-delete-execution-cluster-label)
{{< /multiline >}} |
| Execution queue attribute | {{< multiline>}}
[`uctl get execution-queue-attribute`](./uctl-get/uctl-get-execution-queue-attribute)
[`uctl update execution-queue-attribute`](./uctl-update/uctl-update-execution-queue-attribute)
[`uctl delete execution-queue-attribute`](./uctl-delete/uctl-delete-execution-queue-attribute)
{{< /multiline >}} |
| Files |  [`uctl regiser files`](./uctl-register/uctl-register-files) |
| Launch plan | {{< multiline>}}
[`uctl get launchplan`](./uctl-get/uctl-get-launchplan)
[`uctl update launchplan`](./uctl-update/uctl-update-launchplan)
[`uctl update launchplan-meta`](./uctl-update/uctl-update-launchplan-meta)
{{< /multiline >}} |
| Plugin override | {{< multiline>}}
[`uctl get plugin-override`](./uctl-get/uctl-get-plugin-override)
[`uctl update plugin-override`](./uctl-update/uctl-update-plugin-override)
[`uctl delete plugin-override`](./uctl-delete/uctl-delete-plugin-override)
{{< /multiline >}} |
| Project | {{< multiline>}}
[`uctl create project`](./uctl-create/uctl-create-project)
[`uctl get project`](./uctl-get/uctl-get-project)
[`uctl update project`](./uctl-update/uctl-update-project)
{{< /multiline >}} |
| Task | {{< multiline>}}
[`uctl get task`](./uctl-get/uctl-get-task)
[`uctl update task-meta`](./uctl-update/uctl-update-task-meta)
{{< /multiline >}} |
| Task resource attribute | {{< multiline>}}
[`uctl get task-resource-attribute`](./uctl-get/uctl-get-task-resource-attribute)
[`uctl update task-resource-attribute`](./uctl-update/uctl-update-task-resource-attribute)
[`uctl delete task-resource-attribute`](./uctl-delete/uctl-delete-task-resource-attribute)
{{< /multiline >}} |
| Workflow | {{< multiline>}}
[`uctl get workflow`](./uctl-get/uctl-get-workflow)
[`uctl update workflow-meta`](./uctl-update/uctl-update-workflow-meta)
{{< /multiline >}} |
| Workflow execution config | {{< multiline>}}
[`uctl get workflow-execution-config`](./uctl-get/uctl-get-workflow-execution-config)
[`uctl update workflow-execution-config`](./uctl-update/uctl-update-workflow-execution-config)
[`uctl delete workflow-execution-config`](./uctl-delete/uctl-delete-workflow-execution-config)
{{< /multiline >}} |
