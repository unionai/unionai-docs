---
title: Packaging
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Code packaging for remote execution

When you run Flyte tasks remotely, your code needs to be available in the execution environment. Flyte SDK provides two main approaches for packaging your code:

1. **Code bundling** - Bundle code dynamically at runtime
2. **Container-based deployment** - Embed code directly in container images

## Quick comparison

| Aspect | Code bundling | Container-based |
|--------|---------------|-----------------|
| **Speed** | Fast (no image rebuild) | Slower (requires image build) |
| **Best for** | Rapid development, iteration | Production, immutable deployments |
| **Code changes** | Immediate effect | Requires image rebuild |
| **Setup** | Automatic by default | Manual configuration needed |
| **Reproducibility** | Excellent (hash-based versioning) | Excellent (immutable images) |
| **Rollback** | Requires version control | Tag-based, straightforward |

---

## Code bundling

**Default approach** - Automatically bundles and uploads your code to remote storage at runtime.

### How it works

When you run `flyte run` or call `flyte.run()`, Flyte automatically:

1. **Scans loaded modules** from your codebase
2. **Creates a tarball** (gzipped, without timestamps for consistent hashing)
3. **Uploads to blob storage** (S3, GCS, Azure Blob)
4. **Deduplicates** based on content hashes
5. **Downloads in containers** at runtime

This process happens transparently - every container downloads and extracts the code bundle before execution.

> [!NOTE]
> Code bundling is optimized for speed:
> - Bundles are created without timestamps for consistent hashing
> - Identical code produces identical hashes, enabling deduplication
> - Only modified code triggers new uploads
> - Containers cache downloaded bundles
>
> **Reproducibility:** Flyte automatically versions code bundles based on content hash. The same code always produces the same hash, guaranteeing reproducibility without manual versioning. However, version control is still recommended for rollback capabilities.

### Automatic code bundling

**Default behavior** - Bundles all loaded modules automatically.

#### What gets bundled

Flyte includes modules that are:
- ✅ **Loaded when environment is parsed** (imported at module level)
- ✅ **Part of your codebase** (not system packages)
- ✅ **Within your project directory**
- ❌ **NOT lazily loaded** (imported inside functions)
- ❌ **NOT system-installed packages** (e.g., from site-packages)

#### Example: Basic automatic bundling

```python
# app.py
import flyte
from my_module import helper  # ✅ Bundled automatically

env = flyte.TaskEnvironment(
    name="default",
    image=flyte.Image.from_debian_base().with_pip_packages("pandas", "numpy")
)

@env.task
def process_data(x: int) -> int:
    # This import won't be bundled (lazy load)
    from another_module import util  # ❌ Not bundled automatically
    return helper.transform(x)

if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(process_data, x=42)
    print(run.url)
```

When you run this:
```bash
flyte run app.py process_data --x 42
```

Flyte automatically:
1. Bundles `app.py` and `my_module.py`
2. Preserves the directory structure
3. Uploads to blob storage
4. Makes it available in the remote container

#### Project structure example

```
my_project/
├── app.py              # Main entry point
├── tasks/
│   ├── __init__.py
│   ├── data_tasks.py   # Flyte tasks
│   └── ml_tasks.py
└── utils/
    ├── __init__.py
    ├── preprocessing.py # Business logic
    └── models.py
```

```python
# app.py
import flyte
from tasks.data_tasks import load_data    # ✅ Bundled
from tasks.ml_tasks import train_model    # ✅ Bundled
# utils modules imported in tasks are also bundled

@flyte.task
def pipeline(dataset: str) -> float:
    data = load_data(dataset)
    accuracy = train_model(data)
    return accuracy

if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(pipeline, dataset="train.csv")
```

**All modules are bundled with their directory structure preserved.**

### Manual code bundling

Control exactly what gets bundled by configuring the copy style.

#### Copy styles

Three options available:

1. **`"auto"`** (default) - Bundle loaded modules only
2. **`"all"`** - Bundle everything in the working directory
3. **`"none"`** - Skip bundling entirely (requires code in container)

#### Using `copy_style="all"`

Bundle all files under your project directory:

```python
import flyte

flyte.init_from_config()

# Bundle everything in current directory
run = flyte.with_runcontext(copy_style="all").run(
    my_task,
    input_data="sample.csv"
)
```

Or via CLI:
```bash
flyte run --copy-style=all app.py my_task --input-data sample.csv
```

**Use when:**
- You have data files or configuration that tasks need
- You use dynamic imports or lazy loading
- You want to ensure all project files are available

#### Using `copy_style="none"`

Skip code bundling (see [Container-based Deployment](#container-based-deployment)):

```python
run = flyte.with_runcontext(copy_style="none").run(my_task, x=10)
```

### Controlling the root directory

The `root_dir` parameter controls which directory serves as the bundling root.

#### Why root directory matters

1. **Determines what gets bundled** - All code paths are relative to root_dir
2. **Preserves import structure** - Python imports must match the bundle structure
3. **Affects path resolution** - Files and modules are located relative to root_dir

#### Setting root directory

##### Via CLI

```bash
flyte run --root-dir /path/to/project app.py my_task
```

##### Programmatically

```python
import pathlib
import flyte

flyte.init_from_config(
    root_dir=pathlib.Path(__file__).parent
)
```

#### Root directory use cases

##### Use case 1: Multi-module project

```
project/
├── src/
│   ├── workflows/
│   │   └── pipeline.py
│   └── utils/
│       └── helpers.py
└── config.yaml
```

```python
# src/workflows/pipeline.py
import pathlib
import flyte
from utils.helpers import process  # Relative import from project root

# Set root to project root (not src/)
flyte.init_from_config(
    root_dir=pathlib.Path(__file__).parent.parent.parent
)

@flyte.task
def my_task():
    return process()
```

**Root set to `project/` so imports like `from utils.helpers` work correctly.**

##### Use case 2: Shared utilities

```
workspace/
├── shared/
│   └── common.py
└── project/
    └── app.py
```

```python
# project/app.py
import flyte
import pathlib
from shared.common import shared_function  # Import from parent directory

# Set root to workspace/ to include shared/
flyte.init_from_config(
    root_dir=pathlib.Path(__file__).parent.parent
)
```

##### Use case 3: Monorepo

```
monorepo/
├── libs/
│   ├── data/
│   └── models/
└── services/
    └── ml_service/
        └── workflows.py
```

```python
# services/ml_service/workflows.py
import flyte
import pathlib
from libs.data import loader  # Import from monorepo root
from libs.models import predictor

# Set root to monorepo/ to include libs/
flyte.init_from_config(
    root_dir=pathlib.Path(__file__).parent.parent.parent
)
```

#### Root directory best practices

1. **Set root_dir at project initialization** before importing any task modules
2. **Use absolute paths** with `pathlib.Path(__file__).parent` navigation
3. **Match your import structure** - if imports are relative to project root, set root_dir to project root
4. **Keep consistent** - use the same root_dir for both `flyte run` and `flyte.init()`

### Code bundling examples

#### Example: Standard Python package

```
my_package/
├── pyproject.toml
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── main.py
│       ├── data/
│       │   ├── loader.py
│       │   └── processor.py
│       └── models/
│           └── analyzer.py
```

```python
# src/my_package/main.py
import flyte
import pathlib
from my_package.data.loader import fetch_data
from my_package.data.processor import clean_data
from my_package.models.analyzer import analyze

env = flyte.TaskEnvironment(
    name="pipeline",
    image=flyte.Image.from_debian_base().with_uv_project(
        pyproject_file=pathlib.Path(__file__).parent.parent.parent / "pyproject.toml"
    )
)

@env.task
async def fetch_task(url: str) -> dict:
    return await fetch_data(url)

@env.task
def process_task(raw_data: dict) -> list[dict]:
    return clean_data(raw_data)

@env.task
def analyze_task(data: list[dict]) -> str:
    return analyze(data)

if __name__ == "__main__":
    import flyte.git

    # Set root to project root for proper imports
    flyte.init_from_config(
        flyte.git.config_from_root(),
        root_dir=pathlib.Path(__file__).parent.parent.parent
    )

    # All modules bundled automatically
    run = flyte.run(analyze_task, data=[{"value": 1}, {"value": 2}])
    print(f"Run URL: {run.url}")
```

**Run with:**
```bash
cd my_package
flyte run src/my_package/main.py analyze_task --data '[{"value": 1}]'
```

#### Example: Dynamic environment based on domain

```python
# environment_picker.py
import flyte

def create_env():
    """Create different environments based on domain."""
    if flyte.current_domain() == "development":
        return flyte.TaskEnvironment(
            name="dev",
            image=flyte.Image.from_debian_base(),
            env_vars={"ENV": "dev", "DEBUG": "true"}
        )
    elif flyte.current_domain() == "staging":
        return flyte.TaskEnvironment(
            name="staging",
            image=flyte.Image.from_debian_base(),
            env_vars={"ENV": "staging", "DEBUG": "false"}
        )
    else:  # production
        return flyte.TaskEnvironment(
            name="prod",
            image=flyte.Image.from_debian_base(),
            env_vars={"ENV": "production", "DEBUG": "false"},
            resources=flyte.Resources(cpu="2", memory="4Gi")
        )

env = create_env()

@env.task
async def process(n: int) -> int:
    import os
    print(f"Running in {os.getenv('ENV')} environment")
    return n * 2

if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(process, n=5)
    print(run.url)
```

**Why this works:**
- `flyte.current_domain()` is set correctly when Flyte re-instantiates modules remotely
- Environment configuration is deterministic and reproducible
- Code automatically bundled with domain-specific settings

> [!NOTE]
> `flyte.current_domain()` only works after `flyte.init()` is called:
> - ✅ Works with `flyte run` and `flyte deploy` (auto-initialize)
> - ✅ Works in `if __name__ == "__main__"` after explicit `flyte.init()`
> - ❌ Does NOT work at module level without initialization

### When to use code bundling

✅ **Use code bundling when:**
- Rapid development and iteration
- Frequently changing code
- Multiple developers testing changes
- Jupyter notebook workflows
- Quick prototyping and experimentation

❌ **Consider container-based instead when:**
- Need easy rollback to previous versions (container tags are simpler than finding git commits)
- Working with air-gapped environments (no blob storage access)
- Code changes require coordinated dependency updates

---

## Container-based deployment

**Advanced approach** - Embed code directly in container images for immutable deployments.

### How it works

Instead of bundling code at runtime:

1. **Build container image** with code copied inside
2. **Disable code bundling** with `copy_style="none"`
3. **Container has everything** needed at runtime

**Trade-off:** Every code change requires a new image build (slower), but provides complete reproducibility.

### Configuration

Three key steps:

#### 1. Set `copy_style="none"`

Disable runtime code bundling:

```python
flyte.with_runcontext(copy_style="none").run(my_task, n=10)
```

Or via CLI:
```bash
flyte run --copy-style=none app.py my_task --n 10
```

#### 2. Copy Code into Image

Use `Image.with_source_file()` or `Image.with_source_folder()`:

```python
import pathlib
import flyte

env = flyte.TaskEnvironment(
    name="embedded",
    image=flyte.Image.from_debian_base().with_source_folder(
        src=pathlib.Path(__file__).parent,
        copy_contents_only=True
    )
)
```

#### 3. Set Correct `root_dir`

Match your image copy configuration:

```python
flyte.init_from_config(
    root_dir=pathlib.Path(__file__).parent
)
```

### Image source copying methods

#### `with_source_file()` - Copy individual files

Copy a single file into the container:

```python
image = flyte.Image.from_debian_base().with_source_file(
    src=pathlib.Path(__file__),
    dst="/app/main.py"
)
```

**Use for:**
- Single-file workflows
- Copying configuration files
- Adding scripts to existing images

#### `with_source_folder()` - Copy directories

Copy entire directories into the container:

```python
image = flyte.Image.from_debian_base().with_source_folder(
    src=pathlib.Path(__file__).parent,
    dst="/app",
    copy_contents_only=False  # Copy folder itself
)
```

**Parameters:**
- `src`: Source directory path
- `dst`: Destination path in container (optional, defaults to workdir)
- `copy_contents_only`: If `True`, copies folder contents; if `False`, copies folder itself

##### `copy_contents_only=True` (Recommended)

Copies only the contents of the source folder:

```python
# Project structure:
# my_project/
#   ├── app.py
#   └── utils.py

image = flyte.Image.from_debian_base().with_source_folder(
    src=pathlib.Path(__file__).parent,
    copy_contents_only=True
)

# Container will have:
# /app/app.py
# /app/utils.py

# Set root_dir to match:
flyte.init_from_config(root_dir=pathlib.Path(__file__).parent)
```

##### `copy_contents_only=False`

Copies the folder itself with its name:

```python
# Project structure:
# workspace/
#   └── my_project/
#       ├── app.py
#       └── utils.py

image = flyte.Image.from_debian_base().with_source_folder(
    src=pathlib.Path(__file__).parent,  # Points to my_project/
    copy_contents_only=False
)

# Container will have:
# /app/my_project/app.py
# /app/my_project/utils.py

# Set root_dir to parent to match:
flyte.init_from_config(root_dir=pathlib.Path(__file__).parent.parent)
```

### Complete container-based example

```python
# full_build.py
import pathlib
import flyte
from dep import helper  # Local module

# Configure environment with source copying
env = flyte.TaskEnvironment(
    name="full_build",
    image=flyte.Image.from_debian_base()
        .with_pip_packages("numpy", "pandas")
        .with_source_folder(
            src=pathlib.Path(__file__).parent,
            copy_contents_only=True
        )
)

@env.task
def square(x: int) -> int:
    return x ** helper.get_exponent()

@env.task
def main(n: int) -> list[int]:
    return list(flyte.map(square, range(n)))

if __name__ == "__main__":
    import flyte.git

    # Initialize with matching root_dir
    flyte.init_from_config(
        flyte.git.config_from_root(),
        root_dir=pathlib.Path(__file__).parent
    )

    # Run with copy_style="none" and explicit version
    run = flyte.with_runcontext(
        copy_style="none",
        version="v1.0.0"  # Explicit version for image tagging
    ).run(main, n=10)

    print(f"Run URL: {run.url}")
    run.wait()
```

**Project structure:**
```
project/
├── full_build.py
├── dep.py          # Local dependency
└── .flyte/
    └── config.yaml
```

**Run with:**
```bash
python full_build.py
```

This will:
1. Build a container image with `full_build.py` and `dep.py` embedded
2. Tag it as `v1.0.0`
3. Push to registry
4. Execute remotely without code bundling

### Using externally built images

When containers are built outside of Flyte (e.g., in CI/CD), use `Image.from_ref_name()`:

#### Step 1: Build your image externally

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy your code
COPY src/ /app/

# Install dependencies
RUN pip install flyte pandas numpy

# Ensure flyte executable is available
RUN flyte --help
```

```bash
# Build in CI/CD
docker build -t myregistry.com/my-app:v1.2.3 .
docker push myregistry.com/my-app:v1.2.3
```

#### Step 2: Reference image by name

```python
# app.py
import flyte

env = flyte.TaskEnvironment(
    name="external",
    image=flyte.Image.from_ref_name("my-app-image")  # Reference name
)

@env.task
def process(x: int) -> int:
    return x * 2

if __name__ == "__main__":
    flyte.init_from_config()

    # Pass actual image URI at deploy/run time
    run = flyte.with_runcontext(
        copy_style="none",
        images={"my-app-image": "myregistry.com/my-app:v1.2.3"}
    ).run(process, x=10)
```

Or via CLI:
```bash
flyte run \
  --copy-style=none \
  --image my-app-image=myregistry.com/my-app:v1.2.3 \
  app.py process --x 10
```

**For deployment:**
```bash
flyte deploy \
  --image my-app-image=myregistry.com/my-app:v1.2.3 \
  app.py
```

#### Why use reference names?

1. **Decouples code from image URIs** - Change images without modifying code
2. **Supports multiple environments** - Different images for dev/staging/prod
3. **Integrates with CI/CD** - Build images in pipelines, reference in code
4. **Enables image reuse** - Multiple tasks can reference the same image

#### Example: Multi-environment deployment

```python
import flyte
import os

# Code references image by name
env = flyte.TaskEnvironment(
    name="api",
    image=flyte.Image.from_ref_name("api-service")
)

@env.task
def api_call(endpoint: str) -> dict:
    # Implementation
    return {"status": "success"}

if __name__ == "__main__":
    flyte.init_from_config()

    # Determine image based on environment
    environment = os.getenv("ENV", "dev")
    image_uri = {
        "dev": "myregistry.com/api-service:dev",
        "staging": "myregistry.com/api-service:staging",
        "prod": "myregistry.com/api-service:v1.2.3"
    }[environment]

    run = flyte.with_runcontext(
        copy_style="none",
        images={"api-service": image_uri}
    ).run(api_call, endpoint="/health")
```

### Container-based best practices

1. **Always set explicit versions** when using `copy_style="none"`:
   ```python
   flyte.with_runcontext(copy_style="none", version="v1.0.0")
   ```

2. **Match `root_dir` to `copy_contents_only`**:
   - `copy_contents_only=True` → `root_dir=Path(__file__).parent`
   - `copy_contents_only=False` → `root_dir=Path(__file__).parent.parent`

3. **Ensure `flyte` executable is in container** - Add to PATH or install flyte package

4. **Use `.dockerignore`** to exclude unnecessary files:
   ```
   # .dockerignore
   __pycache__/
   *.pyc
   .git/
   .venv/
   *.egg-info/
   ```

5. **Test containers locally** before deploying:
   ```bash
   docker run -it myimage:latest /bin/bash
   python -c "import mymodule"  # Verify imports work
   ```

### When to use container-based deployment

✅ **Use container-based when:**
- Deploying to production
- Need immutable, reproducible environments
- Working with complex system dependencies
- Deploying to air-gapped or restricted environments
- CI/CD pipelines with automated builds
- Code changes are infrequent

❌ **Don't use container-based when:**
- Rapid development and frequent code changes
- Quick prototyping
- Interactive development (Jupyter notebooks)
- Learning and experimentation

---

## Choosing the right approach

### Decision tree

```
Are you iterating quickly on code?
├─ Yes → Use Code Bundling (Default)
│         (Development, prototyping, notebooks)
│         Both approaches are fully reproducible via hash/tag
└─ No  → Do you need easy version rollback?
          ├─ Yes → Use Container-based
          │         (Production, CI/CD, straightforward tag-based rollback)
          └─ No  → Either works
                    (Code bundling is simpler, container-based for air-gapped)
```

### Hybrid approach

You can use different approaches for different tasks:

```python
import flyte
import pathlib

# Fast iteration for development tasks
dev_env = flyte.TaskEnvironment(
    name="dev",
    image=flyte.Image.from_debian_base().with_pip_packages("pandas")
    # Code bundling (default)
)

# Immutable containers for production tasks
prod_env = flyte.TaskEnvironment(
    name="prod",
    image=flyte.Image.from_debian_base()
        .with_pip_packages("pandas")
        .with_source_folder(pathlib.Path(__file__).parent, copy_contents_only=True)
    # Requires copy_style="none"
)

@dev_env.task
def experimental_task(x: int) -> int:
    # Rapid development with code bundling
    return x * 2

@prod_env.task
def stable_task(x: int) -> int:
    # Production with embedded code
    return x ** 2

if __name__ == "__main__":
    flyte.init_from_config(root_dir=pathlib.Path(__file__).parent)

    # Use code bundling for dev task
    dev_run = flyte.run(experimental_task, x=5)

    # Use container-based for prod task
    prod_run = flyte.with_runcontext(
        copy_style="none",
        version="v1.0.0"
    ).run(stable_task, x=5)
```

---

## Troubleshooting

### Import errors

**Problem:** `ModuleNotFoundError` when task executes remotely

**Solutions:**

1. **Check loaded modules** - Ensure modules are imported at module level:
   ```python
   # ✅ Good - bundled automatically
   from mymodule import helper

   @flyte.task
   def my_task():
       return helper.process()
   ```

   ```python
   # ❌ Bad - not bundled (lazy load)
   @flyte.task
   def my_task():
       from mymodule import helper
       return helper.process()
   ```

2. **Verify `root_dir`** matches your import structure:
   ```python
   # If imports are: from mypackage.utils import foo
   # Then root_dir should be parent of mypackage/
   flyte.init_from_config(root_dir=pathlib.Path(__file__).parent.parent)
   ```

3. **Use `copy_style="all"`** to bundle everything:
   ```bash
   flyte run --copy-style=all app.py my_task
   ```

### Code changes not reflected

**Problem:** Remote execution uses old code despite local changes

> [!NOTE]
> This is rare with code bundling - Flyte automatically versions based on content hash, so code changes should be detected automatically. This issue typically occurs with caching problems or when using `copy_style="none"`.

**Solutions:**

1. **Use explicit version bump** (mainly for container-based deployments):
   ```python
   run = flyte.with_runcontext(version="v2").run(my_task)
   ```

2. **Check if `copy_style="none"`** is set - this requires image rebuild:
   ```python
   # If using copy_style="none", rebuild image
   run = flyte.with_runcontext(
       copy_style="none",
       version="v2"  # Bump version to force rebuild
   ).run(my_task)
   ```

### Files missing in container

**Problem:** Task can't find data files or configs

**Solutions:**

1. **Use `copy_style="all"`** to bundle all files:
   ```bash
   flyte run --copy-style=all app.py my_task
   ```

2. **Copy files explicitly in image**:
   ```python
   image = flyte.Image.from_debian_base().with_source_file(
       src=pathlib.Path("config.yaml"),
       dst="/app/config.yaml"
   )
   ```

3. **Store data in remote storage** instead of bundling:
   ```python
   @flyte.task
   def my_task():
       # Read from S3/GCS instead of local files
       import flyte.io
       data = flyte.io.File("s3://bucket/data.csv").open().read()
   ```

### Container build failures

**Problem:** Image build fails with `copy_style="none"`

**Solutions:**

1. **Check `root_dir` matches `copy_contents_only`**:
   ```python
   # copy_contents_only=True
   image = Image.from_debian_base().with_source_folder(
       src=Path(__file__).parent,
       copy_contents_only=True
   )
   flyte.init(root_dir=Path(__file__).parent)  # Match!
   ```

2. **Ensure `flyte` executable available**:
   ```python
   image = Image.from_debian_base()  # Has flyte pre-installed
   ```

3. **Check file permissions** in source directory:
   ```bash
   chmod -R +r project/
   ```

### Version conflicts

**Problem:** Multiple versions of same image causing confusion

**Solutions:**

1. **Use explicit versions**:
   ```python
   run = flyte.with_runcontext(
       copy_style="none",
       version="v1.2.3"  # Explicit, not auto-generated
   ).run(my_task)
   ```

2. **Clean old images**:
   ```bash
   docker image prune -a
   ```

3. **Use semantic versioning** for clarity:
   ```python
   version = "v1.0.0"  # Major.Minor.Patch
   ```

---

## Further reading

- [Image API Reference](../api-reference/flyte-sdk/packages/flyte/Image.md) - Complete Image class documentation
- [TaskEnvironment](../api-reference/flyte-sdk/packages/flyte/TaskEnvironment.md) - Environment configuration options
- [Configuration Guide](./configuration/) - Setting up Flyte config files

