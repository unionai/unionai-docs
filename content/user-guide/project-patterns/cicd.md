---
title: CI/CD deployments
weight: 3
variants: +flyte +union
---

# CI/CD deployments

This guide walks through deploying a Flyte project from CI. It uses GitHub Actions as the reference implementation, but the building blocks (a non-interactive credential, `flyte deploy`, and a commit-pinned version) translate to GitLab CI, Buildkite, CircleCI, or any runner that can run a Python script.

The examples below assume the project layout and image definitions from the [Monorepo with uv](./monorepo-with-uv) pattern; that guide covers how to structure `pyproject.toml`, `envs.py`, and task modules in a way that makes the `flyte deploy` commands shown here work cleanly.

## What CI needs to do

A deploy pipeline has three jobs:

1. **Install** the project and the `flyte` CLI.
2. **Authenticate** non-interactively against your instance.
3. **Run `flyte deploy`** for every `TaskEnvironment` in your project, pinned to the commit SHA.

Everything else (branch protections, approvals, notifications) is generic CI concerns and out of scope.

{{< variant union >}}
{{< markdown >}}

## Authentication: API keys

Locally, `flyte deploy` typically authenticates via a browser login (PKCE). A CI runner has no browser and no human to click through a consent screen, so you need a credential the CLI can use without any prompts: an **API key**.

### Mint the key

The `flyte create api-key` command is provided by the `flyteplugins-union` package. Add it to a dev dependency group so it's available locally but not baked into task images:

```toml
# pyproject.toml
[dependency-groups]
dev = ["flyteplugins-union"]
```

Then, from a machine already logged in to your instance:

```bash
uv run flyte create api-key --name ci-cd-key
```

The output is a single base64-encoded string of the form `endpoint:client_id:client_secret:org`. **It's shown only once**: copy it immediately.

The creation call doesn't take a permissions argument: the key is created under the caller's organization and identity context. If you need the key's privileges to be narrower than the minting user's, assign a dedicated role or policy to the key's identity using `flyte create role`, `flyte create policy`, and `flyte create assignment`.

### Store the key as a CI secret

Add the string to your CI system's secret store. However it's configured, the secret needs to:

- Be exposed to the deploy job as an environment variable named `FLYTE_API_KEY`.
- Be masked in logs (most CI systems do this automatically for secrets).
- Be scoped to the branches/environments that actually deploy: typically `main` or a release branch, not every feature branch or fork PR.

When `FLYTE_API_KEY` is present in the environment at deploy time, the `flyte` CLI uses it for `ClientSecret` auth, overriding any auth mode configured in `config.yaml`.

### Key scope and rotation

The key inherits the permissions of the user who minted it. For CI you typically want a dedicated service identity with narrow scope: deploy rights on the target project/domain only. Rotate on a schedule (90 days is a reasonable default) by running `flyte create api-key` again and updating the secret.
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}

## Authentication: client credentials

Locally, `flyte deploy` typically authenticates via a browser login (PKCE). A CI runner has no browser and no human to click through a consent screen, so you need a credential the CLI can use without any prompts. For Flyte OSS this is an **OAuth2 client-credentials** application: a client ID and client secret for a machine ("service") identity that your instance's identity provider (IdP) trusts.

### Register a client-credentials application

Client-credentials applications are provisioned in your **identity provider**, not through the `flyte` CLI. (The `flyte create api-key` command referenced elsewhere is a Union feature from the `flyteplugins-union` package and isn't available in Flyte OSS.) The exact steps depend on the IdP your instance is configured against (Okta, Keycloak, Auth0, Google, Azure AD, and so on), but the result is always a **client ID** and a **client secret**.

Ask whoever administers your instance for:

- The **client ID** of a service application authorized to register tasks in the target project and domain.
- The matching **client secret**.
- The admin **endpoint**: the same host you pass to `flyte create config`.

> [!NOTE]
> The application must be granted whatever scopes your admin API requires. Provisioning and scoping the IdP application is an instance-administration task; see your instance's authentication setup for the specifics.

### Store the secret as a CI secret

Add the **client secret** to your CI system's secret store. However it's configured, the secret needs to:

- Be exposed to the deploy job as an environment variable (this guide uses `FLYTE_CLIENT_SECRET`).
- Be masked in logs (most CI systems do this automatically for secrets).
- Be scoped to the branches/environments that actually deploy: typically `main` or a release branch, not every feature branch or fork PR.

The client ID and endpoint aren't secret; they live in the `config.yaml` you check into the repo (see [below](#project-configuration)). Only the client secret goes in the secret store.

### Point the CLI at the credential

The `flyte` CLI reads client-credentials settings from `config.yaml` under `admin:`:

- **`authType: ClientSecret`** selects the OAuth2 client-credentials flow instead of the interactive PKCE default.
- **`clientId`** is the application's client ID.
- **`clientSecretEnvVar`** names the environment variable the CLI reads the secret from: `FLYTE_CLIENT_SECRET` here. (Alternatively, `clientSecretLocation` points at a file containing the secret, which suits runners that mount secrets as files rather than env vars.)

### Scope and rotation

Grant the service identity only the permissions CI needs: deploy rights on the target project/domain, nothing more. Rotate the client secret on a schedule (90 days is a reasonable default) in your IdP and update the CI secret to match.
{{< /markdown >}}
{{< /variant >}}

## Project configuration

Two files drive `flyte deploy` behavior in CI: `pyproject.toml` (or `uv.lock`) for dependencies, and `config.yaml` for your endpoint and image-builder settings.

### `config.yaml`

Save this at `.flyte/config.yaml` (or `config.yaml`) in your repo and check it in. In CI the `flyte` CLI auto-discovers config from the repo checkout: repo-relative paths (`./config.yaml`, `./.flyte/config.yaml`, `<git-root>/.flyte/config.yaml`) take precedence over any home-directory config, so it's picked up automatically after checkout with no `--config` flag needed. See [the config discovery order](../../api-reference/flyte-sdk/packages/flyte.config/_index#auto) for the full precedence; pass `--config <path>` only to point at a non-standard location.

{{< variant union >}}
{{< markdown >}}
It supplies the project, domain, and image builder settings, the things the API key doesn't carry:

```yaml
admin:
  endpoint: dns:///<your-instance>.hosted.unionai.cloud
image:
  builder: remote
task:
  project: <default-project>
  domain: development
```

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
It supplies the endpoint, the client-credentials auth settings, and the (local) image builder, everything `flyte deploy` needs beyond the client secret:

```yaml
admin:
  endpoint: dns:///<your-flyte-host>
  authType: ClientSecret
  clientId: <client-id>
  clientSecretEnvVar: FLYTE_CLIENT_SECRET
image:
  builder: local
task:
  project: <default-project>
  domain: development
```

The `clientId` and `endpoint` are safe to commit; only the client secret named by `clientSecretEnvVar` comes from the CI secret store. `builder: local` means images are built on the runner with Docker (Flyte OSS has no remote builder). See [Container images](../task-configuration/container-images#image-building).
{{< /markdown >}}
{{< /variant >}}

## The GitHub Actions workflow

A minimal deploy workflow, one job, one step per `TaskEnvironment`:

{{< variant union >}}
{{< markdown >}}

```yaml
# .github/workflows/deploy.yml
name: Deploy to Union

on:
  push:
    branches: [main]
  workflow_dispatch:

env:
  FLYTE_PROJECT: my-project
  FLYTE_DOMAIN: development

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true

      - name: Sync dependencies
        run: uv sync --group etl --group ml --group dev

      - name: Deploy etl_env
        env:
          FLYTE_API_KEY: ${{ secrets.FLYTE_API_KEY }}
        run: |
          uv run flyte deploy \
            --copy-style none \
            --version ${{ github.sha }} \
            --project "$FLYTE_PROJECT" \
            --domain "$FLYTE_DOMAIN" \
            src/workspace_app/tasks/etl_tasks.py etl_env

      - name: Deploy ml_env
        env:
          FLYTE_API_KEY: ${{ secrets.FLYTE_API_KEY }}
        run: |
          uv run flyte deploy \
            --copy-style none \
            --version ${{ github.sha }} \
            --project "$FLYTE_PROJECT" \
            --domain "$FLYTE_DOMAIN" \
            src/workspace_app/tasks/ml_tasks.py ml_env
```

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}
The client ID and endpoint live in the checked-in `config.yaml` (auto-discovered from the repo, as above); each deploy step injects the client secret from the CI secret store.

```yaml
# .github/workflows/deploy.yml
name: Deploy to Flyte

on:
  push:
    branches: [main]
  workflow_dispatch:

env:
  FLYTE_PROJECT: my-project
  FLYTE_DOMAIN: development

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true

      - name: Sync dependencies
        run: uv sync --group etl --group ml

      - name: Deploy etl_env
        env:
          FLYTE_CLIENT_SECRET: ${{ secrets.FLYTE_CLIENT_SECRET }}
        run: |
          uv run flyte deploy \
            --copy-style none \
            --version ${{ github.sha }} \
            --project "$FLYTE_PROJECT" \
            --domain "$FLYTE_DOMAIN" \
            src/workspace_app/tasks/etl_tasks.py etl_env

      - name: Deploy ml_env
        env:
          FLYTE_CLIENT_SECRET: ${{ secrets.FLYTE_CLIENT_SECRET }}
        run: |
          uv run flyte deploy \
            --copy-style none \
            --version ${{ github.sha }} \
            --project "$FLYTE_PROJECT" \
            --domain "$FLYTE_DOMAIN" \
            src/workspace_app/tasks/ml_tasks.py ml_env
```

Because Flyte OSS builds images locally, the deploy steps need Docker available on the runner (the `ubuntu-latest` image includes it) and access to your container registry; add a `docker login` step for private registries before the first deploy.
{{< /markdown >}}
{{< /variant >}}

### Key flag choices

- **`--copy-style none`**: bakes source into the image as part of the build layer. Combined with `.with_code_bundle()` on your `flyte.Image` (see [Monorepo with uv](./monorepo-with-uv)), this resolves to a `COPY` instruction so the image is fully self-contained. This is the production path: one immutable artifact per commit, no runtime code bundle download.
- **`--version ${{ github.sha }}`**: makes deploys idempotent and traceable. Re-running the same commit produces the same version identifier; tasks already registered at that version are no-ops.
- **Path argument points at the task file, not `envs.py`.** `flyte deploy` only imports the file you give it, so tasks decorated with `@env.task` in separate files won't register unless you point at (or transitively import) those files. Pointing at `etl_tasks.py` pulls in `envs.py` via its import chain and runs the `@etl_env.task` decorators. As an alternative, you can point at a directory and pass `--recursive` to load every task module under it in one command. For a `src/` layout project, also pass `--root-dir src` so shared modules like `envs.py` resolve to a single import path instead of being loaded twice:

{{< variant union >}}
{{< markdown >}}

  ```yaml
  - name: Deploy all envs
    env:
      FLYTE_API_KEY: ${{ secrets.FLYTE_API_KEY }}
    run: |
      uv run flyte deploy \
        --copy-style none \
        --version ${{ github.sha }} \
        --project "$FLYTE_PROJECT" \
        --domain "$FLYTE_DOMAIN" \
        --root-dir src --recursive src/workspace_app/tasks
  ```

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

  ```yaml
  - name: Deploy all envs
    env:
      FLYTE_CLIENT_SECRET: ${{ secrets.FLYTE_CLIENT_SECRET }}
    run: |
      uv run flyte deploy \
        --copy-style none \
        --version ${{ github.sha }} \
        --project "$FLYTE_PROJECT" \
        --domain "$FLYTE_DOMAIN" \
        --root-dir src --recursive src/workspace_app/tasks
  ```

{{< /markdown >}}
{{< /variant >}}

### Splitting build from deploy

`flyte deploy` builds any missing images before it registers tasks. If you'd rather treat image builds as a separate CI concern (for clearer logs, independent retry, or parallel builds per env), run `flyte build` first and let deploy reuse the result:

{{< variant union >}}
{{< markdown >}}

```yaml
- name: Build etl image
  env:
    FLYTE_API_KEY: ${{ secrets.FLYTE_API_KEY }}
  run: |
    uv run flyte build \
      --copy-style none --root-dir src \
      src/workspace_app/tasks/etl_tasks.py etl_env

- name: Deploy etl_env
  env:
    FLYTE_API_KEY: ${{ secrets.FLYTE_API_KEY }}
  run: |
    uv run flyte deploy \
      --copy-style none \
      --version ${{ github.sha }} \
      --project "$FLYTE_PROJECT" --domain "$FLYTE_DOMAIN" \
      --root-dir src src/workspace_app/tasks/etl_tasks.py etl_env
```

{{< /markdown >}}
{{< /variant >}}
{{< variant flyte >}}
{{< markdown >}}

```yaml
- name: Build etl image
  env:
    FLYTE_CLIENT_SECRET: ${{ secrets.FLYTE_CLIENT_SECRET }}
  run: |
    uv run flyte build \
      --copy-style none --root-dir src \
      src/workspace_app/tasks/etl_tasks.py etl_env

- name: Deploy etl_env
  env:
    FLYTE_CLIENT_SECRET: ${{ secrets.FLYTE_CLIENT_SECRET }}
  run: |
    uv run flyte deploy \
      --copy-style none \
      --version ${{ github.sha }} \
      --project "$FLYTE_PROJECT" --domain "$FLYTE_DOMAIN" \
      --root-dir src src/workspace_app/tasks/etl_tasks.py etl_env
```

{{< /markdown >}}
{{< /variant >}}

Image tags are content hashes of the `flyte.Image` definition: `flyte build` pushes `<registry>:flyte-<hash>`, and `flyte deploy` computes the same hash, sees the image already in the registry, and skips rebuilding. `--copy-style` must match between the two commands; otherwise the hashes diverge and deploy will build again.

{{< variant union >}}
{{< markdown >}}

## Layering on top of an existing image build

If your team already builds container images in CI from a Dockerfile, you can still route them through `flyte build` to get **lazy-loading container pulls**: pod startup that's seconds instead of minutes, regardless of image size. On a 5GB image we measured cold-node pull time drop from ~1m37s to **839ms**, and published benchmarks show 9.9GB CUDA + PyTorch images going from 4m38s to ~1.2s, roughly 240×.

You get this for free whenever you use `flyte.Image` with the remote builder. Images built outside of it, straight from your own `docker build` and `docker push`, don't get the optimization, which is why this section adds a single `flyte build` step on top of your existing pipeline.

How it works: rather than downloading the full image up front, the cluster fetches a small (~14MB) metadata index, mounts the filesystem immediately, and streams file chunks from the registry as the container actually reads them. Files the task never touches never transfer, and chunks are cached on the node so subsequent pulls of the same or related images are sub-second.

The CI shape is two stages: your existing job builds and pushes the base, then a follow-up job runs `flyte build` to layer on top and `flyte deploy` to register tasks against the result.

```yaml
# .github/workflows/deploy.yml
jobs:
  build-base:
    runs-on: ubuntu-latest
    outputs:
      base_uri: ${{ steps.build.outputs.uri }}
    steps:
      # Whatever your team already does to build and push the base image.
      # Output the full URI tagged with the commit SHA.
      - id: build
        run: |
          ./your-existing-build.sh
          echo "uri=ghcr.io/myorg/base:${{ github.sha }}" >> "$GITHUB_OUTPUT"

  deploy:
    needs: build-base
    runs-on: ubuntu-latest
    env:
      BASE_IMAGE: ${{ needs.build-base.outputs.base_uri }}
      FLYTE_API_KEY: ${{ secrets.FLYTE_API_KEY }}
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
      - run: uv sync --group dev
      - run: uv run flyte build --copy-style none --root-dir src src/myproj/envs.py train_env
      - run: uv run flyte deploy --copy-style none --version ${{ github.sha }} --root-dir src src/myproj/envs.py train_env
```

`envs.py` reads the base URI from the environment, so each commit's overlay is pinned to that commit's base:

```python
# src/myproj/envs.py
import os
import flyte

train_env = flyte.TaskEnvironment(
    name="train",
    image=flyte.Image.from_base(os.environ["BASE_IMAGE"]).clone(
        name="train", extendable=True,
    ),
)
```

> [!NOTE]
> This snippet assumes the base image already has the `flyte` SDK installed and your task code on the right `PYTHONPATH`. If it doesn't, see [Bring your own image: Pattern 2](./bring-your-own-image#pattern-2-remote-builder) for the `with_commands()` / `with_env_vars()` / `with_code_bundle()` calls that adapt a Flyte-unaware base.

The `flyte build` job is idempotent; it skips when the same image content has already been published. Workflow code edits don't trigger image rebuilds; only `envs.py` or base-image changes do.
{{< /markdown >}}
{{< /variant >}}
