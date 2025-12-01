---
title: How task deployment works
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# How task deployment works

In this section, we will take a deep dive into how the `flyte deploy` command and the `flyte.deploy()` SDK function work under the hood to deploy tasks to your Flyte backend.

## Overview of the deployment process

When you run perform a deployment here's what happens:

### 1. Module loading and task environment discovery

In the first step, Flyte determines which files to load in order to search for task environments, based on the command line options provided:

**Single file (default):**

```bash
flyte deploy my_example.py env
```

- The file `my_example.py` is executed,
- All declared `TaskEnvironment` objects in the file are instantiated,
  but only the one assigned to the variable `env` is selected for deployment.

**`--all` Option:**

```bash
flyte deploy --all my_app.py
```
- The file `my_example.py` is executed,
- All declared `TaskEnvironment` objects in the file are instantiated and selected for deployment.
- No specific variable name is required.

**`--recursive` Option:**
```bash
flyte deploy --recursive ./directory
```

- The directory is recursively traveresed and all Python files are executed and all `TaskEnvironment` objects are isntantiated.
- All `TaskEnvironment` objects across all files are selected for deployment.

### 2. Task Analysis and Serialization

- For every task environment selected for deployment, all of its tasks are identified.
- Task metadata is extracted: parameter types, return types, and resource requirements.
- Each task is serialized into a Flyte `TaskTemplate`.
- Dependency graphs between environments are built (see below).

### 3. Task Environment Dependency Resolution

In many cases, a task in one task environment may invoke a task in another environment, establishing a dependency between the two environments. For example, if `env_a` has a task that calls a task in `env_b`, then `env_a` depends on `env_b`. This means that when deploying `env_a`, `env_b` must also be deployed to ensure that all tasks can be executed correctly.

To handle this, `TaskEnvironment`s can declare dependencies on other `TaskEnvironment`s using the `depends_on` parameter. During deployment, the system performs the following steps to resolve these dependencies:

1. Starting with specified environment(s)
2. Recursively discovering all transitive dependencies
3. Including all dependencies in the deployment plan
4. Processing dependencies depth-first to ensure correct order

```python
# Define environments with dependencies
prep_env = flyte.TaskEnvironment(name="preprocessing")
ml_env = flyte.TaskEnvironment(name="ml_training", depends_on=[prep_env])
viz_env = flyte.TaskEnvironment(name="visualization", depends_on=[ml_env])

# Deploy only viz_env - automatically includes ml_env and prep_env
deployment = flyte.deploy(viz_env, version="v2.0.0")

# Or deploy multiple environments explicitly
deployment = flyte.deploy(data_env, ml_env, viz_env, version="v2.0.0")
```

For detailed information about working with multiple environments, see [Multiple Environments](../task-configuration/multiple-environments).

### 4. Code bundle creation AND Upload

Once the task environments and their dependencies are resolved, Flyte proceeds to package your code into a bundle based on the `copy_style` option:

**`"loaded_modules"` (default):**
This is the smart bundling approach that analyzes which Python modules were actually imported during the task environment discovery phase.
It examines the runtime module registry (`sys.modules`) and includes only those modules that meet specific criteria: they must have source files located within your project directory (not in system locations like `site-packages`), and they must not be part of the Flyte SDK itself.
This selective approach results in smaller, faster-to-upload bundles that contain exactly the code needed to run your tasks, making it ideal for most development and production scenarios.

**`"all"`:**
This comprehensive bundling strategy takes a directory-walking approach, recursively traversing your entire project directory and including every file it encounters.
Unlike the smart bundling that only includes imported Python modules, this method captures all project files regardless of whether they were imported during discovery.
This is particularly useful for projects that use dynamic imports, load configuration files or data assets at runtime, or have dependencies that aren't captured through normal Python import mechanisms.

**`"none"`:**
This option completely skips code bundle creation, meaning no source code is packaged or uploaded to cloud storage.
When using this approach, you must provide an explicit version parameter since there's no code bundle to generate a version from.
This strategy is designed for scenarios where your code is already baked into custom container images, eliminating the need for separate code injection during task execution.
It results in the fastest deployment times but requires more complex image management workflows.

**Root Directory for Bundling:**
By default, Flyte uses your current working directory as the root for code bundling. You can override this with `--root-dir` to specify a different base directory - particularly useful for monorepos or when deploying from subdirectories. This affects all copy styles: `loaded_modules` will look for imported modules relative to the root directory, `all` will walk the directory tree starting from the root, and the root directory setting works with any copy style. See the [`--root-dir` option](#--root-dir) for detailed usage examples.

After the code bundle is created (if applicable), it is uploaded to a cloud storage location (like S3 or GCS) accessible by your Flyte backend. It is now ready to be run.

### 5. Image Building (if needed)

If your `TaskEnvironment` specifies [custom images](../task-configuration/container-images), Flyte builds and pushes container images before deploying tasks. The build process varies based on your configuration and backend type:

**Local Image Building:**
When `image.builder` is set to `local` in [your `config.yaml`](../getting-started/local-setup), images are built on your local machine using Docker. This approach:
- Requires Docker to be installed and running on your development machine
- Uses Docker BuildKit to build images from generated Dockerfiles or your custom Dockerfile
- Pushes built images to the container registry specified in your `Image` configuration
- Is the only option available for Flyte OSS instances

**Remote Image Building:**
When `image.builder` is set to `remote` in [your `config.yaml`](../getting-started/local-setup), images are built on cloud infrastructure. This approach:
- Builds images using Union's ImageBuilder service (currently only available for Union backends, not OSS Flyte)
- Requires no local Docker installation or configuration
- Can push to Union's internal registry or external registries you specify
- Provides faster, more consistent builds by leveraging cloud resources

> [!NOTE]
> Remote building is currently exclusive to Union backends - OSS Flyte installations must use `local`

#### Understanding Option Relationships

**Environment Discovery vs. Code Bundling:**
- `--recursive`/`--all` control **which files are loaded** to find environments
- `--copy-style` controls **what code gets packaged** for deployment
- These operate independently and can be combined freely

**Single Bundle for Multiple Environments:**
```bash
# All discovered environments share the same code bundle
flyte deploy --recursive --copy-style loaded_modules ./project
```

## Deployment options and configuration

### Command Line Options

The `flyte deploy` command provides extensive configuration options:

**`flyte deploy [OPTIONS] <PATH> [TASK_ENV_VARIABLE]`**

### Core Options

#### `--project`, `--domain`, `--config`

**`flyte deploy --domain <DOMAIN> --project <PROJECT> <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

**`flyte deploy --config <CONFIG_FILE> <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

As with all `flyte` CLI commands, you can specify `--project` and `--domain` or a new `--config` file which will override your default configuration:

```bash
# Use defaults from global configuration (default)
flyte deploy my_app.py env

# Specify target project and domain
flyte deploy --project my-project --domain development my_app.py env

# Specify a specific config file
flyte deploy --config custom-config.yaml my_app.py env
```

#### `--version`

**`flyte deploy --version <VERSION> <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

The `--version` option controls how deployed tasks are tagged and identified in the Flyte backend:

```bash
# Auto-generated version (default)
flyte deploy my_app.py env

# Explicit version
flyte deploy --version v1.0.0 my_app.py env

# Required when using copy-style none (no code bundle to generate hash from)
flyte deploy --copy-style none --version v1.0.0 my_app.py env
```

**When versions are used:**
- **Explicit versioning**: Provides human-readable task identification (e.g., `v1.0.0`, `prod-2024-12-01`)
- **Auto-generated versions**: When no version is specified, Flyte creates an MD5 hash from the code bundle, environment configuration, and image cache
- **Version requirement**: `copy-style none` mandates explicit versions since there's no code bundle to hash
- **Task referencing**: Versions enable precise task references in `flyte run deployed-task` and workflow invocations

#### `--dry-run`

**`flyte deploy --dry-run <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

The `--dry-run` option allows you to preview what would be deployed without actually performing the deployment:

```bash
# Preview what would be deployed
flyte deploy --dry-run my_app.py env
```

### Code bundling options

#### `--copy-style`

**`flyte deploy --copy_style [loaded_modules|all|none] <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

The `--copy-style` option controls what gets packaged:

**Smart Bundling (Default):**
```bash
flyte deploy --copy-style loaded_modules my_app.py env
```
- **Includes**: Only imported Python modules from your project
- **Excludes**: Site-packages, system modules, Flyte SDK
- **Best for**: Most projects (optimal size and speed)

**Comprehensive Bundling:**
```bash
flyte deploy --copy-style all my_app.py env
```
- **Includes**: All files in project directory
- **Best for**: Projects with dynamic imports or data files

**No Bundling:**
```bash
flyte deploy --copy-style none --version v1.0.0 my_app.py env
```
- **Requires**: Explicit version parameter
- **Best for**: Pre-built container images with baked-in code

### Environment Discovery Options

#### `--all` and `--recursive`

**`flyte deploy --all <SOURCE_FILE>`**

**`flyte deploy --recursive <DIRECTORY_PATH>`**

Control which environments get discovered and deployed:

**Single Environment (Default):**
```bash
# Deploy specific environment variable
flyte deploy my_app.py env
```

**All Environments in File:**
```bash
# Deploy all TaskEnvironment objects in file
flyte deploy --all my_app.py
```

**Recursive Directory Deployment:**
```bash
# Deploy all environments in directory tree
flyte deploy --recursive ./src

# Combine with comprehensive bundling
flyte deploy --recursive --copy-style all ./project
```

### Image Management Options

#### `--image`

**`flyte deploy --image <IMAGE_MAPPING> <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

The `--image` option allows you to override image URIs at deployment time without modifying your code. Format: `imagename=imageuri`

**Named Image Mappings:**
```bash
# Map specific image reference to URI
flyte deploy --image base=ghcr.io/org/base:v1.0 my_app.py env

# Multiple named image mappings
flyte deploy \
  --image base=ghcr.io/org/base:v1.0 \
  --image gpu=ghcr.io/org/gpu:v2.0 \
  my_app.py env
```

**Default Image Mapping:**
```bash
# Override default image (used when no specific image is set)
flyte deploy --image ghcr.io/org/default:latest my_app.py env
```

**How it works:**
- Named mappings (e.g., `base=URI`) override images created with `Image.from_ref_name("base")`.
- Unnamed mappings (e.g., just `URI`) override the default "auto" image.
- Multiple `--image` flags can be specified.
- Mappings are resolved during the image building phase of deployment.

#### `--root-dir`

**`flyte deploy --root-dir <DIRECTORY> <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

The `--root-dir` option overrides the default source directory that Flyte uses as the base for code bundling and import resolution. This is particularly useful for monorepos and projects with complex directory structures.

**Default Behavior (without `--root-dir`):**
- Flyte uses the current working directory as the root
- Code bundling starts from this directory
- Import paths are resolved relative to this location

**Common Use Cases:**

**Monorepo Management:**
```bash
# Deploy service from monorepo root
flyte deploy --root-dir ./services/ml ./services/ml/app.py env

# Deploy from anywhere in the monorepo
cd ./docs/
flyte deploy --root-dir ../services/ml ../services/ml/app.py env
```

**Cross-Directory Imports:**
```bash
# When workflow imports modules from sibling directories
# Project structure: project/workflows/main.py imports project/src/utils.py
cd project/workflows/
flyte deploy --root-dir .. main.py env  # Sets root to project/
```

**Working Directory Independence:**
```bash
# Deploy from any location while maintaining consistent bundling
flyte deploy --root-dir /path/to/project /path/to/project/main.py env
```

**How it Works:**

1. **Code Bundling**: Files are collected starting from `--root-dir` instead of the current working directory
2. **Import Resolution**: Python imports are resolved relative to the specified root directory
3. **Path Consistency**: Ensures the same directory structure in local and remote execution environments
4. **Dependency Packaging**: Captures all necessary modules that may be located outside the workflow file's immediate directory

**Example with Complex Project Structure:**
```
my-project/
├── services/
│   ├── ml/
│   │   └── workflows.py     # imports shared.utils
│   └── api/
└── shared/
    └── utils.py
```

```bash
# Deploy ML service workflows with access to shared utilities
flyte deploy --root-dir ./my-project ./my-project/services/ml/workflows.py env
```

This ensures that both `services/ml/` and `shared/` directories are included in the code bundle, allowing the workflow to successfully import `shared.utils` during remote execution.

### Error Handling Options

#### `--ignore-load-errors`

**`flyte deploy --ignore-load-errors <SOURCE_PATH> <TASK_ENV_VARIABLE>`**

The `--ignore-load-errors` option allows the deployment process to continue even if some modules fail to load during the environment discovery phase. This is particularly useful for large projects or monorepos where certain modules may have missing dependencies or other issues that prevent them from being imported successfully.

```bash
# Continue deployment despite module failures
flyte deploy --recursive --ignore-load-errors ./large-project
```

#### `--no-sync-local-sys-paths`

**`flyte deploy --no-sync-local-sys-paths <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

The `--no-sync-local-sys-paths` option disables the automatic synchronization of local `sys.path` entries to the remote container environment. This is an advanced option for specific deployment scenarios.

**Default Behavior (path synchronization enabled):**
- Flyte captures local `sys.path` entries that are under the root directory
- These paths are passed to the remote container via the `_F_SYS_PATH` environment variable
- At runtime, the remote container adds these paths to its `sys.path`, maintaining the same import environment

**When to disable path synchronization:**
```bash
# Disable local sys.path sync (advanced use case)
flyte deploy --no-sync-local-sys-paths my_app.py env
```

**Use cases for disabling:**
- **Custom container images**: When your container already has the correct `sys.path` configuration
- **Conflicting path structures**: When local development paths would interfere with container paths
- **Security concerns**: When you don't want to expose local development directory structures
- **Minimal environments**: When you want precise control over what gets added to the container's Python path

**How it works:**
- **Enabled (default)**: Local paths like `./my_project/utils` get synchronized and added to remote `sys.path`
- **Disabled**: Only the container's native `sys.path` is used, along with the deployed code bundle

Most users should leave path synchronization enabled unless they have specific requirements for container path isolation or are using pre-configured container environments.

## SDK Deployment Options

The core deployment functionality is available programmatically through the `flyte.deploy()` function, though some CLI-specific options are not applicable:

### Basic SDK Deployment

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def process_data(data: str) -> str:
    return f"Processed: {data}"

if __name__ == "__main__":
    flyte.init_from_config()

    # Basic deployment
    deployment = flyte.deploy(env)
```

### SDK Deployment with Options

```python
# Comprehensive deployment configuration
deployment = flyte.deploy(
    env,                          # Environment to deploy
    dryrun=False,                # Set to True for dry run
    version="v1.2.0",            # Explicit version tag
    copy_style="loaded_modules"   # Code bundling strategy
)

print(f"Deployment successful: {deployment[0].summary_repr()}")
```
