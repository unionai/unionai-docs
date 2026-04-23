---
title: CI/CD deployments
weight: 3
variants: -flyte +union
---

# CI/CD deployments

This guide walks through deploying a Flyte project from CI. It uses GitHub Actions as the reference implementation, but the building blocks — an API key secret, `flyte deploy`, and a commit-pinned version — translate to GitLab CI, Buildkite, CircleCI, or any runner that can run a Python script.

The examples below assume the project layout and image definitions from the [Monorepo with uv](./monorepo-with-uv) pattern — that guide covers how to structure `pyproject.toml`, `envs.py`, and task modules in a way that makes the `flyte deploy` commands shown here work cleanly.

## What CI needs to do

A deploy pipeline has three jobs:

1. **Install** the project and the `flyte` CLI.
2. **Authenticate** non-interactively against your tenant.
3. **Run `flyte deploy`** for every `TaskEnvironment` in your project, pinned to the commit SHA.

Everything else — branch protections, approvals, notifications — is generic CI concerns and out of scope.

## Authentication: API keys

Locally, `flyte deploy` typically authenticates via a browser login (PKCE). A CI runner has no browser and no human to click through a consent screen, so you need a credential the CLI can use without any prompts — an **API key**.

### Mint the key

The `flyte create api-key` command is provided by the `flyteplugins-union` package. Add it to a dev dependency group so it's available locally but not baked into task images:

```toml
# pyproject.toml
[dependency-groups]
dev = ["flyteplugins-union"]
```

Then, from a machine already logged in to your tenant:

```bash
uv run flyte create api-key --name ci-cd-key
```

The output is a single base64-encoded string of the form `endpoint:client_id:client_secret:org`. **It's shown only once** — copy it immediately.

The creation call doesn't take a permissions argument — the key is created under the caller's organization and identity context. If you need the key's privileges to be narrower than the minting user's, assign a dedicated role or policy to the key's identity using `flyte create role`, `flyte create policy`, and `flyte create assignment`.

### Store the key as a CI secret

Add the string to your CI system's secret store. However it's configured, the secret needs to:

- Be exposed to the deploy job as an environment variable named `FLYTE_API_KEY`.
- Be masked in logs (most CI systems do this automatically for secrets).
- Be scoped to the branches/environments that actually deploy — typically `main` or a release branch, not every feature branch or fork PR.

When `FLYTE_API_KEY` is present in the environment at deploy time, the `flyte` CLI uses it for `ClientSecret` auth, overriding any auth mode configured in `config.yaml`.

### Key scope and rotation

The key inherits the permissions of the user who minted it. For CI you typically want a dedicated service identity with narrow scope — deploy rights on the target project/domain only. Rotate on a schedule (90 days is a reasonable default) by running `flyte create api-key` again and updating the secret.

## Project configuration

Two files drive `flyte deploy` behavior in CI: `pyproject.toml` (or `uv.lock`) for dependencies, and `config.yaml` for tenant endpoints.

### `config.yaml`

Check this into the repo. It supplies everything `FLYTE_API_KEY` doesn't — `org`, `project`, `domain`, and the image builder setting:

```yaml
admin:
  endpoint: dns:///<tenant>.hosted.unionai.cloud
image:
  builder: remote
task:
  org: <your-org>
  project: <default-project>
  domain: development
```

`FLYTE_API_KEY` overrides only the **auth fields** (endpoint, client_id, client_secret, `auth_mode`). Everything else — `org`, `task.project`, `task.domain`, `image.builder` — can come from `config.yaml`.

## The GitHub Actions workflow

A minimal deploy workflow — one job, one step per `TaskEnvironment`:

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

### Key flag choices

- **`--copy-style none`** — bakes source into the image as part of the build layer. Combined with `.with_code_bundle()` on your `flyte.Image` (see [Monorepo with uv](../monorepo-with-uv#with_code_bundle-one-image-for-dev-and-prod)), this resolves to a `COPY` instruction so the image is fully self-contained. This is the production path: one immutable artifact per commit, no runtime code bundle download.
- **`--version ${{ github.sha }}`** — makes deploys idempotent and traceable. Re-running the same commit produces the same version identifier; tasks already registered at that version are no-ops.
- **Path argument points at the task file, not `envs.py`.** `flyte deploy` only imports the file you give it, so tasks decorated with `@env.task` in separate files won't register unless you point at (or transitively import) those files. Pointing at `etl_tasks.py` pulls in `envs.py` via its import chain and runs the `@etl_env.task` decorators. As an alternative, you can point at a directory and pass `--recursive` to load every task module under it in one command — for a `src/` layout project, also pass `--root-dir src` so shared modules like `envs.py` resolve to a single import path instead of being loaded twice:

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

### Splitting build from deploy

`flyte deploy` builds any missing images before it registers tasks. If you'd rather treat image builds as a separate CI concern — for clearer logs, independent retry, or parallel builds per env — run `flyte build` first and let deploy reuse the result:

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

Image tags are content hashes of the `flyte.Image` definition: `flyte build` pushes `<registry>:flyte-<hash>`, and `flyte deploy` computes the same hash, sees the image already in the registry, and skips rebuilding. `--copy-style` must match between the two commands — otherwise the hashes diverge and deploy will build again.
