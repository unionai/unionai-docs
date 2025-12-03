---
title: "Flyte CLI"
variants: +flyte +byoc +selfmanaged +serverless
weight: 1
---

# Flyte CLI

This is the command line interface for Flyte.

{{< grid >}}
{{< markdown >}}
| Object | Action |
| ------ | -- |
| `run` | [`abort`](#flyte-abort-run), [`get`](#flyte-get-run)  |
| `config` | [`create`](#flyte-create-config), [`get`](#flyte-get-config)  |
| `secret` | [`create`](#flyte-create-secret), [`delete`](#flyte-delete-secret), [`get`](#flyte-get-secret)  |
| `trigger` | [`create`](#flyte-create-trigger), [`delete`](#flyte-delete-trigger), [`get`](#flyte-get-trigger), [`update`](#flyte-update-trigger)  |
| `docs` | [`gen`](#flyte-gen-docs)  |
| `action` | [`get`](#flyte-get-action)  |
| `app` | [`get`](#flyte-get-app), [`update`](#flyte-update-app)  |
| `io` | [`get`](#flyte-get-io)  |
| `logs` | [`get`](#flyte-get-logs)  |
| `project` | [`get`](#flyte-get-project)  |
| `task` | [`get`](#flyte-get-task)  |
| `deployed-task` | [`run`](#flyte-run-deployed-task)  |
{{< /markdown >}}
{{< markdown >}}
| Action | On |
| ------ | -- |
| `abort` | [`run`](#flyte-abort-run)  |
| [`build`](#flyte-build) | - |
| `create` | [`config`](#flyte-create-config), [`secret`](#flyte-create-secret), [`trigger`](#flyte-create-trigger)  |
| `delete` | [`secret`](#flyte-delete-secret), [`trigger`](#flyte-delete-trigger)  |
| [`deploy`](#flyte-deploy) | - |
| `gen` | [`docs`](#flyte-gen-docs)  |
| `get` | [`action`](#flyte-get-action), [`app`](#flyte-get-app), [`config`](#flyte-get-config), [`io`](#flyte-get-io), [`logs`](#flyte-get-logs), [`project`](#flyte-get-project), [`run`](#flyte-get-run), [`secret`](#flyte-get-secret), [`task`](#flyte-get-task), [`trigger`](#flyte-get-trigger)  |
| `run` | [`deployed-task`](#flyte-run-deployed-task)  |
| [`serve`](#flyte-serve) | - |
| `update` | [`app`](#flyte-update-app), [`trigger`](#flyte-update-trigger)  |
| [`whoami`](#flyte-whoami) | - |
{{< /markdown >}}
{{< /grid >}}


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
| `--version` | `boolean` | `False` | Show the version and exit. |
| `--endpoint` | `text` | `Sentinel.UNSET` | The endpoint to connect to. This will override any configuration file and simply use `pkce` to connect. |
| `--insecure` | `boolean` |  | Use an insecure connection to the endpoint. If not specified, the CLI will use TLS. |
| `--auth-type` | `choice` |  | Authentication type to use for the Flyte backend. Defaults to 'pkce'. |
| {{< multiline >}}`-v`
`--verbose`{{< /multiline >}} | `integer` | `0` | Show verbose messages and exception traces. Repeating multiple times increases the verbosity (e.g., -vvv). |
| `--org` | `text` | `Sentinel.UNSET` | The organization to which the command applies. |
| {{< multiline >}}`-c`
`--config`{{< /multiline >}} | `path` | `Sentinel.UNSET` | Path to the configuration file to use. If not specified, the default configuration file is used. |
| {{< multiline >}}`--output-format`
`-of`{{< /multiline >}} | `choice` | `table` | Output format for commands that support it. Defaults to 'table'. |
| `--log-format` | `choice` | `console` | Formatting for logs, defaults to 'console' which is meant to be human readable. 'json' is meant for machine parsing. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte abort

**`flyte abort COMMAND [ARGS]...`**

Abort an ongoing process.

#### flyte abort run

**`flyte abort run [OPTIONS] RUN_NAME`**

Abort a run.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte build

**`flyte build [OPTIONS] COMMAND [ARGS]...`**

Build the environments defined in a python file or directory. This will build the images associated with the
environments.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--noop` | `boolean` | `Sentinel.UNSET` | Dummy parameter, placeholder for future use. Does not affect the build process. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte create

**`flyte create COMMAND [ARGS]...`**

Create resources in a Flyte deployment.

#### flyte create config

**`flyte create config [OPTIONS]`**

Creates a configuration file for Flyte CLI.
If the `--output` option is not specified, it will create a file named `config.yaml` in the current directory.
If the file already exists, it will raise an error unless the `--force` option is used.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--endpoint` | `text` | `Sentinel.UNSET` | Endpoint of the Flyte backend. |
| `--insecure` | `boolean` | `False` | Use an insecure connection to the Flyte backend. |
| `--org` | `text` | `Sentinel.UNSET` | Organization to use. This will override the organization in the configuration file. |
| {{< multiline >}}`-o`
`--output`{{< /multiline >}} | `path` | `.flyte/config.yaml` | Path to the output directory where the configuration will be saved. Defaults to current directory. |
| `--force` | `boolean` | `False` | Force overwrite of the configuration file if it already exists. |
| {{< multiline >}}`--image-builder`
`--builder`{{< /multiline >}} | `choice` | `local` | Image builder to use for building images. Defaults to 'local'. |
| `--auth-type` | `choice` |  | Authentication type to use for the Flyte backend. Defaults to 'pkce'. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

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
| `--from-docker-config` | `boolean` | `False` | Create image pull secret from Docker config file (only for --type image_pull). Mutually exclusive with value, from_file, registry, username, password. |
| `--docker-config-path` | `path` | `Sentinel.UNSET` | Path to Docker config file (defaults to ~/.docker/config.json or $DOCKER_CONFIG). |
| `--registries` | `text` | `Sentinel.UNSET` | Comma-separated list of registries to include (only with --from-docker-config). |
| `--registry` | `text` | `Sentinel.UNSET` | Registry hostname (e.g., ghcr.io, docker.io) for explicit credentials (only for --type image_pull). Mutually exclusive with value, from_file, from_docker_config. |
| `--username` | `text` | `Sentinel.UNSET` | Username for the registry (only with --registry). |
| `--password` | `text` | `Sentinel.UNSET` | Password for the registry (only with --registry). If not provided, will prompt. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

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
| `--trigger-time-var` | `text` | `trigger_time` | Variable name for the trigger time in the task inputs. Defaults to 'trigger_time'. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte delete

**`flyte delete COMMAND [ARGS]...`**

Remove resources from a Flyte deployment.

#### flyte delete secret

**`flyte delete secret [OPTIONS] NAME`**

Delete a secret. The name of the secret is required.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte delete trigger

**`flyte delete trigger [OPTIONS] NAME TASK_NAME`**

Delete a trigger. The name of the trigger is required.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

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
flyte deploy --config my-config.yaml hello.py my_env
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
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--version` | `text` | `Sentinel.UNSET` | Version of the environment to deploy |
| {{< multiline >}}`--dry-run`
`--dryrun`{{< /multiline >}} | `boolean` | `False` | Dry run. Do not actually call the backend service. |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when running the task |
| `--root-dir` | `text` | `Sentinel.UNSET` | Override the root source directory, helpful when working with monorepos. |
| {{< multiline >}}`--recursive`
`-r`{{< /multiline >}} | `boolean` | `False` | Recursively deploy all environments in the current directory |
| `--all` | `boolean` | `False` | Deploy all environments in the current directory, ignoring the file name |
| {{< multiline >}}`--ignore-load-errors`
`-i`{{< /multiline >}} | `boolean` | `False` | Ignore errors when loading environments especially when using --recursive or --all. |
| `--no-sync-local-sys-paths` | `boolean` | `False` | Disable synchronization of local sys.path entries under the root directory to the remote container. |
| `--image` | `text` | `Sentinel.UNSET` | Image to be used in the run. Format: imagename=imageuri. Can be specified multiple times. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte gen

**`flyte gen COMMAND [ARGS]...`**

Generate documentation.

#### flyte gen docs

**`flyte gen docs [OPTIONS]`**

Generate documentation.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--type` | `text` | `Sentinel.UNSET` | Type of documentation (valid: markdown) |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte get

**`flyte get COMMAND [ARGS]...`**

Retrieve resources from a Flyte deployment.

You can get information about projects, runs, tasks, actions, secrets, logs and input/output values.

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
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get app

**`flyte get app [OPTIONS] [NAME]`**

Get a list of all apps, or details of a specific app by name.

Apps are long-running services deployed on the Flyte platform.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of apps to fetch when listing. |
| `--only-mine` | `boolean` | `False` | Show only apps created by the current user (you). |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get config

**`flyte get config`**

Shows the automatically detected configuration to connect with the remote backend.

The configuration will include the endpoint, organization, and other settings that are used by the CLI.

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
| {{< multiline >}}`--inputs-only`
`-i`{{< /multiline >}} | `boolean` | `False` | Show only inputs |
| {{< multiline >}}`--outputs-only`
`-o`{{< /multiline >}} | `boolean` | `False` | Show only outputs |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

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
| {{< multiline >}}`--lines`
`-l`{{< /multiline >}} | `integer` | `30` | Number of lines to show, only useful for --pretty |
| `--show-ts` | `boolean` | `False` | Show timestamps |
| `--pretty` | `boolean` | `False` | Show logs in an auto-scrolling box, where number of lines is limited to `--lines` |
| {{< multiline >}}`--attempt`
`-a`{{< /multiline >}} | `integer` |  | Attempt number to show logs for, defaults to the latest attempt. |
| `--filter-system` | `boolean` | `False` | Filter all system logs from the output. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get project

**`flyte get project [NAME]`**

Get a list of all projects, or details of a specific project by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get run

**`flyte get run [OPTIONS] [NAME]`**

Get a list of all runs, or details of a specific run by name.

The run details will include information about the run, its status, but only the root action will be shown.

If you want to see the actions for a run, use `get action <run_name>`.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of runs to fetch when listing. |
| `--in-phase` | `choice` | `Sentinel.UNSET` | Filter runs by their status. |
| `--only-mine` | `boolean` | `False` | Show only runs created by the current user (you). |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get secret

**`flyte get secret [OPTIONS] [NAME]`**

Get a list of all secrets, or details of a specific secret by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get task

**`flyte get task [OPTIONS] [NAME] [VERSION]`**

Retrieve a list of all tasks, or details of a specific task by name and version.

Currently, both `name` and `version` are required to get a specific task.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of tasks to fetch. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get trigger

**`flyte get trigger [OPTIONS] [TASK_NAME] [NAME]`**

Get a list of all triggers, or details of a specific trigger by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of triggers to fetch. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte run

**`flyte run [OPTIONS] COMMAND [ARGS]...`**

Run a task from a python file or deployed task.

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

Other arguments to the run command are listed below.

Arguments for the task itself are provided after the task name and can be retrieved using `--help`. For example:

```bash
flyte run hello.py my_task --help
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--local` | `boolean` | `False` | Run the task locally |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when running the task |
| `--root-dir` | `text` | `Sentinel.UNSET` | Override the root source directory, helpful when working with monorepos. |
| `--raw-data-path` | `text` | `Sentinel.UNSET` | Override the output prefix used to store offloaded data types. e.g. s3://bucket/ |
| `--service-account` | `text` | `Sentinel.UNSET` | Kubernetes service account. If not provided, the configured default will be used |
| `--name` | `text` | `Sentinel.UNSET` | Name of the run. If not provided, a random name will be generated. |
| {{< multiline >}}`--follow`
`-f`{{< /multiline >}} | `boolean` | `False` | Wait and watch logs for the parent action. If not provided, the CLI will exit after successfully launching a remote execution with a link to the UI. |
| `--image` | `text` | `Sentinel.UNSET` | Image to be used in the run. Format: imagename=imageuri. Can be specified multiple times. |
| `--no-sync-local-sys-paths` | `boolean` | `False` | Disable synchronization of local sys.path entries under the root directory to the remote container. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte run deployed-task

**`flyte run deployed-task [OPTIONS] COMMAND [ARGS]...`**

Run reference task from the Flyte backend

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte serve

**`flyte serve [OPTIONS] COMMAND [ARGS]...`**

Serve an app from a Python file using flyte.serve().

This command allows you to serve apps defined with `flyte.app.AppEnvironment`
in your Python files. The serve command will deploy the app to the Flyte backend
and start it, making it accessible via a URL.

Example usage:

```bash
flyte serve examples/apps/basic_app.py app_env
```

Arguments to the serve command are provided right after the `serve` command and before the file name.

To follow the logs of the served app, use the `--follow` flag:

```bash
flyte serve --follow examples/apps/basic_app.py app_env
```

Note: Log streaming is not yet fully implemented and will be added in a future release.

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
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when serving the app |
| `--root-dir` | `text` | `Sentinel.UNSET` | Override the root source directory, helpful when working with monorepos. |
| `--service-account` | `text` | `Sentinel.UNSET` | Kubernetes service account. If not provided, the configured default will be used |
| `--name` | `text` | `Sentinel.UNSET` | Name of the app deployment. If not provided, the app environment name will be used. |
| {{< multiline >}}`--follow`
`-f`{{< /multiline >}} | `boolean` | `False` | Wait and watch logs for the app. If not provided, the CLI will exit after successfully deploying the app with a link to the UI. |
| `--image` | `text` | `Sentinel.UNSET` | Image to be used in the serve. Format: imagename=imageuri. Can be specified multiple times. |
| `--no-sync-local-sys-paths` | `boolean` | `False` | Disable synchronization of local sys.path entries under the root directory to the remote container. |
| {{< multiline >}}`--env-var`
`-e`{{< /multiline >}} | `text` | `Sentinel.UNSET` | Environment variable to set in the app. Format: KEY=VALUE. Can be specified multiple times. Example: --env-var LOG_LEVEL=DEBUG --env-var DATABASE_URL=postgresql://... |
| `--help` | `boolean` | `False` | Show this message and exit. |

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
| {{< multiline >}}`--activate`
`--deactivate`{{< /multiline >}} | `boolean` |  | Activate or deactivate app. |
| `--wait` | `boolean` | `False` | Wait for the app to reach the desired state. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

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
| {{< multiline >}}`--activate`
`--deactivate`{{< /multiline >}} | `boolean` | `Sentinel.UNSET` | Activate or deactivate the trigger. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte whoami

**`flyte whoami`**

Display the current user information.
