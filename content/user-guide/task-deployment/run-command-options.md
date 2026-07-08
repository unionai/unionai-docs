---
title: Run command options
weight: 4
variants: +flyte +union
---

# Run command options

The `flyte run` command provides the following options:

**`flyte run [OPTIONS] <PATH>|deployed_task <TASK_NAME>`**

| Option                      | Short | Type   | Default                   | Description                                            |
|-----------------------------|-------|--------|---------------------------|--------------------------------------------------------|
| `--project`                 | `-p`  | text   | *from config*             | Project to run tasks in                                |
| `--domain`                  | `-d`  | text   | *from config*             | Domain to run tasks in                                 |
| `--local`                   |       | flag   | `false`                   | Run the task locally                                   |
| `--copy-style`              |       | choice | `loaded_modules|all|none` | Code bundling strategy                                 |
| `--root-dir`                |       | path   | *current dir*             | Override source root directory                         |
| `--raw-data-path`           |       | text   |                           | Override the output location for offloaded data types. |
| `--service-account`         |       | text   |                           | Kubernetes service account.                            |
| `--name`                    |       | text   |                           | Name of the run.                                       |
| `--follow`                  | `-f`  | flag   | `false`                   | Wait and watch logs for the parent action.             |
| `--image`                   |       | text   |                           | Image to be used in the run (format: `name=uri`).      |
| `--no-sync-local-sys-paths` |       | flag   | `false`                   | Disable synchronization of local sys.path entries.      |
| `--run-project`             |       | text   | *from config*             | Execute deployed task in this project (`deployed-task` only). |
| `--run-domain`              |       | text   | *from config*             | Execute deployed task in this domain (`deployed-task` only).  |

## `--project`, `--domain`

**`flyte run --domain <DOMAIN> --project <PROJECT> <PATH>|deployed_task <TASK_NAME>`**

You can specify `--project` and `--domain` which will override any defaults defined in your `config.yaml`:

```bash
flyte run my_example.py my_task
```

Specify a target project and domain:

```bash
flyte run --project my-project --domain development my_example.py my_task
```

## `--run-project`, `--run-domain`

**`flyte run --run-project <PROJECT> --run-domain <DOMAIN> deployed-task <TASK_REF>`**

When using the `deployed-task` subcommand, `--run-project` and `--run-domain` specify the [project-domain pair](../core-concepts/projects-and-domains) in which to *execute* the task. This lets you run a deployed task in a different project or domain than the one configured in your `config.yaml`:

```bash
flyte run --run-project prod-project --run-domain production deployed-task my_env.my_task
```

If not provided, these default to the `task.project` and `task.domain` values in your configuration file. These options only apply to the `deployed-task` subcommand and are ignored for file-based runs.

## `--local`

**`flyte run --local <PATH> <TASK_NAME>`**

The `--local` option runs tasks locally instead of submitting them to the remote Flyte backend:

```bash
flyte run --local my_example.py my_task --input "test_data"
```

Compare with remote execution:

```bash
flyte run my_example.py my_task --input "test_data"
```

### When to use local execution

- **Development and testing**: Quick iteration without deployment overhead
- **Debugging**: Full access to local debugging tools and environment
- **Resource constraints**: When remote resources are unavailable or expensive
- **Data locality**: When working with large local datasets

## `--copy-style`

**`flyte run --copy-style [loaded_modules|all|none] <PATH> <TASK_NAME>`**

The `--copy-style` option controls code bundling for remote execution.
This applies to the ephemeral preparation step of the `flyte run` command and works similarly to `flyte deploy`:

Smart bundling (default) — includes only imported project modules:

```bash
flyte run --copy-style loaded_modules my_example.py my_task
```

Include all project files:

```bash
flyte run --copy-style all my_example.py my_task
```

No code bundling (task must be pre-deployed):

```bash
flyte run --copy-style none deployed_task my_deployed_task
```

### Copy style options

- **`loaded_modules` (default)**: Bundles only imported Python modules from your project
- **`all`**: Includes all files in the project directory
- **`none`**: No bundling; requires permanently deployed tasks

## `--root-dir`

**`flyte run --root-dir <DIRECTORY> <PATH> <TASK_NAME>`**

Override the source directory for code bundling and import resolution:

Run from a monorepo root with a specific root directory:

```bash
flyte run --root-dir ./services/ml ./services/ml/my_example.py my_task
```

Handle cross-directory imports:

```bash
flyte run --root-dir .. my_example.py my_workflow
```
This applies to the ephemeral preparation step of the `flyte run` command.
It works identically to the `flyte deploy` command's `--root-dir` option.

## `--raw-data-path`

**`flyte run --raw-data-path <PATH> <SOURCE> <TASK_NAME>`**

Override the default output location for offloaded data types (large objects, DataFrames, etc.):

Use a custom S3 location for large outputs:

```bash
flyte run --raw-data-path s3://my-bucket/custom-path/ my_example.py process_large_data
```

Use a local directory for development:

```bash
flyte run --local --raw-data-path ./output/ my_example.py my_task
```

### Use cases

- **Custom storage locations**: Direct outputs to specific S3 buckets or paths
- **Cost optimization**: Use cheaper storage tiers for temporary data
- **Access control**: Ensure outputs go to locations with appropriate permissions
- **Local development**: Store large outputs locally when testing

## `--service-account`

**`flyte run --service-account <ACCOUNT_NAME> <PATH> <TASK_NAME>`**

Specify a Kubernetes service account for task execution:

```bash
flyte run --service-account ml-service-account my_example.py train_model
flyte run --service-account data-reader-sa my_example.py load_data
```

### Use cases

- **Cloud resource access**: Service accounts with permissions for S3, GCS, etc.
- **Security isolation**: Different service accounts for different workload types
- **Compliance requirements**: Enforcing specific identity and access policies

## `--name`

**`flyte run --name <EXECUTION_NAME> <PATH> <TASK_NAME>`**

Provide a custom name for the execution run:

```bash
flyte run --name "daily-training-run-2024-12-02" my_example.py train_model
flyte run --name "experiment-lr-0.01-batch-32" my_example.py hyperparameter_sweep
```

### Benefits of custom names

- **Easy identification**: Find specific runs in the Flyte console
- **Experiment tracking**: Include key parameters or dates in names
- **Automation**: Programmatically generate meaningful names for scheduled runs

## `--follow`

**`flyte run --follow <PATH> <TASK_NAME>`**

Wait and watch logs for the execution in real-time:

```bash
flyte run --follow my_example.py long_running_task
```

Combine with other options:

```bash
flyte run --follow --name "training-session" my_example.py train_model
```

### Behavior

- **Log streaming**: Real-time output from task execution
- **Blocking execution**: Command waits until task completes
- **Exit codes**: Returns appropriate exit code based on task success/failure

## `--image`

**`flyte run --image <IMAGE_MAPPING> <PATH> <TASK_NAME>`**

Override container images during ephemeral preparation, same as the equivalent `flyte deploy` option:

Override a specific named image:

```bash
flyte run --image gpu=ghcr.io/org/gpu:v2.1 my_example.py gpu_task
```

Override the default image:

```bash
flyte run --image ghcr.io/org/custom:latest my_example.py my_task
```

Multiple image overrides:

```bash
flyte run \
  --image base=ghcr.io/org/base:v1.0 \
  --image gpu=ghcr.io/org/gpu:v2.0 \
  my_example.py multi_env_workflow
```

### Image mapping formats

- **Named mapping**: `name=uri` overrides images created with `Image.from_ref_name("name")`
- **Default mapping**: `uri` overrides the default "auto" image
- **Multiple mappings**: Use multiple `--image` flags for different image references

## `--no-sync-local-sys-paths`

**`flyte run --no-sync-local-sys-paths <PATH> <TASK_NAME>`**

Disable synchronization of local `sys.path` entries to the remote execution environment during ephemeral preparation.
Identical to the `flyte deploy` command's `--no-sync-local-sys-paths` option:

```bash
flyte run --no-sync-local-sys-paths my_example.py my_task
```

This advanced option works identically to the deploy command equivalent, useful for:
- **Container isolation**: Prevent local development paths from affecting remote execution
- **Custom environments**: When containers have pre-configured Python paths
- **Security**: Avoiding exposure of local directory structures

## Task argument passing

A task's inputs are passed **after** the task name. On the CLI every input is a **named option**, `--<input_name> <value>`, where `<input_name>` is the exact parameter name in the task's function signature:

```bash
flyte run my_file.py my_task --name "World" --count 5 --verbose
```

The equivalent SDK call passes the same inputs as keyword arguments:

```python
result = flyte.run(my_task, name="World", count=5, verbose=True)
```

A few rules apply to every input:

- **The option name matches the parameter name exactly, including underscores.** A parameter `event_time` is passed as `--event_time` (not `--event-time`).
- **Quote any value that contains spaces**, for example `--name "Ada Lovelace"`.
- **An input with a default is optional**; an input with no default is required.

### Passing inputs by type

Flyte parses each value according to the parameter's Python type. The type-specific syntax is summarized below and detailed in the following sections.

| Python type | CLI syntax | Example |
|---|---|---|
| `str` | Plain text (quote if it contains spaces) | `--name "Ada"` |
| `int` | Integer literal | `--count 5` |
| `float` | Decimal literal | `--rate 0.01` |
| `bool` | A flag (see [Boolean inputs](#boolean-inputs)) | `--verbose` |
| `datetime.datetime` / `datetime.date` | ISO 8601, `now`, `today`, or a relative expression | `--start 2024-01-15` |
| `datetime.timedelta` | ISO 8601 duration or a human-readable duration | `--timeout PT2H30M` |
| `enum.Enum` | The **member name** (case-sensitive) | `--color RED` |
| `list` / `dict` | A JSON literal (or a path to a `.json`/`.yaml` file) | `--nums '[1, 2, 3]'` |
| dataclass / Pydantic model / `TypedDict` / `NamedTuple` | A JSON literal (or a path to a `.json`/`.yaml` file) | `--config '{"lr": 0.01}'` |
| `flyte.io.File` / `flyte.io.Dir` | A local path or a remote URI | `--data ./input.csv` |
| `flyte.io.DataFrame` | A path to a `.parquet` or `.csv` file (local or remote) | `--df ./data.parquet` |

The `now`/`today`, relative-datetime, human-duration, and JSON-string forms are **CLI conveniences**. When you call `flyte.run()` programmatically, pass the corresponding native Python objects instead (a `datetime.datetime`, a `datetime.timedelta`, a dataclass instance, and so on).

### Boolean inputs

A `bool` input is a **flag**, not a value-taking option — do not write `--debug true`.

- If the parameter defaults to `False` (or has no default), pass the bare flag to set it `True`, and omit it to leave it `False`:

  ```bash
  flyte run my_file.py my_task --verbose      # verbose=True
  flyte run my_file.py my_task                # verbose=False
  ```

- If the parameter defaults to `True`, Flyte also registers a `--no-` form so you can turn it off:

  ```bash
  flyte run my_file.py my_task --no-cache     # cache=False
  ```

### Datetime and duration inputs

A `datetime.datetime` (or `datetime.date`) input accepts an ISO 8601 timestamp, the keywords `now` or `today`, or a **relative expression** of the form `<base> <+|-> <ISO 8601 duration>` (the spaces around the sign are required, so quote the value):

```bash
flyte run my_file.py my_task --start 2024-01-15
flyte run my_file.py my_task --start "2024-01-15T13:30:00"
flyte run my_file.py my_task --start now
flyte run my_file.py my_task --start "now - P1D"        # 24 hours ago
flyte run my_file.py my_task --start "today + P1DT2H"   # tomorrow, 02:00
```

A `datetime.timedelta` input accepts an ISO 8601 duration or a human-readable duration (`<minutes>:<seconds>`, or a value with a unit such as `days`, `hours`, `minutes`, `seconds`):

```bash
flyte run my_file.py my_task --timeout P1DT2H30M    # 1 day, 2 hours, 30 minutes
flyte run my_file.py my_task --timeout "10 days"
flyte run my_file.py my_task --timeout "1 minute"
flyte run my_file.py my_task --timeout 1:24         # 1 minute, 24 seconds
```

### Enum inputs

For an `enum.Enum` input, pass the **name** of the member (case-sensitive), not its value:

```python
# my_file.py
import enum

class Color(enum.Enum):
    RED = "red"
    GREEN = "green"
```

```bash
flyte run my_file.py my_task --color RED
```

### List, dict, dataclass, and other structured inputs

Collections (`list`, `dict`) and structured types (dataclasses, Pydantic models, `TypedDict`, `NamedTuple`) are passed as a **JSON literal**:

```bash
flyte run my_file.py my_task --nums '[1, 2, 3]'
flyte run my_file.py my_task --mapping '{"a": 1, "b": 2}'
flyte run my_file.py my_task --config '{"lr": 0.01, "epochs": 5}'
```

For anything larger than a one-liner, pass a **path to a `.json` or `.yaml` file** instead — Flyte reads and parses the file:

```bash
flyte run my_file.py my_task --config ./config.yaml
```

### File, directory, and dataframe inputs

A `flyte.io.File`, `flyte.io.Dir`, or `flyte.io.DataFrame` input accepts either a **local path** or a **remote URI**. A local path is uploaded to the run's data store before execution; a remote URI (for example `s3://…` or `gs://…`) is used as-is. Under `--local`, the local path is used directly without uploading:

```bash
flyte run my_file.py my_task --data ./input.csv
flyte run my_file.py my_task --data s3://my-bucket/input.csv
flyte run my_file.py my_task --df ./data.parquet
```

### Optional inputs

An `Optional[...]` input (or any input with a default) is not required — omit the option to leave it at its default:

```bash
flyte run my_file.py my_task --count 5      # `name` omitted, uses its default
```

## Positional arguments

**The CLI has no positional form for task inputs.** `flyte run` always passes inputs as named options (`--<input_name>`), as shown above — there is no `flyte run my_file.py my_task "World" 5` form.

Positional arguments apply only when you invoke a task **programmatically**. `flyte.run()`, and a direct (native) call to one task from inside another, accept positional arguments and map them to the task's parameters in signature order:

```python
# Positional and keyword forms are equivalent here:
flyte.run(greet, "Good morning!")
flyte.run(greet, message="Good morning!")
```

Two caveats apply:

- **Deployed tasks are keyword-only.** A task retrieved with `flyte.remote.Task.get()` (or run via the `deployed-task` CLI subcommand) does **not** accept positional arguments — pass its inputs by keyword (or, on the CLI, as `--<input_name>` options).
- **Don't provide the same input both positionally and by keyword.**

## SDK options

The core `flyte run` functionality is also available programmatically through the `flyte.run()` function.
For SDK-level configuration of all run parameters (storage, caching, identity, logging, and more),
see [Run context](./run-context).
