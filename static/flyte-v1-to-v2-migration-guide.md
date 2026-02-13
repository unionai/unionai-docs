# Flyte v1 to v2 Migration Context Guide

This document provides comprehensive context for migrating Flyte workflows from v1 (flytekit) to v2 (flyte SDK). Use this as a reference when assisting with migration tasks.

---

## Table of Contents

1. [Philosophy and Architecture Changes](#1-philosophy-and-architecture-changes)
2. [Package Imports](#2-package-imports)
3. [ImageSpec to flyte.Image Migration](#3-imagespec-to-flyteimage-migration)
4. [Configuration Files](#4-configuration-files)
5. [CLI Commands](#5-cli-commands)
6. [Task and Workflow Migration](#6-task-and-workflow-migration)
7. [Secrets Migration](#7-secrets-migration)
8. [Resources Migration](#8-resources-migration)
9. [Caching Migration](#9-caching-migration)
10. [map_task to flyte.map and Async Loops](#10-map_task-to-flytemap-and-async-loops)
11. [Sync and Async Tasks](#11-sync-and-async-tasks)
12. [Triggers and Scheduling](#12-triggers-and-scheduling)
13. [Dynamic Workflows](#13-dynamic-workflows)
14. [Complete Migration Examples](#14-complete-migration-examples)
15. [Common Gotchas](#15-common-gotchas)

---

## 1. Philosophy and Architecture Changes

### Key Paradigm Shifts

| Concept | v1 (flytekit) | v2 (flyte) |
|---------|--------------|------------|
| Workflow Definition | `@workflow` decorator (DSL-constrained) | Tasks calling tasks (pure Python) |
| Task Configuration | Per-task decorator parameters | `TaskEnvironment` (shared config) |
| Parallelism | `map_task()` function | `flyte.map()` or `asyncio.gather()` |
| Conditionals | `flytekit.conditional()` | Native Python `if/else` |
| Error Handling | Decorator-based retries | Python `try/except` + retries |
| Execution Model | Static DAG compilation | Dynamic pure Python execution |

### What v2 Eliminates

- **`@workflow` decorator**: No longer exists - workflows are just tasks that call other tasks
- **`@dynamic` decorator**: No longer needed - all tasks can have dynamic behavior
- **DSL constraints**: No more restrictions on what Python constructs you can use
- **Separate workflow/task execution contexts**: Everything runs as a task

### What v2 Introduces

- **`TaskEnvironment`**: Centralized configuration for groups of tasks
- **Native async support**: First-class `async/await` with distributed execution
- **`flyte.map()`**: Simplified parallel execution with generator support
- **`Trigger`**: Task-based scheduling (replaces LaunchPlan schedules)
- **Pure Python workflows**: Full Python flexibility in orchestration logic

---

## 2. Package Imports

### Basic Import Changes

```python
# v1 imports
import flytekit
from flytekit import task, workflow, dynamic, map_task
from flytekit import ImageSpec, Resources, Secret
from flytekit import current_context, LaunchPlan, CronSchedule

# v2 imports
import flyte
from flyte import TaskEnvironment, Resources, Secret
from flyte import Image, Trigger, Cron
```

### Import Mapping Table

| v1 Import | v2 Import | Notes |
|-----------|-----------|-------|
| `flytekit.task` | `env.task` | Decorator from TaskEnvironment |
| `flytekit.workflow` | `env.task` | Workflows are now tasks |
| `flytekit.dynamic` | `env.task` | All tasks can be dynamic |
| `flytekit.map_task` | `flyte.map` / `asyncio.gather` | Different API |
| `flytekit.ImageSpec` | `flyte.Image` | Different API |
| `flytekit.Resources` | `flyte.Resources` | Similar API |
| `flytekit.Secret` | `flyte.Secret` | Different access pattern |
| `flytekit.current_context()` | `flyte.ctx()` | Different API |
| `flytekit.LaunchPlan` | `flyte.Trigger` | Different concept |
| `flytekit.CronSchedule` | `flyte.Cron` | Used with Trigger |
| `flytekit.conditional` | Native `if/else` | No longer needed |

---

## 3. ImageSpec to flyte.Image Migration

### Overview

v1's `ImageSpec` is replaced by v2's `flyte.Image` with a fluent builder API.

### Basic Migration

```python
# v1: ImageSpec
from flytekit import ImageSpec

image_spec = ImageSpec(
    name="my-image",
    registry="ghcr.io/myorg",
    python_version="3.11",
    packages=["pandas", "numpy"],
    apt_packages=["curl", "git"],
    env={"MY_VAR": "value"},
)

@task(container_image=image_spec)
def my_task(): ...

# v2: flyte.Image
from flyte import Image, TaskEnvironment

image = (
    Image.from_debian_base(
        name="my-image",
        registry="ghcr.io/myorg",
        python_version=(3, 11),
    )
    .with_pip_packages("pandas", "numpy")
    .with_apt_packages("curl", "git")
    .with_env_vars({"MY_VAR": "value"})
)

env = TaskEnvironment(name="my_env", image=image)

@env.task
def my_task(): ...
```

### Image Constructor Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| `Image.from_debian_base()` | Start from Flyte's Debian base | Most common, includes Flyte SDK |
| `Image.from_base(image_uri)` | Start from any existing image | Custom base images |
| `Image.from_dockerfile(path)` | Build from Dockerfile | Complex custom builds |
| `Image.from_uv_script(path)` | Build from UV script | UV-based projects |

### Image Builder Methods (Chainable)

```python
image = (
    Image.from_debian_base(
        python_version=(3, 12),
        registry="ghcr.io/myorg",
        name="my-image",
        # registry_secret="my-secret",  # For private registries
    )
    # Python packages
    .with_pip_packages("pandas", "numpy>=1.24.0", pre=True)
    .with_requirements(Path("requirements.txt"))
    .with_uv_project(Path("pyproject.toml"))
    .with_poetry_project(Path("pyproject.toml"))

    # System packages
    .with_apt_packages("curl", "git", "build-essential")

    # Custom commands
    .with_commands([
        "mkdir -p /app/data",
        "chmod +x /app/scripts/*.sh",
    ])

    # Files
    .with_source_file(Path("config.yaml"), dst="/app/config.yaml")
    .with_source_folder(Path("./src"), dst="/app/src")
    .with_dockerignore(Path(".dockerignore"))

    # Environment
    .with_env_vars({"LOG_LEVEL": "INFO", "WORKERS": "4"})
    .with_workdir("/app")
)
```

### Builder Configuration (Local vs Remote)

v2 supports two build modes:

**Local Builder** (default):
- Builds using local Docker
- Pushes to registry
- Requires: Docker installed, authenticated to registry

**Remote Builder** (Union instances):
- Builds on Union's ImageBuilder
- No local Docker required
- Faster in CI/CD

```yaml
# In config file (~/.flyte/config.yaml or specified via --config)
image:
  builder: local  # or "remote"
```

```python
# Or via code
flyte.init(image_builder="local")  # or "remote" for local runs
flyte.init_from_config(image_builder="local")  # or "remote" for remote remote
```

### ImageSpec to Image Parameter Mapping

| v1 ImageSpec | v2 Image | Notes |
|--------------|----------|-------|
| `name` | `name` (in constructor) | Same |
| `registry` | `registry` (in constructor) | Same |
| `python_version` | `python_version` (tuple) | `"3.11"` → `(3, 11)` |
| `packages` | `.with_pip_packages()` | Method instead of param |
| `apt_packages` | `.with_apt_packages()` | Method instead of param |
| `conda_packages` | N/A | Use micromamba or custom base |
| `requirements` | `.with_requirements()` | Supports txt, poetry.lock, uv.lock |
| `env` | `.with_env_vars()` | Method instead of param |
| `commands` | `.with_commands()` | Method instead of param |
| `copy` | `.with_source_file/folder()` | More explicit methods |
| `source_root` | `.with_source_folder()` | Method instead of param |
| `pip_index` | `index_url` param in `.with_pip_packages()` | Moved to method |
| `pip_extra_index_url` | `extra_index_urls` param | Moved to method |
| `base_image` | `Image.from_base()` | Different constructor |
| `builder` | Config file or `flyte.init()` | Global setting |
| `platform` | `platform` (in constructor) | Tuple: `("linux/amd64", "linux/arm64")` |

### Private Registry with Secrets

```python
# v1
image_spec = ImageSpec(
    registry="private.registry.com",
    registry_config="/path/to/config.json",
)

# v2
# First create the secret:
# flyte create secret --type image_pull my-registry-secret --from-file ~/.docker/config.json

image = Image.from_debian_base(
    registry="private.registry.com",
    name="my-image",
    registry_secret="my-registry-secret",  # Or Secret object
)
```

---

## 4. Configuration Files

### Config File Location

| Version | Default Location | Environment Variable |
|---------|-----------------|---------------------|
| v1 | `~/.flyte/config.yaml` | `FLYTECTL_CONFIG` |
| v2 | `~/.flyte/config.yaml` | `FLYTE_CONFIG` |

### v1 Config Format (YAML)

```yaml
union:
  connection:
    host: dns:///your-cluster.hosted.unionai.cloud
    insecure: false
  auth:
    type: Pkce
admin:
  endpoint: dns:///your-cluster.hosted.unionai.cloud
  insecure: false
  authType: Pkce
```

### v2 Config Format (YAML)

```yaml
admin:
  endpoint: dns:///your-cluster.hosted.unionai.cloud

image:
  builder: remote  # or "local"

task:
  domain: development
  org: your-org
  project: your-project
```

### Key Config Differences

| Setting | v1 Location | v2 Location |
|---------|-------------|-------------|
| Endpoint | `admin.endpoint` or `union.connection.host` | `admin.endpoint` |
| Auth type | `admin.authType` or `union.auth.type` | Generally auto-detected (PKCE default) |
| Project | CLI flag `-p` | `task.project` (can set default) |
| Domain | CLI flag `-d` | `task.domain` (can set default) |
| Organization | CLI flag `--org` | `task.org` (can set default) |
| Image builder | N/A | `image.builder` (`local` or `remote`) |

### Specifying Config via CLI

```bash
# v1
pyflyte --config ~/.flyte/config.yaml run ...

# v2
flyte --config ~/.flyte/config.yaml run ...
flyte -c ~/.flyte/config.yaml run ...
```

### Specifying Config in Code

```python
# v2
import flyte

# From config file
flyte.init_from_config()  # Auto-discovers config
flyte.init_from_config("path/to/config.yaml")  # Explicit path

# Programmatic configuration
flyte.init(
    endpoint="flyte.example.com",
    insecure=False,
    project="my-project",
    domain="development",
)
```

---

## 5. CLI Commands

### Command Mapping

| v1 Command | v2 Command | Notes |
|------------|------------|-------|
| `pyflyte run` | `flyte run` | Similar but different flags |
| `pyflyte run --remote` | `flyte run` | Remote is default in v2 |
| `pyflyte run` (no --remote) | `flyte run --local` | Local execution |
| `pyflyte register` | `flyte deploy` | Different concept |
| `pyflyte package` | N/A | Not needed in v2 |
| `pyflyte serialize` | N/A | Not needed in v2 |

### Running Tasks

```bash
# v1: Run locally
pyflyte run my_module.py my_workflow --arg1 value1

# v1: Run remotely
pyflyte --config config.yaml run --remote my_module.py my_workflow --arg1 value1

# v2: Run remotely (default)
flyte run my_module.py my_task --arg1 value1

# v2: Run locally
flyte run --local my_module.py my_task --arg1 value1

# v2: With explicit config
flyte --config config.yaml run my_module.py my_task --arg1 value1
```

### Key CLI Flag Differences

| v1 Flag | v2 Flag | Notes |
|---------|---------|-------|
| `--remote` | (default) | Remote is default in v2 |
| `--copy-all` | `--copy-style all` | File copying |
| N/A | `--copy-style loaded_modules` | Default: only imported modules |
| N/A | `--copy-style none` | Don't copy files |
| `-p, --project` | `--project` | Same |
| `-d, --domain` | `--domain` | Same |
| `-i, --image` | `--image` | Same format |
| N/A | `--follow, -f` | Follow execution logs |

### Deploying/Registering

```bash
# v1: Register workflows
pyflyte register my_module.py -p my-project -d development

# v2: Deploy task environments
flyte deploy my_module.py my_env --project my-project --domain development

# v2: Deploy all environments in file
flyte deploy --all my_module.py

# v2: Deploy with version
flyte deploy --version v1.0.0 my_module.py my_env

# v2: Recursive deployment
flyte deploy --recursive --all ./src

# v2: Dry run (preview)
flyte deploy --dry-run my_module.py my_env
```

### Running Deployed Tasks

```bash
# v2: Run a deployed task
flyte run deployed-task my_env.my_task --arg1 value1

# v2: Run specific version
flyte run deployed-task my_env.my_task:v1.0.0 --arg1 value1
```

### Complete v2 CLI Options

```bash
# Global options
flyte --endpoint <URL>           # Override endpoint
flyte --config <PATH>            # Config file path
flyte --org <TEXT>               # Organization
flyte -v, --verbose              # Verbose output (can repeat: -vvv)
flyte --output-format [table|json]  # Output format

# Run command options
flyte run [OPTIONS] <file> <task> [TASK_ARGS]
  --local                        # Run locally
  --project <TEXT>               # Project
  --domain <TEXT>                # Domain
  --copy-style [loaded_modules|all|none]  # File copying
  --root-dir <PATH>              # Source root directory
  --follow, -f                   # Follow logs
  --image [NAME=]URI             # Image override
  --name <TEXT>                  # Execution name
  --service-account <TEXT>       # K8s service account

# Deploy command options
flyte deploy [OPTIONS] <file> [ENV_NAME]
  --project <TEXT>               # Project
  --domain <TEXT>                # Domain
  --version <TEXT>               # Version
  --dry-run                      # Preview without deploying
  --copy-style [loaded_modules|all|none]
  --recursive, -r                # Deploy recursively
  --all                          # Deploy all environments
  --image [NAME=]URI             # Image override
```

---

## 6. Task and Workflow Migration

### Basic Task Migration

```python
# v1: Task with decorator parameters
from flytekit import task, Resources

@task(
    cache=True,
    cache_version="1.0",
    retries=3,
    timeout=3600,
    container_image="python:3.11",
    requests=Resources(cpu="1", mem="2Gi"),
    limits=Resources(cpu="2", mem="4Gi"),
)
def my_task(x: int) -> int:
    return x * 2

# v2: TaskEnvironment + @env.task
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    image="python:3.11",
    resources=flyte.Resources(cpu="1", memory="2Gi"),
    cache="auto",  # or flyte.Cache(...)
)

@env.task(retries=3, timeout=3600)
def my_task(x: int) -> int:
    return x * 2
```

### Workflow to Task Migration

```python
# v1: Workflow calling tasks
from flytekit import task, workflow

@task
def step1(x: int) -> int:
    return x + 1

@task
def step2(y: int) -> int:
    return y * 2

@task
def step3(z: int) -> str:
    return f"Result: {z}"

@workflow
def my_workflow(x: int) -> str:
    a = step1(x=x)
    b = step2(y=a)
    c = step3(z=b)
    return c

# v2: Tasks calling tasks (synchronous)
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def step1(x: int) -> int:
    return x + 1

@env.task
def step2(y: int) -> int:
    return y * 2

@env.task
def step3(z: int) -> str:
    return f"Result: {z}"

@env.task
def main(x: int) -> str:
    a = step1(x)
    b = step2(a)
    c = step3(b)
    return c
```

```python
# v2: Tasks calling tasks (asynchronous)
# IMPORTANT: To await tasks, the tasks themselves MUST be async
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def step1(x: int) -> int:
    return x + 1

@env.task
async def step2(y: int) -> int:
    return y * 2

@env.task
async def step3(z: int) -> str:
    return f"Result: {z}"

@env.task
async def main(x: int) -> str:
    a = await step1(x)
    b = await step2(a)
    c = await step3(b)
    return c
```

> **Important**: You can only `await` async tasks. If you try to `await` a sync task, it will fail. If your subtasks are sync, call them directly without `await` (they will execute synchronously/sequentially).

### TaskEnvironment Configuration

```python
import flyte

# Full TaskEnvironment example
env = flyte.TaskEnvironment(
    name="my_env",                           # Required: unique name
    image=flyte.Image.from_debian_base(...), # Or string, or "auto"
    resources=flyte.Resources(
        cpu="2",
        memory="4Gi",
        gpu="A100:1",
        disk="10Gi",
        shm="auto",
    ),
    env_vars={"LOG_LEVEL": "INFO"},
    secrets=[
        flyte.Secret(key="api-key", as_env_var="API_KEY"),
    ],
    cache="auto",  # "auto", "override", "disable", or Cache object
    reusable=flyte.ReusePolicy(replicas=5, idle_ttl=60),
    queue="gpu-queue",
    interruptible=True,
)

# Task decorator can override some settings
@env.task(
    short_name="my_task",      # Display name
    cache="disable",           # Override cache
    retries=3,                 # Retry count
    timeout=3600,              # Seconds or timedelta
    report=True,               # Generate HTML report
)
def my_task(x: int) -> int:
    return x
```

### Parameter Mapping: @task to TaskEnvironment + @env.task

| v1 @task Parameter | v2 Location | Notes |
|--------------------|-------------|-------|
| `container_image` | `TaskEnvironment(image=...)` | Env-level only |
| `requests` | `TaskEnvironment(resources=...)` | Env-level only |
| `limits` | `TaskEnvironment(resources=...)` | Combined with requests |
| `environment` | `TaskEnvironment(env_vars=...)` | Env-level only |
| `secret_requests` | `TaskEnvironment(secrets=...)` | Env-level only |
| `cache` | Both | Can override at task level |
| `cache_version` | `flyte.Cache(version_override=...)` | In Cache object |
| `retries` | `@env.task(retries=...)` | Task-level only |
| `timeout` | `@env.task(timeout=...)` | Task-level only |
| `interruptible` | Both | Can override at task level |
| `pod_template` | Both | Can override at task level |
| `deprecated` | N/A | Not in v2 |
| `docs` | `@env.task(docs=...)` | Task-level only |

---

## 7. Secrets Migration

### Declaring and Accessing Secrets

```python
# v1: Declare in decorator, access via current_context()
from flytekit import task, Secret, current_context

@task(secret_requests=[
    Secret(group="mygroup", key="mykey"),
    Secret(group="db", key="password", mount_requirement=Secret.MountType.ENV_VAR),
])
def my_task() -> str:
    ctx = current_context()
    secret_value = ctx.secrets.get(key="mykey", group="mygroup")
    db_password = ctx.secrets.get(key="password", group="db")
    return f"Got secrets"

# v2: Declare in TaskEnvironment, access via environment variables
import flyte
import os

env = flyte.TaskEnvironment(
    name="my_env",
    secrets=[
        flyte.Secret(key="mykey", as_env_var="MY_SECRET"),
        flyte.Secret(key="db-password", as_env_var="DB_PASSWORD"),
    ],
)

@env.task
def my_task() -> str:
    secret_value = os.environ["MY_SECRET"]
    db_password = os.environ["DB_PASSWORD"]
    return f"Got secrets"
```

### Secret Configuration Options

```python
# v2 Secret options
flyte.Secret(
    key="secret-name",                    # Required: secret key in store
    group="optional-group",               # Optional: organizational group
    as_env_var="CUSTOM_ENV_VAR_NAME",    # Mount as this env var name
    # OR
    mount="/etc/flyte/secrets",           # Mount as file (fixed path)
)

# Examples
secrets=[
    # Simple: key becomes uppercase env var (MY_API_KEY)
    flyte.Secret(key="my-api-key"),

    # Custom env var name
    flyte.Secret(key="openai-key", as_env_var="OPENAI_API_KEY"),

    # With group (env var: AWS_ACCESS_KEY)
    flyte.Secret(key="access-key", group="aws"),

    # As file
    flyte.Secret(key="ssl-cert", mount="/etc/flyte/secrets"),
]
```

### Secret Name Convention Changes

| v1 Pattern | v2 Pattern |
|------------|------------|
| `ctx.secrets.get(key="mykey", group="mygroup")` | `os.environ["MYGROUP_MYKEY"]` (auto-named) |
| `ctx.secrets.get(key="mykey")` | `os.environ["MY_SECRET"]` (with `as_env_var`) |

### Creating Secrets via CLI

```bash
# v2: Create secret
flyte create secret MY_SECRET_KEY my_secret_value

# From file
flyte create secret MY_SECRET_KEY --from-file /path/to/secret

# Scoped to project/domain
flyte create secret --project my-project --domain development MY_SECRET_KEY value

# List secrets
flyte get secret

# Delete secret
flyte delete secret MY_SECRET_KEY
```

---

## 8. Resources Migration

### Basic Resource Configuration

```python
# v1: Separate requests and limits
from flytekit import task, Resources

@task(
    requests=Resources(cpu="1", mem="2Gi"),
    limits=Resources(cpu="2", mem="4Gi"),
)
def my_task(): ...

# v1: Unified resources (tuple for request/limit)
@task(resources=Resources(cpu=("1", "2"), mem="2Gi"))
def my_task(): ...

# v2: Resources at TaskEnvironment level
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    resources=flyte.Resources(
        cpu="2",           # Request and limit same
        memory="4Gi",      # Note: "memory" not "mem"
        gpu="A100:1",      # GPU type and count
        disk="10Gi",
        shm="auto",        # Shared memory
    ),
)
```

### GPU Configuration

```python
# v1: GPU specification
from flytekit import task, Resources
from flytekit.extras.accelerators import A100

@task(
    requests=Resources(gpu="1"),
    accelerator=A100,
)
def gpu_task(): ...

# v2: GPU in Resources
import flyte

env = flyte.TaskEnvironment(
    name="gpu_env",
    resources=flyte.Resources(
        cpu="4",
        memory="32Gi",
        gpu="A100:2",         # Type:count format
        # Or: gpu="A100 80G:1"
        # Or: gpu=2            # Count only, no type
    ),
)

# GPU with partition (MIG)
env = flyte.TaskEnvironment(
    name="mig_env",
    resources=flyte.Resources(
        gpu=flyte.GPU("A100", count=1, partition="1g.5gb"),
    ),
)
```

### Supported GPU Types (v2)

- A10, A10G, A100, A100 80G
- B200, H100, H200
- L4, L40s
- T4, V100
- RTX PRO 6000, GB10

### Resource Parameter Mapping

| v1 | v2 | Notes |
|----|----| ------|
| `cpu="1"` | `cpu="1"` | Same |
| `mem="2Gi"` | `memory="2Gi"` | Renamed |
| `gpu="1"` | `gpu="A100:1"` | Type:count format |
| `ephemeral_storage="10Gi"` | `disk="10Gi"` | Renamed |
| N/A | `shm="auto"` | New: shared memory |

---

## 9. Caching Migration

### Basic Caching

```python
# v1: Boolean or Cache object
from flytekit import task, Cache

@task(cache=True, cache_version="1.0")
def cached_task(x: int) -> int:
    return x * 2

# With Cache object
@task(cache=Cache(
    version="1.0",
    serialize=True,
    ignored_inputs=("debug",),
))
def advanced_cached_task(x: int, debug: bool = False) -> int:
    return x * 2

# v2: String or Cache object
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    cache="auto",  # Enable caching at env level
)

@env.task
def cached_task(x: int) -> int:
    return x * 2

# Or override at task level
@env.task(cache="disable")
def uncached_task(x: int) -> int:
    return x * 2

# Advanced caching
@env.task(cache=flyte.Cache(
    behavior="auto",           # "auto", "override", "disable"
    version_override="v1.0",   # Explicit version
    serialize=True,            # Force serial execution
    ignored_inputs=("debug",), # Exclude from hash
    salt="my-salt",            # Additional hash salt
))
def advanced_cached_task(x: int, debug: bool = False) -> int:
    return x * 2
```

### Cache Behavior Options (v2)

| Behavior | Description |
|----------|-------------|
| `"auto"` | Cache results and reuse if available |
| `"override"` | Always execute and overwrite cache |
| `"disable"` | No caching (default for TaskEnvironment) |

---

## 10. map_task to flyte.map and Async Loops

### Basic map_task Migration

```python
# v1: map_task
from flytekit import task, workflow, map_task

@task
def process_item(x: int) -> int:
    return x * 2

@workflow
def my_workflow(items: list[int]) -> list[int]:
    return map_task(process_item)(x=items)

# v2: flyte.map (synchronous)
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def process_item(x: int) -> int:
    return x * 2

@env.task
def main(items: list[int]) -> list[int]:
    return list(flyte.map(process_item, items))
```

### map_task with Concurrency

```python
# v1: map_task with concurrency
@workflow
def my_workflow(items: list[int]) -> list[int]:
    return map_task(process_item, concurrency=5)(x=items)

# v2: flyte.map with concurrency
@env.task
def main(items: list[int]) -> list[int]:
    return list(flyte.map(process_item, items, concurrency=5))
```

### Async Parallel Execution with asyncio.gather() (Recommended)

```python
# v2: asyncio.gather for async parallel execution (RECOMMENDED)
import asyncio
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def process_item(item: int) -> str:
    return f"processed_{item}"

@env.task
async def main(items: list[int]) -> list[str]:
    tasks = [process_item(item) for item in items]
    results = await asyncio.gather(*tasks)
    return list(results)
```

### Concurrency Control with Semaphore

```python
# v2: Use asyncio.Semaphore to limit concurrent tasks
import asyncio

@env.task
async def process_item(item: int) -> str:
    # Simulate some async work
    await asyncio.sleep(1)
    return f"processed_{item}"

@env.task
async def main_with_concurrency_limit(
    items: list[int],
    max_concurrent: int = 5
) -> list[str]:
    """Limit concurrency using a semaphore."""
    semaphore = asyncio.Semaphore(max_concurrent)

    async def process_with_limit(item: int) -> str:
        async with semaphore:  # Only max_concurrent tasks run at once
            return await process_item(item)

    tasks = [process_with_limit(item) for item in items]
    results = await asyncio.gather(*tasks)
    return list(results)
```

### Error Handling with asyncio.gather()

```python
@env.task
async def main_with_error_handling(
    items: list[int],
    max_concurrent: int = 5
) -> list[str]:
    """Handle errors gracefully with return_exceptions."""
    semaphore = asyncio.Semaphore(max_concurrent)

    async def process_with_limit(item: int) -> str:
        async with semaphore:
            return await process_item(item)

    tasks = [process_with_limit(item) for item in items]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    processed = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Item {items[i]} failed: {result}")
            processed.append(f"Failed: {items[i]}")
        else:
            processed.append(result)
    return processed
```

### flyte.map vs asyncio.gather Comparison

| Feature | flyte.map (sync) | asyncio.gather (async)            |
|---------|------------------|-----------------------------------|
| Syntax | `list(flyte.map(fn, items))` | `await asyncio.gather(*tasks)`    |
| Concurrency limit | Built-in `concurrency=N` | Use `asyncio.Semaphore`           |
| Streaming/as-completed | No control | Yes, via `asyncio.as_completed()` |
| Error handling | `return_exceptions=True` | Check return type                 |
| Flexibility | Less flexible | More flexible                     |

### Recommended Pattern Selection

Use **flyte.map** when:
- You are forced to use synchronous Python
- You want minimal code changes from v1 `map_task`

Use **asyncio.gather** when (RECOMMENDED):
- You want maximum flexibility and control
- You need streaming results (`asyncio.as_completed`)
- You need fine-grained concurrency control (semaphores)
- You're writing new v2 code

---

## 11. Sync and Async Tasks

Keep task types consistent within a call chain for clarity and predictability.

### Sync Tasks Calling Sync Tasks

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def step1(x: int) -> int:
    return x + 1

@env.task
def step2(y: int) -> int:
    return y * 2

@env.task
def main(x: int) -> int:
    a = step1(x)   # Runs, returns result
    b = step2(a)   # Runs after step1 completes
    return b
```

### Async Tasks Calling Async Tasks

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def step1(x: int) -> int:
    return x + 1

@env.task
async def step2(y: int) -> int:
    return y * 2

@env.task
async def main(x: int) -> int:
    a = await step1(x)   # Runs, waits for result
    b = await step2(a)   # Runs after step1 completes
    return b
```

### Sequential Execution with `await`

When you `await` async tasks one after another, they run **sequentially** - just like v1 workflows:

```python
# v1: Sequential workflow
@workflow
def my_workflow(x: int) -> str:
    a = step1(x=x)      # Runs first
    b = step2(y=a)      # Runs second (after step1 finishes)
    c = step3(z=b)      # Runs third (after step2 finishes)
    return c

# v2: Sequential async task (equivalent behavior)
@env.task
async def main(x: int) -> str:
    a = await step1(x)      # Runs first
    b = await step2(a)      # Runs second (after step1 finishes)
    c = await step3(b)      # Runs third (after step2 finishes)
    return c
```

> **Key Point**: `await` means "wait for this to finish before continuing." Sequential `await` calls behave the same as sequential task calls in v1 workflows.

---

## 12. Triggers and Scheduling

### LaunchPlan to Trigger Migration

```python
# v1: LaunchPlan with schedule
from flytekit import workflow, LaunchPlan, CronSchedule, FixedRate
from datetime import timedelta

@workflow
def my_workflow(x: int) -> int:
    return process(x)

# Cron schedule
cron_lp = LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="hourly_run",
    default_inputs={"x": 10},
    schedule=CronSchedule(schedule="0 * * * *"),  # Every hour
)

# Fixed rate
rate_lp = LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="frequent_run",
    default_inputs={"x": 5},
    schedule=FixedRate(duration=timedelta(minutes=30)),
)

# v2: Trigger on task
import flyte
from datetime import datetime

env = flyte.TaskEnvironment(name="my_env")

# Hourly trigger (convenience method)
@env.task(triggers=flyte.Trigger.hourly())
def hourly_task(x: int = 10) -> int:
    return process(x)

# Custom cron trigger
cron_trigger = flyte.Trigger(
    name="custom_cron",
    automation=flyte.Cron("0 * * * *"),  # Every hour
    inputs={"x": 10},
    auto_activate=True,
)

@env.task(triggers=cron_trigger)
def scheduled_task(x: int) -> int:
    return process(x)

# Fixed rate trigger
rate_trigger = flyte.Trigger(
    name="frequent",
    automation=flyte.FixedRate(timedelta(minutes=30)),
    inputs={"x": 5},
    auto_activate=True,
)

@env.task(triggers=rate_trigger)
def frequent_task(x: int) -> int:
    return process(x)
```

### Trigger Options

```python
# Convenience methods
flyte.Trigger.hourly()           # Every hour
flyte.Trigger.hourly("my_time")  # Custom time parameter name
flyte.Trigger.minutely()         # Every minute

# Custom Trigger
flyte.Trigger(
    name="my_trigger",           # Required: trigger name
    automation=flyte.Cron(...),  # Cron or FixedRate
    inputs={"x": 10},            # Default inputs
    auto_activate=True,          # Activate on deploy
)

# Cron options
flyte.Cron(
    schedule="0 9 * * 1-5",      # 9 AM weekdays
    timezone="America/New_York", # Optional timezone
)

# FixedRate options
flyte.FixedRate(timedelta(hours=1))  # Every hour
```

### TriggerTime Parameter

```python
# v2: Automatic trigger time injection
from datetime import datetime

@env.task(triggers=flyte.Trigger.hourly())
def my_task() -> str:
    return f"Triggered"

# Custom parameter name
custom_trigger = flyte.Trigger(
    name="my_trigger",
    automation=flyte.Cron("0 * * * *"),
    inputs={"x": 10},
)

@env.task(triggers=custom_trigger)
def my_task(x: int) -> str:
    return f"Started with x={x}"
```

### Deploying Triggers

```bash
# Deploy environment (triggers deploy with it)
flyte deploy my_module.py my_env

# Triggers with auto_activate=True activate automatically
# Otherwise, activate manually via UI or API
```

---

## 13. Dynamic Workflows

### v1 @dynamic to v2 Tasks

```python
# v1: Dynamic workflow for variable task counts
from flytekit import dynamic, task, workflow

@task
def get_tiles(n: int) -> list[int]:
    return list(range(n))

@task
def process_tile(tile: int) -> int:
    return tile * 2

@dynamic
def process_all_tiles(tiles: list[int]) -> list[int]:
    results = []
    for tile in tiles:
        results.append(process_tile(tile=tile))
    return results

@workflow
def main_workflow(n: int) -> list[int]:
    tiles = get_tiles(n=n)
    return process_all_tiles(tiles=tiles)

# v2: Just regular tasks (all tasks can be "dynamic")
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
def process_tile(tile: int) -> int:
    return tile * 2

@env.task
def process_all_tiles(tiles: list[int]) -> list[int]:
    results = []
    for tile in tiles:
        results.append(process_tile(tile=tile))
    return results

@env.task
def main_workflow(n: int) -> list[int]:
    tiles = list(range(n))
    return process_all_tiles(tiles=tiles)

# v2: Async version
@env.task
async def process_tile(tile: int) -> int:
    return tile * 2

@env.task
async def process_all_tiles(tiles: list[int]) -> list[int]:
    results = []
    for tile in tiles:
        results.append(await process_tile(tile=tile))
    return results

@env.task
async def main_workflow(n: int) -> list[int]:
    tiles = list(range(n))
    return await process_all_tiles(tiles=tiles)
```

### Conditional Task Execution

```python
# v1: flytekit.conditional (DSL)
from flytekit import conditional

@workflow
def conditional_wf(x: int) -> int:
    return conditional("test")
        .if_(x > 0)
        .then(positive_task(x=x))
        .else_()
        .then(negative_task(x=x))

# v2: Native Python if/else
@env.task
def main(x: int) -> int:
    if x > 0:
        return positive_task(x)
    else:
        return negative_task(x)
```

### Subworkflows to Nested Tasks

```python
# v1: Subworkflow
@workflow
def sub_workflow(x: int) -> int:
    a = step1(x)
    b = step2(a)
    return b

@workflow
def main_workflow(item: int) -> int:
    result = sub_workflow(x=item)
    return result

# v2: Just nested task calls
@env.task
def sub_task(x: int) -> int:
    a = step1(x)
    b = step2(a)
    return b

@env.task
def main(item: int) -> int:
    result = sub_workflow(x=item)
    return result
```

---

## 14. Complete Migration Examples

### Example 1: Simple ML Pipeline

```python
# ============ V1 VERSION ============
from flytekit import task, workflow, ImageSpec, Resources, current_context
from flytekit.types.file import FlyteFile
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

image = ImageSpec(
    name="ml-image",
    packages=["pandas", "scikit-learn", "joblib", "pyarrow"],
    builder="union",
)


@task(
    container_image=image,
    requests=Resources(cpu="2", mem="4Gi"),
    cache=True,
    cache_version="1.1",
)
def load_data() -> pd.DataFrame:
    # Directly reading from a public URL
    CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    return pd.read_csv(CSV_URL)


@task(container_image=image)
def train_model(data: pd.DataFrame) -> FlyteFile:
    model = RandomForestClassifier()
    # Iris dataset columns: sepal_length, sepal_width, petal_length, petal_width, species
    X = data.drop("species", axis=1)
    y = data["species"]

    model.fit(X, y)

    model_path = os.path.join(current_context().working_directory, "model.joblib")
    joblib.dump(model, model_path)
    return FlyteFile(path=model_path)


@task(container_image=image)
def evaluate(model_file: FlyteFile, data: pd.DataFrame) -> float:
    # Download the FlyteFile and load the model
    model = joblib.load(model_file.download())

    X = data.drop("species", axis=1)
    y = data["species"]
    return float(model.score(X, y))


@workflow
def ml_pipeline() -> float:
    data = load_data()
    model = train_model(data=data)
    score = evaluate(model_file=model, data=data)
    return score


# ============ V2 VERSION ============
import os
import joblib
import pandas as pd
import flyte
from flyte import TaskEnvironment, Resources, Image
from flyte.io import File  # Replaces FlyteFile
from sklearn.ensemble import RandomForestClassifier

# 1. Define the Image using the fluent builder API
image = (
    Image.from_debian_base(
        name="ml-image",
        python_version=(3, 11),
    )
    .with_pip_packages("pandas", "scikit-learn", "joblib", "pyarrow")
)

# 2. Define the TaskEnvironment (Centralized config for your tasks)
env = TaskEnvironment(
    name="ml_env",
    image=image,
    resources=Resources(cpu="2", memory="4Gi"),
    cache="auto",  # Enables caching for all tasks in this env by default
)


@env.task
async def load_data() -> pd.DataFrame:
    CSV_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    return pd.read_csv(CSV_URL)


@env.task
async def train_model(data: pd.DataFrame) -> File:
    model = RandomForestClassifier()
    X = data.drop("species", axis=1)
    y = data["species"]
    model.fit(X, y)

    # Use os.getcwd() instead of current_context()
    root_dir = os.getcwd()
    model_path = os.path.join(root_dir, "model.joblib")
    joblib.dump(model, model_path)
    return await File.from_local(model_path)


@env.task
async def evaluate(model_file: File, data: pd.DataFrame) -> float:
    # Flyte v2 File objects can be used directly with joblib/open
    local_path = await model_file.download()
    print(f"Downloaded model to {local_path}")
    model = joblib.load(local_path)

    X = data.drop("species", axis=1)
    y = data["species"]
    return float(model.score(X, y))


# 3. The Workflow is now just an orchestrating task
# Note: Using 'async' here is recommended for orchestration in v2
@env.task
async def ml_pipeline() -> float:
    data = await load_data()
    model = await train_model(data)
    score = await evaluate(model, data)
    return score
```

### Example 2: Parallel Processing with map_task

```python
# ============ V1 VERSION ============
from flytekit import task, workflow, map_task, dynamic
from functools import partial

@task(cache=True, cache_version="1.0")
def get_chunks(n: int) -> list[int]:
    return list(range(n))

@task(cache=True, cache_version="1.0")
def process_chunk(chunk_id: int, multiplier: int) -> int:
    return chunk_id * multiplier

@workflow
def parallel_pipeline(n: int, multiplier: int) -> list[int]:
    chunk_ids = get_chunks(n)
    results = map_task(
        partial(process_chunk, multiplier=multiplier),
        concurrency=10,
    )(chunk_id=chunk_ids)
    return results


# ============ V2 VERSION (Sync) ============
from functools import partial
import flyte

env = flyte.TaskEnvironment(name="parallel_env", cache="auto")


@env.task
def process_chunk(chunk_id: int, multiplier: int) -> int:
    return chunk_id * multiplier


@env.task
def main(n: int, multiplier: int) -> list[int]:
    chunk_ids = list(range(n))

    # Use partial instead of lambda
    bound_task = partial(process_chunk, multiplier=multiplier)

    results = list(flyte.map(
        bound_task,
        chunk_ids,
        concurrency=10,
    ))
    return results


# ============ V2 VERSION (Async - Recommended) ============
import asyncio
import flyte

env = flyte.TaskEnvironment(name="parallel_env", cache="auto")


@env.task
async def process_chunk(chunk_id: int, multiplier: int) -> int:
    # This simulates work that will be limited by the semaphore
    return chunk_id * multiplier


@env.task
async def main(n: int, multiplier: int) -> list[int]:
    chunk_ids = list(range(n))

    # Initialize the semaphore with your limit (e.g., 10)
    sem = asyncio.Semaphore(10)

    async def throttled_task(cid):
        # The 'async with' block ensures the slot is released
        # even if the task fails
        async with sem:
            return await process_chunk(cid, multiplier)

    # Create the list of throttled coroutines
    tasks = [throttled_task(cid) for cid in chunk_ids]

    # Gather will now run them, but no more than 10 at a time
    results = await asyncio.gather(*tasks)
    return list(results)
```

---

## 15. Common Gotchas

### 1. current_context() → flyte.ctx() or Environment Variables

```python
# v1
ctx = flytekit.current_context()
secret = ctx.secrets.get(key="mykey", group="mygroup")
working_dir = ctx.working_directory
execution_id = ctx.execution_id

# v2 - Secrets via environment variables
secret = os.environ["MYGROUP_MYKEY"]

# v2 - Context via flyte.ctx()
ctx = flyte.ctx()
# Note: API is different, check v2 documentation
```

### 2. Workflow `>>` Ordering Notation

```python
# v1: Using >> to indicate ordering
@workflow
def my_workflow():
    t1_result = task1()
    t2_result = task2()
    t1_result >> t2_result  # Explicit ordering
    return t2_result

# v2: Sequential calls are naturally ordered (sync)
@env.task
def main():
    t1_result = task1()  # Runs first
    t2_result = task2()  # Runs second (sequential)
    return t2_result

# v2: For async, use await to sequence
@env.task
async def main():
    t1_result = await task1()  # Runs first
    t2_result = await task2()  # Runs second
    return t2_result
```

### 3. flyte.map Returns a Generator

```python
# v1: map_task returns list directly
results = map_task(my_task)(items=my_list)

# v2: flyte.map returns generator - must convert to list
results = list(flyte.map(my_task, my_list))  # Add list()!

# v2 async: Use asyncio.gather for async parallel execution
tasks = [my_task(item) for item in my_list]
results = await asyncio.gather(*tasks)
```

### 4. Image Configuration Location

```python
# v1: Image per task
@task(container_image=my_image)
def task1(): ...

@task(container_image=my_image)  # Repeated
def task2(): ...

# v2: Image at TaskEnvironment level (DRY)
env = flyte.TaskEnvironment(name="my_env", image=my_image)

@env.task
def task1(): ...  # Uses env's image

@env.task
def task2(): ...  # Uses env's image
```

### 5. Resource Configuration

```python
# v1: Resources per task
@task(requests=Resources(cpu="1"), limits=Resources(cpu="2"))
def my_task(): ...

# v2: Resources at TaskEnvironment level
env = flyte.TaskEnvironment(
    name="my_env",
    resources=flyte.Resources(cpu="1"),  # No separate limits
)
```

### 6. Cache Version

```python
# v1: Explicit cache_version required
@task(cache=True, cache_version="1.0")
def my_task(): ...

# v2: Auto-versioning or explicit
@env.task(cache="auto")  # Auto-versioned
def my_task(): ...

@env.task(cache=flyte.Cache(behavior="auto", version_override="1.0"))
def my_task_explicit(): ...
```

### 7. Entrypoint Task Naming

```python
# v1: Workflow is the entrypoint
@workflow
def my_workflow(): ...

# v2: Use a main() task or any task name
@env.task
def main(): ...  # Common convention

# Run with: flyte run my_module.py main
```

### 8. Memory Parameter Name

```python
# v1
Resources(mem="2Gi")

# v2
flyte.Resources(memory="2Gi")  # Note: "memory" not "mem"
```

### 9. Type Annotations Required

```python
# v2 is less string about type annotations, but explicit typing is preferred

# v1
@task
def my_task(x: int) -> dict: # would fail, need to specify key value type like dict[str, int]
    return {"a": x}

# v2
@task
def my_task(x: int) -> dict: # would succeed, v2 will pickle I/O where typing isn't explicit
    return {"a": x}
```

---

## Quick Reference Cheat Sheet

```python
# V2 MINIMAL TEMPLATE
import flyte
import asyncio

# 1. Define image
image = (
    flyte.Image.from_debian_base(python_version=(3, 11))
    .with_pip_packages("pandas", "numpy")
)

# 2. Create TaskEnvironment
env = flyte.TaskEnvironment(
    name="my_env",
    image=image,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)

# 3. Define tasks
@env.task
async def process(x: int) -> int:
    return x * 2

# 4. Define main entrypoint
@env.task
async def main(items: list[int]) -> list[int]:
    tasks = [process(x) for x in items]
    results = await asyncio.gather(*tasks)
    return list(results)

# 5. Run
if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(main, items=[1, 2, 3, 4, 5])
    run.wait()
```

```bash
# CLI COMMANDS
flyte run my_module.py main --items '[1,2,3,4,5]'
flyte run --local my_module.py main --items '[1,2,3,4,5]'
flyte deploy my_module.py my_env
```