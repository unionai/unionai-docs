---
title: Run command options
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Run command options

The `flyte run` command provides the following options:

**`flyte run [OPTIONS] <PATH>|deployed_task <TASK_NAME>`**

| Option                      | Short | Type   | Default                   | Description                                            |
|-----------------------------|-------|--------|---------------------------|--------------------------------------------------------|
| `--project`                 | `-p`  | text   | *from config*             | Project to deploy to                                   |
| `--domain`                  | `-d`  | text   | *from config*             | Domain to deploy to                                    |
| `--local`                   |       | flag   | `false`                   | Run the task locally                                   |
| `--copy-style`              |       | choice | `loaded_modules|all|none` | Code bundling strategy                                 |
| `--root-dir`                |       | path   | *current dir*             | Override source root directory                         |
| `--raw-data-path`           |       | text   |                           | Override the output location for offloaded data types. |
| `--service-account`         |       | text   |                           | Kubernetes service account.                            |
| `--name`                    |       | text   |                           | Name of the run.                                       |
| `--follow`                  | `-f`  | flag   | `false`                   | Wait and watch logs for the parent action.             |
| `--image`                   |       | text   |                           | Image to be used in the run (format: `name=uri`).      |
| `--no-sync-local-sys-paths` |       | flag   | `false`                   | Disable synchronization of local sys.path entries.      |

## `--project`, `--domain`

**`flyte run --domain <DOMAIN> --project <PROJECT> <PATH>|deployed_task <TASK_NAME>`**

You can specify `--project` and `--domain` which will override any defaults defined in your `config.yaml`:

```bash
# Use defaults from default config.yaml
flyte run my_example.py my_task

# Specify target project and domain
flyte run --project my-project --domain development my_example.py my_task
```

## `--local`

**`flyte run --local <PATH> <TASK_NAME>`**

The `--local` option runs tasks locally instead of submitting them to the remote Flyte backend:

```bash
# Run task locally (default behavior when using flyte.run() without deployment)
flyte run --local my_example.py my_task --input "test_data"

# Compare with remote execution
flyte run my_example.py my_task --input "test_data"  # Runs on Flyte backend
```

### When to use local execution

- **Development and testing**: Quick iteration without deployment overhead
- **Debugging**: Full access to local debugging tools and environment
- **Resource constraints**: When remote resources are unavailable or expensive
- **Data locality**: When working with large local datasets

## `--copy-style`

**`flyte run --copy-style [loaded_modules|all|none] <PATH> <TASK_NAME>`**

The `--copy-style` option controls code bundling for remote execution.
This applies to the deployment step of the `flyte run` command and works the same way as it does for `flyte deploy`:

```bash
# Smart bundling (default) - includes only imported project modules
flyte run --copy-style loaded_modules my_example.py my_task

# Include all project files
flyte run --copy-style all my_example.py my_task

# No code bundling (task must be pre-deployed)
flyte run --copy-style none deployed_task my_deployed_task
```

### Copy style options

- **`loaded_modules` (default)**: Bundles only imported Python modules from your project
- **`all`**: Includes all files in the project directory
- **`none`**: No bundling; requires pre-deployed tasks

## `--root-dir`

**`flyte run --root-dir <DIRECTORY> <PATH> <TASK_NAME>`**

Override the source directory for code bundling and import resolution:

```bash
# Run from monorepo root with specific root directory
flyte run --root-dir ./services/ml ./services/ml/my_example.py my_task

# Handle cross-directory imports
flyte run --root-dir .. my_example.py my_workflow  # When my_example.py imports sibling directories
```
This applies to the deployment step of the `flyte run` command.
It works identically to the `flyte deploy` command's `--root-dir` option.

## `--raw-data-path`

**`flyte run --raw-data-path <PATH> <SOURCE> <TASK_NAME>`**

Override the default output location for offloaded data types (large objects, DataFrames, etc.):

```bash
# Use custom S3 location for large outputs
flyte run --raw-data-path s3://my-bucket/custom-path/ my_example.py process_large_data

# Use local directory for development
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
# Run with specific service account for cloud resource access
flyte run --service-account ml-service-account my_example.py train_model

# Use service account with specific permissions
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
# Named execution for easy identification
flyte run --name "daily-training-run-2024-12-02" my_example.py train_model

# Include experiment parameters in name
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
# Stream logs to console and wait for completion
flyte run --follow my_example.py long_running_task

# Combine with other options
flyte run --follow --name "training-session" my_example.py train_model
```

### Behavior

- **Log streaming**: Real-time output from task execution
- **Blocking execution**: Command waits until task completes
- **Exit codes**: Returns appropriate exit code based on task success/failure

## `--image`

**`flyte run --image <IMAGE_MAPPING> <PATH> <TASK_NAME>`**

Override container images on deploy, same as the equivalent `flyte deploy` option:

```bash
# Override specific named image
flyte run --image gpu=ghcr.io/org/gpu:v2.1 my_example.py gpu_task

# Override default image
flyte run --image ghcr.io/org/custom:latest my_example.py my_task

# Multiple image overrides
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

Disable synchronization of local `sys.path` entries to the remote execution environment on deploy.
Identical to the `flyte deploy` command's `--no-sync-local-sys-paths` option:

```bash
# Disable path synchronization for clean container environment
flyte run --no-sync-local-sys-paths my_example.py my_task
```

This advanced option works identically to the deploy command equivalent, useful for:
- **Container isolation**: Prevent local development paths from affecting remote execution
- **Custom environments**: When containers have pre-configured Python paths
- **Security**: Avoiding exposure of local directory structures

## Task argument passing

Arguments are passed directly as function parameters:

```bash
# CLI: Arguments as flags
flyte run my_file.py my_task --name "World" --count 5 --debug true

# SDK: Arguments as function parameters
result = flyte.run(my_task, name="World", count=5, debug=True)
```

## SDK options

The core `flyte run` functionality is also available programmatically through the `flyte.run()` function, with extensive configuration options available via the `flyte.with_runcontext()` function:

```python
# Run context configuration
result = flyte.with_runcontext(
    mode="remote",              # "remote", "local"
    copy_style="loaded_modules", # Code bundling strategy
    version="v1.0.0",           # Deployment version
    dry_run=False,              # Preview mode
).run(my_task, name="World")
```
