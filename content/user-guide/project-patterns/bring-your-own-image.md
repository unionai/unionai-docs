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

## Decision matrix

| Scenario | Pattern |
|---|---|
| Teams own full images, can't let Flyte touch them | Pure BYOI |
| Teams hand off a base image (no Flyte knowledge required) | Remote Builder |
| Code change should not require image rebuild | Remote Builder + `with_code_bundle()` |
| Base has non-standard Python location | `.with_commands()` to fix PATH before Flyte uses it |
| Production deploy, self-contained containers | `copy_style="none"` in `flyte.deploy()` |
