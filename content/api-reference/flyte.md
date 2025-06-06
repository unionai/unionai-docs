---
title: "Flyte CLI"
variants: +flyte +byoc +selfmanaged +serverless
---

# Flyte CLI

This is the command line interface for Flyte.

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

The flyte cli follows a simple verb based structure, where the top-level commands are verbs that describe the action
    to be taken, and the subcommands are nouns that describe the object of the action.

|  Option                                                    |  Type     |  Default  |  Description                                                                                                  |
|------------------------------------------------------------|-----------|---------|---------------------------------------------------------------------------------------------------------------|
| `--endpoint`                                               | `text`    |         | The endpoint to connect to, this will override any config and simply used pkce to connect.                    |
| {{< multiline >}}`--insecure`
`--secure`{{< /multiline >}} | `boolean` |         | Use insecure connection to the endpoint. If secure is specified, the CLI will use TLS                         |
| {{< multiline >}}`-v`
`--verbose`{{< /multiline >}}        | `integer` | `0`     | Show verbose messages and exception traces                                                                    |
| `--org`                                                    | `text`    |         | Organization to use                                                                                           |
| {{< multiline >}}`-c`
`--config`{{< /multiline >}}         | `path`    |         | Path to config file (YAML format) to use for the CLI. If not specified, the default config file will be used. |
| `--help`                                                   | `boolean` | `False` | Show this message and exit.                                                                                   |

* * *

### flyte abort

Abort a run.

#### flyte abort run

Abort a run.

|  Option                                             |  Type     |  Default  |  Description                |
|-----------------------------------------------------|-----------|---------|-----------------------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |         | Project to operate on       |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |         | Domain to operate on        |
| `--help`                                            | `boolean` | `False` | Show this message and exit. |

* * *

### flyte create

Create a new task or environment.

#### flyte create config

Create a new config file.

|  Option                                             |  Type     |  Default                                             |  Description                                                                          |
|-----------------------------------------------------|-----------|------------------------------------------------------|---------------------------------------------------------------------------------------|
| `--endpoint`                                        | `text`    |                                                      | Endpoint of the Flyte backend.                                                        |
| `--insecure`                                        | `boolean` | `False`                                              | Use insecure connection to the Flyte backend.                                         |
| `--org`                                             | `text`    |                                                      | Organization to use, this will override the organization in the config file.          |
| {{< multiline >}}`-o`
`--output`{{< /multiline >}}  | `path`    | `/Users/nelson/src/unionai/docs-builder/config.yaml` | Path to the output dir where the config will be saved, defaults to current directory. |
| `--force`                                           | `boolean` | `False`                                              | Force overwrite the config file if it already exists.                                 |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |                                                      | Project to operate on                                                                 |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |                                                      | Domain to operate on                                                                  |
| `--help`                                            | `boolean` | `False`                                              | Show this message and exit.                                                           |

#### flyte create secret

Create a new secret.

|  Option                                             |  Type     |  Default  |  Description                             |
|-----------------------------------------------------|-----------|-----------|------------------------------------------|
| `--from-file`                                       | `path`    |           | Path to the file with the binary secret. |
| `--type`                                            | `choice`  | `regular` | Type of the secret.                      |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |           | Project to operate on                    |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |           | Domain to operate on                     |
| `--help`                                            | `boolean` | `False`   | Show this message and exit.              |

* * *

### flyte deploy

deploy one or more environments from a python file.

|  Option                                                   |  Type     |  Default         |  Description                                       |
|-----------------------------------------------------------|-----------|------------------|----------------------------------------------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}}       | `text`    |                  | Project to operate on                              |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}        | `text`    |                  | Domain to operate on                               |
| `--version`                                               | `text`    |                  | Version of the environment to deploy               |
| {{< multiline >}}`--dry-run`
`--dryrun`{{< /multiline >}} | `boolean` | `False`          | Dry run, do not actually call the backend service. |
| `--local`                                                 | `boolean` | `False`          | Run the task locally                               |
| `--copy-style`                                            | `choice`  | `loaded_modules` | Copy style to use when running the task            |
| `--help`                                                  | `boolean` | `False`          | Show this message and exit.                        |

* * *

### flyte gen

Generate documentation

#### flyte gen docs

Generate documentation

|  Option                                             |  Type     |  Default  |  Description                            |
|-----------------------------------------------------|-----------|---------|-----------------------------------------|
| `--type`                                            | `text`    |         | Type of documentation (valid: markdown) |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |         | Project to operate on                   |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |         | Domain to operate on                    |
| `--help`                                            | `boolean` | `False` | Show this message and exit.             |

* * *

### flyte get

Get the value of a task or environment.

#### flyte get action

Get all actions for a run or details for a specific action.

|  Option                                             |  Type     |  Default  |  Description                |
|-----------------------------------------------------|-----------|---------|-----------------------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |         | Project to operate on       |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |         | Domain to operate on        |
| `--help`                                            | `boolean` | `False` | Show this message and exit. |

#### flyte get config

Shows the automatically detected configuration to connect with remote Flyte services.

#### flyte get io

Get the inputs and outputs of a run or action.

|  Option                                                  |  Type     |  Default  |  Description                |
|----------------------------------------------------------|-----------|---------|-----------------------------|
| {{< multiline >}}`--inputs-only`
`-i`{{< /multiline >}}  | `boolean` | `False` | Show only inputs            |
| {{< multiline >}}`--outputs-only`
`-o`{{< /multiline >}} | `boolean` | `False` | Show only outputs           |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}}      | `text`    |         | Project to operate on       |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}       | `text`    |         | Domain to operate on        |
| `--help`                                                 | `boolean` | `False` | Show this message and exit. |

#### flyte get logs

Stream logs for the provided run or action. If the run is provided, only the logs for the parent action will be
    streamed.

|  Option                                             |  Type     |  Default  |  Description                                                                     |
|-----------------------------------------------------|-----------|---------|----------------------------------------------------------------------------------|
| {{< multiline >}}`--lines`
`-l`{{< /multiline >}}   | `integer` | `30`    | Number of lines to show, only useful for --pretty                                |
| `--show-ts`                                         | `boolean` | `False` | Show timestamps                                                                  |
| `--pretty`                                          | `boolean` | `False` | Show logs in a auto scrolling box, where number of lines is limited to `--lines` |
| {{< multiline >}}`--attempt`
`-a`{{< /multiline >}} | `integer` |         | Attempt number to show logs for, defaults to the latest attempt.                 |
| `--filter-system`                                   | `boolean` | `False` | Filter all system logs from the output.                                          |
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |         | Project to operate on                                                            |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |         | Domain to operate on                                                             |
| `--help`                                            | `boolean` | `False` | Show this message and exit.                                                      |

#### flyte get project

Get the current project.

|  Option  |  Type     |  Default  |  Description                |
|----------|-----------|---------|-----------------------------|
| `--help` | `boolean` | `False` | Show this message and exit. |

#### flyte get run

Get the current run.

|  Option                                             |  Type     |  Default  |  Description                |
|-----------------------------------------------------|-----------|---------|-----------------------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |         | Project to operate on       |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |         | Domain to operate on        |
| `--help`                                            | `boolean` | `False` | Show this message and exit. |

#### flyte get secret

Get the current secret.

|  Option                                             |  Type     |  Default  |  Description                |
|-----------------------------------------------------|-----------|---------|-----------------------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |         | Project to operate on       |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |         | Domain to operate on        |
| `--help`                                            | `boolean` | `False` | Show this message and exit. |

#### flyte get task

Get the current task.

|  Option                                             |  Type     |  Default  |  Description                |
|-----------------------------------------------------|-----------|---------|-----------------------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |         | Project to operate on       |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |         | Domain to operate on        |
| `--help`                                            | `boolean` | `False` | Show this message and exit. |

* * *

### flyte run

Run a task from a python file.

|  Option                                             |  Type     |  Default         |  Description                                                                                                                                         |
|-----------------------------------------------------|-----------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| {{< multiline >}}`-p`
`--project`{{< /multiline >}} | `text`    |                  | Project to operate on                                                                                                                                |
| {{< multiline >}}`-d`
`--domain`{{< /multiline >}}  | `text`    |                  | Domain to operate on                                                                                                                                 |
| `--local`                                           | `boolean` | `False`          | Run the task locally                                                                                                                                 |
| `--copy-style`                                      | `choice`  | `loaded_modules` | Copy style to use when running the task                                                                                                              |
| `--name`                                            | `text`    |                  | Name of the run. If not provided, a random name will be generated.                                                                                   |
| {{< multiline >}}`--follow`
`-f`{{< /multiline >}}  | `boolean` | `False`          | Wait and watch logs for the parent action. If not provided, the cli will exit after successfully launching a remote execution with a link to the UI. |
| `--help`                                            | `boolean` | `False`          | Show this message and exit.                                                                                                                          |
