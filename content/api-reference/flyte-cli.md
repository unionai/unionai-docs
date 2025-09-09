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
| `docs` | [`gen`](#flyte-gen-docs)  |
| `action` | [`get`](#flyte-get-action)  |
| `io` | [`get`](#flyte-get-io)  |
| `logs` | [`get`](#flyte-get-logs)  |
| `project` | [`get`](#flyte-get-project)  |
| `task` | [`get`](#flyte-get-task)  |
{{< /markdown >}}
{{< markdown >}}
| Action | On |
| ------ | -- |
| `abort` | [`run`](#flyte-abort-run)  |
| [`build`](#flyte-build) | - |
| `create` | [`config`](#flyte-create-config), [`secret`](#flyte-create-secret)  |
| `delete` | [`secret`](#flyte-delete-secret)  |
| [`deploy`](#flyte-deploy) | - |
| `gen` | [`docs`](#flyte-gen-docs)  |
| `get` | [`action`](#flyte-get-action), [`config`](#flyte-get-config), [`io`](#flyte-get-io), [`logs`](#flyte-get-logs), [`project`](#flyte-get-project), [`run`](#flyte-get-run), [`secret`](#flyte-get-secret), [`task`](#flyte-get-task)  |
| [`run`](#flyte-run) | - |
{{< /markdown >}}
{{< /grid >}}


## flyte

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
| `--endpoint` | `text` |  | The endpoint to connect to. This will override any configuration file and simply use `pkce` to connect. |
| `--insecure` | `boolean` |  | Use an insecure connection to the endpoint. If not specified, the CLI will use TLS. |
| `--auth-type` | `choice` |  | Authentication type to use for the Flyte backend. Defaults to 'pkce'. |
| {{< multiline >}}`-v`
`--verbose`{{< /multiline >}} | `integer` | `0` | Show verbose messages and exception traces. Repeating multiple times increases the verbosity (e.g., -vvv). |
| `--org` | `text` |  | The organization to which the command applies. |
| {{< multiline >}}`-c`
`--config`{{< /multiline >}} | `path` |  | Path to the configuration file to use. If not specified, the default configuration file is used. |
| {{< multiline >}}`--output-format`
`-of`{{< /multiline >}} | `choice` | `table` | Output format for commands that support it. Defaults to 'table'. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte abort

Abort an ongoing process.

#### flyte abort run

Abort a run.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte build

Build the environments defined in a python file or directory. This will build the images associated with the
environments.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--noop` | `boolean` |  | Dummy parameter, placeholder for future use. Does not affect the build process. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte create

Create resources in a Flyte deployment.

#### flyte create config

Creates a configuration file for Flyte CLI.
If the `--output` option is not specified, it will create a file named `config.yaml` in the current directory.
If the file already exists, it will raise an error unless the `--force` option is used.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--endpoint` | `text` |  | Endpoint of the Flyte backend. |
| `--insecure` | `boolean` | `False` | Use an insecure connection to the Flyte backend. |
| `--org` | `text` |  | Organization to use. This will override the organization in the configuration file. |
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

```bash
$ flyte create secret my_secret --type image_pull
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--value` | `text` |  | Secret value Mutually exclusive with from_file. |
| `--from-file` | `path` |  | Path to the file with the binary secret. Mutually exclusive with value. |
| `--type` | `choice` | `regular` | Type of the secret. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte delete

Remove resources from a Flyte deployment.

#### flyte delete secret

Delete a secret. The name of the secret is required.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte deploy

Deploy one or more environments from a python file.
This command will create or update environments in the Flyte system.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--version` | `text` |  | Version of the environment to deploy |
| {{< multiline >}}`--dry-run`
`--dryrun`{{< /multiline >}} | `boolean` | `False` | Dry run. Do not actually call the backend service. |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when running the task |
| {{< multiline >}}`--recursive`
`-r`{{< /multiline >}} | `boolean` | `False` | Recursively deploy all environments in the current directory |
| `--all` | `boolean` | `False` | Deploy all environments in the current directory, ignoring the file name |
| {{< multiline >}}`--ignore-load-errors`
`-i`{{< /multiline >}} | `boolean` | `False` | Ignore errors when loading environments especially when using --recursive or --all. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte gen

Generate documentation.

#### flyte gen docs

Generate documentation.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--type` | `text` |  | Type of documentation (valid: markdown) |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte get

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

Get all actions for a run or details for a specific action.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get config

Shows the automatically detected configuration to connect with the remote backend.

The configuration will include the endpoint, organization, and other settings that are used by the CLI.

#### flyte get io

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

Get a list of all projects, or details of a specific project by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get run

Get a list of all runs, or details of a specific run by name.

The run details will include information about the run, its status, but only the root action will be shown.

If you want to see the actions for a run, use `get action <run_name>`.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--limit` | `integer` | `100` | Limit the number of runs to fetch when listing. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get secret

Get a list of all secrets, or details of a specific secret by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to which this command applies. |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to which this command applies. |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get task

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

### flyte run

Run a task from a python file or deployed task.

To run a remote task that already exists in Flyte, use the deployed-task command:

Example usage:

```bash
flyte run --project my-project --domain development hello.py my_task --arg1 value1 --arg2 value2
```

Arguments to the run command are provided right after the `run` command and before the file name.
For example, the command above specifies the project and domain.

To run a task locally, use the `--local` flag. This will run the task in the local environment instead of the remote
Flyte environment:

```bash
flyte run --local hello.py my_task --arg1 value1 --arg2 value2
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
| `--name` | `text` |  | Name of the run. If not provided, a random name will be generated. |
| {{< multiline >}}`--follow`
`-f`{{< /multiline >}} | `boolean` | `False` | Wait and watch logs for the parent action. If not provided, the CLI will exit after successfully launching a remote execution with a link to the UI. |
| `--help` | `boolean` | `False` | Show this message and exit. |
