---
title: "Flyte CLI"
variants: +flyte +byoc +selfmanaged +serverless
weight: 2
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
| `io` | [`get`](#flyte-get-io)  |
| `logs` | [`get`](#flyte-get-logs)  |
| `project` | [`get`](#flyte-get-project)  |
| `task` | [`get`](#flyte-get-task)  |
| `deployed-task` | [`run`](#flyte-run-deployed-task)  |
| `connector` | [`serve`](#flyte-serve-connector)  |
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
| `get` | [`action`](#flyte-get-action), [`config`](#flyte-get-config), [`io`](#flyte-get-io), [`logs`](#flyte-get-logs), [`project`](#flyte-get-project), [`run`](#flyte-get-run), [`secret`](#flyte-get-secret), [`task`](#flyte-get-task), [`trigger`](#flyte-get-trigger)  |
| `run` | [`deployed-task`](#flyte-run-deployed-task)  |
| `serve` | [`connector`](#flyte-serve-connector)  |
| `update` | [`trigger`](#flyte-update-trigger)  |
| [`whoami`](#flyte-whoami) | - |
{{< /markdown >}}
{{< /grid >}}


## flyte

```
Usage: flyte [OPTIONS] COMMAND [ARGS]...
```

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

```
Usage: flyte abort COMMAND [ARGS]...
```

Abort an ongoing process.

#### flyte abort run

```
Usage: flyte abort run [OPTIONS] RUN_NAME
```

Abort a run.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte build

```
Usage: flyte build [OPTIONS] COMMAND [ARGS]...
```

Build the environments defined in a python file or directory. This will build the images associated with the
environments.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--noop` | `boolean` | `Sentinel.UNSET` | Dummy parameter, placeholder for future use. Does not affect the build process. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte create

```
Usage: flyte create COMMAND [ARGS]...
```

Create resources in a Flyte deployment.

#### flyte create config

```
Usage: flyte create config [OPTIONS]
```

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

```
Usage: flyte create secret [OPTIONS] NAME
```

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

```
Usage: flyte create trigger [OPTIONS] TASK_NAME NAME
```

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

```
Usage: flyte delete COMMAND [ARGS]...
```

Remove resources from a Flyte deployment.

#### flyte delete secret

```
Usage: flyte delete secret [OPTIONS] NAME
```

Delete a secret. The name of the secret is required.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte delete trigger

```
Usage: flyte delete trigger [OPTIONS] NAME TASK_NAME
```

Delete a trigger. The name of the trigger is required.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte deploy

```
Usage: flyte deploy [OPTIONS] COMMAND [ARGS]...
```

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

```
Usage: flyte gen COMMAND [ARGS]...
```

Generate documentation.

#### flyte gen docs

```
Usage: flyte gen docs [OPTIONS]
```

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

```
Usage: flyte get COMMAND [ARGS]...
```

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

```
Usage: flyte get action [OPTIONS] RUN_NAME [ACTION_NAME]
```

Get all actions for a run or details for a specific action.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get config

```
Usage: flyte get config
```

Shows the automatically detected configuration to connect with the remote backend.

The configuration will include the endpoint, organization, and other settings that are used by the CLI.

#### flyte get io

```
Usage: flyte get io [OPTIONS] RUN_NAME [ACTION_NAME]
```

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

```
Usage: flyte get logs [OPTIONS] RUN_NAME [ACTION_NAME]
```

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

```
Usage: flyte get project [NAME]
```

Get a list of all projects, or details of a specific project by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get run

```
Usage: flyte get run [OPTIONS] [NAME]
```

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

```
Usage: flyte get secret [OPTIONS] [NAME]
```

Get a list of all secrets, or details of a specific secret by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get task

```
Usage: flyte get task [OPTIONS] [NAME] [VERSION]
```

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

```
Usage: flyte get trigger [OPTIONS] [TASK_NAME] [NAME]
```

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

```
Usage: flyte run [OPTIONS] COMMAND [ARGS]...
```

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

```
Usage: flyte run deployed-task [OPTIONS] COMMAND [ARGS]...
```

Run reference task from the Flyte backend

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte serve

```
Usage: flyte serve COMMAND [ARGS]...
```

Start the specific service. For example:

```bash
flyte serve connector
```

#### flyte serve connector

```
Usage: flyte serve connector [OPTIONS]
```

Start a grpc server for the connector service.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--port` | `integer` | `8000` | Grpc port for the connector service |
| `--prometheus_port` | `integer` | `9090` | Prometheus port for the connector service |
| `--worker` | `integer` | `10` | Number of workers for the grpc server |
| `--timeout` | `integer` |  | It will wait for the specified number of seconds before shutting down grpc server. It should only be used for testing. |
| `--modules` | `text` | `Sentinel.UNSET` | List of additional files or module that defines the connector |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte update

```
Usage: flyte update COMMAND [ARGS]...
```

Update various flyte entities.

#### flyte update trigger

```
Usage: flyte update trigger [OPTIONS] NAME TASK_NAME
```

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

```
Usage: flyte whoami
```

Display the current user information.
