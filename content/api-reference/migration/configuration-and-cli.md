---
title: Configuration and CLI
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Configuration and CLI

## Configuration files

### Config file location

| Version | Default location | Environment variable |
|---------|-----------------|---------------------|
| Flyte 1 | `~/.flyte/config.yaml` | `FLYTECTL_CONFIG` |
| Flyte 2 | `~/.flyte/config.yaml` | `FLYTE_CONFIG` |

### Config format

{{< tabs "migration-config-format" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
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
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
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
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Key config differences

| Setting | Flyte 1 location | Flyte 2 location |
|---------|-------------|-------------|
| Endpoint | `admin.endpoint` or `union.connection.host` | `admin.endpoint` |
| Auth type | `admin.authType` or `union.auth.type` | Generally auto-detected (PKCE default) |
| Project | CLI flag `-p` | `task.project` (can set default) |
| Domain | CLI flag `-d` | `task.domain` (can set default) |
| Organization | CLI flag `--org` | `task.org` (can set default) |
| Image builder | N/A | `image.builder` (`local` or `remote`) |

### Specifying config via CLI

{{< tabs "migration-config-cli" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```shell
pyflyte --config ~/.flyte/config.yaml run ...
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```shell
flyte --config ~/.flyte/config.yaml run ...
flyte -c ~/.flyte/config.yaml run ...
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Specifying config in code

```python
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

## CLI commands

### Command mapping

| Flyte 1 command | Flyte 2 command | Notes |
|------------|------------|-------|
| `pyflyte run` | `flyte run` | Similar but different flags |
| `pyflyte run --remote` | `flyte run` | Remote is default in Flyte 2 |
| `pyflyte run` (no --remote) | `flyte run --local` | Local execution |
| `pyflyte register` | `flyte deploy` | Different concept |
| `pyflyte package` | N/A | Not needed in Flyte 2 |
| `pyflyte serialize` | N/A | Not needed in Flyte 2 |

### Running tasks

{{< tabs "migration-cli-run" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```shell
# Run locally
pyflyte run my_module.py my_workflow --arg1 value1

# Run remotely
pyflyte --config config.yaml run --remote my_module.py my_workflow --arg1 value1
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```shell
# Run remotely (default)
flyte run my_module.py my_task --arg1 value1

# Run locally
flyte run --local my_module.py my_task --arg1 value1

# With explicit config
flyte --config config.yaml run my_module.py my_task --arg1 value1
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Key CLI flag differences

| Flyte 1 flag | Flyte 2 flag | Notes |
|---------|---------|-------|
| `--remote` | (default) | Remote is default in Flyte 2 |
| `--copy-all` | `--copy-style all` | File copying |
| N/A | `--copy-style loaded_modules` | Default: only imported modules |
| N/A | `--copy-style none` | Don't copy files |
| `-p, --project` | `--project` | Same |
| `-d, --domain` | `--domain` | Same |
| `-i, --image` | `--image` | Same format |
| N/A | `--follow, -f` | Follow execution logs |

### Deploying

{{< tabs "migration-cli-deploy" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```shell
pyflyte register my_module.py -p my-project -d development
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```shell
# Deploy task environments
flyte deploy my_module.py my_env --project my-project --domain development

# Deploy all environments in file
flyte deploy --all my_module.py

# Deploy with version
flyte deploy --version v1.0.0 my_module.py my_env

# Recursive deployment
flyte deploy --recursive --all ./src

# Dry run (preview)
flyte deploy --dry-run my_module.py my_env
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Running deployed tasks

```shell
# Run a deployed task
flyte run deployed-task my_env.my_task --arg1 value1

# Run specific version
flyte run deployed-task my_env.my_task:v1.0.0 --arg1 value1
```

### Complete Flyte 2 CLI options

```shell
# Global options
flyte --endpoint <URL>                     # Override endpoint
flyte --config <PATH>                      # Config file path
flyte --org <TEXT>                          # Organization
flyte -v, --verbose                        # Verbose output (can repeat: -vvv)
flyte --output-format [table|json]         # Output format

# Run command options
flyte run [OPTIONS] <file> <task> [TASK_ARGS]
  --local                                  # Run locally
  --project <TEXT>                         # Project
  --domain <TEXT>                          # Domain
  --copy-style [loaded_modules|all|none]   # File copying
  --root-dir <PATH>                        # Source root directory
  --follow, -f                             # Follow logs
  --image [NAME=]URI                       # Image override
  --name <TEXT>                            # Execution name
  --service-account <TEXT>                 # K8s service account

# Deploy command options
flyte deploy [OPTIONS] <file> [ENV_NAME]
  --project <TEXT>                         # Project
  --domain <TEXT>                          # Domain
  --version <TEXT>                         # Version
  --dry-run                                # Preview without deploying
  --copy-style [loaded_modules|all|none]   # File copying
  --recursive, -r                          # Deploy recursively
  --all                                    # Deploy all environments
  --image [NAME=]URI                       # Image override
```

For full CLI reference, see [Flyte CLI](../flyte-cli).
