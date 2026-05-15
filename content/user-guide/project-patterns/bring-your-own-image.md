---
title: Bring your own image (BYOI)
weight: 1
variants: +flyte +union
---

# Bring your own image

This guide is for teams who own their Docker images and want Flyte for orchestration without handing over their build pipeline.

> [!NOTE]
> This guide does **not** cover `flyte.Image.from_debian_base()`, the Flyte-managed image builder. It assumes you already have images.

## The multi-team problem

Two teams. Two images. One workflow.

| | Team A (data-prep) | Team B (training) |
|---|---|---|
| Base | `python:3.11-slim` | `python:3.10-slim` (prod: CUDA) |
| Python | 3.11 | 3.10 |
| WORKDIR | `/app` | `/workspace` |
| Packages | pandas, pyarrow | torch, numpy |

The `prepare` task runs in Team A's container. It processes the input and calls `train`, which runs in Team B's container. One workflow, two images, different filesystem layouts.

Two patterns solve this. Pick based on who controls what:

| | Pattern 1: Pure BYOI | Pattern 2: Remote Builder |
|---|---|---|
| Who owns the image? | Each team owns everything | Each team owns the base |
| Flyte-aware? | Yes — code is baked in | No — Flyte adapts on top |
| Code change = image rebuild? | Yes | No |
| Use when | Teams can't let Flyte touch images | Teams can hand off a base |

## Pattern 1: Pure BYOI

Teams build complete, Flyte-aware images. Workflow code is COPYed into the Dockerfile. Flyte runs the container as a black box — it sends no code and modifies nothing.

### Dockerfiles

Both teams install `flyte` and COPY the shared `workflow_code/` into their image. The only difference is their base, Python version, and WORKDIR.

**Team A (data prep):**

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/pure_byoi/data_prep/Dockerfile" lang="dockerfile" >}}

**Team B (training):**

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/pure_byoi/training/Dockerfile" lang="dockerfile" >}}

Both expose `import workflow_code.tasks` at runtime because each image's PYTHONPATH points to its own WORKDIR where the code was COPYed.

### Build and push

The build context is the `pure_byoi/` directory so that `workflow_code/` is available to both Dockerfiles:

```bash
docker build -f data_prep/Dockerfile -t <your-registry>/data-prep:latest .
docker build -f training/Dockerfile  -t <your-registry>/training:latest  .
docker push <your-registry>/data-prep:latest
docker push <your-registry>/training:latest
```

### Python code

**Environment definitions** — image names are specified via `from_ref_name()`:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/pure_byoi/workflow_code/envs.py" lang="python" >}}

`from_ref_name()` is a placeholder resolved at runtime. The actual URIs are passed in the entry point via `init_from_config(images=...)`. This is necessary because the envs file is COPYed into both images — hardcoding a URI would create a circular reference.

**Task definitions:**

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/pure_byoi/workflow_code/tasks.py" lang="python" >}}

**Entry point** — this is where image URIs are wired in:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/pure_byoi/main.py" lang="python" >}}

### Run and deploy

```bash
uv run main.py
```

There is no separate deploy step. The image tag is the version. To ship a code change: edit tasks, rebuild both images, push new tags, update the tag constants in `main.py`, run again.

## Pattern 2: Remote Builder

Teams hand you their base images. They built these images for their own purposes — Flyte was never a consideration. Your job is to adapt them.

{{< variant union >}}
{{< markdown >}}
> [!TIP]
> Want Union to optimize your images so image pulls for a new image (cold-start) drops from minutes to under a second? See [Layering on top of an existing image build](./cicd#layering-on-top-of-an-existing-image-build) for the equivalent flow when your base is built in CI.
{{< /markdown >}}
{{< /variant >}}

### The base images

**Team A** uses `continuumio/miniconda3` as their base:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/remote_builder/data_prep/Dockerfile" lang="dockerfile" >}}

- Python at `/opt/conda/bin/python` (conda manages this)
- conda's Dockerfile already adds `/opt/conda/bin` to `PATH`
- No PYTHONPATH set
- WORKDIR `/app`

**Team B** uses `python:3.10-slim` with a pip venv at `/opt/venv`:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/remote_builder/training/Dockerfile" lang="dockerfile" >}}

- Python at `/opt/venv/bin/python`
- `PATH` does **not** include `/opt/venv/bin` — the venv was created but never activated
- No PYTHONPATH set
- WORKDIR `/workspace`

### Adapting with `flyte.Image`

`flyte.Image.from_base()` takes the base URI and lets you layer on top. This is where the adaptation happens:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/remote_builder/tasks/envs.py" lang="python" >}}

**Team A** only needs `flyte` installed and `PYTHONPATH` set. conda's PATH is already correct.

**Team B** needs three things: `flyte` installed in the venv, `PATH` updated so the venv's `python` is the default, and `PYTHONPATH` set. `$PATH` in an `ENV` instruction expands at Docker build time.

`.with_code_bundle()` tells Flyte to inject task source at runtime (dev) or bake it into the image at deploy time (prod).

### Task definitions

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/remote_builder/tasks/tasks.py" lang="python" >}}

### Entry point

{{< code file="/unionai-examples/v2/user-guide/project-patterns/bring-your-own-image/remote_builder/main.py" lang="python" >}}

### Run and deploy

```bash
uv run main.py
```

During development you only rebuild the base image when the Dockerfile changes. Code changes are free — they travel as a tarball at runtime.

### Base image USER and WORKDIR requirements

The remote builder honors whatever `USER` and `WORKDIR` your base image declares — it does not override them. The runtime extracts the code bundle into the container's `WORKDIR` at the start of every task, so the resolved `USER` needs to be able to read, write, and traverse that directory.

#### What the runtime needs

The container's working directory must satisfy all three for the resolved `USER`:

| Permission | Why |
|---|---|
| `+x` (traverse) | The runtime stats the bundle path before extracting. |
| `+w` (write) | `tar -xvf` writes the extracted bundle here. |
| `+r` (read) | Subsequent imports resolve from this directory. |

A base image with `USER root` (or no `USER` declared) trivially satisfies this. Hardened bases that ship a non-root `USER` (UBI `nonroot` uid `65532`, distroless `nonroot`, chainguard `nonroot`) are fine **as long as their `WORKDIR` is a path that user owns** — for example `/home/nonroot`, `/app`, or `/workspace`. The trap is when a hardened base image leaves `WORKDIR` empty or set to `/root`: that path is typically owned by `root` with mode `0700`, and the non-root `USER` cannot use it.

#### What you'll see

The remote builder logs the resolved runtime identity at the end of every build:

```text
Built image runtime identity: USER="nonroot" WORKDIR="/home/nonroot" (base: registry.example.com/ubi9-minimal/python3.13-runtime:3.13.0)
```

If the resolved `USER` and `WORKDIR` are incompatible (non-root `USER` with `WORKDIR` set to `""`, `/`, or `/root`), the builder emits a warning naming the problem and pointing here. **Fix the base image when you see this warning.** The runtime will not crash on the broken combination, but that's a fail-safe to keep workflows running while you fix the image — not a supported configuration. If you ignore the warning, you'll also see this line in your task pod logs at every task start:

```text
CWD /root not writable for current user; rerouting code bundle to /tmp/flyte-bundle/<version>
```

Treat that line as an unfixed-bug indicator. The platform behavior around it may change.

#### Inspecting your base image

`docker inspect <your-image>` shows the two fields you need to reconcile:

```json
"Config": {
  "User": "nonroot",
  "WorkingDir": "/root",
  ...
}
```

In that example, `User` is non-root but `WorkingDir` is `/root` — the runtime warning will fire. Fix the base image's Dockerfile:

```dockerfile
USER nonroot
WORKDIR /home/nonroot
```

#### If you cannot modify the base image

If you do not control the base image, layer a `WORKDIR` fix into the Flyte build with `.with_commands()`:

```python
env = flyte.TaskEnvironment(
    name="hello_world_private_artifactory",
    image=flyte.Image.from_base("registry.example.com/ubi9-minimal/python3.13-runtime:3.13.0")
    .clone(
        registry="registry.example.com/team-images",
        registry_secret="image-builder-secret",
        name="hello-world",
        extendable=True,
    )
    .with_pip_packages("flyte")
    # Make the base image's WORKDIR writable for the declared USER.
    # Look up the uid:gid your base image uses with `docker inspect <image> --format '{{.Config.User}}'`.
    .with_commands(["chmod 0755 /root && chown 65532:65532 /root"]),
)
```

If your base image uses a different working directory (for example `/app`), substitute that path. If it uses a username instead of a numeric uid, resolve it via `getent passwd <name>` inside the image first.

## Decision matrix

| Scenario | Pattern |
|---|---|
| Teams own full images, can't let Flyte touch them | Pure BYOI |
| Teams hand off a base image (no Flyte knowledge required) | Remote Builder |
| Code change should not require image rebuild | Remote Builder + `with_code_bundle()` |
| Base has non-standard Python location | `.with_commands()` to fix PATH before Flyte uses it |
| Base runs as a non-root `USER` | Make sure base's `WORKDIR` is owned by that `USER`; if not, use `.with_commands()` to fix it (see above) |
| Production deploy, self-contained containers | `copy_style="none"` in `flyte.deploy()` |
