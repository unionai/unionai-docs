---
title: Secrets, resources, and caching
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Secrets, resources, and caching

## Secrets

### Declaring and accessing secrets

{{< tabs "migration-secrets" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
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
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
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
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Secret configuration options

```python
# Flyte 2 Secret options
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

### Secret name convention changes

| Flyte 1 pattern | Flyte 2 pattern |
|------------|------------|
| `ctx.secrets.get(key="mykey", group="mygroup")` | `os.environ["MYGROUP_MYKEY"]` (auto-named) |
| `ctx.secrets.get(key="mykey")` | `os.environ["MY_SECRET"]` (with `as_env_var`) |

### Creating secrets via CLI

```bash
# Create secret
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

For full details on secrets, see [Secrets](../../user-guide/task-configuration/secrets).

## Resources

### Basic resource configuration

{{< tabs "migration-resources" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import task, Resources

# Separate requests and limits
@task(
    requests=Resources(cpu="1", mem="2Gi"),
    limits=Resources(cpu="2", mem="4Gi"),
)
def my_task(): ...

# Unified resources (tuple for request/limit)
@task(resources=Resources(cpu=("1", "2"), mem="2Gi"))
def my_task(): ...
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
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
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### GPU configuration

{{< tabs "migration-gpu" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import task, Resources
from flytekit.extras.accelerators import A100

@task(
    requests=Resources(gpu="1"),
    accelerator=A100,
)
def gpu_task(): ...
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
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
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Supported GPU types (Flyte 2)

- A10, A10G, A100, A100 80G
- B200, H100, H200
- L4, L40s
- T4, V100
- RTX PRO 6000, GB10

### Resource parameter mapping

| Flyte 1 | Flyte 2 | Notes |
|----|----| ------|
| `cpu="1"` | `cpu="1"` | Same |
| `mem="2Gi"` | `memory="2Gi"` | Renamed |
| `gpu="1"` | `gpu="A100:1"` | Type:count format |
| `ephemeral_storage="10Gi"` | `disk="10Gi"` | Renamed |
| N/A | `shm="auto"` | New: shared memory |

For full details on resources, see [Resources](../../user-guide/task-configuration/resources).

## Caching

### Basic caching

{{< tabs "migration-caching" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
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
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    cache="auto",  # Enable caching at env level
)

@env.task
def cached_task(x: int) -> int:
    return x * 2

# Override at task level
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
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Cache behavior options (Flyte 2)

| Behavior | Description |
|----------|-------------|
| `"auto"` | Cache results and reuse if available |
| `"override"` | Always execute and overwrite cache |
| `"disable"` | No caching (default for TaskEnvironment) |

For full details on caching, see [Caching](../../user-guide/task-configuration/caching).
