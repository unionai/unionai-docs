---
title: "Flyte CLI"
weight: 2
variants: +flyte +byoc +selfmanaged +serverless
---

# Flyte CLI

This is the command line interface for Flyte.

The Flyte CLI is a command line interface for interacting with Flyte.

It follows a simple verb based structure, where the top-level commands are verbs that describe the action to be taken,
and the sub-commands are nouns that describe the object of the action.

Here is a tree of all the commands:

{{< grid >}}
{{< markdown >}}
| Object | Action |
| ------ | -- |
| `run` | [`abort`](#flyte-abort-run), [`get`](#flyte-get-run)  |
| `config` | [`create`](#flyte-create-config), [`get`](#flyte-get-config)  |
| `secret` | [`create`](#flyte-create-secret), [`get`](#flyte-get-secret)  |
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
| `create` | [`config`](#flyte-create-config), [`secret`](#flyte-create-secret)  |
| `deploy` |   |
| `gen` | [`docs`](#flyte-gen-docs)  |
| `get` | [`action`](#flyte-get-action), [`config`](#flyte-get-config), [`io`](#flyte-get-io), [`logs`](#flyte-get-logs), [`project`](#flyte-get-project), [`run`](#flyte-get-run), [`secret`](#flyte-get-secret), [`task`](#flyte-get-task)  |
| `run` |   |
{{< /markdown >}}
{{< /grid >}}

## flyte

The root command (`flyte`) can be used to setting persistent context for the CLI ,such as the endpoint, organization, and verbosity level.

Set endpoint and organization:

```bash
flyte --endpoint <endpoint> --org <org> get project <project_name>
```

Increase the verbosity level (This is useful for debugging, this will show more logs and exception traces):

```bash
flyte -vvv get logs <run-name>
```

Override the default config file:

```bash
flyte --config /path/to/config.yaml run ...
```

* [Documentation](https://www.union.ai/docs/flyte/user-guide/)
* [GitHub](https://github.com/flyteorg/flyte) - Please leave a ⭐.
* [Slack](https://slack.flyte.org) - Join the community and ask questions.
* [Issues](https://github.com/flyteorg/flyte/issues)

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--endpoint` | `text` |  | The endpoint to connect to, this will override any config and simply used pkce to connect. |
| {{< multiline >}}`--insecure`
`--secure`{{< /multiline >}} | `boolean` |  | Use insecure connection to the endpoint. If secure is specified, the CLI will use TLS. |
| {{< multiline >}}`-v`
`--verbose`{{< /multiline >}} | `integer` | `0` | Show verbose messages and exception traces, multiple times increases verbosity (e.g., -vvv). |
| `--org` | `text` |  | Organization to use |
| {{< multiline >}}`-c`
`--config`{{< /multiline >}} | `path` |  | Path to config file (YAML format) to use for the CLI. If not specified, the default config file will be used. |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte abort

Abort an ongoing process. Currently, only relevant for runs.

#### flyte abort run

Abort a run.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte create

The create subcommand allows you to create resources in a Flyte deployment.

#### flyte create config

This command creates a configuration file for Flyte CLI.

* If the `--output` option is not specified, it will create a file named `config.yaml` in the current directory.
* If the file already exists, it will raise an error unless the `--force` option is used.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--endpoint` | `text` |  | Endpoint of the Flyte backend. |
| `--insecure` | `boolean` | `False` | Use insecure connection to the Flyte backend. |
| `--org` | `text` |  | Organization to use, this will override the organization in the config file. |
| {{< multiline >}}`-o`
`--output`{{< /multiline >}} | `path` | `config.yaml` | Path to the output dir where the config will be saved, defaults to current directory. |
| `--force` | `boolean` | `False` | Force overwrite the config file if it already exists. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte create secret

Create a new secret, the name of the secret is required:

```bash
flyte create secret my_secret --value my_value
```

If `--from-file` is specified, the value will be read from the file instead of being provided directly:

```bash
flyte create secret my_secret --from-file /path/to/secret_file
```

Secret types can be used to create specific types of secrets. Some secrets are useful for image pull, while some
are `regular` / general purpose secrets:

```bash
flyte create secret my_secret --type image_pull
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--from-file` | `path` |  | Path to the file with the binary secret. |
| `--type` | `choice` | `regular` | Type of the secret. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte deploy

Deploy one or more environments from a python file.
The deploy command will create or update environments in the Flyte system.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--version` | `text` |  | Version of the environment to deploy |
| {{< multiline >}}`--dry-run`
`--dryrun`{{< /multiline >}} | `boolean` | `False` | Dry run, do not actually call the backend service. |
| `--local` | `boolean` | `False` | Run the task locally |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when running the task |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte gen

Generate documentation

#### flyte gen docs

Generate documentation

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--type` | `text` |  | Type of documentation (valid: markdown) |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte get

The `get` subcommand allows you to retrieve various resources from a Flyte deployment.

You can get information about projects, runs, tasks, actions, secrets, and more.
Each command supports optional parameters to filter or specify the resource you want to retrieve.
Every `get` subcommand for example ``get project` without any arguments will list all projects.
`get project my_project` will return the details of the project named `my_project`.
In some cases `get action my_run` will return all actions for the run named `my_run` and
`get action my_run my_action` will return the details of the action named `my_action` for the run `my_run`.

#### flyte get action

Get all actions for a run or details for a specific action.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get config

Shows the automatically detected configuration to connect with remote Flyte services.

The configuration will include the endpoint, organization, and other settings that are used by the CLI.

#### flyte get io

Get the inputs and outputs of a run or action.

* If only the run name is provided, it will show the inputs and outputs of the root action of that run.
* If an action name is provided, it will show the inputs and outputs for that action.
* If `--inputs-only` or `--outputs-only` is specified, it will only show the inputs or outputs respectively.

Example:

```bash
flyte get io my_run
```

or

```bash
flyte get io my_run my_action
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`--inputs-only`
`-i`{{< /multiline >}} | `boolean` | `False` | Show only inputs |
| {{< multiline >}}`--outputs-only`
`-o`{{< /multiline >}} | `boolean` | `False` | Show only outputs |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get logs

Stream logs for the provided run or action.

If only the run is provided, only the logs for the parent action will be streamed:

```bash
flyte get logs my_run
```

But, if you want to see the logs for a specific action, you can provide the action name as well:

```bash
flyte get logs my_run my_action
```

By default, logs will be shown in the raw format, will scroll on the terminal.
If automatic scrolling and only tailing `--lines` number of lines is desired, use the `--pretty` flag:

```bash
flyte get logs my_run my_action --pretty --lines 50
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`--lines`
`-l`{{< /multiline >}} | `integer` | `30` | Number of lines to show, only useful for --pretty |
| `--show-ts` | `boolean` | `False` | Show timestamps |
| `--pretty` | `boolean` | `False` | Show logs in a auto scrolling box, where number of lines is limited to `--lines` |
| {{< multiline >}}`--attempt`
`-a`{{< /multiline >}} | `integer` |  | Attempt number to show logs for, defaults to the latest attempt. |
| `--filter-system` | `boolean` | `False` | Filter all system logs from the output. |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get project

Retrieve a list of all projects or details of a specific project by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get run

Get list of all runs or details of a specific run by name.

The run details will include information about the run, its status, but only the root action will be shown.

If you want to see the actions for a run, use `get action <run_name>`.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get secret

Retrieve a list of all secrets or details of a specific secret by name.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get task

Retrieve a list of all tasks or details of a specific task by name and version.

Currently name+version are required to get a specific task.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--help` | `boolean` | `False` | Show this message and exit. |

### flyte run

Run a task from a python file.

Example usage:

```bash
flyte run --name examples/basics/hello.py my_task --arg1 value1 --arg2 value2
```

Note: all arguments for the run command are provided right after the `run` command and before the file name.

You can also specify the project and domain using the `--project` and `--domain` options, respectively. These
options can be set in the config file or passed as command line arguments.

Note: The arguments for the task are provided after the task name and can be retrieved using `--help`

Example:

```bash
flyte run --name examples/basics/hello.py my_task --help
```

To run a task locally, use the `--local` flag.
This will run the task in the local environment instead of the remote Flyte environment.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text` |  | Project to operate on |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}} | `text` |  | Domain to operate on |
| `--local` | `boolean` | `False` | Run the task locally |
| `--copy-style` | `choice` | `loaded_modules` | Copy style to use when running the task |
| `--name` | `text` |  | Name of the run. If not provided, a random name will be generated. |
| {{< multiline >}}`--follow`
`-f`{{< /multiline >}} | `boolean` | `False` | Wait and watch logs for the parent action. If not provided, the cli will exit after successfully launching a remote execution with a link to the UI. |
| `--help` | `boolean` | `False` | Show this message and exit. |
