---
title: Container images
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Container images

Flyte 1's `ImageSpec` is replaced by Flyte 2's `flyte.Image` with a fluent builder API.

## Basic migration

{{< tabs "migration-image-basic" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
from flytekit import ImageSpec

image_spec = ImageSpec(
    name="my-image",
    registry="ghcr.io/myorg",
    python_version="3.11",
    packages=["pandas", "numpy"],
    apt_packages=["curl", "git"],
    env={"MY_VAR": "value"},
)

@task(container_image=image_spec)
def my_task(): ...
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
```python
from flyte import Image, TaskEnvironment

image = (
    Image.from_debian_base(
        name="my-image",
        registry="ghcr.io/myorg",
        python_version=(3, 11),
    )
    .with_pip_packages("pandas", "numpy")
    .with_apt_packages("curl", "git")
    .with_env_vars({"MY_VAR": "value"})
)

env = TaskEnvironment(name="my_env", image=image)

@env.task
def my_task(): ...
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Image constructor methods

| Method | Description | Use case |
|--------|-------------|----------|
| `Image.from_debian_base()` | Start from Flyte's Debian base | Most common, includes Flyte SDK |
| `Image.from_base(image_uri)` | Start from any existing image | Custom base images |
| `Image.from_dockerfile(path)` | Build from Dockerfile | Complex custom builds |
| `Image.from_uv_script(path)` | Build from UV script | UV-based projects |

## Image builder methods (chainable)

```python
image = (
    Image.from_debian_base(
        python_version=(3, 12),
        registry="ghcr.io/myorg",
        name="my-image",
    )
    # Python packages
    .with_pip_packages("pandas", "numpy>=1.24.0", pre=True)
    .with_requirements(Path("requirements.txt"))
    .with_uv_project(Path("pyproject.toml"))
    .with_poetry_project(Path("pyproject.toml"))

    # System packages
    .with_apt_packages("curl", "git", "build-essential")

    # Custom commands
    .with_commands([
        "mkdir -p /app/data",
        "chmod +x /app/scripts/*.sh",
    ])

    # Files
    .with_source_file(Path("config.yaml"), dst="/app/config.yaml")
    .with_source_folder(Path("./src"), dst="/app/src")
    .with_dockerignore(Path(".dockerignore"))

    # Environment
    .with_env_vars({"LOG_LEVEL": "INFO", "WORKERS": "4"})
    .with_workdir("/app")
)
```

## Builder configuration (local vs remote)

Flyte 2 supports two build modes:

**Local builder** (default): Builds using local Docker and pushes to registry. Requires Docker installed and authenticated to registry.

**Remote builder** (Union instances): Builds on Union's ImageBuilder. No local Docker required. Faster in CI/CD.

```yaml
# In config file
image:
  builder: local  # or "remote"
```

```python
# Or via code
flyte.init(image_builder="local")  # or "remote"
flyte.init_from_config(image_builder="local")  # or "remote"
```

## Private registry with secrets

{{< tabs "migration-image-private" >}}
{{< tab "Flyte 1" >}}
{{< markdown >}}
```python
image_spec = ImageSpec(
    registry="private.registry.com",
    registry_config="/path/to/config.json",
)
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< markdown >}}
First create the secret:
```shell
flyte create secret --type image_pull my-registry-secret --from-file ~/.docker/config.json
```

Then reference it in the image:
```python
image = Image.from_debian_base(
    registry="private.registry.com",
    name="my-image",
    registry_secret="my-registry-secret",
)
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Parameter mapping

| Flyte 1 ImageSpec | Flyte 2 Image | Notes |
|--------------|----------|-------|
| `name` | `name` (in constructor) | Same |
| `registry` | `registry` (in constructor) | Same |
| `python_version` | `python_version` (tuple) | `"3.11"` becomes `(3, 11)` |
| `packages` | `.with_pip_packages()` | Method instead of param |
| `apt_packages` | `.with_apt_packages()` | Method instead of param |
| `conda_packages` | N/A | Use micromamba or custom base |
| `requirements` | `.with_requirements()` | Supports txt, poetry.lock, uv.lock |
| `env` | `.with_env_vars()` | Method instead of param |
| `commands` | `.with_commands()` | Method instead of param |
| `copy` | `.with_source_file/folder()` | More explicit methods |
| `source_root` | `.with_source_folder()` | Method instead of param |
| `pip_index` | `index_url` param in `.with_pip_packages()` | Moved to method |
| `pip_extra_index_url` | `extra_index_urls` param | Moved to method |
| `base_image` | `Image.from_base()` | Different constructor |
| `builder` | Config file or `flyte.init()` | Global setting |
| `platform` | `platform` (in constructor) | Tuple: `("linux/amd64", "linux/arm64")` |

For full details on container images in Flyte 2, see [Container images](../../user-guide/task-configuration/container-images).
