---
title: Task configuration
weight: 5
variants: +flyte +union
---

# Task configuration

In Flyte 1, image, resources, caching, secrets, and scheduling were configured per-task on the `@task` decorator or per-workflow on a `LaunchPlan`. In Flyte 2 most of this moves to the `flyte.TaskEnvironment`, so it's declared once and shared. See [Migration](./migration) for the overall approach.

## Image, resources, and caching

Image, resources, and caching move from the `@task` decorator to the `TaskEnvironment`. Per-task settings like `retries` and `timeout` stay on `@env.task`. Note that `mem` is renamed to `memory`, and there are no separate `requests`/`limits` — a single `Resources` value serves as both.

{{< tabs "migration-task-config" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/task_config_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/task_config_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

For the full `@task` → `TaskEnvironment` + `@env.task` parameter mapping, see [Tasks and workflows](./tasks-and-workflows).

## Container images

Flyte 1's `ImageSpec` is replaced by Flyte 2's `flyte.Image` with a fluent builder API.

```python
from flyte import Image

image = (
    Image.from_debian_base(name="my-image", registry="ghcr.io/myorg", python_version=(3, 11))
    .with_pip_packages("pandas", "numpy")
    .with_apt_packages("curl", "git")
    .with_env_vars({"MY_VAR": "value"})
)
```

Instead of one constructor with many arguments, you start from a base and chain builder methods:

| Constructor | Use case |
|---|---|
| `Image.from_debian_base()` | Most common; includes the Flyte SDK |
| `Image.from_base(image_uri)` | Start from any existing image |
| `Image.from_dockerfile(path)` | Complex custom builds |
| `Image.from_uv_script(path)` | UV-based projects |

Common chainable builder methods: `.with_pip_packages(...)`, `.with_requirements(path)`, `.with_uv_project(path)`, `.with_apt_packages(...)`, `.with_commands([...])`, `.with_source_file(path, dst=...)`, `.with_source_folder(path, dst=...)`, `.with_env_vars({...})`, and `.with_workdir(...)`.

| Flyte 1 `ImageSpec` | Flyte 2 `Image` | Notes |
|---|---|---|
| `name` | `name` (constructor) | Same |
| `registry` | `registry` (constructor) | Same |
| `python_version` | `python_version` (tuple) | `"3.11"` becomes `(3, 11)` |
| `packages` | `.with_pip_packages()` | Method instead of param |
| `apt_packages` | `.with_apt_packages()` | Method instead of param |
| `requirements` | `.with_requirements()` | Supports txt, poetry.lock, uv.lock |
| `env` | `.with_env_vars()` | Method instead of param |
| `commands` | `.with_commands()` | Method instead of param |
| `copy` / `source_root` | `.with_source_file()` / `.with_source_folder()` | More explicit methods |
| `base_image` | `Image.from_base()` | Different constructor |
| `builder` | Config file or `flyte.init()` | Global setting |
| `platform` | `platform` (constructor) | Tuple: `("linux/amd64", "linux/arm64")` |

For a private registry, create an image-pull secret and reference it:

```shell
flyte create secret --type image_pull my-registry-secret --from-file ~/.docker/config.json
```

```python
image = Image.from_debian_base(
    registry="private.registry.com",
    name="my-image",
    registry_secret="my-registry-secret",
)
```

See [Container images](../../task-configuration/container-images) for more.

## Resources

A single `flyte.Resources` value serves as both request and limit — there are no separate `requests`/`limits`. Several parameters were renamed.

| Flyte 1 | Flyte 2 | Notes |
|---|---|---|
| `cpu="1"` | `cpu="1"` | Same |
| `mem="2Gi"` | `memory="2Gi"` | Renamed |
| `gpu="1"` | `gpu="A100:1"` | `Type:count` format |
| `ephemeral_storage="10Gi"` | `disk="10Gi"` | Renamed |
| N/A | `shm="auto"` | New: shared memory |

GPU type and count are combined into one string, replacing the separate Flyte 1 `accelerator=` argument:

```python
env = flyte.TaskEnvironment(
    name="gpu_env",
    resources=flyte.Resources(
        cpu="4",
        memory="32Gi",
        gpu="A100:2",              # Type:count
        # gpu="A100 80G:1"         # 80GB variant
        # gpu=flyte.GPU("A100", count=1, partition="1g.5gb")   # MIG partition
    ),
)
```

Supported GPU types include A10, A10G, A100, A100 80G, B200, H100, H200, L4, L40s, T4, V100, RTX PRO 6000, and GB10. See [Resources](../../task-configuration/resources) for more.

## Caching

Caching is enabled at the env level with `cache="auto"` (or per-task on `@env.task`). The explicit `cache_version` string moves into a `flyte.Cache` object.

| Behavior | Description |
|---|---|
| `"auto"` | Cache results and reuse if available |
| `"override"` | Always execute and overwrite the cache |
| `"disable"` | No caching (default for a `TaskEnvironment`) |

```python
# Flyte 1: @task(cache=True, cache_version="1.0")
# Flyte 2:
@env.task(cache="auto")
def cached_task(x: int) -> int:
    return x * 2

# Advanced control (replaces cache_version, serialize, ignored_inputs, ...)
@env.task(cache=flyte.Cache(
    behavior="auto",
    version_override="v1.0",
    serialize=True,
    ignored_inputs=("debug",),
))
def advanced(x: int, debug: bool = False) -> int:
    return x * 2
```

See [Caching](../../task-configuration/caching) for more.

## Secrets

Secrets move from `secret_requests` on the task to `secrets` on the `TaskEnvironment`, and you read them from environment variables instead of `current_context().secrets` — for example, an API key for a model registry or hosted LLM.

{{< tabs "migration-secrets" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/secrets_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/secrets_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

A `flyte.Secret` can be mounted as an environment variable or as a file, and the access convention changes:

```python
flyte.Secret(key="openai-key", as_env_var="OPENAI_API_KEY")   # mount as env var
flyte.Secret(key="access-key", group="aws")                    # env var: AWS_ACCESS_KEY
flyte.Secret(key="ssl-cert", mount="/etc/flyte/secrets")       # mount as a file
```

| Flyte 1 pattern | Flyte 2 pattern |
|---|---|
| `ctx.secrets.get(key="mykey", group="mygroup")` | `os.environ["MYGROUP_MYKEY"]` (auto-named) |
| `ctx.secrets.get(key="mykey")` | `os.environ["MY_SECRET"]` (with `as_env_var="MY_SECRET"`) |

Create and manage secrets from the CLI:

```bash
flyte create secret MY_SECRET_KEY --value my_secret_value
flyte create secret MY_SECRET_KEY --from-file /path/to/secret
flyte get secret
flyte delete secret MY_SECRET_KEY
```

See [Secrets](../../task-configuration/secrets) for more.

## Scheduling

A `LaunchPlan` with a `CronSchedule` (say, a nightly retraining job) becomes a `flyte.Trigger` attached directly to the task. Use `flyte.TriggerTime` to bind the scheduled fire time to an input, and deploy the trigger with `flyte deploy`.

{{< tabs "migration-scheduling" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/scheduling_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/scheduling_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

Triggers support `flyte.Cron("0 9 * * *", timezone="America/New_York")` and `flyte.FixedRate(timedelta(hours=1))` as automations, plus convenience constructors like `flyte.Trigger.hourly()` and `flyte.Trigger.daily()`. See [Triggers](../../task-configuration/triggers) for more.

## Next

- [CLI and configuration](./cli-and-configuration) — `pyflyte` → `flyte` command and config-file mapping
- [Control flow](./control-flow) — conditionals, dynamic behavior, and error handling
- [Data types and I/O](./data-io) — files, DataFrames, and dataclasses
