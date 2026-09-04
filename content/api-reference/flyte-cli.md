---
title: "Flyte CLI"
version: 2.7.0
variants: +flyte +union
layout: py_api
weight: 3
---

# Flyte CLI

This is the command line interface for Flyte.

{{< variant flyte >}}
{{< grid >}}
{{< markdown >}}
| Object | Action |
| ------ | -- |
| `action` | [`abort`](#flyte-abort-action), [`get`](#flyte-get-action)  |
| `run` | [`abort`](#flyte-abort-run), [`get`](#flyte-get-run)  |
| `artifact` | [`create`](#flyte-create-artifact), [`get`](#flyte-get-artifact)  |
| `config` | [`create`](#flyte-create-config), [`get`](#flyte-get-config)  |
| `project` | [`create`](#flyte-create-project), [`get`](#flyte-get-project), [`update`](#flyte-update-project)  |
| `secret` | [`create`](#flyte-create-secret), [`delete`](#flyte-delete-secret), [`get`](#flyte-get-secret)  |
| `trigger` | [`create`](#flyte-create-trigger), [`delete`](#flyte-delete-trigger), [`get`](#flyte-get-trigger), [`update`](#flyte-update-trigger)  |
| `app` | [`delete`](#flyte-delete-app), [`get`](#flyte-get-app), [`update`](#flyte-update-app)  |
| `devbox` | [`delete`](#flyte-delete-devbox), [`get`](#flyte-get-devbox), [`start`](#flyte-start-devbox), [`stop`](#flyte-stop-devbox)  |
| `local-cache` | [`delete`](#flyte-delete-local-cache)  |
| `settings` | [`edit`](#flyte-edit-settings), [`get`](#flyte-get-settings)  |
| `docs` | [`gen`](#flyte-gen-docs)  |
| `condition` | [`get`](#flyte-get-condition), [`signal`](#flyte-signal-condition)  |
| `io` | [`get`](#flyte-get-io)  |
| `logs` | [`get`](#flyte-get-logs)  |
| `task` | [`get`](#flyte-get-task)  |
| `hf-model` | [`prefetch`](#flyte-prefetch-hf-model)  |
| `hello` | [`run`](#flyte-run-hello)  |
| `deployed-task` | [`run`](#flyte-run-deployed-task)  |
| `tui` | [`start`](#flyte-start-tui)  |
{{< /markdown >}}
{{< markdown >}}
| Action | On |
| ------ | -- |
| `abort` | [`action`](#flyte-abort-action), [`run`](#flyte-abort-run)  |
| [`build`](#flyte-build) | - |
| `create` | [`artifact`](#flyte-create-artifact), [`config`](#flyte-create-config), [`project`](#flyte-create-project), [`secret`](#flyte-create-secret), [`trigger`](#flyte-create-trigger)  |
| `delete` | [`app`](#flyte-delete-app), [`devbox`](#flyte-delete-devbox), [`local-cache`](#flyte-delete-local-cache), [`secret`](#flyte-delete-secret), [`trigger`](#flyte-delete-trigger)  |
| [`deploy`](#flyte-deploy) | - |
| `edit` | [`settings`](#flyte-edit-settings)  |
| `gen` | [`docs`](#flyte-gen-docs)  |
| `get` | [`action`](#flyte-get-action), [`app`](#flyte-get-app), [`artifact`](#flyte-get-artifact), [`condition`](#flyte-get-condition), [`config`](#flyte-get-config), [`devbox`](#flyte-get-devbox), [`io`](#flyte-get-io), [`logs`](#flyte-get-logs), [`project`](#flyte-get-project), [`run`](#flyte-get-run), [`secret`](#flyte-get-secret), [`settings`](#flyte-get-settings), [`task`](#flyte-get-task), [`trigger`](#flyte-get-trigger)  |
| `prefetch` | [`hf-model`](#flyte-prefetch-hf-model)  |
| [`rerun`](#flyte-rerun) | - |
| `run` | [`hello`](#flyte-run-hello), [`deployed-task`](#flyte-run-deployed-task)  |
| [`serve`](#flyte-serve) | - |
| `signal` | [`condition`](#flyte-signal-condition)  |
| `start` | [`devbox`](#flyte-start-devbox), [`tui`](#flyte-start-tui)  |
| `stop` | [`devbox`](#flyte-stop-devbox)  |
| `update` | [`app`](#flyte-update-app), [`project`](#flyte-update-project), [`trigger`](#flyte-update-trigger)  |
| [`whoami`](#flyte-whoami) | - |
{{< /markdown >}}
{{< /grid >}}
{{< /variant >}}
{{< variant union >}}
{{< grid >}}
{{< markdown >}}
| Object | Action |
| ------ | -- |
| `action` | [`abort`](#flyte-abort-action), [`get`](#flyte-get-action)  |
| `run` | [`abort`](#flyte-abort-run), [`get`](#flyte-get-run)  |
| `api-key` | [`create⁺`](#flyte-create-api-key), [`delete⁺`](#flyte-delete-api-key), [`get⁺`](#flyte-get-api-key)  |
| `artifact` | [`create`](#flyte-create-artifact), [`get`](#flyte-get-artifact)  |
| `assignment` | [`create⁺`](#flyte-create-assignment), [`delete⁺`](#flyte-delete-assignment), [`get⁺`](#flyte-get-assignment)  |
| `cluster` | [`create⁺`](#flyte-create-cluster), [`delete⁺`](#flyte-delete-cluster), [`get⁺`](#flyte-get-cluster), [`undelete⁺`](#flyte-undelete-cluster), [`update⁺`](#flyte-update-cluster)  |
| `cluster-pool` | [`create⁺`](#flyte-create-cluster-pool), [`delete⁺`](#flyte-delete-cluster-pool), [`get⁺`](#flyte-get-cluster-pool), [`undelete⁺`](#flyte-undelete-cluster-pool), [`update⁺`](#flyte-update-cluster-pool)  |
| `config` | [`create`](#flyte-create-config), [`get`](#flyte-get-config)  |
| `policy` | [`create⁺`](#flyte-create-policy), [`delete⁺`](#flyte-delete-policy), [`get⁺`](#flyte-get-policy), [`update⁺`](#flyte-update-policy)  |
| `project` | [`create`](#flyte-create-project), [`get`](#flyte-get-project), [`update`](#flyte-update-project)  |
| `queue` | [`create⁺`](#flyte-create-queue), [`delete⁺`](#flyte-delete-queue), [`get⁺`](#flyte-get-queue), [`undelete⁺`](#flyte-undelete-queue), [`update⁺`](#flyte-update-queue)  |
| `role` | [`create⁺`](#flyte-create-role), [`delete⁺`](#flyte-delete-role), [`get⁺`](#flyte-get-role), [`update⁺`](#flyte-update-role)  |
| `secret` | [`create`](#flyte-create-secret), [`delete`](#flyte-delete-secret), [`get`](#flyte-get-secret)  |
| `trigger` | [`create`](#flyte-create-trigger), [`delete`](#flyte-delete-trigger), [`get`](#flyte-get-trigger), [`update`](#flyte-update-trigger)  |
| `user` | [`create⁺`](#flyte-create-user), [`delete⁺`](#flyte-delete-user), [`get⁺`](#flyte-get-user)  |
| `app` | [`delete`](#flyte-delete-app), [`get`](#flyte-get-app), [`update`](#flyte-update-app)  |
| `devbox` | [`delete`](#flyte-delete-devbox), [`get`](#flyte-get-devbox), [`start`](#flyte-start-devbox), [`stop`](#flyte-stop-devbox)  |
| `local-cache` | [`delete`](#flyte-delete-local-cache)  |
| `settings` | [`edit`](#flyte-edit-settings), [`get`](#flyte-get-settings)  |
| `volume` | [`explore⁺`](#flyte-explore-volume)  |
| `docs` | [`gen`](#flyte-gen-docs)  |
| `cluster-config` | [`get⁺`](#flyte-get-cluster-config)  |
| `condition` | [`get`](#flyte-get-condition), [`signal`](#flyte-signal-condition)  |
| `io` | [`get`](#flyte-get-io)  |
| `logs` | [`get`](#flyte-get-logs)  |
| `member` | [`get⁺`](#flyte-get-member)  |
| `metrics` | [`get⁺`](#flyte-get-metrics)  |
| `system-logs` | [`get⁺`](#flyte-get-system-logs)  |
| `task` | [`get`](#flyte-get-task)  |
| `hf-model` | [`prefetch`](#flyte-prefetch-hf-model)  |
| `hello` | [`run`](#flyte-run-hello)  |
| `deployed-task` | [`run`](#flyte-run-deployed-task)  |
| `tui` | [`start`](#flyte-start-tui)  |
{{< /markdown >}}
{{< markdown >}}
| Action | On |
| ------ | -- |
| `abort` | [`action`](#flyte-abort-action), [`run`](#flyte-abort-run)  |
| [`build`](#flyte-build) | - |
| `create` | [`api-key⁺`](#flyte-create-api-key), [`artifact`](#flyte-create-artifact), [`assignment⁺`](#flyte-create-assignment), [`cluster⁺`](#flyte-create-cluster), [`cluster-pool⁺`](#flyte-create-cluster-pool), [`config`](#flyte-create-config), [`policy⁺`](#flyte-create-policy), [`project`](#flyte-create-project), [`queue⁺`](#flyte-create-queue), [`role⁺`](#flyte-create-role), [`secret`](#flyte-create-secret), [`trigger`](#flyte-create-trigger), [`user⁺`](#flyte-create-user)  |
| [`debug⁺`](#flyte-debug) | - |
| `delete` | [`api-key⁺`](#flyte-delete-api-key), [`app`](#flyte-delete-app), [`assignment⁺`](#flyte-delete-assignment), [`cluster⁺`](#flyte-delete-cluster), [`cluster-pool⁺`](#flyte-delete-cluster-pool), [`devbox`](#flyte-delete-devbox), [`local-cache`](#flyte-delete-local-cache), [`policy⁺`](#flyte-delete-policy), [`queue⁺`](#flyte-delete-queue), [`role⁺`](#flyte-delete-role), [`secret`](#flyte-delete-secret), [`trigger`](#flyte-delete-trigger), [`user⁺`](#flyte-delete-user)  |
| [`deploy`](#flyte-deploy) | - |
| `edit` | [`settings`](#flyte-edit-settings)  |
| `explore⁺` | [`volume⁺`](#flyte-explore-volume)  |
| [`fork⁺`](#flyte-fork) | - |
| `gen` | [`docs`](#flyte-gen-docs)  |
| `get` | [`action`](#flyte-get-action), [`api-key⁺`](#flyte-get-api-key), [`app`](#flyte-get-app), [`artifact`](#flyte-get-artifact), [`assignment⁺`](#flyte-get-assignment), [`cluster⁺`](#flyte-get-cluster), [`cluster-config⁺`](#flyte-get-cluster-config), [`cluster-pool⁺`](#flyte-get-cluster-pool), [`condition`](#flyte-get-condition), [`config`](#flyte-get-config), [`devbox`](#flyte-get-devbox), [`io`](#flyte-get-io), [`logs`](#flyte-get-logs), [`member⁺`](#flyte-get-member), [`metrics⁺`](#flyte-get-metrics), [`policy⁺`](#flyte-get-policy), [`project`](#flyte-get-project), [`queue⁺`](#flyte-get-queue), [`role⁺`](#flyte-get-role), [`run`](#flyte-get-run), [`secret`](#flyte-get-secret), [`settings`](#flyte-get-settings), [`system-logs⁺`](#flyte-get-system-logs), [`task`](#flyte-get-task), [`trigger`](#flyte-get-trigger), [`user⁺`](#flyte-get-user)  |
| `prefetch` | [`hf-model`](#flyte-prefetch-hf-model)  |
| [`rerun`](#flyte-rerun) | - |
| `run` | [`hello`](#flyte-run-hello), [`deployed-task`](#flyte-run-deployed-task)  |
| [`serve`](#flyte-serve) | - |
| `signal` | [`condition`](#flyte-signal-condition)  |
| `start` | [`devbox`](#flyte-start-devbox), [`tui`](#flyte-start-tui)  |
| `stop` | [`devbox`](#flyte-stop-devbox)  |
| `undelete⁺` | [`cluster⁺`](#flyte-undelete-cluster), [`cluster-pool⁺`](#flyte-undelete-cluster-pool), [`queue⁺`](#flyte-undelete-queue)  |
| `update` | [`app`](#flyte-update-app), [`cluster⁺`](#flyte-update-cluster), [`cluster-pool⁺`](#flyte-update-cluster-pool), [`policy⁺`](#flyte-update-policy), [`project`](#flyte-update-project), [`queue⁺`](#flyte-update-queue), [`role⁺`](#flyte-update-role), [`trigger`](#flyte-update-trigger)  |
| [`whoami`](#flyte-whoami) | - |
{{< /markdown >}}
{{< /grid >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}

## Union-specific functionality {#plugin-commands}

> [!NOTE]
> Commands marked with **⁺** are provided by the `flyteplugins-union` plugin,
> which adds Union-specific functionality to the Flyte CLI
> (user management, RBAC, API keys).
> Install it with `pip install flyteplugins-union`.
>
> See the [flyteplugins.union API reference](../union-plugin/_index)
> for the programmatic interface.

{{< /markdown >}}
{{< /variant >}}


## flyte

**`flyte [OPTIONS] COMMAND [ARGS]...`**

The Flyte CLI is the command line interface for working with the Flyte SDK and backend.

It follows a simple verb/noun structure,
where the top-level commands are verbs that describe the action to be taken,
and the subcommands are nouns that describe the object of the action.

The root command can be used to configure the CLI for persistent settings,
such as the endpoint, organization, and verbosity level.

Set endpoint and organization:

```bash
$ flyte --endpoint <endpoint> --org <org> get project <project_name>
```

Increase verbosity level (This is useful for debugging,
this will show more logs and exception traces):

```bash
$ flyte -vvv get logs <run-name>
```

Override the default config file:

```bash
$ flyte --config /path/to/config.yaml run ...
```

* [Documentation](https://www.union.ai/docs/flyte/user-guide/)
* [GitHub](https://github.com/flyteorg/flyte): Please leave a star if you like Flyte!
* [Slack](https://slack.flyte.org): Join the community and ask questions.
* [Issues](https://github.com/flyteorg/flyte/issues)

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--version` | `boolean` | `Sentinel.UNSET` | Show the version and exit. |
| `--endpoint` | `text` | `Sentinel.UNSET` | The endpoint to connect to. This will override any configuration file and simply use `pkce` to connect. |
| `--insecure` | `boolean` |  | Use an insecure connection to the endpoint. If not specified, the CLI will use TLS. |
| `--image-builder` `--builder` | `choice` |  | Image builder to use for building images. Overrides the config file setting. If not specified, the builder from the config file (image.builder) is used, falling back to `local`. |
| `--auth-type` | `choice` |  | Authentication type to use for the Flyte backend. Defaults to `pkce`. |
| `-v` `--verbose` | `integer` | `0` | Show verbose messages and exception traces. Repeating multiple times increases the verbosity (e.g., -vvv). |
| `--org` | `text` | `Sentinel.UNSET` | The organization to which the command applies. |
| `-c` `--config` | `file` | `Sentinel.UNSET` | Path to the configuration file to use. If not specified, the default configuration file is used. |
| `--output-format` `-of` | `choice` | `table` | Output format for commands that support it. Defaults to `table`. |
| `--log-format` | `choice` | `console` | Formatting for logs, defaults to `console` which is meant to be human readable. `json` is meant for machine parsing. |
| `--user-log-level` | `choice` | `info` | Log level for user task logs. Independent of the internal Flyte log level (-v). |
| `--reset-root-logger` | `boolean` | `False` | If set, the root logger will be reset to use Flyte logging style |
| `--no-progress` | `boolean` | `False` | Disable the animated progress spinner — useful in CI / non-interactive logs. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte abort

**`flyte abort COMMAND [ARGS]...`**

Abort an ongoing process.

#### flyte abort action

**`flyte abort action [OPTIONS] RUN_NAME ACTION_NAME`**

Abort an action associated with a run.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--reason` | `text` | `Manually aborted from the CLI` | The reason to abort the run. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte abort run

**`flyte abort run [OPTIONS] RUN_NAME`**

Abort a run.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--reason` | `text` | `Manually aborted from the CLI` | The reason to abort the run. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte build

**`flyte build [OPTIONS] COMMAND [ARGS]...`**

Build the environments defined in a python file or directory. This will build the images associated with the
environments.

To build the image for a single named environment:

```bash
flyte build hello.py my_env
```

To build the images for all environments in a file (without naming one), use the `--all` flag:

```bash
flyte build --all hello.py
```

To recursively build all environments in a directory and its subdirectories, use the `--recursive` flag:

```bash
flyte build --all --recursive ./src
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--copy-style` | `choice` | `loaded_modules` | Copy style of the eventual deploy. Must match the deploy's `--copy-style` so the image content hash — and therefore the registry tag — lines up. |
| `--root-dir` | `text` | `Sentinel.UNSET` | Override the root source directory, helpful when working with monorepos. |
| `--recursive` `-r` | `boolean` | `Sentinel.UNSET` | Recursively build all environments in the current directory and its subdirectories. |
| `--all` | `boolean` | `Sentinel.UNSET` | Build the images for all environments in the file or directory, ignoring the file name. |
| `--ignore-load-errors` `-i` | `boolean` | `Sentinel.UNSET` | Ignore errors when loading environments, especially when using `--recursive` or `--all`. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte create

**`flyte create COMMAND [ARGS]...`**

Create resources in a Flyte deployment.

{{< variant union >}}
{{< markdown >}}
#### flyte create api-key

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte create api-key [OPTIONS]`**

Create an API key for headless authentication.

This creates OAuth application credentials that can be used to authenticate
with Union without interactive login. The generated API key should be set
as the FLYTE_API_KEY environment variable. Oauth applications should not be
confused with Union Apps, which are a different construct entirely.

Examples:

```bash
# Create an API key named "ci-pipeline"
$ flyte create api-key --name ci-pipeline

# Create a locked-down key with no default policy attachments
$ flyte create api-key --name ci-pipeline --no-default-policies

# The output will include an export command like:
# export FLYTE_API_KEY="<base64-encoded-credentials>"
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--name` | `text` | `Sentinel.UNSET` | Name for API key |
| `--no-default-policies` | `boolean` | `Sentinel.UNSET` | Skip attaching the server's default policies. Grant access explicitly via 'flyte create assignment'. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte create artifact

**`flyte create artifact [OPTIONS] NAME`**

Publish an artifact from the local machine.

The file is uploaded to blob storage and stored in the artifact service as a
File artifact. Primitive values (strings, numbers) are not allowed as
artifacts: an artifact is an addressable asset, not a scalar.


Example usage:

```bash
flyte create artifact my_model --from-file model.pt --kind model --attr framework=torch
flyte create artifact llama3 --from-file weights.bin --external-ref hf://meta-llama/Meta-Llama-3-8B
flyte create artifact my_model --from-file model.pt --card model_card.html --card-type model
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--from-file` | `path` | `Sentinel.UNSET` | Publish a local file as a File artifact (contents upload to blob storage). |
| `--version` | `text` |  | Version to publish. Defaults to a random version. |
| `--description` | `text` |  | Human readable description. |
| `--attr` | `text` | `Sentinel.UNSET` | Free-form user metadata as key=value pairs. Can be specified multiple times. |
| `--kind` | `choice` |  | What the artifact is. Recorded under the reserved `flyte.io/kind` attr. Distinct from `--card-type`, which controls how an attached card renders. |
| `--external-ref` | `text` |  | Opaque reference into an external system (a URI, model id, ...) recorded as the artifact's source. |
| `--card` | `file` |  | Local card file (HTML by default) to upload and attach to the artifact for display in the UI. |
| `--card-format` | `choice` |  | Format of the card. Defaults to the card file's extension, or `html` when it has none. |
| `--card-type` | `choice` | `generic` | Kind of card being attached. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte create assignment

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte create assignment [OPTIONS]`**

Assign a policy to an identity.

Exactly one of --user-subject, --creds-subject, or --email must be provided.

Examples:

```bash
$ flyte --org my-org create assignment --user-subject user-123 --policy admin
$ flyte --org my-org create assignment --creds-subject app-456 --policy admin
$ flyte --org my-org create assignment --email jane@example.com --policy admin
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--user-subject` | `text` |  | User subject identifier |
| `--creds-subject` | `text` |  | Client credentials application subject |
| `--email` | `text` |  | User email for lookup |
| `--policy` | `text` | `Sentinel.UNSET` | Policy name to assign |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte create cluster

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte create cluster [OPTIONS] NAME`**

Register a new cluster.

The cluster also gets an implicit queue of the same name, in the same pool,
routing to it and nothing else. The cluster owns that name: `flyte create
queue` is rejected for it, and the queue's clusters/pool can no longer be
edited directly. The name 'default' is reserved and cannot be used.

Without --pool the cluster joins the reserved pool named 'default'; any
other pool must already exist and be live. When the default pool has been
deleted, --pool is required — name a pool or undelete the default pool.

Examples:

```bash
$ flyte create cluster my-cluster

$ flyte create cluster my-cluster --pool my-pool
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--pool` | `text` | `` | Cluster pool to associate the cluster with. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte create cluster-pool

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte create cluster-pool [OPTIONS] NAME`**

Create a cluster pool.

A cluster pool holds the object store / secret store / image registry config
shared by its member clusters. Requires --file or --edit to supply the config.

Examples:

```bash
$ flyte create cluster-pool my-pool --edit

$ flyte create cluster-pool my-pool --file pool.yaml
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--file` | `path` |  | Create pool from a YAML file |
| `--edit` | `boolean` | `Sentinel.UNSET` | Open an editor to configure the pool before creating |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte create config

**`flyte create config [OPTIONS]`**

Creates a configuration file for Flyte CLI.
If the `--output` option is not specified, it will create a file named `config.yaml` in the current directory.
If the file already exists, it will raise an error unless the `--force` option is used.

To point the CLI at a local devbox cluster started with `flyte start devbox`, use the `--devbox` shortcut:

```bash
$ flyte create config --devbox
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--devbox` | `boolean` | `False` | Configure for a local devbox cluster (see 'flyte start devbox'). Shortcut for '--endpoint localhost:30080 --insecure --project flytesnacks --domain development --builder local'. Mutually exclusive with --endpoint; --project/--domain may still be overridden. |
| `--endpoint` | `text` | `Sentinel.UNSET` | Endpoint of the Flyte backend. |
| `--insecure` | `boolean` | `Sentinel.UNSET` | Use an insecure connection to the Flyte backend. |
| `--org` | `text` | `Sentinel.UNSET` | Organization to use. This will override the organization in the configuration file. |
| `-o` `--output` | `path` | `.flyte/config.yaml` | Path to the output directory where the configuration will be saved. Defaults to current directory. |
| `--force` | `boolean` | `False` | Force overwrite of the configuration file if it already exists. |
| `--image-builder` `--builder` | `choice` | `local` | Image builder to use for building images. Defaults to `local`. |
| `--registry` | `text` |  | Container registry to use as the base registry when building images (e.g. `ghcr.io/my-org`). When set, this overrides the built-in default base registry. Equivalent to the `image.registry` config entry or the FLYTE_IMAGE_REGISTRY environment variable. |
| `--auth-type` | `choice` |  | Authentication type to use for the Flyte backend. Defaults to `pkce`. |
| `--local-persistence` | `boolean` | `False` | Enable SQLite persistence for local run metadata, allowing past runs to be browsed via `flyte start tui`. |
| `--local-tracked` | `boolean` | `False` | Report local run state to the Flyte control plane so local runs show up in the console. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte create policy

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte create policy [OPTIONS] NAME`**

Create a policy.

Requires --file or --edit to specify bindings for the policy.

Examples:

```bash
$ flyte --org my-org create policy my-policy --edit
$ flyte --org my-org create policy my-policy --file policy.yaml
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--file` | `path` |  | Create policy from a YAML file |
| `--edit` | `boolean` | `Sentinel.UNSET` | Open an editor to configure the policy before creating |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte create project

**`flyte create project [OPTIONS]`**

Create a new project.


Example usage:

```bash
flyte create project --id my_project_id --name "My Project"
flyte create project --id my_project_id --name "My Project" --description "My project" -l team=ml -l env=prod
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--id` | `text` | `Sentinel.UNSET` | Unique identifier for the project (immutable). |
| `--name` | `text` | `Sentinel.UNSET` | Display name for the project. |
| `--description` | `text` | `` | Description for the project. |
| `--label` `-l` | `text` | `Sentinel.UNSET` | Labels as key=value pairs. Can be specified multiple times. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte create queue

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte create queue [OPTIONS] NAME`**

Create a scheduling queue.

Examples:

```bash
$ flyte create queue my-queue --run-concurrency 100 --action-concurrency 1000

$ flyte create queue gpu-queue --run-concurrency 50 --action-concurrency 500 \
    --priority min --cluster gpu-cluster-1

$ flyte create queue pool-queue --run-concurrency 50 --action-concurrency 500 \
    --cluster-pool gpu-pool

$ flyte create queue backfill --run-concurrency 10 --action-concurrency 100 \
    --depth 5000 --priority max

$ flyte create queue team-queue --run-concurrency 100 --action-concurrency 1000 \
    --project my-project --domain production
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--run-concurrency` | `integer` | `Sentinel.UNSET` | Max concurrent runs (required) |
| `--action-concurrency` | `integer` | `Sentinel.UNSET` | Max concurrent actions (required) |
| `--depth` | `integer` | `10000` | Max queue depth |
| `--priority` | `choice` | `medium` | Queue priority |
| `--fairness` | `choice` | `round_robin` | Fairness algorithm |
| `--cluster` | `text` | `Sentinel.UNSET` | Target cluster(s). Repeat for multiple. |
| `--cluster-pool` | `text` |  | Cluster pool to bind the queue to. Optional; defaults to the pool named 'default'. |
| `--project` | `text` | `` | Scope queue to a project |
| `--domain` | `text` | `` | Scope queue to a domain |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte create role

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte create role [OPTIONS] NAME`**

Create a role.

Requires --file or --edit to specify actions for the role.

Examples:

```bash
$ flyte --org my-org create role my-role --edit
$ flyte --org my-org create role my-role --file role.yaml
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--file` | `path` |  | Create role from a YAML file |
| `--edit` | `boolean` | `Sentinel.UNSET` | Open an editor to configure the role before creating |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte create secret

**`flyte create secret [OPTIONS] NAME`**

Create a new secret. The name of the secret is required. For example:

```bash
$ flyte create secret my_secret --value my_value
```

If you don't provide a `--value` flag, you will be prompted to enter the
secret value in the terminal.

```bash
$ flyte create secret my_secret
Enter secret value:
```

If `--from-file` is specified, the value will be read from the file instead of being provided directly:

```bash
$ flyte create secret my_secret --from-file /path/to/secret_file
```

The `--type` option can be used to create specific types of secrets.
Either `regular` or `image_pull` can be specified.
Secrets intended to access container images should be specified as `image_pull`.
Other secrets should be specified as `regular`.
If no type is specified, `regular` is assumed.

For image pull secrets, you have several options:

1. Interactive mode (prompts for registry, username, password):
```bash
$ flyte create secret my_secret --type image_pull
```

2. With explicit credentials:
```bash
$ flyte create secret my_secret --type image_pull --registry ghcr.io --username myuser
```

3. Lastly, you can create a secret from your existing Docker installation (i.e., you've run `docker login` in
the past) and you just want to pull from those credentials. Since you may have logged in to multiple registries,
you can specify which registries to include. If no registries are specified, all registries are added.
```bash
$ flyte create secret my_secret --type image_pull --from-docker-config --registries ghcr.io,docker.io
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--value` | `text` | `Sentinel.UNSET` | Secret value Mutually exclusive with from_file, from_docker_config, registry. |
| `--from-file` | `path` | `Sentinel.UNSET` | Path to the file with the binary secret. Mutually exclusive with value, from_docker_config, registry. |
| `--type` | `choice` | `regular` | Type of the secret. |
| `--from-docker-config` | `boolean` | `Sentinel.UNSET` | Create image pull secret from Docker config file (only for `--type` image_pull). Mutually exclusive with value, from_file, registry, username, password. |
| `--docker-config-path` | `path` | `Sentinel.UNSET` | Path to Docker config file (defaults to ~/.docker/config.json or $DOCKER_CONFIG). Requires from_docker_config. |
| `--registries` | `text` | `Sentinel.UNSET` | Comma-separated list of registries to include (only with `--from-docker-config`). |
| `--registry` | `text` | `Sentinel.UNSET` | Registry hostname (e.g., ghcr.io, docker.io) for explicit credentials (only for `--type` image_pull). Mutually exclusive with value, from_file, from_docker_config. |
| `--username` | `text` | `Sentinel.UNSET` | Username for the registry (only with `--registry`). |
| `--password` | `text` | `Sentinel.UNSET` | Password for the registry (only with `--registry`). If not provided, will prompt. |
| `--cluster-pool` | `text` |  | Scope the secret to a cluster pool. Mutually exclusive with `--project` and `--domain`. Mutually exclusive with project, domain. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte create trigger

**`flyte create trigger [OPTIONS] TASK_NAME NAME`**

Create a new trigger for a task. The task name and trigger name are required.

Example:

```bash
$ flyte create trigger my_task my_trigger --schedule "0 0 * * *"
```

This will create a trigger that runs every day at midnight.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--schedule` | `text` | `Sentinel.UNSET` | Cron schedule for the trigger. Defaults to every minute. |
| `--description` | `text` | `` | Description of the trigger. |
| `--auto-activate` | `boolean` | `True` | Whether the trigger should not be automatically activated. Defaults to True. |
| `--trigger-time-var` | `text` | `trigger_time` | Variable name for the trigger time in the task inputs. Defaults to `trigger_time`. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte create user

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte create user [OPTIONS]`**

Create (invite) a new user.

Examples:

```bash
$ flyte --org my-org create user --first-name Jane --last-name Doe --email jane@example.com
$ flyte --org my-org create user --first-name Jane --last-name Doe --email jane@example.com --policy admin
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--first-name` | `text` | `Sentinel.UNSET` | First name of the user |
| `--last-name` | `text` | `Sentinel.UNSET` | Last name of the user |
| `--email` | `text` | `Sentinel.UNSET` | Email address of the user |
| `--policy` | `text` |  | Policy to assign to the user after creation |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
### flyte debug

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte debug [OPTIONS] RUN_NAME [ACTION_NAME]`**

Relaunch RUN_NAME's task with ssh-debug enabled, then connect.

Only RUN_NAME is required; ACTION_NAME defaults to the root action ``a0``. The new run
re-uses the original inputs and comes up with sshd; this then prints its ssh-config.

Re-running ``flyte debug RUN_NAME`` reconnects to the same debug run (it isn't relaunched
twice) and refreshes the token in place — so it doubles as "just reattach".

Examples:

```bash
# Relaunch a prior run in debug mode and print its ssh-config
$ flyte debug my-run

# Named session (ssh Host alias + remote run name), written into ~/.ssh/config
$ flyte debug my-run --name my-dbg --api-key --write-config

# A new --name starts a fresh debug run (e.g. the previous one died)
$ flyte debug my-run --name my-dbg2

# Fire-and-forget: relaunch and return without waiting for the pod to come up
$ flyte debug my-run --no-wait

# Then connect (or VS Code -> Remote-SSH -> <name>)
$ ssh my-dbg
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--user` | `text` | `root` | SSH login user inside the pod. |
| `--identity-file` | `text` |  | Private key to authenticate with. Defaults to the auto-managed ~/.flyte/ssh-debug/id_ed25519 (created for you; no ssh-keygen needed). |
| `--name` | `text` |  | Name for this debug session — used as both the ~/.ssh/config Host alias and the remote debug run name. Re-running with the same name reconnects to the live session; a new name starts a fresh debug run (handy if the previous one died). Defaults to a name derived from RUN_NAME. |
| `--api-key` `--no-api-key` | `boolean` | `False` | Authenticate the tunnel with a dedicated, long-lived API key (created/reused as `flyte-ssh-debug`) instead of your interactive session token. Survives re-logins and won't expire mid-session. |
| `--refresh-token` | `boolean` | `Sentinel.UNSET` | Force a fresh Bearer instead of reusing the cached one (use if you hit auth errors). |
| `--write-config` | `boolean` | `Sentinel.UNSET` | Write the Host block into ~/.ssh/config (replacing any prior block for the same name). |
| `--wait` `--no-wait` | `boolean` | `True` | Wait for the debug run to start and its ssh route to become ready, then print the ssh-config. With --no-wait, relaunch and return immediately (don't block on the pod coming up); re-run the same command later to attach once it's running. |
| `--timeout` | `float` | `300.0` | Seconds to wait for the debug route to become ready. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

### flyte delete

**`flyte delete COMMAND [ARGS]...`**

Remove resources from a Flyte deployment.

{{< variant union >}}
{{< markdown >}}
#### flyte delete api-key

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte delete api-key [OPTIONS] CLIENT_ID`**

Delete an API key.

Examples:

```bash
# Delete an API key (with confirmation)
$ flyte delete api-key my-client-id

# Delete without confirmation
$ flyte delete api-key my-client-id --yes
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--yes` | `boolean` | `Sentinel.UNSET` | Skip confirmation prompt |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte delete app

**`flyte delete app [OPTIONS] NAME`**

Delete apps from a Flyte deployment.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte delete assignment

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte delete assignment [OPTIONS]`**

Unassign a policy from an identity.

Exactly one of --user-subject, --creds-subject, or --email must be provided.

Examples:

```bash
$ flyte --org my-org delete assignment --user-subject user-123 --policy admin
$ flyte --org my-org delete assignment --creds-subject app-456 --policy admin
$ flyte --org my-org delete assignment --email jane@example.com --policy admin
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--user-subject` | `text` |  | User subject identifier |
| `--creds-subject` | `text` |  | Client credentials application subject |
| `--email` | `text` |  | User email for lookup |
| `--policy` | `text` | `Sentinel.UNSET` | Policy name to unassign |
| `--yes` | `boolean` | `Sentinel.UNSET` | Skip confirmation prompt |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte delete cluster

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte delete cluster [OPTIONS] NAME`**

Delete a cluster.

A cluster can be deleted from any live state. A drained cluster — already
confirmed empty — is soft-deleted right away. An active or draining
cluster enters the 'deleting' state instead: it stops receiving work, its
workers are disconnected, and its running work is rescheduled on other
clusters, after which it becomes 'deleted'. Deletion does not wait for
running work and cannot be cancelled; pods left on the dataplane are your
responsibility to clean up. To let running work finish first, drain the
cluster and wait for 'drained' before deleting.

The delete is a soft delete: the cluster stops being routed to and drops out
of `flyte get cluster`, but it keeps its name reserved — creating a cluster
with the same name is rejected until it is restored with
`flyte undelete cluster`.

The cluster's co-named implicit queue is deleted with it, whatever state
that queue is in. Any other live queue that pins this cluster blocks the
delete and has to be unpinned first; already-deleted queues do not block
it. Apps assigned to the cluster are evicted.

Examples:

```bash
$ flyte delete cluster my-cluster

$ flyte delete cluster my-cluster --yes
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--yes` | `boolean` | `Sentinel.UNSET` | Skip confirmation prompt |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte delete cluster-pool

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte delete cluster-pool [OPTIONS] NAME`**

Delete a cluster pool.

The delete is a soft delete: the pool drops out of `flyte get cluster-pool`
and can no longer be assigned to clusters or queues, but it keeps its name
reserved — creating a pool with the same name is rejected until it is
restored with `flyte undelete cluster-pool`.

The pool must be empty: no member clusters and no live queues assigned to it.
Queues that are themselves deleted do not block it, but they can only be
undeleted once the pool is. The reserved 'default' pool follows the same
rules: deleting it requires draining and deleting its 'default' queue first,
and while the pool is deleted, `flyte create cluster` without --pool is
rejected instead of falling back to it.

Examples:

```bash
$ flyte delete cluster-pool my-pool

$ flyte delete cluster-pool my-pool --yes
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--yes` | `boolean` | `Sentinel.UNSET` | Skip confirmation prompt |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte delete devbox

**`flyte delete devbox [OPTIONS]`**

Stop and remove the local Flyte devbox cluster container.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--volume` | `boolean` | `False` | Also delete the Docker volume used for persistent storage. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte delete local-cache

**`flyte delete local-cache`**

Delete the entire local cache directory (~/.flyte/local-cache).

This removes the local SQLite cache used for image lookups, bundle uploads,
run history, and task caching.

{{< variant union >}}
{{< markdown >}}
#### flyte delete policy

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte delete policy [OPTIONS] NAME`**

Delete a policy.

Examples:

```bash
$ flyte --org my-org delete policy my-policy
$ flyte --org my-org delete policy my-policy --yes
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--yes` | `boolean` | `Sentinel.UNSET` | Skip confirmation prompt |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte delete queue

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte delete queue [OPTIONS] NAME`**

Delete a queue.

The queue must not be accepting work: an active queue is rejected and has
to be drained first (`flyte update queue NAME --drain`), so deleting a
serving queue always takes two deliberate steps. A drained queue — already
confirmed empty — is soft-deleted right away. A queue still draining
enters the 'deleting' state instead: it stays listed, and becomes
'deleted' once its remaining work is cleaned up. Deletion cannot be
cancelled; a deleted queue can be restored with `flyte undelete queue`.

The delete is a soft delete: the queue stops being scheduled on and drops out
of the `flyte get queue` listing (fetching it by name still works and shows
when it was deleted), but it keeps its name reserved — creating a queue with
the same name is rejected until it is restored with `flyte undelete queue`.

A queue referenced as run.default_queue in settings at any scope cannot be
deleted until those settings are updated or unset. The reserved 'default'
queue is no exception: it can be drained and deleted like any other queue,
but while it is deleted, runs that name no queue (and have no
run.default_queue setting) are rejected.

Examples:

```bash
$ flyte update queue my-queue --drain

$ flyte delete queue my-queue

$ flyte delete queue my-queue --yes
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--project` | `text` | `` | Scope to a project |
| `--domain` | `text` | `` | Scope to a domain |
| `--yes` | `boolean` | `Sentinel.UNSET` | Skip confirmation prompt |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte delete role

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte delete role [OPTIONS] NAME`**

Delete a role.

Examples:

```bash
$ flyte --org my-org delete role my-role
$ flyte --org my-org delete role my-role --yes
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--yes` | `boolean` | `Sentinel.UNSET` | Skip confirmation prompt |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte delete secret

**`flyte delete secret [OPTIONS] NAME`**

Delete a secret. The name of the secret is required.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--cluster-pool` | `text` |  | Scope the secret to a cluster pool. Mutually exclusive with `--project` and `--domain`. Mutually exclusive with project, domain. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte delete trigger

**`flyte delete trigger [OPTIONS] NAME TASK_NAME`**

Delete a trigger. The name of the trigger is required.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte delete user

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte delete user [OPTIONS] SUBJECT`**

Delete a user.

Examples:

```bash
$ flyte --org my-org delete user user-subject-id
$ flyte --org my-org delete user user-subject-id --yes
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--yes` | `boolean` | `Sentinel.UNSET` | Skip confirmation prompt |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

### flyte deploy

**`flyte deploy [OPTIONS] COMMAND [ARGS]...`**

Deploy one or more environments from a python file.

This command will create or update environments in the Flyte system, registering
all tasks and their dependencies.

Example usage:

```bash
flyte deploy hello.py my_env
```

Arguments to the deploy command are provided right after the `deploy` command and before the file name.

To deploy all environments in a file, use the `--all` flag:

```bash
flyte deploy --all hello.py
```

To recursively deploy all environments in a directory and its subdirectories, use the `--recursive` flag:

```bash
flyte deploy --recursive ./src
```

You can combine `--all` and `--recursive` to deploy everything:

```bash
flyte deploy --all --recursive ./src
```

You can provide image mappings with `--image` flag. This allows you to specify
the image URI for the task environment during CLI execution without changing
the code. Any images defined with `Image.from_ref_name("name")` will resolve to the
corresponding URIs you specify here.

```bash
flyte deploy --image my_image=ghcr.io/myorg/my-image:v1.0 hello.py my_env
```

If the image name is not provided, it is regarded as a default image and will
be used when no image is specified in TaskEnvironment:

```bash
flyte deploy --image ghcr.io/myorg/default-image:latest hello.py my_env
```

You can specify multiple image arguments:

```bash
flyte deploy --image ghcr.io/org/default:latest --image gpu=ghcr.io/org/gpu:v2.0 hello.py my_env
```

To deploy a specific version, use the `--version` flag:

```bash
flyte deploy --version v1.0.0 hello.py my_env
```

To preview what would be deployed without actually deploying, use the `--dry-run` flag:

```bash
flyte deploy --dry-run hello.py my_env
```

You can specify the `--config` flag to point to a specific Flyte cluster:

```bash
flyte --config my-config.yaml deploy hello.py my_env
```

You can override the default configured project and domain:

```bash
flyte deploy --project my-project --domain development hello.py my_env
```

If loading some files fails during recursive deployment, you can use the `--ignore-load-errors` flag
to continue deploying the environments that loaded successfully:

```bash
flyte deploy --recursive --ignore-load-errors ./src
```

Other arguments to the deploy command are listed below.

To see the environments available in a file, use `--help` after the file name:

```bash
flyte deploy hello.py --help
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--version` | `text` | `Sentinel.UNSET` | Version of the environment to deploy |
| `--dry-run` `--dryrun` | `boolean` | `False` | Dry run. Do not actually call the backend service. |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when running the task |
| `--root-dir` | `text` | `Sentinel.UNSET` | Override the root source directory, helpful when working with monorepos. |
| `--recursive` `-r` | `boolean` | `Sentinel.UNSET` | Recursively deploy all environments in the current directory |
| `--all` | `boolean` | `Sentinel.UNSET` | Deploy all environments in the current directory, ignoring the file name |
| `--ignore-load-errors` `-i` | `boolean` | `Sentinel.UNSET` | Ignore errors when loading environments especially when using `--recursive` or `--all`. |
| `--no-sync-local-sys-paths` | `boolean` | `False` | Disable synchronization of local sys.path entries under the root directory to the remote container. |
| `--image` | `text` | `Sentinel.UNSET` | Image to be used in the run. Format: imagename=imageuri. Can be specified multiple times. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte edit

**`flyte edit COMMAND [ARGS]...`**

#### flyte edit settings

**`flyte edit settings [OPTIONS]`**

Edit hierarchical settings interactively — or apply a YAML file directly.

**Interactive mode** (default). Opens settings in your `$EDITOR`. Three
comment tiers appear:

- `###` section headers and the scope line
- `##` per-field descriptions and inline metadata
- `#` inactive settings (uncomment the single `#` to activate)

If the edited YAML fails to parse, the editor reopens with an error
header so you can fix the syntax without losing your edits. If you
decline to reopen — or if the server rejects the update — your buffer
is saved under `~/.flyte/settings-edit-<timestamp>.yaml`.

**Non-interactive mode**: pass `--from-file <path>` to skip the editor
entirely. The file's contents are parsed, the diff is printed, and the
overrides are applied without a confirmation prompt. Ideal for
CI/automation.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--from-file` `-f` | `file` |  | Apply overrides from a YAML file and skip the editor. The file can be produced by `flyte get settings` (comment markers are honoured) or be a plain YAML mapping of flat dot-notation keys to values. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
### flyte explore

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte explore COMMAND [ARGS]...`**

Explore artifacts produced by Flyte runs.
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte explore volume

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte explore volume [OPTIONS] [RUN_NAME] [ACTION_NAME]`**

Browse a Volume's metadata index in an interactive TUI.

Only RUN_NAME is required: ACTION_NAME defaults to the root action
``a0``, and when ``--op-name`` is omitted the action's outputs are
searched for a Volume, then its inputs.

Examples:

```bash
# Root action's Volume, auto-discovered.
$ flyte explore volume my-run

# A specific action; still auto-discovers the Volume op.
$ flyte explore volume my-run my-action

# Pin the exact output (or input) to explore.
$ flyte explore volume my-run my-action --op-name ckpt

# Different project / domain than the CLI default.
$ flyte explore volume my-run my-action --project p --domain d

# Already-downloaded Volume .json — no control-plane round-trip.
$ flyte explore volume --from-file ./my-volume.json

# Raw index file (sqlite | redis) — debug path.
$ flyte explore volume --from-file ./index.db --store-type sqlite
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--op-name` | `text` |  | Name of the Volume value on the action (output or input). If omitted, the action's outputs are searched for a Volume, then its inputs. |
| `--from-file` | `file` |  | Skip remote resolution; open a local Volume .json or raw index file directly. |
| `--store-type` | `choice` |  | Backend type when --from-file points at a raw index. Auto-detected from a Volume value otherwise. |
| `--name` | `text` |  | Display name shown in the TUI header (only meaningful with --from-file on a raw index). |
| `--project` | `text` |  | Override the project context for resolution. Defaults to the CLI config. |
| `--domain` | `text` |  | Override the domain context for resolution. Defaults to the CLI config. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
### flyte fork

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte fork [OPTIONS] COMMAND [ARGS]...`**

Fork a prior run: reuse its succeeded actions, but run your *current* local code.

```bash
flyte fork ul56wcvgqrb9vzhzz5l2 hello.py my_task
```

A fresh code bundle is built from your working tree, so actions (tasks and traces) whose code
changed re-execute while everything that succeeded and is unchanged is reused. This is "time
travel debugging": go back to a run, change code, and replay only what that change affects.

How it differs from the built-in verbs:

```bash
flyte rerun <run>            # same code, same inputs, everything re-executes
flyte rerun <run> --recover  # same code, reuse succeeded actions (failure recovery)
flyte fork <run> ...         # NEW code, reuse succeeded actions
```

Force specific actions to re-execute even though they succeeded:

```bash
flyte fork --force-rerun-action a3 <run> hello.py my_task
```

`flyte fork` takes the run to fork first, then the file and task, with `flyte run`'s options —
image, copy-style, service-account, env, labels, queue and the rest — before them. It takes no
task inputs: a fork replays the ones the source run was launched with. Remote-only — forking a
run has no local equivalent.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--local` | `boolean` | `Sentinel.UNSET` | Run the task locally |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when running the task |
| `--root-dir` | `text` | `Sentinel.UNSET` | Override the root source directory, helpful when working with monorepos. |
| `--raw-data-path` | `text` | `Sentinel.UNSET` | Override the output prefix used to store offloaded data types. e.g. s3://bucket/ |
| `--service-account` | `text` | `Sentinel.UNSET` | Kubernetes service account. If not provided, the configured default will be used |
| `--name` | `text` | `Sentinel.UNSET` | Name of the run. If not provided, a random name will be generated. |
| `--follow` `-f` | `boolean` | `False` | Wait and watch logs for the parent action. If not provided, the CLI will exit after successfully launching a remote execution with a link to the UI. |
| `--tui` | `boolean` | `False` | Show interactive TUI for local execution (requires flyte[tui]). |
| `--tracked` | `boolean` | `False` | Run the task locally (implies `--local`) while reporting run state to the Flyte control plane so the run shows up in the console. Requires a configured endpoint, project and domain. |
| `--tracked-strict` | `boolean` | `False` | Strict tracked-run reporting for debugging (only valid with `--tracked`): any reporting failure fails the run loudly instead of being logged and swallowed. |
| `--image` | `text` | `Sentinel.UNSET` | Image to be used in the run. Format: imagename=imageuri. Can be specified multiple times. |
| `--no-sync-local-sys-paths` | `boolean` | `False` | Disable synchronization of local sys.path entries under the root directory to the remote container. |
| `--run-project` | `text` |  | Run the remote task in this project, only applicable when using `deployed-task` subcommand. |
| `--run-domain` | `text` |  | Run the remote task in this domain, only applicable when using `deployed-task` subcommand. |
| `--debug` | `boolean` | `False` | Run the task as a VSCode debug task. Starts a code-server in the container so you can connect via the UI to interactively debug/run the task. |
| `--env` `-e` | `text` | `Sentinel.UNSET` | Environment variable to set on the run context. Format: KEY=VALUE. Can be specified multiple times, e.g. `-e LOG_LEVEL=debug -e FOO=bar`. |
| `--max-action-concurrency` | `integer range` |  | Maximum number of actions that can run concurrently within the run. If not provided, the platform default (run.max_action_concurrency setting) applies. |
| `--label` | `text` | `Sentinel.UNSET` | User-defined label to attach to the run. Format: KEY=VALUE. Can be specified multiple times, e.g. `--label team=ml --label env=prod`. |
| `--queue` | `text` |  | Queue (cluster) to send the run to. Overrides any queue set on the task. |
| `--force-rerun-action` | `text` | `Sentinel.UNSET` | Name of an action to re-execute even though it succeeded in the forked run. Repeatable. A listed parent re-enqueues its children (list them too to force the whole subtree); unknown names are ignored. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

### flyte gen

**`flyte gen COMMAND [ARGS]...`**

Generate documentation.

#### flyte gen docs

**`flyte gen docs [OPTIONS]`**

Generate documentation.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--type` | `text` | `Sentinel.UNSET` | Type of documentation (valid: markdown, json) |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte get

**`flyte get COMMAND [ARGS]...`**

Retrieve resources from a Flyte deployment.

You can get information about projects, runs, tasks, actions, secrets, logs and input/output values,
as well as the status of the local devbox cluster.

Each command supports optional parameters to filter or specify the resource you want to retrieve.

Using a `get` subcommand without any arguments will retrieve a list of available resources to get.
For example:

* `get project` (without specifying a project), will list all projects.
* `get project my_project` will return the details of the project named `my_project`.

In some cases, a partially specified command will act as a filter and return available further parameters.
For example:

* `get action my_run` will return all actions for the run named `my_run`.
* `get action my_run my_action` will return the details of the action named `my_action` for the run `my_run`.

#### flyte get action

**`flyte get action [OPTIONS] RUN_NAME [ACTION_NAME]`**

Get all actions for a run or details for a specific action.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--in-phase` | `choice` | `Sentinel.UNSET` | Filter actions by their phase. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte get api-key

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get api-key [OPTIONS] [CLIENT_ID]`**

Get or list API keys.

If CLIENT-ID is provided, gets a specific API key.
Otherwise, lists all API keys.

Examples:

```bash
# List all API keys
$ flyte get api-key

# List with a limit
$ flyte get api-key --limit 10

# Get a specific API key
$ flyte get api-key my-client-id
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Maximum number of keys to list |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte get app

**`flyte get app [OPTIONS] [NAME]`**

Get a list of all apps, or details of a specific app by name.

Apps are long-running services deployed on the Flyte platform.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of apps to fetch when listing. |
| `--only-mine` | `boolean` | `False` | Show only apps created by the current user (you). |
| `--status` | `choice` |  | Filter apps by deployment status. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte get artifact

**`flyte get artifact [OPTIONS] [NAME] [VERSION]`**

Get artifacts: names, versions of a name, or one version's details.


Example usage:

```bash
flyte get artifact                       # distinct artifact names (latest info + version count)
flyte get artifact my_artifact           # every version of my_artifact, newest first
flyte get artifact my_artifact 1.0       # details of a pinned version
flyte get artifact --search model        # names containing "model"
flyte get artifact --source-run my_run   # versions produced by a run
flyte get artifact --source-external-ref hf://meta-llama/Meta-Llama-3-8B
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of results to fetch when listing. |
| `--search` | `text` |  | Substring match on the artifact name when listing names. |
| `--created-after` | `datetime` |  | Show versions created at or after this datetime (UTC). Accepts ISO dates, `now`, `today`, or `now - 1 day`. |
| `--source-run` | `text` |  | Only artifact versions produced by this run. |
| `--source-action` | `text` |  | Only artifact versions produced by this action; usually combined with `--source-run`. |
| `--source-external-ref` | `text` |  | Only artifact versions imported from this external reference. |
| `--kind` | `choice` |  | Only artifacts of this kind. Shorthand for `--attr` on the reserved kind key. |
| `--attr` | `text` | `Sentinel.UNSET` | Only artifacts whose attrs match, as key=value. Repeatable; separate keys must all match. Filtering happens server-side. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte get assignment

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get assignment [OPTIONS]`**

Get or list assignments.

Without --user-subject, --creds-subject, or --email, lists all assignments.

Examples:

```bash
$ flyte --org my-org get assignment
$ flyte --org my-org get assignment --user-subject user-123
$ flyte --org my-org get assignment --creds-subject app-456
$ flyte --org my-org get assignment --email jane@example.com
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--user-subject` | `text` |  | User subject identifier |
| `--creds-subject` | `text` |  | Client credentials application subject |
| `--email` | `text` |  | User email for lookup |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte get cluster

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get cluster [OPTIONS] [NAME]`**

Get a cluster or list all clusters.

If NAME is provided, fetch that specific cluster and render a detailed view.
Otherwise list all clusters.

Deleted clusters are hidden by default; --deleted lists them instead, which
is how you find a cluster to pass to `flyte undelete cluster`.

Examples:

```bash
$ flyte get cluster

$ flyte get cluster my-cluster

$ flyte get cluster --deleted
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Maximum number of clusters to return. |
| `--deleted` | `boolean` | `Sentinel.UNSET` | List only soft-deleted clusters (candidates for 'flyte undelete cluster'). Cannot be combined with NAME. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte get cluster-config

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get cluster-config [OPTIONS] CLUSTER_NAME`**

Get the tracked ConfigMaps of a cluster.

Shows the live contents of the ConfigMaps the cluster is running with, read
from the cluster's dataplane. Values are served verbatim.

Examples:

```bash
$ flyte get cluster-config my-cluster

$ flyte get cluster-config my-cluster --config-map union-operator

$ flyte get cluster-config my-cluster --config-map executor --key config.yaml --raw
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--config-map` | `text` |  | Only show this ConfigMap (e.g. union-operator, executor, leaseworker, flyte-propeller-config). |
| `--key` | `text` |  | Only show this key within the ConfigMap. Requires --config-map. |
| `--raw` | `boolean` | `Sentinel.UNSET` | Print the selected value(s) unformatted, with no panels — useful for piping. Requires --config-map. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte get cluster-pool

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get cluster-pool [OPTIONS] [NAME]`**

Get or list cluster pools.

If NAME is provided, gets a specific pool. Otherwise, lists all pools.

Deleted pools are hidden by default; --deleted lists them instead, which is
how you find a pool to pass to `flyte undelete cluster-pool`.

Examples:

```bash
$ flyte get cluster-pool

$ flyte get cluster-pool my-pool

$ flyte get cluster-pool --deleted
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Maximum number of cluster pools to list |
| `--deleted` | `boolean` | `Sentinel.UNSET` | List only soft-deleted cluster pools (candidates for 'flyte undelete cluster-pool'). Cannot be combined with NAME. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte get condition

**`flyte get condition [OPTIONS] RUN_NAME [ACTION_NAME]`**

List conditions (paused condition actions) for a run, optionally filtered to a
specific parent action.

Each condition corresponds to a condition action registered via
`flyte.new_condition(...)` from a workflow. Use `flyte signal condition` to
resolve one.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte get config

**`flyte get config`**

Shows the automatically detected configuration to connect with the remote backend.

The configuration will include the endpoint, organization, and other settings that are used by the CLI.

#### flyte get devbox

**`flyte get devbox [OPTIONS]`**

Get the status of the local Flyte devbox cluster started with `flyte start devbox`.

Shows the run state, the UI and image registry endpoints, the container image
version in use, and where the cluster keeps its state on disk.

Pass an output format to the top-level command for a machine-readable report:


```bash
flyte -of json-raw get devbox
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--no-probes` | `boolean` | `False` | Skip the HTTP readiness probe and the container resource usage sample, for a faster, offline check. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte get io

**`flyte get io [OPTIONS] RUN_NAME [ACTION_NAME]`**

Get the inputs and outputs of a run or action.
If only the run name is provided, it will show the inputs and outputs of the root action of that run.
If an action name is provided, it will show the inputs and outputs for that action.
If `--inputs-only` or `--outputs-only` is specified, it will only show the inputs or outputs respectively.

Examples:

```bash
$ flyte get io my_run
```

```bash
$ flyte get io my_run my_action
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--inputs-only` `-i` | `boolean` | `Sentinel.UNSET` | Show only inputs |
| `--outputs-only` `-o` | `boolean` | `Sentinel.UNSET` | Show only outputs |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte get logs

**`flyte get logs [OPTIONS] RUN_NAME [ACTION_NAME]`**

Stream logs for the provided run or action.
If only the run is provided, only the logs for the parent action will be streamed:

```bash
$ flyte get logs my_run
```

If you want to see the logs for a specific action, you can provide the action name as well:

```bash
$ flyte get logs my_run my_action
```

By default, logs will be shown in the raw format and will scroll the terminal.
If automatic scrolling and only tailing `--lines` number of lines is desired, use the `--pretty` flag:

```bash
$ flyte get logs my_run my_action --pretty --lines 50
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--lines` `-l` | `integer` | `30` | Number of lines to show, only useful for `--pretty` |
| `--show-ts` | `boolean` | `Sentinel.UNSET` | Show timestamps |
| `--pretty` | `boolean` | `False` | Show logs in an auto-scrolling box, where number of lines is limited to `--lines` |
| `--attempt` `-a` | `integer` |  | Attempt number to show logs for, defaults to the latest attempt. |
| `--filter-system` | `boolean` | `False` | Filter all system logs from the output. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte get member

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get member`**

List all members (users and applications) in an organization.

Examples:

```bash
$ flyte --org my-org get member
```
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte get metrics

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get metrics [OPTIONS] [RUN_NAME] [ACTION_NAME]`**

Get pod metrics for a task's action attempt or an app.

Metrics (CPU, memory, GPU utilization and health, app request metrics) are
collected from the pods an execution ran on and answered by the cluster's
dataplane, as shown in the Union UI.

Examples:

```bash
# Metrics of a run's root action (its task pod)
$ flyte get metrics my-run

# Metrics of a specific action attempt, restricted to two metrics
$ flyte get metrics my-run a1 --attempt 2 -m cpu_utilization -m memory_utilization

# Metrics of an app's pods over the last 6 hours
$ flyte get metrics --app my-app --since 6h

# Full prometheus time series, as JSON
$ flyte get metrics my-run --output json
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--app` | `text` |  | Get metrics for this app instead of a run's action. |
| `--attempt` `-a` | `integer` |  | Attempt number to get metrics for, defaults to the latest attempt. |
| `--metric` `-m` | `choice` | `Sentinel.UNSET` | Metric to query; repeat for several. Defaults to the server's default set for the queried object. |
| `--since` | `text` |  | Only with --app: start of the time window as a duration before now, e.g. 6h, 2d. Defaults to 24h. |
| `--since-time` | `text` |  | Only with --app: start of the time window as an RFC3339 time, e.g. 2026-08-20T10:00:00Z. |
| `--end-time` | `text` |  | Only with --app: end of the time window as an RFC3339 time. Defaults to now. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte get policy

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get policy [OPTIONS] [NAME]`**

Get or list policies.

If NAME is provided, gets a specific policy. Otherwise, lists all policies.

Examples:

```bash
$ flyte --org my-org get policy
$ flyte --org my-org get policy --limit 10
$ flyte --org my-org get policy my-policy
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Maximum number of policies to list |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte get project

**`flyte get project [OPTIONS] [NAME]`**

Get a list of all projects, or details of a specific project by name.

By default, only active (unarchived) projects are shown. Use `--archived` to
show archived projects instead.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--archived` | `boolean` | `False` | Show archived projects instead of active ones. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte get queue

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get queue [OPTIONS] [NAME]`**

Get a queue or list all queues.

If NAME is provided, fetch that specific queue with its current metrics.
Use --watch to stream live metrics with progress bars. Metrics are
available for a queue in any state — a draining or drained queue can be
watched to confirm its in-flight work has finished.
Otherwise list all queues.

Deleted queues are hidden from the listing by default; --deleted lists them
instead, which is how you find a queue to pass to `flyte undelete queue`.
Fetching a queue by NAME returns it even when deleted, showing its deletion
time.

--state narrows the listing to queues in one state (active, draining,
drained, deleting or deleted); the server does the filtering. A deleting
queue is still live and listed; deleted queues only show up under
--deleted.

Examples:

```bash
$ flyte get queue

$ flyte get queue my-queue

$ flyte get queue my-queue --watch

$ flyte get queue --state active

$ flyte get queue --deleted
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--project` | `text` | `` | Scope to a project |
| `--domain` | `text` | `` | Scope to a domain |
| `--limit` | `integer` | `100` | Maximum number of queues to return |
| `--watch` | `boolean` | `Sentinel.UNSET` | Stream live queue metrics (requires NAME) |
| `--deleted` | `boolean` | `Sentinel.UNSET` | List only soft-deleted queues (candidates for 'flyte undelete queue'). Cannot be combined with NAME. |
| `--state` | `choice` |  | List only queues in this state. Cannot be combined with NAME. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte get role

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get role [OPTIONS] [NAME]`**

Get or list roles.

If NAME is provided, gets a specific role. Otherwise, lists all roles.

Examples:

```bash
$ flyte --org my-org get role
$ flyte --org my-org get role --limit 10
$ flyte --org my-org get role my-role
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Maximum number of roles to list |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte get run

**`flyte get run [OPTIONS] [NAME]`**

Get a list of all runs, or details of a specific run by name.

The run details will include information about the run, its status, but only the root action will be shown.

If you want to see the actions for a run, use `get action <run_name>`.

You can filter runs by task name and optionally task version:

```bash
$ flyte get run --task-name my_task
$ flyte get run --task-name my_task --task-version v1.0
```

You can filter runs by their user-defined labels:

```bash
$ flyte get run --with-label team=ml --with-label env=prod
$ flyte get run --with-label-key team
```

You can show only runs that have a paused action (waiting on a human in the loop):

```bash
$ flyte get run --paused-only
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of runs to fetch when listing. |
| `--in-phase` | `choice` | `Sentinel.UNSET` | Filter runs by their status. |
| `--only-mine` | `boolean` | `False` | Show only runs created by the current user (you). |
| `--paused-only` | `boolean` | `False` | Show only runs that have a paused action (waiting on a human in the loop). |
| `--task-name` | `text` |  | Filter runs by task name. |
| `--task-version` | `text` |  | Filter runs by task version. |
| `--created-after` | `datetime` |  | Show runs created at or after this datetime (UTC). Accepts ISO dates, `now`, `today`, or `now - 1 day`. |
| `--created-before` | `datetime` |  | Show runs created before this datetime (UTC). |
| `--updated-after` | `datetime` |  | Show runs updated at or after this datetime (UTC). Accepts ISO dates, `now`, `today`, or `now - 1 day`. |
| `--updated-before` | `datetime` |  | Show runs updated before this datetime (UTC). |
| `--with-label` | `text` | `()` | Filter runs that have this label key=value. Can be specified multiple times (AND semantics). |
| `--with-label-key` | `text` | `()` | Filter runs that have this label key present (existence check). Can be specified multiple times. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte get secret

**`flyte get secret [OPTIONS] [NAME]`**

Get a list of all secrets, or details of a specific secret by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--cluster-pool` | `text` |  | Scope the secret to a cluster pool. Mutually exclusive with `--project` and `--domain`. Mutually exclusive with project, domain. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte get settings

**`flyte get settings [OPTIONS]`**

Get settings for a scope as editable YAML.

Renders three sections:


* Local overrides — uncommented, applied at this scope.
* Inherited settings — commented, with the scope they come from.
* Available settings — commented placeholders for every key that
  isn't set anywhere yet, so you can see what can be configured.


Examples:

```bash
# Get ORG-level settings
flyte get settings

# Get settings for a domain
flyte get settings --domain production

# Get settings for a project (inherits from domain, which inherits from org)
flyte get settings --domain production --project ml-pipeline

# Dump to a file, edit it, then apply non-interactively
flyte get settings --domain production -o prod.yaml
# ...edit prod.yaml...
flyte edit settings --domain production --from-file prod.yaml
```

Use `flyte edit settings` to interactively modify these values.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--to-file` `-o` | `file` |  | Write the scope's YAML to this file instead of printing it. The file round-trips through `flyte edit settings --from-file`. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte get system-logs

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get system-logs [OPTIONS] CLUSTER_NAME`**

Stream the system logs of a cluster's dataplane components.

Tails the logs of the Union infrastructure running on a cluster (the union
operator, flytepropeller, the lease worker), read from the cluster's
dataplane. The stream ends when the dataplane closes it.

Examples:

```bash
$ flyte get system-logs my-cluster -n my-namespace

$ flyte get system-logs my-cluster -n my-namespace --application flytepropeller --since 5m

$ flyte get system-logs my-cluster -n my-ns --pod-label-selector "app.kubernetes.io/name=flyte-pod-webhook"

$ flyte get system-logs my-cluster -n my-namespace --source persistedonly --since-time 2026-08-20T10:00:00Z
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--namespace` `-n` | `text` | `Sentinel.UNSET` | Kubernetes namespace the components run in. |
| `--application` | `choice` |  | Component to tail. Defaults to unionoperator. Cannot be combined with --pod-label-selector. |
| `--pod-label-selector` | `text` |  | Tail the pods matching this Kubernetes label selector instead of a named application. |
| `--node` | `text` |  | Only tail pods running on this Kubernetes node. |
| `--since` | `text` |  | Show logs newer than this duration, e.g. 5m, 1h30m. Cannot be combined with --since-time. |
| `--since-time` | `text` |  | Show logs newer than this RFC3339 time, e.g. 2026-08-20T10:00:00Z. |
| `--source` | `choice` | `liveorpersisted` | Where to read logs from: live pods, the persisted backend, or (default) live falling back to persisted. |
| `--lines` `-l` | `integer` | `30` | Number of lines to keep in view, only useful for --pretty. |
| `--show-ts` | `boolean` | `Sentinel.UNSET` | Show timestamps. |
| `--pretty` | `boolean` | `False` | Show logs in an auto-scrolling box, where number of lines is limited to `--lines`. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte get task

**`flyte get task [OPTIONS] [NAME] [VERSION]`**

Retrieve a list of all tasks, or details of a specific task by name and version.

Currently, both `name` and `version` are required to get a specific task.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of tasks to fetch. |
| `--entrypoint` | `boolean` | `False` | Show only entrypoint tasks. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte get trigger

**`flyte get trigger [OPTIONS] [TASK_NAME] [NAME]`**

Get a list of all triggers, or details of a specific trigger by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of triggers to fetch. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte get user

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte get user [OPTIONS] [SUBJECT]`**

Get or list users.

If SUBJECT is provided, gets a specific user. Otherwise, lists all users.

Examples:

```bash
$ flyte --org my-org get user
$ flyte --org my-org get user --limit 10
$ flyte --org my-org get user user-subject-id
$ flyte --org my-org get user --email jane@example.com
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Maximum number of users to list |
| `--email` | `text` |  | Filter by email address |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

### flyte prefetch

**`flyte prefetch COMMAND [ARGS]...`**

Prefetch artifacts from remote registries.

These commands help you download and prefetch artifacts like HuggingFace models
to your Flyte storage for faster access during task execution.

#### flyte prefetch hf-model

**`flyte prefetch hf-model [OPTIONS] REPO`**

Prefetch a HuggingFace model to Flyte storage.

Downloads a model from the HuggingFace Hub and prefetches it to your configured
Flyte storage backend. This is useful for:

- Pre-fetching large models before running inference tasks
- Sharding models for tensor-parallel inference
- Avoiding repeated downloads during development

**Basic Usage:**

```bash
$ flyte prefetch hf-model meta-llama/Llama-2-7b-hf --hf-token-key HF_TOKEN
```

**With Sharding:**

Create a shard config file (shard_config.yaml):

```yaml
engine: vllm
args:
  tensor_parallel_size: 8
  dtype: auto
  trust_remote_code: true
```

Then run:

```bash
$ flyte prefetch hf-model meta-llama/Llama-2-70b-hf \
```bash
--shard-config shard_config.yaml \
--gpu A100:8 \
--hf-token-key HF_TOKEN
```
```

**Wait for Completion:**

```bash
$ flyte prefetch hf-model meta-llama/Llama-2-7b-hf --wait
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--raw-data-path` | `text` |  | Object store path to store the model. If not provided, the model will be stored using the default path generated by Flyte storage layer. |
| `--artifact-name` | `text` |  | Artifact name to use for the stored model. Must only contain alphanumeric characters, underscores, and hyphens. If not provided, the repo name will be used (replacing '.' with '-'). |
| `--architecture` | `text` | `Sentinel.UNSET` | Model architecture, as given in HuggingFace config.json. |
| `--task` | `text` | `auto` | Model task, e.g., `generate`, `classify`, `embed`, `score`, etc. Refer to vLLM docs. `auto` will try to discover this automatically. |
| `--modality` | `text` | `('text',)` | Modalities supported by the model, e.g., `text`, `image`, `audio`, `video`. Can be specified multiple times. |
| `--format` | `text` | `Sentinel.UNSET` | Model serialization format, e.g., safetensors, onnx, torchscript, joblib, etc. |
| `--model-type` | `text` | `Sentinel.UNSET` | Model type, e.g., `transformer`, `xgboost`, `custom`, etc. For HuggingFace models, this is auto-determined from config.json['model_type']. |
| `--short-description` | `text` | `Sentinel.UNSET` | Short description of the model. |
| `--force` | `integer` | `0` | Force store of the model. Increment value (`--force`=1, `--force`=2, ...) to force a new store. |
| `--wait` | `boolean` | `Sentinel.UNSET` | Wait for the model to be stored before returning. |
| `--hf-token-key` | `text` | `HF_TOKEN` | Name of the Flyte secret containing your HuggingFace token. Note: This is not the HuggingFace token itself, but the name of the secret in the Flyte secret store. |
| `--cpu` | `text` | `2` | CPU request for the prefetch task (e.g., `2`, `4`, '2,4' for 2-4 CPUs). |
| `--mem` | `text` | `8Gi` | Memory request for the prefetch task (e.g., `16Gi`, `64Gi`, '16Gi,64Gi' for 16-64GB). |
| `--gpu` | `choice` |  | The gpu to use for downloading and (optionally) sharding the model. Format: '{type}:{quantity}' (e.g., `A100:8`, `L4:1`). |
| `--disk` | `text` | `50Gi` | Disk storage request for the prefetch task (e.g., `100Gi`, `500Gi`). |
| `--shm` | `text` |  | Shared memory request for the prefetch task (e.g., `100Gi`, `auto`). |
| `--shard-config` | `path` | `Sentinel.UNSET` | Path to a YAML file containing sharding configuration. The file should have `engine` (currently only `vllm`) and `args` keys. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte rerun

**`flyte rerun [OPTIONS] RUN_NAME`**

Re-run an existing run RUN_NAME with its original code and inputs.

Fetches the prior run's task + inputs from the platform (no local code needed) and launches a
new run that returns the same way `flyte run` does. `--recover` reuses the prior run's
succeeded actions, re-running only what failed or never ran; `--force-rerun-action` forces
named actions to re-execute anyway.

`--action-name` narrows the whole thing to a single action: the new run is rooted at that
action's task, run with the exact inputs it received inside RUN_NAME. That is always a plain
re-execution, so it cannot be combined with `--recover`.

The task's own inputs are options too, built from RUN_NAME's interface just as `flyte run`
builds them from local code — run `flyte rerun RUN_NAME --help` to list them. Every input left
out keeps RUN_NAME's value. With `--recover`, the new run starts from the changed inputs but
still reuses RUN_NAME's succeeded actions, which keep the outputs they produced under the
*original* inputs — force the ones that must re-execute with `--force-rerun-action`.

Examples:

```bash
$ flyte rerun rxyz
$ flyte rerun rxyz --name retry-1 --follow
$ flyte rerun rxyz --recover
$ flyte rerun rxyz --recover --force-rerun-action a3 --force-rerun-action a7
$ flyte rerun rxyz --action-name a3
$ flyte rerun rxyz --help
$ flyte rerun rxyz --n 10 --cfg '{"lr": 0.1}'
$ flyte rerun rxyz --recover --n 10 --force-rerun-action a3
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project for the new run (defaults to config). |
| `-d` `--domain` | `text` |  | Domain for the new run (defaults to config). |
| `--name` | `text` |  | Name for the new run (a random name is generated if unset). |
| `-e` `--env` | `text` | `Sentinel.UNSET` | Env var KEY=VALUE for the new run. Repeatable. |
| `--label` | `text` | `Sentinel.UNSET` | Label KEY=VALUE for the new run. Repeatable. |
| `--follow` `-f` | `boolean` | `False` | Stream the parent action logs after launch. |
| `--recover` | `boolean` | `False` | Reuse the prior run's succeeded actions, re-running only what failed or never ran. Remote-only. |
| `--action-name` | `text` |  | Re-run only this action from the run, instead of the whole run: the new run is rooted at that action's task with the inputs it received. Cannot be combined with `--recover`. List names with `flyte get action <run>`. |
| `--force-rerun-action` | `text` | `Sentinel.UNSET` | With `--recover`: name of an action to re-execute even though it succeeded in the source run. Repeatable. A listed parent re-enqueues its children (list them too to force the whole subtree); unknown names are ignored. |
| `--allow-missing-outputs` | `boolean` | `False` | Proceed when the source run's outputs were cleaned up from storage, using its inputs URI directly. The inputs cannot be verified from the client — if they were deleted too, the new run fails at runtime. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte run

**`flyte run [OPTIONS] COMMAND [ARGS]...`**

Run a task from a python file or deployed task.

If you have never run a Flyte workflow before, start with the built-in example. It needs no files
of your own, and prints the path to its source so you can copy it into a project:

```bash
flyte run hello
```

Example usage:

```bash
flyte run hello.py my_task --arg1 value1 --arg2 value2
```

Arguments to the run command are provided right after the `run` command and before the file name.
Arguments for the task itself are provided after the task name.

To run a task locally, use the `--local` flag. This will run the task in the local environment instead of the remote
Flyte environment:

```bash
flyte run --local hello.py my_task --arg1 value1 --arg2 value2
```

You can provide image mappings with `--image` flag. This allows you to specify
the image URI for the task environment during CLI execution without changing
the code. Any images defined with `Image.from_ref_name("name")` will resolve to the
corresponding URIs you specify here.

```bash
flyte run --image my_image=ghcr.io/myorg/my-image:v1.0 hello.py my_task
```

If the image name is not provided, it is regarded as a default image and will
be used when no image is specified in TaskEnvironment:

```bash
flyte run --image ghcr.io/myorg/default-image:latest hello.py my_task
```

You can specify multiple image arguments:

```bash
flyte run --image ghcr.io/org/default:latest --image gpu=ghcr.io/org/gpu:v2.0 hello.py my_task
```

To run tasks that you've already deployed to Flyte, use the deployed-task command:

```bash
flyte run deployed-task my_env.my_task --arg1 value1 --arg2 value2
```

To run a specific version of a deployed task, use the `env.task:version` syntax:

```bash
flyte run deployed-task my_env.my_task:xyz123 --arg1 value1 --arg2 value2
```

You can specify the `--config` flag to point to a specific Flyte cluster:

```bash
flyte run --config my-config.yaml deployed-task ...
```

You can override the default configured project and domain:

```bash
flyte run --project my-project --domain development hello.py my_task
```

You can discover what deployed tasks are available by running:

```bash
flyte run deployed-task
```

To run an arbitrary Python script on a remote cluster (without defining a task), use `python-script`:

```bash
flyte run python-script script.py --gpu 1 --gpu-type A100 --memory 64Gi
```

You can also install extra packages and wait for completion:

```bash
flyte run --follow python-script train.py --packages torch,transformers
```

Other arguments to the run command are listed below.

Arguments for the task itself are provided after the task name and can be retrieved using `--help`. For example:

```bash
flyte run hello.py my_task --help
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--local` | `boolean` | `Sentinel.UNSET` | Run the task locally |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when running the task |
| `--root-dir` | `text` | `Sentinel.UNSET` | Override the root source directory, helpful when working with monorepos. |
| `--raw-data-path` | `text` | `Sentinel.UNSET` | Override the output prefix used to store offloaded data types. e.g. s3://bucket/ |
| `--service-account` | `text` | `Sentinel.UNSET` | Kubernetes service account. If not provided, the configured default will be used |
| `--name` | `text` | `Sentinel.UNSET` | Name of the run. If not provided, a random name will be generated. |
| `--follow` `-f` | `boolean` | `False` | Wait and watch logs for the parent action. If not provided, the CLI will exit after successfully launching a remote execution with a link to the UI. |
| `--tui` | `boolean` | `False` | Show interactive TUI for local execution (requires flyte[tui]). |
| `--tracked` | `boolean` | `False` | Run the task locally (implies `--local`) while reporting run state to the Flyte control plane so the run shows up in the console. Requires a configured endpoint, project and domain. |
| `--tracked-strict` | `boolean` | `False` | Strict tracked-run reporting for debugging (only valid with `--tracked`): any reporting failure fails the run loudly instead of being logged and swallowed. |
| `--image` | `text` | `Sentinel.UNSET` | Image to be used in the run. Format: imagename=imageuri. Can be specified multiple times. |
| `--no-sync-local-sys-paths` | `boolean` | `False` | Disable synchronization of local sys.path entries under the root directory to the remote container. |
| `--run-project` | `text` |  | Run the remote task in this project, only applicable when using `deployed-task` subcommand. |
| `--run-domain` | `text` |  | Run the remote task in this domain, only applicable when using `deployed-task` subcommand. |
| `--debug` | `boolean` | `False` | Run the task as a VSCode debug task. Starts a code-server in the container so you can connect via the UI to interactively debug/run the task. |
| `--env` `-e` | `text` | `Sentinel.UNSET` | Environment variable to set on the run context. Format: KEY=VALUE. Can be specified multiple times, e.g. `-e LOG_LEVEL=debug -e FOO=bar`. |
| `--max-action-concurrency` | `integer range` |  | Maximum number of actions that can run concurrently within the run. If not provided, the platform default (run.max_action_concurrency setting) applies. |
| `--label` | `text` | `Sentinel.UNSET` | User-defined label to attach to the run. Format: KEY=VALUE. Can be specified multiple times, e.g. `--label team=ml --label env=prod`. |
| `--queue` | `text` |  | Queue (cluster) to send the run to. Overrides any queue set on the task. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte run hello

**`flyte run hello [OPTIONS]`**

Run a built-in first workflow -- no files needed.

The example fans a small computation out over a list of inputs with `flyte.map` and averages
the results. Its source is written to `hello.py` in a scratch directory and the
path is printed, so you can copy it into a project of your own.

```bash
flyte run hello
flyte run --local hello
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--x_list` | `json list` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` |  |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte run deployed-task

**`flyte run deployed-task [OPTIONS] COMMAND [ARGS]...`**

Run remote task from the Flyte backend

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte serve

**`flyte serve [OPTIONS] COMMAND [ARGS]...`**

Serve an app from a Python file using flyte.serve().

This command allows you to serve apps defined with `flyte.app.AppEnvironment`
in your Python files. The serve command will deploy the app to the Flyte backend
and start it, making it accessible via a URL.

If you have never served a Flyte app before, start with the built-in example. It needs no files
of your own, and prints the path to its source so you can copy it into a project:

```bash
flyte serve hello
flyte serve --local hello
```

Example usage:

```bash
flyte serve examples/apps/basic_app.py app_env
```

**Local serving:** Use the `--local` flag to serve the app on localhost without
deploying to the Flyte backend. This is useful for local development and testing:

```bash
flyte serve --local examples/apps/single_script_fastapi.py env
```

Arguments to the serve command are provided right after the `serve` command and before the file name.

To follow the logs of the served app, use the `--follow` flag. After the app is
deployed and active, its logs are streamed to the terminal. Press Ctrl+C to stop
following; the app keeps running.

```bash
flyte serve --follow examples/apps/basic_app.py app_env
```

You can provide image mappings with `--image` flag. This allows you to specify
the image URI for the app environment during CLI execution without changing
the code. Any images defined with `Image.from_ref_name("name")` will resolve to the
corresponding URIs you specify here.

```bash
flyte serve --image my_image=ghcr.io/myorg/my-image:v1.0 examples/apps/basic_app.py app_env
```

If the image name is not provided, it is regarded as a default image and will
be used when no image is specified in AppEnvironment:

```bash
flyte serve --image ghcr.io/myorg/default-image:latest examples/apps/basic_app.py app_env
```

You can specify multiple image arguments:

```bash
flyte serve --image ghcr.io/org/default:latest --image gpu=ghcr.io/org/gpu:v2.0 examples/apps/basic_app.py app_env
```

You can specify the `--config` flag to point to a specific Flyte cluster:

```bash
flyte serve --config my-config.yaml examples/apps/basic_app.py app_env
```

You can override the default configured project and domain:

```bash
flyte serve --project my-project --domain development examples/apps/basic_app.py app_env
```

Other arguments to the serve command are listed below.

Note: This pattern is primarily useful for serving apps defined in tasks.
Serving deployed apps is not currently supported through this CLI command.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when serving the app |
| `--root-dir` | `text` | `Sentinel.UNSET` | Override the root source directory, helpful when working with monorepos. |
| `--service-account` | `text` | `Sentinel.UNSET` | Kubernetes service account. If not provided, the configured default will be used |
| `--name` | `text` | `Sentinel.UNSET` | Name of the app deployment. If not provided, the app environment name will be used. |
| `--follow` `-f` | `boolean` | `False` | Wait and watch logs for the app. If not provided, the CLI will exit after successfully deploying the app with a link to the UI. |
| `--image` | `text` | `Sentinel.UNSET` | Image to be used in the serve. Format: imagename=imageuri. Can be specified multiple times. |
| `--no-sync-local-sys-paths` | `boolean` | `False` | Disable synchronization of local sys.path entries under the root directory to the remote container. |
| `--env-var` `-e` | `text` | `Sentinel.UNSET` | Environment variable to set in the app. Format: KEY=VALUE. Can be specified multiple times. Example: `--env-var` LOG_LEVEL=DEBUG `--env-var` DATABASE_URL=postgresql://... |
| `--local` | `boolean` | `False` | Serve the app locally on localhost instead of deploying to the Flyte backend. The app will be served on the port defined in the AppEnvironment. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte signal

**`flyte signal COMMAND [ARGS]...`**

Signal a paused condition action.

#### flyte signal condition

**`flyte signal condition [OPTIONS] RUN_NAME ACTION_NAME [VALUE]`**

Signal a paused condition action.

The condition's declared payload type and prompt are read from the
backend. If VALUE is omitted the condition's prompt is displayed and a
typed interactive prompt is shown to collect the payload. When VALUE is
provided it's coerced to the expected type (`true`/`false` for bool,
integer literals for int, decimal literals for float, any string for str).

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte start

**`flyte start COMMAND [ARGS]...`**

Start various Flyte services.

#### flyte start devbox

**`flyte start devbox [OPTIONS]`**

Start a local Flyte devbox cluster.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--image` | `text` |  | Docker image to use for the devbox cluster. |
| `--dev` | `boolean` | `False` | Enable dev mode inside the devbox cluster (sets FLYTE_DEV=True). |
| `--gpu` | `boolean` | `False` | Pass host GPUs into the devbox container (adds `--gpus` all to docker run). Requires an NVIDIA-enabled host. Defaults `--image` to a GPU-capable image if `--image` is not explicitly set. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

#### flyte start tui

**`flyte start tui [OPTIONS]`**

Launch the Flyte TUI. Install with `pip install flyte[tui]`.

The mode is chosen from the resolved config:

* Remote (config has an endpoint, or FLYTE_API_KEY is set): browse a remote
  Flyte v2 cluster — projects, runs, actions, logs, tasks, apps, and triggers.
  `flyte start tui --config remote.yaml`
* Local (no endpoint): explore past local runs recorded with persistence.
  `flyte start tui --config local.yaml`

Local persistence can be enabled in 2 ways:

1. In the config, to record every local run:
   `flyte create config --endpoint ... --local-persistence`
2. Via `flyte.init(local_persistence=True)`, recording `flyte.run` runs
   that are local and within the active `flyte.init`.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-c` `--config` | `file` |  | Path to the Flyte configuration file. Defaults to ~/.flyte/config.yaml. |
| `--poll-interval` | `float` | `2.0` | Seconds between run detail refreshes while browsing a remote run. Remote mode only. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte stop

**`flyte stop COMMAND [ARGS]...`**

Stop various Flyte services.

#### flyte stop devbox

**`flyte stop devbox`**

Pause the local Flyte devbox cluster without removing it.

{{< variant union >}}
{{< markdown >}}
### flyte undelete

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte undelete COMMAND [ARGS]...`**

Restore soft-deleted objects.
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte undelete cluster

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte undelete cluster NAME`**

Restore a soft-deleted cluster.

The cluster comes back with the spec, status and pool it had when it was
deleted, always in the 'drained' state — activate it to let it accept work
again; its co-named implicit queue is restored with it, also drained, and
is activated with the cluster. That holds even if the queue had been
deleted on its own earlier: undeleting the cluster is the only way to bring
it back, since `flyte undelete queue` refuses a queue whose cluster is
gone. A cluster that is still 'deleting' cannot be undeleted — its deletion
has to finish first. List the clusters eligible for this with
`flyte get cluster --deleted`.

The cluster's pool must not itself be deleted; undelete the pool first.

Examples:

```bash
$ flyte get cluster --deleted

$ flyte undelete cluster my-cluster

$ flyte update cluster my-cluster --activate
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte undelete cluster-pool

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte undelete cluster-pool NAME`**

Restore a soft-deleted cluster pool.

The pool comes back with the config it had when it was deleted. Queues and
clusters that were deleted while assigned to it stay deleted and can now be
undeleted too. List the pools eligible for this with
`flyte get cluster-pool --deleted`.

Examples:

```bash
$ flyte get cluster-pool --deleted

$ flyte undelete cluster-pool my-pool
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte undelete queue

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte undelete queue [OPTIONS] NAME`**

Restore a soft-deleted queue.

The queue comes back with the configuration it had when it was deleted,
always in the 'drained' state — activate it to let it accept work again. A
queue still 'deleting' cannot be undeleted; its deletion has to finish
first. List the queues eligible for this with `flyte get queue --deleted`.

Every cluster the queue routes to must be live and in its pool, and the pool
must be live too. A cluster's co-named queue therefore cannot be restored on
its own — `flyte undelete cluster NAME` brings it back with the cluster.

Examples:

```bash
$ flyte get queue --deleted

$ flyte undelete queue my-queue

$ flyte update queue my-queue --activate
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--project` | `text` | `` | Scope to a project |
| `--domain` | `text` | `` | Scope to a domain |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

### flyte update

**`flyte update COMMAND [ARGS]...`**

Update various flyte entities.

#### flyte update app

**`flyte update app [OPTIONS] NAME`**

Update an app by starting or stopping it.


Example usage:

```bash
flyte update app <app_name> --activate | --deactivate [--wait] [--project <project_name>] [--domain <domain_name>]
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--activate` `--deactivate` | `boolean` |  | Activate or deactivate app. |
| `--wait` | `boolean` | `False` | Wait for the app to reach the desired state. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte update cluster

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte update cluster [OPTIONS] NAME`**

Update a cluster: drain it, re-activate it, or move it to another pool.

Use --drain to begin draining: the cluster stops receiving new work while
work already on it keeps running, and its co-named implicit queue is set to
draining with it. Draining requires that no apps are assigned to the
cluster and that no other queue explicitly pins it. The drain completes
asynchronously — watch `flyte get cluster NAME` until the drain state
reaches 'drained'. To take a cluster out of service without waiting for
its work, use `flyte delete cluster` instead.

Use --activate to re-activate a draining or drained cluster. Its co-named
queue is activated with it — even when the queue had been drained on its
own. A deleting or deleted cluster cannot be drained or activated.

Use --pool to move the cluster to a different cluster pool. The target pool
must already exist, be live, and differ from the cluster's current one. The
cluster's co-named implicit queue moves along with it, so that queue must be
drained first. Any other live queue pinning this cluster blocks the move and
has to be unpinned; already-deleted ones don't block it.

Examples:

```bash
$ flyte update cluster my-cluster --drain

$ flyte update cluster my-cluster --activate
```
Moving a cluster to another pool:

```bash
$ flyte update queue my-cluster --drain    # wait for status 'drained'

$ flyte update cluster my-cluster --pool my-pool

$ flyte update queue my-cluster --activate
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--pool` | `text` | `` | Cluster pool to move the cluster to. |
| `--drain` | `boolean` | `Sentinel.UNSET` | Begin draining the cluster (it stops receiving new work) |
| `--activate` | `boolean` | `Sentinel.UNSET` | Re-activate a draining or drained cluster |
| `--yes` | `boolean` | `Sentinel.UNSET` | Skip confirmation prompt |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte update cluster-pool

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte update cluster-pool NAME`**

Update a cluster pool interactively.

Opens the pool in your $EDITOR as YAML. Save and close to apply changes.

Examples:

```bash
$ flyte update cluster-pool my-pool
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte update policy

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte update policy NAME`**

Update a policy interactively.

Opens the policy in your $EDITOR as YAML. Save and close to apply changes.
Bindings that are added or removed will be applied to the policy.

Examples:

```bash
$ flyte --org my-org update policy my-policy
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte update project

**`flyte update project [OPTIONS] ID`**

Update a project's name, description, labels, or archive state.


Example usage:

```bash
flyte update project my_project --archive
flyte update project my_project --unarchive
flyte update project my_project --description "New description"
flyte update project my_project --name "New Display Name"
flyte update project my_project --label team=ml --label env=prod
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--name` | `text` |  | Update the project display name. |
| `--description` | `text` |  | Update the project description. |
| `--label` `-l` | `text` | `Sentinel.UNSET` | Set labels as key=value pairs. Can be specified multiple times. Replaces all existing labels. |
| `--archive` `--unarchive` | `boolean` |  | Archive or unarchive the project. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

{{< variant union >}}
{{< markdown >}}
#### flyte update queue

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte update queue [OPTIONS] NAME`**

Update a queue.

Use --drain to begin draining (stops new submissions). Any queue can be
drained, including one referenced as run.default_queue in settings —
runs that resolve to a queue that is not accepting work are rejected at
creation with an actionable error. Only deleting such a queue is refused
(see `flyte delete queue`).
Use --activate to re-activate a draining or drained queue.
Use --edit to interactively modify queue configuration, including moving
the queue to a different cluster pool. A pool move is only accepted once the
queue is fully drained, so --drain it first and wait for its status to reach
'drained'; --activate it again after the move.

Examples:

```bash
$ flyte update queue my-queue --drain

$ flyte update queue my-queue --activate

$ flyte update queue my-queue --edit
```
Moving a queue to another cluster pool:

```bash
$ flyte update queue my-queue --drain     # wait for status 'drained'

$ flyte update queue my-queue --edit      # set cluster_pool: other-pool

$ flyte update queue my-queue --activate
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--project` | `text` | `` | Scope to a project |
| `--domain` | `text` | `` | Scope to a domain |
| `--drain` | `boolean` | `Sentinel.UNSET` | Begin draining the queue |
| `--activate` | `boolean` | `Sentinel.UNSET` | Re-activate a draining or drained queue |
| `--edit` | `boolean` | `Sentinel.UNSET` | Open an editor to modify queue settings |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}
#### flyte update role

> **Note:** This command is provided by the [`flyteplugins-union`](#plugin-commands) plugin.

**`flyte update role NAME`**

Update a role's actions interactively.

Opens the role in your $EDITOR as YAML. Save and close to apply changes.
Only actions can be edited; the role name and description cannot be changed.

Examples:

```bash
$ flyte --org my-org update role my-role
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |
{{< /markdown >}}
{{< /variant >}}

#### flyte update trigger

**`flyte update trigger [OPTIONS] NAME TASK_NAME`**

Update a trigger.


Example usage:

```bash
flyte update trigger <trigger_name> <task_name> --activate | --deactivate
[--project <project_name> --domain <domain_name>]
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--activate` `--deactivate` | `boolean` | `Sentinel.UNSET` | Activate or deactivate the trigger. |
| `-p` `--project` | `text` |  | Project to which this command applies. |
| `-d` `--domain` | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `Sentinel.UNSET` | Show this message and exit. |

### flyte whoami

**`flyte whoami`**

Display the current user information.
