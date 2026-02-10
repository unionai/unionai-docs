---
title: Local setup
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Local setup

This guide covers setting up your local development environment and configuring the `flyte` CLI and SDK to connect to your Union/Flyte instance.

## Prerequisites

- **Python 3.10+**
- **`uv`** — A fast Python package installer. See the [`uv` installation guide](https://docs.astral.sh/uv/getting-started/installation/).
- Access to a Union/Flyte instance (URL and a project where you can run workflows)

## Install the flyte package

Create a virtual environment and install the `flyte` package:

```shell
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install --prerelease=allow flyte
```

Verify installation:

```shell
flyte --version
```

## Configuration file

As we did in [Quickstart](./quickstart), use `flyte create config` to create a configuration file:

{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}
```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --domain development \
    --project my-project \
    --builder remote
```
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --domain development \
    --project my-project \
    --builder local
```
{{< /markdown >}}
{{< /variant >}}

This creates `./.flyte/config.yaml`:

{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}
```yaml
admin:
  endpoint: dns:///my-org.my-company.com
image:
  builder: remote
task:
  org: my-org
  domain: development
  project: my-project
```
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
```yaml
admin:
  endpoint: dns:///my-org.my-company.com
image:
  builder: local
task:
  org: my-org
  domain: development
  project: my-project
```
{{< /markdown >}}
{{< /variant >}}

{{< dropdown title="Full example with all options" icon="bento" >}}

{{< variant byoc selfmanaged serverless >}}
{{< markdown >}}
Create a custom config file with all available options:
```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --org my-org \
    --domain development \
    --project my-project \
    --builder remote \
    --insecure \
    --output my-config.yaml \
    --force
```
{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
Create a custom config file with all available options:
```shell
flyte create config \
    --endpoint my-org.my-company.com \
    --org my-org \
    --domain development \
    --project my-project \
    --builder local \
    --insecure \
    --output my-config.yaml \
    --force
```
{{< /markdown >}}
{{< /variant >}}

{{< markdown >}}
See the [CLI reference](../api-reference/flyte-cli#flyte-create-config) for all parameters.
{{< /markdown >}}

{{< /dropdown >}}

{{< dropdown title="Config properties explained" icon="control_knobs" >}}
{{< markdown >}}

**`admin`** — Connection details for your Union/Flyte instance.

- `endpoint`: URL with `dns:///` prefix. If your UI is at `https://my-org.my-company.com`, use `dns:///my-org.my-company.com`.
- `insecure`: Set to `true` only for local instances without TLS.

**`image`** — Docker image building configuration.

- `builder`: How container images are built.
  - `remote` (Union): Images built on Union's infrastructure.
  - `local` (Flyte OSS): Images built on your machine. Requires Docker. See [Image building](./task-configuration/container-images#image-building).

**`task`** — Default settings for task execution.

- `org`: Organization name (usually matches the first part of your endpoint URL).
- `domain`: Environment separation (`development`, `staging`, `production`).
- `project`: Default project for deployments. Must already exist on your instance.

<!-- TODO: add link to project creation when available -->
{{< /markdown >}}
{{< /dropdown >}}

## Using the configuration

You can reference your config file explicitly or let the SDK find it automatically.

### Explicit configuration

**CLI**: Use `--config` or `-c`:

```shell
flyte --config my-config.yaml run hello.py main
flyte -c my-config.yaml run hello.py main
```

**Python**: Initialize with [`flyte.init_from_config`](../api-reference/flyte-sdk/packages/flyte#init_from_config):

```python
flyte.init_from_config("my-config.yaml")
run = flyte.run(main)
```

{{< dropdown title="Configuration precedence" icon="control_knobs" >}}
{{< markdown >}}

Without an explicit path, the SDK searches these locations in order:

1. `./config.yaml`
2. `./.flyte/config.yaml`
3. `UCTL_CONFIG` environment variable
4. `FLYTECTL_CONFIG` environment variable
5. `~/.union/config.yaml`
6. `~/.flyte/config.yaml`

{{< /markdown >}}
{{< /dropdown >}}

**CLI:**
```shell
flyte run hello.py main
```

**Python:**
```python
flyte.init_from_config()
```

### Check current configuration

```shell
flyte get config
```

Output shows the active configuration:

```shell
CLIConfig(
    Config(
        platform=PlatformConfig(endpoint='dns:///my-org.my-company.com', scopes=[]),
        task=TaskConfig(org='my-org', project='my-project', domain='development'),
        source=PosixPath('/Users/me/.flyte/config.yaml')
    ),
    ...
)
```

## Inline configuration

Skip the config file entirely by passing parameters directly.

### CLI

Some parameters go after `flyte`, others after the subcommand:

```shell
flyte \
    --endpoint my-org.my-company.com \
    --org my-org \
    run \
    --domain development \
    --project my-project \
    hello.py \
    main
```

See the [CLI reference](../api-reference/flyte-cli) for details.

### Python

Use [`flyte.init`](../api-reference/flyte-sdk/packages/flyte#init):

```python
flyte.init(
    endpoint="dns:///my-org.my-company.com",
    org="my-org",
    project="my-project",
    domain="development",
)
```

See related methods:

* [`flyte.init_from_api_key`](../api-reference/flyte-sdk/packages/flyte##init_from_api_key)
* [`flyte.init_from_config`](../api-reference/flyte-sdk/packages/flyte##init_from_config)
* [`flyte.init_in_cluster`](../api-reference/flyte-sdk/packages/flyte##init_in_cluster)
* [`flyte.init_passthrough`](../api-reference/flyte-sdk/packages/flyte##init_passthrough)

## Next steps

With your environment fully configured, you're ready to build:

- [**Core concepts**](./core-concepts): Understand `TaskEnvironment`s, tasks, runs, and actions through working examples.
