---
title: Monorepo with uv
weight: 2
variants: +flyte +union
---

# Structuring Flyte projects with uv

## The two layers

Every Flyte + uv project involves two distinct layers. Understanding this distinction is the foundation for every decision that follows.

**The image** (slow-changing): the Python environment, installed packages, system dependencies, the interpreter. The SDK computes an MD5 hash of the image's layer stack and only rebuilds when a layer actually changes.

**The code bundle** (fast-changing): your task source code, packaged as a tarball and uploaded on every run. The container downloads and unpacks it at startup.

```
+-----------------------------------+
|       Docker Image (slow path)    |
|  Python interpreter               |
|  Installed packages (uv sync)     |  <- rebuilt only when deps change
|  System packages (apt)            |
|  Content-hashed, registry-cached  |
+-----------------------------------+
|       Code Bundle (fast path)     |
|  Your task source files           |  <- uploaded on every run
|  Local library code               |
|  Tarball extracted at startup     |
+-----------------------------------+
```

Keep these two layers separate. Your image definition should describe only the environment. Source code travels in the code bundle (in fast-deploy mode) or gets baked in at deploy time (in full-build mode).

Violating this principle (copying source into the image with `with_source_folder()` or using `install_project` mode for local code) means your image hash changes on every code edit, causing a full Docker build and push on every iteration.

## How the image gets built

`flyte.Image` is a frozen, content-addressed layer stack. Each `.with_*()` call appends an immutable layer. The final image tag is an MD5 hash of all layers.

The primary method for uv projects is `.with_uv_project()`:

```python
image = flyte.Image.from_debian_base().with_uv_project(
    pyproject_file=Path("my_app/pyproject.toml"),
)
```

**Two installation modes:**

- `dependencies_only` (default): Only `pyproject.toml` and `uv.lock` are included in the build context. The image hash covers only these two files. Your code does not affect the image hash.

- `install_project`: The entire project directory is copied into the build context. Any code change triggers a full image rebuild. Use this only when you need the project installed as a proper package (e.g., when you need package entry points or compiled extension modules).

## `with_code_bundle()` — one image for dev and prod

`with_code_bundle()` is how you write an image definition that works for both development and production without changing any code.

```python
image = (
    flyte.Image.from_debian_base()
    .with_uv_project(pyproject_file=Path("pyproject.toml"))
    .with_code_bundle()
)
```

Its behavior depends on `copy_style` at run time:

- **Fast deploy** (default): `with_code_bundle()` is a no-op. Source travels as a tarball. The image only rebuilds when `pyproject.toml` or `uv.lock` changes.
- **Full build** (`copy_style="none"`): `with_code_bundle()` resolves to a `COPY` instruction. Source is baked into the image. This is your production path.

```python
# Development
flyte.run(my_task)

# Production
flyte.deploy(my_env, copy_style="none", version="1.2.3")
```

## `root_dir`

`root_dir` tells Flyte where to look when building the code bundle and what path prefix to strip when packaging.

**The rule:** set `root_dir` to the directory you would `cd` into before running `python -c "import my_module"`.

For **src-layout** projects, set `root_dir` to `src/`:

```python
flyte.init_from_config(root_dir=Path(__file__).parent.parent)  # -> src/
```

For **flat layout** projects, set `root_dir` to the project root:

```python
flyte.init_from_config(root_dir=Path(__file__).parent)  # -> my_project/
```

## Monorepo patterns

Three patterns cover most cases:

| | Pattern A: Shared Lockfile | Pattern B: Independent Packages | Pattern C: uv workspace |
|---|---|---|---|
| Lockfile | One `uv.lock` for everything | Each package has its own | One `uv.lock` for the whole workspace |
| Package model | Single package; libraries are modules under one `src/` | Separate, independently-locked packages | Multiple installable members sharing the root lockfile |
| Sibling code reaches the container via | Code bundle (fast deploy) | `with_source_folder()` baked into the image | uv install of workspace members (fast deploy preserved) |
| Use when | Packages developed together, shared dep graph | Different release cadences, fully independent | Multiple versioned packages developed and locked together |

### Pattern A: Shared lockfile (recommended)

All packages live under one `src/` directory with a single `pyproject.toml` and `uv.lock`. Tasks install different subsets via dependency groups.

```
workspace_root/
├── pyproject.toml         <- defines dependency groups
├── uv.lock                <- one lockfile for everything
└── src/
    ├── workspace_app/
    │   ├── main.py
    │   └── tasks/
    │       ├── envs.py
    │       ├── etl_tasks.py
    │       └── ml_tasks.py
    ├── lib_transforms/
    │   └── ops.py
    └── lib_models/
        └── baseline.py
```

**`pyproject.toml`** — only external PyPI deps in dependency groups. Local libraries travel via the code bundle:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/01_workspace_monorepo/pyproject.toml" lang="toml" >}}

**Per-task images using dependency groups:**

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/01_workspace_monorepo/src/workspace_app/tasks/envs.py" lang="python" >}}

Both `etl_env` and `ml_env` point to the same `pyproject.toml` but install different dependency groups. The `extra_args` string is included in the image hash, so they produce separate images.

**ETL tasks** (use the shared `lib_transforms` library):

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/01_workspace_monorepo/src/workspace_app/tasks/etl_tasks.py" lang="python" >}}

**ML tasks** (use the shared `lib_models` library):

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/01_workspace_monorepo/src/workspace_app/tasks/ml_tasks.py" lang="python" >}}

**Entry point** — `root_dir` is set to `src/` so the code bundle covers all packages:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/01_workspace_monorepo/src/workspace_app/main.py" lang="python" >}}

### Pattern B: Independent packages

Each package has its own `pyproject.toml` and `uv.lock`. Fully independent image builds.

```
repo_root/
├── pyproject.toml         <- dev-only convenience (optional)
├── my_app/
│   ├── pyproject.toml     <- lists external deps + my-lib as editable path dep
│   ├── uv.lock            <- deployment lockfile
│   └── src/my_app/
│       ├── env.py
│       ├── main.py
│       └── tasks.py
└── my_lib/
    ├── pyproject.toml
    └── src/my_lib/
        └── stats.py
```

**Root `pyproject.toml`** — dev-only, installs both packages as editable for local development:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/02_sibling_packages/pyproject.toml" lang="toml" >}}

**`my_app/pyproject.toml`** — declares `my-lib` as an editable path dep:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/02_sibling_packages/my_app/pyproject.toml" lang="toml" >}}

**Image definition** — sibling library baked into the image via `with_source_folder()`:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/02_sibling_packages/my_app/src/my_app/env.py" lang="python" >}}

`with_source_folder(MY_LIB_PKG)` copies the `my_lib` package directory into the image at `/root/my_lib/`. This is necessary because the editable install's `.pth` file points to a path that only exists during the image build stage. The `my_lib` layer is part of the image hash, so the image rebuilds when `my_lib` changes — correct behavior for a dependency.

**Task definitions:**

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/02_sibling_packages/my_app/src/my_app/tasks.py" lang="python" >}}

**Entry point** — `root_dir` covers only `my_app` source; `my_lib` is baked into the image:

{{< code file="/unionai-examples/v2/user-guide/project-patterns/monorepo-with-uv/02_sibling_packages/my_app/src/my_app/main.py" lang="python" >}}

### Pattern C: uv workspace (`[tool.uv.workspace]`)

A uv *workspace* is uv's native mechanism for a multi-package repository: several packages share **one root `uv.lock`**, and any package can depend on its siblings through `[tool.uv.sources]` entries marked `{ workspace = true }`. Unlike Pattern A, each member is a real installable package rather than a plain module under a shared `src/`; unlike Pattern B, you manage a single lockfile for the whole tree instead of one per package.

Reach for a workspace when your packages are distinct, versioned distributions that are nonetheless developed and locked together.

```
albatross/
├── pyproject.toml         <- workspace root: [tool.uv.workspace] + shared deps
├── uv.lock                <- ONE lockfile for the whole workspace
├── src/
│   └── albatross/         <- the root package's source
│       ├── main.py
│       └── condor/
│           └── strategy.py
└── packages/              <- workspace members
    ├── bird_feeder/
    │   ├── pyproject.toml  <- member package
    │   └── src/bird_feeder/actions.py
    └── seeds/
        ├── pyproject.toml
        └── src/seeds/...
```

**Workspace root `pyproject.toml`** — declares the members and wires the sibling packages as workspace sources:

```toml
[project]
name = "albatross"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["bird-feeder"]

[tool.uv.sources]
bird-feeder = { workspace = true }
seeds = { workspace = true }

[tool.uv.workspace]
members = ["packages/*"]

[build-system]
requires = ["uv_build>=0.9.3,<0.10.0"]
build-backend = "uv_build"

[dependency-groups]
albatross = ["numpy", "bird-feeder"]
```

`members = ["packages/*"]` includes every package under `packages/`. The `{ workspace = true }` sources tell uv to resolve `bird-feeder` and `seeds` from the workspace instead of PyPI, so a single `uv.lock` covers the whole tree. A member package is an ordinary package that can itself depend on other members:

```toml
# packages/bird_feeder/pyproject.toml
[project]
name = "bird-feeder"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["seeds"]

[tool.uv]
package = true
```

**Building the image** — point `.with_uv_project()` at the *workspace-root* `pyproject.toml`. Because `project_install_mode` defaults to `dependencies_only`, only the workspace's `pyproject.toml` and `uv.lock` enter the build context, so the image rebuilds only when dependencies change — fast registration is preserved. Select a dependency group with `extra_args` to keep the image lean:

```python
from pathlib import Path

from bird_feeder.actions import bird_env, get_feeder
from seeds.actions import get_seed

import flyte
from albatross.condor.strategy import get_strategy

UV_WORKSPACE_ROOT = Path(__file__).parent.parent.parent  # -> albatross/

env = flyte.TaskEnvironment(
    name="uv_workspace",
    image=flyte.Image.from_debian_base().with_uv_project(
        pyproject_file=UV_WORKSPACE_ROOT / "pyproject.toml",
        extra_args="--only-group albatross",
    ),
    depends_on=[bird_env],
)
```

Because uv installs the workspace members into the environment, sibling imports (`from bird_feeder.actions import ...`, `from seeds.actions import ...`) resolve directly — you do **not** need `with_source_folder()` to bake sibling code into the image, as Pattern B requires.

**Entry point** — set `root_dir` to the workspace root so the code bundle packages every member's source and imports resolve the same way locally and at runtime:

```python
@env.task
async def albatross_task() -> str:
    get_feeder()
    get_strategy()
    seed = get_seed(seed_name="Sun Flower seed")
    return f"Get bird feeder and feed with {seed}"


if __name__ == "__main__":
    flyte.init_from_config(root_dir=UV_WORKSPACE_ROOT)
    run = flyte.run(albatross_task)
    print(run.url)
```

Each member can define its own `TaskEnvironment` pointing at the same workspace-root `pyproject.toml`; because they all resolve against the one lockfile, their images stay mutually consistent. For production, bake the bundle with `flyte.deploy(env, copy_style="none", version="1.2.3")` exactly as in the other patterns.

## The full build path (production)

For production deployments where you need immutable, self-contained images:

```python
flyte.deploy(my_env, copy_style="none", version="1.2.3")
```

`with_code_bundle()` on the image resolves to a `COPY` instruction. The image is fully self-contained.

Use a deterministic version string — a git commit SHA, a git tag, a CI build number. Avoid auto-generated strings so you can trace which code is in which image.

> [!IMPORTANT]
> Do not use `install_project` mode for production builds. `install_project` copies the entire project directory into the build context and hashes all of it. Every code change triggers a full image rebuild. `with_code_bundle()` + `copy_style="none"` is more surgical: only the files you select are in the image.
