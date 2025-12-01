---
title: Deploy command options
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Deploy command options

The `flyte deploy` command provides extensive configuration options:

**`flyte deploy [OPTIONS] <PATH> [TASK_ENV_VARIABLE]`**

| Option                      | Short | Type   | Default                   | Description                                       |
|-----------------------------|-------|--------|---------------------------|---------------------------------------------------|
| `--project`                 | `-p`  | text   | *from config*             | Project to deploy to                              |
| `--domain`                  | `-d`  | text   | *from config*             | Domain to deploy to                               |
| `--config`                  | `-c`  | path   | *from default location*   | Path to configuration file                        |
| `--version`                 |       | text   | *auto-generated*          | Explicit version tag for deployment               |
| `--dry-run`/`--dryrun`      |       | flag   | `false`                   | Preview deployment without executing              |
| `--all`                     |       | flag   | `false`                   | Deploy all environments in specified path         |
| `--recursive`               | `-r`  | flag   | `false`                   | Deploy environments recursively in subdirectories |
| `--copy-style`              |       | choice | `loaded_modules|all|none` | Code bundling strategy                            |
| `--root-dir`                |       | path   | *current dir*             | Override source root directory                    |
| `--image`                   |       | text   |                           | Image URI mappings (format: `name=uri`)           |
| `--ignore-load-errors`      | `-i`  | flag   | `false`                   | Continue deployment despite module load failures  |
| `--no-sync-local-sys-paths` |       | flag   | `false`                   | Disable local `sys.path` synchronization          |

## Common options

### `--project`, `--domain`, `--config`

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

### `--version`

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

### `--dry-run`

**`flyte deploy --dry-run <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

The `--dry-run` option allows you to preview what would be deployed without actually performing the deployment:

```bash
# Preview what would be deployed
flyte deploy --dry-run my_app.py env
```

## TaskEnvironment discovery options

### `--all` and `--recursive`

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

## Code bundling options

### `--copy-style`

**`flyte deploy --copy_style [loaded_modules|all|none] <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

The `--copy-style` option controls what gets packaged:

**`--copy-style loaded_modules` (default):**

```bash
flyte deploy --copy-style loaded_modules my_app.py env
```

- **Includes**: Only imported Python modules from your project
- **Excludes**: Site-packages, system modules, Flyte SDK
- **Best for**: Most projects (optimal size and speed)

**`--copy-style all`:**

```bash
flyte deploy --copy-style all my_app.py env
```

- **Includes**: All files in project directory
- **Best for**: Projects with dynamic imports or data files

**`--copy-style none`:**

```bash
flyte deploy --copy-style none --version v1.0.0 my_app.py env
```

- **Requires**: Explicit version parameter
- **Best for**: Pre-built container images with baked-in code

### `--root-dir`

**`flyte deploy --root-dir <DIRECTORY> <SOURCE_FILE> <TASK_ENV_VARIABLE>`**

The `--root-dir` option overrides the default source directory that Flyte uses as the base for code bundling and import resolution.
This is particularly useful for monorepos and projects with complex directory structures.

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

## SDK deployment options

The core deployment functionality is available programmatically through the `flyte.deploy()` function, though some CLI-specific options are not applicable:

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def process_data(data: str) -> str:
    return f"Processed: {data}"

if __name__ == "__main__":
    flyte.init_from_config()

    # Comprehensive deployment configuration
    deployment = flyte.deploy(
        env,                          # Environment to deploy
        dryrun=False,                 # Set to True for dry run
        version="v1.2.0",             # Explicit version tag
        copy_style="loaded_modules"   # Code bundling strategy
    )
    print(f"Deployment successful: {deployment[0].summary_repr()}")
```
