---
title: Connecting to a cluster
weight: 5
variants: +flyte +byoc +selfmanaged
---

# Connecting to a cluster

This guide covers setting up your local development environment and configuring the `flyte` CLI and SDK to connect to your Union/Flyte instance.

{{< note >}}
Want to try Flyte without installing anything? [Try Flyte 2 in your browser](https://flyte2intro.apps.demo.hosted.unionai.cloud/).
{{< /note >}}

## Prerequisites

- **Python 3.10+**
- **`uv`** — A fast Python package installer. See the [`uv` installation guide](https://docs.astral.sh/uv/getting-started/installation/).
- Access to a Union/Flyte instance (URL and a project where you can run workflows)

## Install the flyte package

Create a virtual environment and install the `flyte` package:

```bash
uv venv
source .venv/bin/activate
uv pip install flyte
```

> [!NOTE]
> On Windows, use `.venv\Scripts\activate` instead.

Verify installation:

```bash
flyte --version
```

## Configuration file

As we did in [Quickstart](./quickstart), use `flyte create config` to create a configuration file:

{{< variant byoc selfmanaged >}}
{{< markdown >}}
```bash
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
```bash
flyte create config \
    --endpoint my-org.my-company.com \
    --domain development \
    --project my-project \
    --builder local
```
{{< /markdown >}}
{{< /variant >}}

This creates `./.flyte/config.yaml`:

{{< variant byoc selfmanaged >}}
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

{{< variant byoc selfmanaged >}}
{{< markdown >}}
Create a custom config file with all available options:
```bash
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
```bash
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

### Set up local Docker

Since Flyte OSS uses local image building, you'll need Docker running and logged into the GitHub registry:

```bash
docker login ghcr.io
```

> [!NOTE]
> The `--builder local` option means images are [built locally](./task-configuration/container-images). Union instances can use `--builder remote` instead.

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
- `project`: Default project for deployments. Must already exist on your instance. See [Projects and domains](./projects-and-domains) for how to create projects.
{{< /markdown >}}
{{< /dropdown >}}

## Using the configuration

You can reference your config file explicitly or let the SDK find it automatically.

### Explicit configuration

{{< tabs "explicit-config" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
Initialize with [`flyte.init_from_config`](../api-reference/flyte-sdk/packages/flyte/_index#init_from_config):

```python
flyte.init_from_config("my-config.yaml")
run = flyte.run(main)
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
Use `--config` or `-c`:

```bash
flyte --config my-config.yaml run hello.py main
flyte -c my-config.yaml run hello.py main
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

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

{{< tabs "auto-config" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
```python
flyte.init_from_config()
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
```bash
flyte run hello.py main
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Check current configuration

```bash
flyte get config
```

Output:

```bash
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

{{< tabs "inline-config" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
Use [`flyte.init`](../api-reference/flyte-sdk/packages/flyte/_index#init):

```python
flyte.init(
    endpoint="dns:///my-org.my-company.com",
    org="my-org",
    project="my-project",
    domain="development",
)
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
Some parameters go after `flyte`, others after the subcommand:

```bash
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
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

See related methods:

* [`flyte.init_from_api_key`](../api-reference/flyte-sdk/packages/flyte/_index#init_from_api_key)
* [`flyte.init_from_config`](../api-reference/flyte-sdk/packages/flyte/_index#init_from_config)
* [`flyte.init_in_cluster`](../api-reference/flyte-sdk/packages/flyte/_index#init_in_cluster)
* [`flyte.init_passthrough`](../api-reference/flyte-sdk/packages/flyte/_index#init_passthrough)

## Next steps

With your environment fully configured, you're ready to build:

- [**Core concepts**](./core-concepts/_index): Understand `TaskEnvironment`s, tasks, runs, and actions through working examples.
