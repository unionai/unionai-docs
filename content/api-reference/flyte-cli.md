---
title: Flyte CLI reference
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Flyte CLI reference

`flyte [OPTIONS] COMMAND [ARGS]`

## Commands

The Flyte CLI follows a simple verb/noun based structure, where the top-level commands are verbs that describe the action to be taken, and the sub-commands are nouns that describe the object of the action.

Here is the full tree of commands:

* `flyte`
  * [`abort run`]()
  * `create`
    * [`config`]()
    * [`secret`]()
  * [`deploy`]()
  * `get`
    * [`action`]()
    * [`config`]()
    * [`io`]()
    * [`logs`]()
    * [`project`]()
    * [`run`]()
    * [`secret`]()
    * [`task`]()
  * [`run`]()

### `flyte abort run`

`flyte abort run [OPTIONS] RUN_NAME`

Abort a run.

| Option | Type | Description |
|--------|------|-------------|
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--help` | | Display help. |

### `flyte create config`

`flyte create config [OPTIONS]`

Create a new config file.

| Option | Type | Description |
|--------|------|-------------|
| `--endpoint` | `TEXT` | Endpoint of the backend. |
| `--insecure` | | Use an insecure connection to the backend. |
| `--org` | `TEXT` | Organization to operate on. This will override the organization in the config file. |
| `--output` | `PATH` | Path to the output directory where the config will be saved. Defaults to current directory. |
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--help` | | Display help. |

### `flyte create secret`

`flyte create secret [OPTIONS] NAME [VALUE]`

Create a new secret.

| Option | Type | Description |
|--------|------|-------------|
| `--from-file` | `PATH` | Path to a file with a binary secret. |
│ `--type` | `[regular|image_pull]` | Type of the secret. Defaults to `regular` |]
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--help` | | Display help. |

### `flyte deploy`

`flyte deploy [OPTIONS] COMMAND [ARGS]`

Deploy one or more environments from a Python file.

| Option | Type | Description |
|--------|------|-------------|
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--version` | `TEXT` | Version of the environment to deploy. |
| `--dry-run`  `--dryrun` | | Dry run. Do not actually call the backend service. |
| `--local` | | Run the task locally. |
| `--copy-style` | `[loaded_modules|all|none]` | Copy style to use when running the task. Defaults to `loaded_modules` |
| `--help` | | Display help. |

### `flyte get action`

`flyte get action [OPTIONS] RUN_NAME [ACTION_NAME]`

Get all actions for a run or details for a specific action.

| Option | Type | Description |
|--------|------|-------------|
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--help` | | Display help. |


### `flyte get config`

`flyte get config [OPTIONS]`

Shows the automatically detected configuration to connect with remote backend services.

| Option | Type | Description |
|--------|------|-------------|
| `--help` | | Display help. |

### `flyte get io`

`flyte get io [OPTIONS] RUN_NAME [ACTION_NAME]`

Get the inputs and outputs of a run or action.

| Option | Type | Description |
|--------|------|-------------|
| `--inputs-only -i` | | Show only inputs │
| `--outputs-only -0` | | Show only outputs │
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--help` | | Display help. |

### `flyte get logs`

`flyte get logs [OPTIONS] RUN_NAME [ACTION_NAME]`

Stream logs for the provided run or action. If the run is provided, only the logs for the parent action will be streamed.

| Option | Type | Description |
|--------|------|-------------|
| `--lines -l` | `INTEGER` | `Number of lines to show. Only useful for `--pretty` │
│ `--show-ts` | | Show timestamps │
│ `--pretty` | | Show logs in an auto-scrolling box, where number of lines is limited to `--lines` │
│ `--attempt -a` | | `INTEGER` |  Attempt number to show logs for, defaults to the latest attempt. │
│ `--filter-system` | | Filter all system logs from the output. |
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--help` | | Display help. |

### `flyte get project`

`flyte get project [OPTIONS] [NAME]`

Get the specified project.

| Option | Type | Description |
|--------|------|-------------|
| `--help` | | Display help. |

### `flyte get run`

`flyte get run [OPTIONS] [NAME]`

Get the specified run.

| Option | Type | Description |
|--------|------|-------------|
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--help` | | Display help. |

### `flyte get secret`

`flyte get secret [OPTIONS] [NAME]`

Get the specified secret.

| Option | Type | Description |
|--------|------|-------------|
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--help` | | Display help. |

### `flyte get task`

`flyte get task [OPTIONS] [NAME] [VERSION]`

Get the specified task.

| Option | Type | Description |
|--------|------|-------------|
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--help` | | Display help. |

### `flyte run`

`flyte run [OPTIONS] COMMAND [ARGS]`

Run a task directly from a Python file.

| Option | Type | Description |
|--------|------|-------------|
| `--endpoint` | `TEXT` | Endpoint of the backend. If not provided, the CLI will use the endpoint from the default config file. |
| `--config` | `PATH` | Path to the config file. If not provided, the CLI will use the default config file.
| `--project` `-p` | `TEXT` | Project to operate on. |
| `--domain` `-d` | `TEXT` | Domain to operate on. |
| `--local` | | Run the task locally. |
| `--copy-style` | `[loaded_modules|all|none]` | Copy style to use when running the task. Defaults to `loaded_modules` |
| `--name` | `TEXT` | Name of the run. If not provided, a random name will be generated. │
│ `--follow` `-f` | | Wait and watch logs for the parent action. If not provided, the CLI will exit after successfully launching a remote execution with a link to the UI. |
| `--help` | | Display help. |
