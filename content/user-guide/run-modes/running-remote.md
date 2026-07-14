---
title: Run on a remote cluster
weight: 6
variants: +flyte +union
---

# Run on a remote cluster

This guide covers setting up your local development environment and configuring the `flyte` CLI and SDK to connect to your {{< key product_name >}} instance.

{{< note >}}
Want to try Flyte without installing anything? [Try Flyte 2 in your browser](https://flyte2intro.apps.demo.hosted.unionai.cloud/).
{{< /note >}}

## Prerequisites

- **Python 3.10+**
- **`uv`** — A fast Python package installer. See the [`uv` installation guide](https://docs.astral.sh/uv/getting-started/installation/).
- Access to a {{< key product_name >}} instance (URL and a project where you can run workflows)

{{< variant flyte >}}
{{< markdown >}}
> [!NOTE]
> Don't have a Flyte cluster yet? See [Platform deployment](../../oss-deployment/_index)
> to stand one up, or use the [Devbox](./running-devbox) to run a local cluster in Docker.
{{< /markdown >}}
{{< /variant >}}
{{< variant union >}}
{{< markdown >}}
> [!NOTE]
> Don't have a Union.ai instance yet? See [Platform deployment](../../deployment/_index)
> to stand one up, or use the [Devbox](./running-devbox) to run a local cluster in Docker.
{{< /markdown >}}
{{< /variant >}}

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

As we did in [Quickstart](../quickstart), use `flyte create config` to create a configuration file:

{{< variant union >}}
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
    --builder local \
    --registry ghcr.io/my-org
```
{{< /markdown >}}
{{< /variant >}}

This creates `./.flyte/config.yaml`:

{{< variant union >}}
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
  registry: ghcr.io/my-org
task:
  org: my-org
  domain: development
  project: my-project
```
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
### Set up local Docker

The `--builder local` setting means container images are
[built locally](../task-configuration/container-images) on your machine and pushed to a
container registry that your Flyte cluster can pull from. You'll need Docker running and
logged into that registry, for example:

```bash
docker login ghcr.io
```

See [Image building](../task-configuration/container-images#image-building) for how to
specify the registry in your `Image` definitions. (Union instances can use
`--builder remote` instead, which builds images on the cluster with no local Docker
required.)
{{< /markdown >}}
{{< /variant >}}

{{< dropdown title="Full example with all options" icon="bento" >}}

{{< variant union >}}
{{< markdown >}}
Create a custom config file with all available options:
```bash
flyte create config \
    --endpoint my-org.my-company.com \
    --org my-org \
    --domain development \
    --project my-project \
    --builder remote \
    --registry ghcr.io/my-org \
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
    --registry ghcr.io/my-org \
    --insecure \
    --output my-config.yaml \
    --force
```
{{< /markdown >}}
{{< /variant >}}

{{< markdown >}}
See the [CLI reference](../../api-reference/flyte-cli#flyte-create-config) for all parameters.
{{< /markdown >}}

{{< /dropdown >}}

{{< dropdown title="Config properties explained" icon="control_knobs" >}}
{{< markdown >}}

**`admin`** — Connection details for your {{< key product_name >}} instance.

- `endpoint`: URL with `dns:///` prefix. If your UI is at `https://my-org.my-company.com`, use `dns:///my-org.my-company.com`.
- `insecure`: Set to `true` only for local instances without TLS.

**`image`** — Docker image building configuration.

- `builder`: How container images are built.
  - `remote` (Union): Images built on Union's infrastructure.
  - `local` (Flyte OSS): Images built on your machine. Requires Docker. See [Image building](../task-configuration/container-images#image-building).
- `registry`: Optional registry prefix to use for image builds. This is helpful when you want the SDK to push or pull images from a custom registry without changing your code. You can also set it with the `FLYTE_IMAGE_REGISTRY` environment variable.

**`task`** — Default settings for task execution.

- `org`: Organization name (usually matches the first part of your endpoint URL).
- `domain`: Environment separation (`development`, `staging`, `production`).
- `project`: Default project for deployments. Must already exist on your instance. See [Projects and domains](../core-concepts/projects-and-domains) for how to create projects.
{{< /markdown >}}
{{< /dropdown >}}

## Using the configuration

You can reference your config file explicitly or let the SDK find it automatically.

### Explicit configuration

{{< tabs "explicit-config" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
Initialize with `flyte.init_from_config`:

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
Use `flyte.init`:

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

See the [CLI reference](../../api-reference/flyte-cli) for details.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

See related methods:

* `flyte.init_from_api_key`
* `flyte.init_from_config`
* `flyte.init_in_cluster`
* `flyte.init_passthrough`

## Next steps

With your environment fully configured, you're ready to build:

- [**Core concepts**](../core-concepts/_index): Understand `TaskEnvironment`s, tasks, runs, and actions through working examples.
