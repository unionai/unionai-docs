---
title: Union CLI
weight: 3
variants: -flyte +serverless +byoc +selfmanaged
---

# {{< key cli_name >}} CLI

The `{{< key cli >}}` CLI is the main tool developers use to interact with {{< key product_name >}} on the command line.

## Installation

The recommended way to install the union CLI outside a workflow project is to use [`uv`](https://docs.astral.sh/uv/):

```shell
$ uv tool install {{< key kit >}}
```

This will install the `{{< key cli >}}` CLI globally on your system [as a `uv` tool](https://docs.astral.sh/uv/concepts/tools/).


## Configure the `{{< key cli >}}` CLI

{{< variant serverless >}}
{{< markdown >}}
To configure the `{{< key cli >}}` CLI to connect to {{< key product_name >}} Serverless, run the following command:

```shell
$ {{< key cli >}} create login --serverless
```

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

To configure the `{{< key cli >}}` CLI to connect to you {{< key product_name >}}  BYOC or Self-managed instance, run the following command:

```shell
$ {{< key cli >}} create login --host <{{< key product >}}-host-url>
```

where `<{{< key cli >}}-host-url>` is the URL of your {{< key product_name >}}  instance.

{{< /markdown >}}
{{< /variant >}}

These command will create the file `~/.{{< key product >}}/config.yaml` with the configuration information to connect to the {{< key product_name >}}  instance.

See [Getting started > Local setup](../user-guide/getting-started/local-setup) for more details.

## Overriding the configuration file location

By default, the `{{< key cli >}}` CLI will look for a configuration file at `~/.{{< key product >}}/config.yaml`.

You can override this behavior to specify a different configuration file by setting the `{{< key config_env >}} ` environment variable:

```shell
export {{< key config_env >}}=~/.my-config-location/my-config.yaml
```

Alternatively, you can always specify the configuration file on the command line when invoking `{{< key cli >}}` by using the `--config` flag:

```shell
$ {{< key cli >}} --config ~/.my-config-location/my-config.yaml run my_script.py my_workflow
```

## `{{< key cli >}}` CLI configuration search path

The `{{< key cli >}}` CLI will check for configuration files as follows:

First, if a `--config` option is used, it will use the specified config file.

{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

Second, the config files pointed to by the following environment variables (in this order):

* `UNION_CONFIG`
* `UNIONAI_CONFIG`
* `UCTL_CONFIG`

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

Second, the config file pointed to by the `FLYTECTL_CONFIG` environment variable.

{{< /markdown >}}
{{< /variant >}}

Third, the following hard-coded locations (in this order):

{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

Third, the following hard-coded locations (in this order):

* `~/.union/config.yaml`
* `~/.uctl/config.yaml`

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

Third, the hard-coded location `~/.flyte/config.yaml`.

{{< /markdown >}}
{{< /variant >}}

If none of these are present, the CLI will raise an error.

## `{{< key cli >}}` CLI commands

Entrypoint for all the user commands.

```shell
union [OPTIONS] COMMAND [ARGS]...
```

### Options

- `-v`, `--verbose`
  Show verbose messages and exception traces.

- `-k`, `--pkgs <pkgs>`
  Dot-delineated python packages to operate on. Multiple may be specified (can use commas, or specify the switch multiple times). Please note that this option will override the option specified in the configuration file, or environment variable.

- `-c`, `--config <config>`
  Path to config file for use within container.

---

### `backfill`

The backfill command generates and registers a new workflow based on the input launchplan to run an automated backfill. The workflow can be managed using the UI and can be canceled, relaunched, and recovered.

> - `launchplan` refers to the name of the Launchplan.
> - `launchplan_version` is optional and should be a valid version for a Launchplan version.

```shell
union backfill [OPTIONS] LAUNCHPLAN [LAUNCHPLAN_VERSION]
```

#### Options

- `-p`, `--project <project>`
  Project for workflow/launchplan. Can also be set through envvar `FLYTE_DEFAULT_PROJECT`.
  **Default:** `flytesnacks`

- `-d`, `--domain <domain>`
  Domain for workflow/launchplan, can also be set through envvar `FLYTE_DEFAULT_DOMAIN`.
  **Default:** `'development'`

- `-v`, `--version <version>`
  Version for the registered workflow. If not specified, it is auto-derived using the start and end date.

- `-n`, `--execution-name <execution_name>`
  Create a named execution for the backfill. This can prevent launching multiple executions.

- `--dry-run`
  Just generate the workflow - do not register or execute.
  **Default:** `False`

- `--parallel`, `--serial`
  All backfill steps can be run in parallel (limited by max-parallelism) if using `--parallel`. Else all steps will be run sequentially (`--serial`).
  **Default:** `False`

- `--execute`, `--do-not-execute`
  Generate the workflow and register, do not execute.
  **Default:** `True`

- `--from-date <from_date>`
  Date from which the backfill should begin. Start date is inclusive.

- `--to-date <to_date>`
  Date to which the backfill should run until. End date is inclusive.

- `--backfill-window <backfill_window>`
  Timedelta for number of days, minutes, or hours after the from-date or before the to-date to compute the backfills between. This is needed with from-date / to-date. Optional if both from-date and to-date are provided.

- `--fail-fast`, `--no-fail-fast`
  If set to true, the backfill will fail immediately if any of the backfill steps fail. If set to false, the backfill will continue to run even if some of the backfill steps fail.
  **Default:** `True`

- `--overwrite-cache`
  Whether to overwrite the cache if it already exists.
  **Default:** `False`

#### Arguments

- `LAUNCHPLAN`
  Required argument.

- `LAUNCHPLAN_VERSION`
  Optional argument.

---

### `build`

This command can build an image for a workflow or a task from the command line, for fully self-contained scripts.

```shell
union build [OPTIONS] COMMAND [ARGS]...
```

#### Options

- `-p`, `--project <project>`
  Project to register and run this workflow in. Can also be set through envvar `FLYTE_DEFAULT_PROJECT`.
  **Default:** `flytesnacks`

- `-d`, `--domain <domain>`
  Domain to register and run this workflow in, can also be set through envvar `FLYTE_DEFAULT_DOMAIN`.
  **Default:** `'development'`

- `--destination-dir <destination_dir>`
  Directory inside the image where the tar file containing the code will be copied to.
  **Default:** `'.'`

- `--copy-all`
  [Deprecated, see `--copy`] Copy all files in the source root directory to the destination directory. You can specify `--copy all` instead.
  **Default:** `False`

- `--copy <copy>`
  Specifies how to detect which files to copy into the image. `all` will behave as the deprecated copy-all flag, `auto` copies only loaded Python modules.
  **Default:** `'auto'`
  **Options:** `all | auto`

- `-i`, `--image <image_config>`
  Multiple values allowed. Image used to register and run.
  **Default:** `'cr.union.ai/union/unionai:py3.11-latest' (Serverless), 'cr.flyte.org/flyteorg/flytekit:py3.9-latest' (BYOC)`

- `--service-account <service_account>`
  Service account used when executing this workflow.

- `--wait`, `--wait-execution`
  Whether to wait for the execution to finish.
  **Default:** `False`

- `--poll-interval <poll_interval>`
  Poll interval in seconds to check the status of the execution.

- `--dump-snippet`
  Whether to dump a code snippet instructing how to load the workflow execution using UnionRemote.
  **Default:** `False`

- `--overwrite-cache`
  Whether to overwrite the cache if it already exists.
  **Default:** `False`

- `--envvars`, `--env <envvars>`
  Multiple values allowed. Environment variables to set in the container, of the format `ENV_NAME=ENV_VALUE`.

- `--tags`, `--tag <tags>`
  Multiple values allowed. Tags to set for the execution.

- `--name <name>`
  Name to assign to this execution.

- `--labels`, `--label <labels>`
  Multiple values allowed. Labels to be attached to the execution of the format `label_key=label_value`.

- `--annotations`, `--annotation <annotations>`
  Multiple values allowed. Annotations to be attached to the execution of the format `key=value`.

- `--raw-output-data-prefix`, `--raw-data-prefix <raw_output_data_prefix>`
  File Path prefix to store raw output data. Examples are `file://`, `s3://`, `gs://` etc., as supported by fsspec. If not specified, raw data will be stored in the default configured location in remote or locally to the temp file system.

- `--max-parallelism <max_parallelism>`
  Number of nodes of a workflow that can be executed in parallel. If not specified, project/domain defaults are used. If 0, then it is unlimited.

- `--disable-notifications`
  Should notifications be disabled for this execution.
  **Default:** `False`

- `-r`, `--remote`
  Whether to register and run the workflow on a Union deployment.
  **Default:** `False`

- `--limit <limit>`
  Use this to limit the number of entities to fetch.
  **Default:** `50`

- `--cluster-pool <cluster_pool>`
  Assign newly created execution to a given cluster pool.

- `--execution-cluster-label`, `--ecl <execution_cluster_label>`
  Assign newly created execution to a given execution cluster label.

- `--fast`
  Use fast serialization. The image won’t contain the source code.
  **Default:** `False`

---

### `build.py`

Build an image for [workflow|task] from build.py

```shell
union build build.py [OPTIONS] COMMAND [ARGS]...
```

---

### `create`

Create a resource.

```shell
union create [OPTIONS] COMMAND [ARGS]...
```

#### `api-key`

Manage API keys.

```shell
union create api-key [OPTIONS] COMMAND [ARGS]...
```

##### `admin`

Create an api key.

```shell
union create api-key admin [OPTIONS]
```

###### Options

- `--name <name>`
  Required Name for API key.

---

#### `artifact`

Create an artifact with NAME.

```shell
union create artifact [OPTIONS] NAME
```

##### Options

- `--version <version>`
  Required Version of the artifact.

- `-p`, `--partitions <partitions>`
  Partitions for the artifact.

- `--short-description <short_description>`
  Short description of the artifact.

- `-p`, `--project <project>`
  Project to operate on.
  **Default:** `functools.partial(<function _get_default_project at 0x7fcfcc43b6a0>, previous_default='default')`

- `-d`, `--domain <domain>`
  Domain to operate on.
  **Default:** `'development'`

- `--from_float <from_float>`
  Create an artifact of type (float).

- `--from_int <from_int>`
  Create an artifact of type (int).

- `--from_str <from_str>`
  Create an artifact of type (str).

- `--from_bool <from_bool>`
  Create an artifact of type (bool).

- `--from_datetime <from_datetime>`
  Create an artifact of type (datetime).

- `--from_duration <from_duration>`
  Create an artifact of type (duration).

- `--from_json <from_json>`
  Create an artifact of type (struct).

- `--from_dataframe <from_dataframe>`
  Create an artifact of type (parquet).

- `--from_file <from_file>`
  Create an artifact of type (file).

- `--from_dir <from_dir>`
  Create an artifact of type (dir).

###### Arguments

- `NAME`
  Required argument.

---

#### `login`

Log into Union.

On Union Serverless run: `union create login --serverless`

On Union BYOC run: `union create login --host UNION_TENANT`

```shell
union create login [OPTIONS]
```

##### Options

- `--auth <auth>`
  Authorization method to use.
  **Options:** `device-flow | pkce`

- `--host <host>`
  Host to connect to. Mutually exclusive with serverless.

- `--serverless`
  Connect to serverless. Mutually exclusive with host.

---

#### `secret`

Create a secret with NAME.

```shell
union create secret [OPTIONS] NAME
```

##### Options

- `--value <value>`
  Secret value. Mutually exclusive with value_file.

- `-f`, `--value-file <value_file>`
  Path to file containing the secret. Mutually exclusive with value.

- `--project <project>`
  Project name.

- `--domain <domain>`
  Domain name.

###### Arguments

- `NAME`
  Required argument.

---

#### `workspace`

Create workspace.

```shell
union create workspace [OPTIONS] CONFIG_FILE
```

###### Arguments

- `CONFIG_FILE`
  Required argument.

---

#### `workspace-config`

Create workspace config at CONFIG_FILE.

```shell
union create workspace-config [OPTIONS] CONFIG_FILE
```

##### Options

- `--init <init>`
  Required.
  **Options:** `base_image`

###### Arguments

- `CONFIG_FILE`
  Required argument.

---

### `delete`

Delete a resource.

```shell
union delete [OPTIONS] COMMAND [ARGS]...
```

#### `api-key`

Manage API keys.

```shell
union delete api-key [OPTIONS] COMMAND [ARGS]...
```

##### `admin`

Delete api key.

```shell
union delete api-key admin [OPTIONS]
```

###### Options

- `--name <name>`
  Required Name for API key.

---

#### `login`

Delete login information.

```shell
union delete login [OPTIONS]
```

---

#### `secret`

Delete secret with NAME.

```shell
union delete secret [OPTIONS] NAME
```

##### Options

- `--project <project>`
  Project name.

- `--domain <domain>`
  Domain name.

###### Arguments

- `NAME`
  Required argument.

---

#### `workspace`

Delete workspace with NAME.

```shell
union delete workspace [OPTIONS] NAME
```

##### Options

- `--project <project>`
  Project name.

- `--domain <domain>`
  Domain name.

###### Arguments

- `NAME`
  Required argument.

---

### `deploy`

Deploy a resource.

```shell
union deploy [OPTIONS] COMMAND [ARGS]...
```

#### `apps`

Deploy application on Union.

```shell
union deploy apps [OPTIONS] COMMAND [ARGS]...
```

##### Options

- `-p`, `--project <project>`
  Project to run deploy.
  **Default:** `flytesnacks`

- `-d`, `--domain <domain>`
  Domain to run deploy.
  **Default:** `'development'`

- `-n`, `--name <name>`
  Application name to start.

---

#### `build.py`

Deploy application in build.py.

```shell
union deploy apps build.py [OPTIONS] COMMAND [ARGS]...
```

---

### `execution`

The execution command allows you to interact with Union’s execution system, such as recovering/relaunching a failed execution.

```shell
union execution [OPTIONS] COMMAND [ARGS]...
```

##### Options

- `-p`, `--project <project>`
  Project for workflow/launchplan. Can also be set through envvar `FLYTE_DEFAULT_PROJECT`.
  **Default:** `flytesnacks`

- `-d`, `--domain <domain>`
  Domain for workflow/launchplan, can also be set through envvar `FLYTE_DEFAULT_DOMAIN`.
  **Default:** `'development'`

- `--execution-id <execution_id>`
  Required The execution id.

---

#### `recover`

Recover a failed execution.

```shell
union execution recover [OPTIONS]
```

---

#### `relaunch`

Relaunch a failed execution.

```shell
union execution relaunch [OPTIONS]
```

---

### `fetch`

Retrieve Inputs/Outputs for a Union execution or any of the inner node executions from the remote server.

The URI can be retrieved from the UI, or by invoking the get_data API.

```shell
union fetch [OPTIONS] FLYTE-DATA-URI (format flyte://...) DOWNLOAD-TO Local path (optional)
```

##### Options

- `-r`, `--recursive`
  Fetch recursively, all variables in the URI. This is not needed for directories as they are automatically recursively downloaded.

###### Arguments

- `FLYTE-DATA-URI (format flyte://...)`
  Required argument.

- `DOWNLOAD-TO Local path (optional)`
  Optional argument.

---

### `get`

Get a single or multiple remote objects.

```shell
union get [OPTIONS] COMMAND [ARGS]...
```

#### `api-key`

Manage API keys.

```shell
union get api-key [OPTIONS] COMMAND [ARGS]...
```

##### `admin`

Show existing API keys for admin.

```shell
union get api-key admin [OPTIONS]
```

---

#### `apps`

Get apps.

```shell
union get apps [OPTIONS]
```

##### Options

- `--name <name>`
- `--project <project>`
  Project name.

- `--domain <domain>`
  Domain name.

---

#### `launchplan`

Interact with launchplans.

```shell
union get launchplan [OPTIONS] LAUNCHPLAN-NAME LAUNCHPLAN-VERSION
```

##### Options

- `--active-only`, `--scheduled`
  Only return active launchplans.

- `-p`, `--project <project>`
  Project for workflow/launchplan. Can also be set through envvar `FLYTE_DEFAULT_PROJECT`.
  **Default:** `flytesnacks`

- `-d`, `--domain <domain>`
  Domain for workflow/launchplan, can also be set through envvar `FLYTE_DEFAULT_DOMAIN`.
  **Default:** `'development'`

- `-l`, `--limit <limit>`
  Limit the number of launchplans returned.

###### Arguments

- `LAUNCHPLAN-NAME`
  Optional argument.

- `LAUNCHPLAN-VERSION`
  Optional argument.

---

#### `secret`

Get secrets.

```shell
union get secret [OPTIONS]
```

##### Options

- `--project <project>`
  Project name.

- `--domain <domain>`
  Domain name.

---

#### `workspace`

Get workspaces.

```shell
union get workspace [OPTIONS]
```

##### Options

- `--name <name>`
- `--project <project>`
  Project name.

- `--domain <domain>`
  Domain name.

- `--show-details`
  Show additional details.

---

### `info`

```shell
union info [OPTIONS]
```

---

### `init`

Create Union-ready projects.

```shell
union init [OPTIONS] PROJECT_NAME
```

##### Options

- `--template <template>`
  Template folder name to be used in the repo - `flyteorg/flytekit-python-template.git`.

###### Arguments

- `PROJECT_NAME`
  Required argument.

---

### `launchplan`

The launchplan command activates or deactivates a specified or the latest version of the launchplan. If `--activate` is chosen then the previous version of the launchplan will be deactivated.

> - `launchplan` refers to the name of the Launchplan.
> - `launchplan_version` is optional and should be a valid version for a Launchplan version. If not specified the latest will be used.

```shell
union launchplan [OPTIONS] LAUNCHPLAN [LAUNCHPLAN_VERSION]
```

##### Options

- `-p`, `--project <project>`
  Project for workflow/launchplan. Can also be set through envvar `FLYTE_DEFAULT_PROJECT`.
  **Default:** `flytesnacks`

- `-d`, `--domain <domain>`
  Domain for workflow/launchplan, can also be set through envvar `FLYTE_DEFAULT_DOMAIN`.
  **Default:** `'development'`

- `--activate`, `--deactivate`
  Required Activate or Deactivate the launchplan.

###### Arguments

- `LAUNCHPLAN`
  Required argument.

- `LAUNCHPLAN_VERSION`
  Optional argument.

---

### `local-cache`

Interact with the local cache.

```shell
union local-cache [OPTIONS] COMMAND [ARGS]...
```

#### `clear`

This command will remove all stored objects from local cache.

```shell
union local-cache clear [OPTIONS]
```

---

### `metrics`

```shell
union metrics [OPTIONS] COMMAND [ARGS]...
```

##### Options

- `-d`, `--depth <depth>`
  The depth of Flyte entity hierarchy to traverse when computing metrics for this execution.

- `-p`, `--project <project>`
  The project of the workflow execution.

- `-d`, `--domain <domain>`
  The domain of the workflow execution.

---

#### `dump`

The dump command aggregates workflow execution metrics and displays them. This aggregation is meant to provide an easy to understand breakdown of where time is spent in a hierarchical manner.

> - `execution_id` refers to the id of the workflow execution.

```shell
union metrics dump [OPTIONS] EXECUTION_ID
```

###### Arguments

- `EXECUTION_ID`
  Required argument.

---

#### `explain`

The explain command prints each individual execution span and the associated timestamps and Flyte entity reference. This breakdown provides precise information into exactly how and when Flyte processes a workflow execution.

> - `execution_id` refers to the id of the workflow execution.

```shell
union metrics explain [OPTIONS] EXECUTION_ID
```

###### Arguments

- `EXECUTION_ID`
  Required argument.

---

### `package`

This command produces a Union backend registrable package of all entities in Union. For tasks, one pb file is produced for each task, representing one TaskTemplate object. For workflows, one pb file is produced for each workflow, representing a WorkflowClosure object. The closure object contains the WorkflowTemplate, along with the relevant tasks for that workflow. This serialization step will set the name of the tasks to the fully qualified name of the task function.

```shell
union package [OPTIONS]
```

##### Options

- `-i`, `--image <image_config>`
  A fully qualified tag for a docker image, for example `somedocker.com/myimage:someversion123`. This is a multi-option and can be of the form `--image xyz.io/docker:latest --image my_image=xyz.io/docker2:latest`. Note, the name=image_uri. The name is optional, if not provided the image will be used as the default image. All the names have to be unique, and thus there can only be one `--image` option with no name.

- `-s`, `--source <source>`
  Local filesystem path to the root of the package.

- `-o`, `--output <output>`
  Filesystem path to the source of the Python package (from where the pkgs will start).

- `--fast`
  [Deprecated, see `--copy`] This flag enables fast packaging, that allows no container build deploys of flyte workflows and tasks. You should specify `--copy all/auto` instead. Note this needs additional configuration, refer to the docs.

- `--copy <copy>`
  Specify whether local files should be copied and uploaded so task containers have up-to-date code. `all` will behave as the current `fast` flag, copying all files, `auto` copies only loaded Python modules.
  **Default:** `'none'`
  **Options:** `all | auto | none`

- `-f`, `--force`
  This flag enables overriding existing output files. If not specified, package will exit with an error, when an output file already exists.

- `-p`, `--python-interpreter <python_interpreter>`
  Use this to override the default location of the in-container python interpreter that will be used by Flyte to load your program. This is usually where you install union and flytekit within the container.

- `-d`, `--in-container-source-path <in_container_source_path>`
  Filesystem path to where the code is copied into within the Dockerfile. look for `COPY . /root` like command.

- `--deref-symlinks`
  Enables symlink dereferencing when packaging files in fast registration.

- `--env`, `--envvars <env>`
  Environment variables to set in the container, of the format `ENV_NAME=ENV_VALUE`.

---

### `register`

This command is similar to package but instead of producing a zip file, all your Flyte entities are compiled, and then sent to the backend specified by your config file. Think of this as combining the `union package` and the `uctl register` steps in one command. This is why you see switches you’d normally use with `uctl` like service account here.

Note: This command runs “fast” register by default. This means that a zip is created from the detected root of the packages given and uploaded. Just like with `union run`, tasks registered from this command will download and unzip that code package before running.

Note: This command only works on regular Python packages, not namespace packages. When determining the root of your project, it finds the first folder that does not have a `__init__.py` file.

```shell
union register [OPTIONS] [PACKAGE_OR_MODULE]...
```

##### Options

- `-p`, `--project <project>`
  Project for workflow/launchplan. Can also be set through envvar `FLYTE_DEFAULT_PROJECT`.
  **Default:** `flytesnacks`

- `-d`, `--domain <domain>`
  Domain for workflow/launchplan, can also be set through envvar `FLYTE_DEFAULT_DOMAIN`.
  **Default:** `'development'`

- `-i`, `--image <image_config>`
  A fully qualified tag for a docker image, for example `somedocker.com/myimage:someversion123`. This is a multi-option and can be of the form `--image xyz.io/docker:latest --image my_image=xyz.io/docker2:latest`. Note, the name=image_uri. The name is optional, if not provided the image will be used as the default image. All the names have to be unique, and thus there can only be one `--image` option with no name.

- `-o`, `--output <output>`
  Directory to write the output tar file containing the protobuf definitions.

- `-D`, `--destination-dir <destination_dir>`
  Directory inside the image where the tar file containing the code will be copied to.

- `--service-account <service_account>`
  Service account used when creating launch plans.

- `--raw-data-prefix <raw_data_prefix>`
  Raw output data prefix when creating launch plans, where offloaded data will be stored.

- `-v`, `--version <version>`
  Version the package or module is registered with.

- `--deref-symlinks`
  Enables symlink dereferencing when packaging files in fast registration.

- `--non-fast`
  [Deprecated, see `--copy`] Skip zipping and uploading the package. You should specify `--copy none` instead.

- `--copy <copy>`
  Specify how and whether to use fast register. `all` is the current behavior copying all files from root, `auto` copies only loaded Python modules, `none` means no files are copied, i.e. don’t use fast register.
  **Default:** `'all'`
  **Options:** `all | auto | none`

- `--dry-run`
  Execute registration in dry-run mode. Skips actual registration to remote.

- `--activate-launchplans`, `--activate-launchplan`
  Activate newly registered Launchplans. This operation deactivates previous versions of Launchplans.

- `--env`, `--envvars <env>`
  Environment variables to set in the container, of the format `ENV_NAME=ENV_VALUE`.

- `--skip-errors`, `--skip-error`
  Skip errors during registration. This is useful when registering multiple packages and you want to skip errors for some packages.

###### Arguments

- `PACKAGE_OR_MODULE`
  Optional argument(s).

---

### `run`

This command can execute either a workflow or a task from the command line, allowing for fully self-contained scripts. Tasks and workflows can be imported from other files.

Note: This command is compatible with regular Python packages, but not with namespace packages. When determining the root of your project, it identifies the first folder without an `__init__.py` file.

```shell
union run [OPTIONS] COMMAND [ARGS]...
```

##### Options

- `-p`, `--project <project>`
  Project to register and run this workflow in. Can also be set through envvar `FLYTE_DEFAULT_PROJECT`.
  **Default:** `flytesnacks`

- `-d`, `--domain <domain>`
  Domain to register and run this workflow in, can also be set through envvar `FLYTE_DEFAULT_DOMAIN`.
  **Default:** `'development'`

- `--destination-dir <destination_dir>`
  Directory inside the image where the tar file containing the code will be copied to.
  **Default:** `'.'`

- `--copy-all`
  [Deprecated, see `--copy`] Copy all files in the source root directory to the destination directory. You can specify `--copy all` instead.
  **Default:** `False`

- `--copy <copy>`
  Specifies how to detect which files to copy into the image. `all` will behave as the deprecated copy-all flag, `auto` copies only loaded Python modules.
  **Default:** `'auto'`
  **Options:** `all | auto`

- `-i`, `--image <image_config>`
  Multiple values allowed. Image used to register and run.
  **Default:** `'cr.union.ai/union/unionai:py3.11-latest' (Serverless), 'cr.flyte.org/flyteorg/flytekit:py3.9-latest' (BYOC)`

- `--service-account <service_account>`
  Service account used when executing this workflow.

- `--wait`, `--wait-execution`
  Whether to wait for the execution to finish.
  **Default:** `False`

- `--poll-interval <poll_interval>`
  Poll interval in seconds to check the status of the execution.

- `--dump-snippet`
  Whether to dump a code snippet instructing how to load the workflow execution using UnionRemote.
  **Default:** `False`

- `--overwrite-cache`
  Whether to overwrite the cache if it already exists.
  **Default:** `False`

- `--envvars`, `--env <envvars>`
  Multiple values allowed. Environment variables to set in the container, of the format `ENV_NAME=ENV_VALUE`.

- `--tags`, `--tag <tags>`
  Multiple values allowed. Tags to set for the execution.

- `--name <name>`
  Name to assign to this execution.

- `--labels`, `--label <labels>`
  Multiple values allowed. Labels to be attached to the execution of the format `label_key=label_value`.

- `--annotations`, `--annotation <annotations>`
  Multiple values allowed. Annotations to be attached to the execution of the format `key=value`.

- `--raw-output-data-prefix`, `--raw-data-prefix <raw_output_data_prefix>`
  File Path prefix to store raw output data. Examples are `file://`, `s3://`, `gs://` etc., as supported by fsspec. If not specified, raw data will be stored in the default configured location in remote or locally to the temp file system.

- `--max-parallelism <max_parallelism>`
  Number of nodes of a workflow that can be executed in parallel. If not specified, project/domain defaults are used. If 0, then it is unlimited.

- `--disable-notifications`
  Should notifications be disabled for this execution.
  **Default:** `False`

- `-r`, `--remote`
  Whether to register and run the workflow on a Union deployment.
  **Default:** `False`

- `--limit <limit>`
  Use this to limit the number of entities to fetch.
  **Default:** `50`

- `--cluster-pool <cluster_pool>`
  Assign newly created execution to a given cluster pool.

- `--execution-cluster-label`, `--ecl <execution_cluster_label>`
  Assign newly created execution to a given execution cluster label.

---

#### `build.py`

Run a [workflow|task|launch plan] from build.py.

```shell
union run build.py [OPTIONS] COMMAND [ARGS]...
```

---

#### `remote-launchplan`

Retrieve remote-launchplan from a remote Union instance and execute them. The command only lists the names of the entities, but it is possible to pass in a specific version of the entity if known in the format `<name>:<version>`. If version is not provided, the latest version is used for tasks and active or latest version is used for launchplans.

```shell
union run remote-launchplan [OPTIONS] COMMAND [ARGS]...
```

---

#### `remote-task`

Retrieve remote-task from a remote Union instance and execute them. The command only lists the names of the entities, but it is possible to pass in a specific version of the entity if known in the format `<name>:<version>`. If version is not provided, the latest version is used for tasks and active or latest version is used for launchplans.

```shell
union run remote-task [OPTIONS] COMMAND [ARGS]...
```

---

#### `remote-workflow`

Retrieve remote-workflow from a remote Union instance and execute them. The command only lists the names of the entities, but it is possible to pass in a specific version of the entity if known in the format `<name>:<version>`. If version is not provided, the latest version is used for tasks and active or latest version is used for launchplans.

```shell
union run remote-workflow [OPTIONS] COMMAND [ARGS]...
```

---

### `serialize`

This command produces protobufs for tasks and templates. For tasks, one pb file is produced for each task, representing one TaskTemplate object. For workflows, one pb file is produced for each workflow, representing a WorkflowClosure object. The closure object contains the WorkflowTemplate, along with the relevant tasks for that workflow. In lieu of Admin, this serialization step will set the URN of the tasks to the fully qualified name of the task function.

```shell
union serialize [OPTIONS] COMMAND [ARGS]...
```

##### Options

- `-i`, `--image <image_config>`
  A fully qualified tag for a docker image, for example `somedocker.com/myimage:someversion123`. This is a multi-option and can be of the form `--image xyz.io/docker:latest --image my_image=xyz.io/docker2:latest`. Note, the name=image_uri. The name is optional, if not provided the image will be used as the default image. All the names have to be unique, and thus there can only be one `--image` option with no name.

- `--local-source-root <local_source_root>`
  Root dir for Python code containing workflow definitions to operate on when not the current working directory. Optional when running `union serialize` in out-of-container-mode and your code lies outside of your working directory.

- `--in-container-config-path <in_container_config_path>`
  This is where the configuration for your task lives inside the container. The reason it needs to be a separate option is because this union utility cannot know where the Dockerfile writes the config file to. Required for running `union serialize` in out-of-container-mode.

- `--in-container-virtualenv-root <in_container_virtualenv_root>`
  **DEPRECATED:** This flag is ignored! This is the root of the flytekit virtual env in your container. The reason it needs to be a separate option is because this union utility cannot know where flytekit is installed inside your container. Required for running `union serialize` in out of container mode when your container installs the flytekit virtualenv outside of the default `/opt/venv`.

- `--env`, `--envvars <env>`
  Environment variables to set in the container, of the format `ENV_NAME=ENV_VALUE`.

---

#### `fast`

```shell
union serialize fast [OPTIONS] COMMAND [ARGS]...
```

---

#### `workflows`

```shell
union serialize fast workflows [OPTIONS]
```

##### Options

- `--deref-symlinks`
  Enables symlink dereferencing when packaging files in fast registration.

- `-f`, `--folder <folder>`
---

#### `workflows`

```shell
union serialize workflows [OPTIONS]
```

##### Options

- `-f`, `--folder <folder>`
---

### `serve`

Start the specific service.

```shell
union serve [OPTIONS] COMMAND [ARGS]...
```

#### `agent`

Start a grpc server for the agent service.

```shell
union serve agent [OPTIONS]
```

##### Options

- `--port <port>`
  Grpc port for the agent service.

- `--worker <worker>`
  Number of workers for the grpc server.

- `--timeout <timeout>`
  It will wait for the specified number of seconds before shutting down grpc server. It should only be used for testing.

---

### `stop`

Stop a resource.

```shell
union stop [OPTIONS] COMMAND [ARGS]...
```

#### `apps`

```shell
union stop apps [OPTIONS]
```

##### Options

- `--name <name>`
  Required.

- `--project <project>`
  Project name.

- `--domain <domain>`
  Domain name.

---

### `update`

Update a resource.

```shell
union update [OPTIONS] COMMAND [ARGS]...
```

#### `secret`

Update secret with NAME.

```shell
union update secret [OPTIONS] NAME
```

##### Options

- `--value <value>`
  Secret value. Mutually exclusive with value_file.

- `-f`, `--value-file <value_file>`
  Path to file containing the secret. Mutually exclusive with value.

- `--project <project>`
  Project name.

- `--domain <domain>`
  Domain name.

###### Arguments

- `NAME`
  Required argument.