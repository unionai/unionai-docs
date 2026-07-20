---
title: CLI and configuration
weight: 6
variants: +flyte +union
---

# CLI and configuration

The command-line tool is renamed from `pyflyte` to `flyte`, and the config file is trimmed down. See [Migration](./migration) for the overall approach.

## CLI command mapping

| Flyte 1 | Flyte 2 | Notes |
|---|---|---|
| `pyflyte run` | `flyte run` | Similar, different flags |
| `pyflyte run --remote` | `flyte run` | Remote is the default in Flyte 2 |
| `pyflyte run` (local) | `flyte run --local` | Local execution is now explicit |
| `pyflyte register` | `flyte deploy` | Different concept |
| `pyflyte package` | N/A | Not needed in Flyte 2 |
| `pyflyte serialize` | N/A | Not needed in Flyte 2 |

### Running tasks

{{< tabs "migration-cli-run" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```shell
# Local
pyflyte run my_module.py my_workflow --arg1 value1

# Remote
pyflyte --config config.yaml run --remote my_module.py my_workflow --arg1 value1
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```shell
# Remote (default)
flyte run my_module.py my_task --arg1 value1

# Local
flyte run --local my_module.py my_task --arg1 value1

# With an explicit config file
flyte --config config.yaml run my_module.py my_task --arg1 value1
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Deploying

In Flyte 1 you registered a module; in Flyte 2 you deploy task environments.

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
# Deploy a task environment
flyte deploy my_module.py my_env --project my-project --domain development

# Deploy all environments in a file
flyte deploy --all my_module.py

# Deploy with an explicit version, or recursively
flyte deploy --version v1.0.0 my_module.py my_env
flyte deploy --recursive --all ./src
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Key flag differences

| Flyte 1 flag | Flyte 2 flag | Notes |
|---|---|---|
| `--remote` | (default) | Remote is the default |
| `--copy-all` | `--copy-style all` | File copying |
| N/A | `--copy-style loaded_modules` | Default: only imported modules |
| `-p, --project` | `--project` | Same |
| `-d, --domain` | `--domain` | Same |
| `-i, --image` | `--image` | Same format |
| N/A | `--follow, -f` | Follow execution logs |

## Configuration files

The config file lives in the same place (`~/.flyte/config.yaml`), but the environment variable changes from `FLYTECTL_CONFIG` to `FLYTE_CONFIG`, and the format is simpler.

{{< tabs "migration-config-format" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```yaml
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

| Setting | Flyte 1 | Flyte 2 |
|---|---|---|
| Endpoint | `admin.endpoint` | `admin.endpoint` |
| Auth type | `admin.authType` | Auto-detected (PKCE default) |
| Project | CLI flag `-p` | `task.project` (default) |
| Domain | CLI flag `-d` | `task.domain` (default) |
| Organization | CLI flag `--org` | `task.org` (default) |
| Image builder | N/A | `image.builder` (`local` or `remote`) |

### Configuring in code

```python
import flyte

# From a config file (auto-discovers, or pass a path)
flyte.init_from_config()
flyte.init_from_config("path/to/config.yaml")

# Programmatically
flyte.init(
    endpoint="flyte.example.com",
    project="my-project",
    domain="development",
)
```

For API-key authentication in non-interactive environments, use `flyte.init_from_api_key()` — see [Run on a remote cluster](../../run-modes/running-remote).

## Next

- [Control flow](./control-flow) — conditionals, dynamic behavior, and error handling
- [Hybrid v1 and v2 pipelines](./hybrid-pipelines) — calling between v1 and v2 during the transition
