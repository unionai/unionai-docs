---
title: Deployment patterns
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Deployment patterns

Once you understand the basics of task deployment, you can leverage various deployment patterns to handle different project structures, dependency management approaches, and deployment requirements. This guide covers the most common patterns with practical examples.

## Overview of deployment patterns

Flyte supports multiple deployment patterns to accommodate different project structures and requirements:

1. **[Simple file deployment](#simple-file-deployment)** - Single file with tasks and environments
2. **[Custom Dockerfile deployment](#custom-dockerfile-deployment)** - Full control over container environment
3. **[PyProject package deployment](#pyproject-package-deployment)** - Structured Python packages with dependencies and async tasks
4. **[Package structure deployment](#package-structure-deployment)** - Organized packages with shared environments
5. **[Full build deployment](#full-build-deployment)** - Complete code embedding in containers
6. **[Python path deployment](#python-path-deployment)** - Multi-directory project structures
7. **[Dynamic environment deployment](#dynamic-environment-deployment)** - Environment selection based on domain context

Each pattern serves specific use cases and can be combined as needed for complex projects.

## Simple file deployment

The simplest deployment pattern involves defining both your tasks and task environment in a single Python file. This pattern works well for:

- Prototyping and experimentation
- Simple tasks with minimal dependencies
- Educational examples and tutorials

### Example structure

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/simple_file.py" lang="python" >}}

### Deployment commands

```bash
# Deploy the environment
flyte deploy my_example.py env

# Run the task ephemerally
flyte run my_example.py my_task --name "World"
```

### When to use

- Quick prototypes and experiments
- Single-purpose scripts
- Learning Flyte basics
- Tasks with no external dependencies

## Custom Dockerfile deployment

When you need full control over the container environment, you can specify a custom Dockerfile. This pattern is ideal for:

- Complex system dependencies
- Specific OS or runtime requirements
- Custom base images
- Multi-stage builds

### Example structure

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/dockerfile/Dockerfile" lang="dockerfile" >}}

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/dockerfile/dockerfile_env.py" lang="python" >}}

### Alternative: Dockerfile in different directory

You can also reference Dockerfiles from subdirectories:

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/dockerfile/src/docker_env_in_dir.py" lang="python" >}}

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/dockerfile/Dockerfile.workdir" lang="dockerfile" >}}

### Key considerations

- **Path handling**: Use `Path(__file__).parent` for relative Dockerfile paths
  ```python
  # relative paths in python change based on where you call, so set it relative to this file
  Path(__file__).parent / "Dockerfile"
  ```
- **Registry configuration**: Specify a registry for image storage
- **Build context**: The directory containing the Dockerfile becomes the build context
- **Flyte installation**: Ensure Flyte is installed in the container and available on `$PATH`
  ```dockerfile
  # Install Flyte in your Dockerfile
  RUN pip install flyte
  ```
- **Dependencies**: Include all application requirements in the Dockerfile or requirements.txt

### When to use

- Need specific system packages or tools
- Custom base image requirements
- Complex installation procedures
- Multi-stage build optimization

## PyProject package deployment

For structured Python projects with proper package management, use the PyProject pattern. This approach demonstrates a **realistic Python project structure** that provides:

- Proper dependency management with `pyproject.toml` and external packages like `httpx`
- Clean separation of business logic and Flyte tasks across multiple modules
- Professional project structure with `src/` layout
- Async task execution with API calls and data processing
- Entrypoint patterns for both command-line and programmatic execution

### Example structure

```
pyproject_package/
├── pyproject.toml          # Project metadata and dependencies
├── README.md              # Documentation
└── src/
    └── pyproject_package/
        ├── __init__.py     # Package initialization
        ├── main.py         # Entrypoint script
        ├── data/
        │   ├── __init__.py
        │   ├── loader.py   # Data loading utilities (no Flyte)
        │   └── processor.py # Data processing utilities (no Flyte)
        ├── models/
        │   ├── __init__.py
        │   └── analyzer.py # Analysis utilities (no Flyte)
        └── tasks/
            ├── __init__.py
            └── tasks.py    # Flyte task definitions
```

### Business logic modules

The business logic is completely separate from Flyte and can be used independently:

#### Data Loading (`data/loader.py`)
{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pyproject_package/src/pyproject_package/data/loader.py" lang="python" >}}

#### Data Processing (`data/processor.py`)
{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pyproject_package/src/pyproject_package/data/processor.py" lang="python" >}}

#### Analysis (`models/analyzer.py`)
{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pyproject_package/src/pyproject_package/models/analyzer.py" lang="python" >}}

These modules demonstrate:
- **No Flyte dependencies** - can be tested and used independently
- **Pydantic models** for data validation with custom validators
- **Async patterns** with proper context managers and error handling
- **NumPy integration** for statistical calculations
- **Professional error handling** with timeouts and validation

### Flyte orchestration layer

The Flyte tasks orchestrate the business logic with proper async execution:

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pyproject_package/src/pyproject_package/tasks/tasks.py" lang="python" >}}

### Entrypoint configuration

The main entrypoint demonstrates proper initialization and execution patterns:

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pyproject_package/src/pyproject_package/main.py" lang="python" >}}

### Dependencies and configuration

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pyproject_package/pyproject.toml" lang="toml" >}}

### Key features

- **Async task chains**: Tasks can be chained together with proper async/await patterns
- **External dependencies**: Demonstrates integration with external libraries (`httpx`, `pyyaml`)
- **uv integration**: Uses `.with_uv_project()` for dependency management
- **Resource specification**: Shows how to set memory and CPU requirements
- **Proper error handling**: Includes timeout and error handling in API calls

### Key learning points

1. **Separation of concerns**: Business logic (`data/`, `models/`) separate from orchestration (`main.py`)
2. **Reusable code**: Non-Flyte modules can be tested independently and reused
3. **Async support**: Demonstrates async Flyte tasks for I/O-bound operations
4. **Dependency management**: Shows how external packages integrate with Flyte
5. **Realistic structure**: Mirrors real-world Python project organization
6. **Entrypoint script**: Shows how to create runnable entry points

### Usage patterns

**Run locally:**
```bash
python -m pyproject_package.main
```

**Deploy to Flyte:**
```bash
flyte deploy .
```

**Run remotely:**
```bash
python -m pyproject_package.main  # Uses remote execution
```

### What this example demonstrates

- Multiple files and modules in a package
- Async Flyte tasks with external API calls
- Separation of business logic from orchestration
- External dependencies (`httpx`, `numpy`, `pydantic`)
- **Data validation with Pydantic models** for robust data processing
- **Professional error handling** with try/catch for data validation
- **Timeout configuration** for external API calls (`timeout=10.0`)
- **Async context managers** for proper resource management (`async with httpx.AsyncClient()`)
- Entrypoint script pattern with `project.scripts`
- Realistic project structure with `src/` layout
- Task chaining and data flow
- How non-Flyte code integrates with Flyte tasks

### When to use

- Production-ready, maintainable projects
- Projects requiring external API integration
- Complex data processing pipelines
- Team development with proper separation of concerns
- Applications needing async execution patterns

## Package structure deployment

For organizing Flyte workflows in a package structure with shared task environments and utilities, use this pattern. It's particularly useful for:

- Multiple workflows that share common environments and utilities
- Organized code structure with clear module boundaries
- Projects where you want to reuse task environments across workflows

### Example structure

```
lib/
├── __init__.py
└── workflows/
    ├── __init__.py
    ├── workflow1.py    # First workflow
    ├── workflow2.py    # Second workflow
    ├── env.py          # Shared task environment
    └── utils.py        # Shared utilities
```

### Key concepts

- **Shared environments**: Define task environments in `env.py` and import across workflows
- **Utility modules**: Common functions and utilities shared between workflows
- **Root directory handling**: Use `--root-dir` flag for proper Python path configuration

### Running with root directory

When running workflows with a package structure, specify the root directory:

```bash
# Run first workflow
flyte run --root-dir . lib/workflows/workflow1.py process_workflow

# Run second workflow
flyte run --root-dir . lib/workflows/workflow2.py math_workflow --n 6
```

### How `--root-dir` works

The `--root-dir` flag automatically configures the Python path (`sys.path`) to ensure:

1. **Local execution**: Package imports work correctly when running locally
2. **Consistent behavior**: Same Python path configuration locally and at runtime
3. **No manual PYTHONPATH**: Eliminates need to manually export environment variables
4. **Runtime packaging**: Flyte packages and copies code correctly to execution environment
5. **Runtime consistency**: The same package structure is preserved in the runtime container

### Alternative: Using a Python project

For larger projects, create a proper Python project with `pyproject.toml`:

```toml
# pyproject.toml
[project]
name = "lib"
version = "0.1.0"

[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"
```

Then install in editable mode:

```bash
pip install -e .
```

After installation, you can run workflows without `--root-dir`:

```bash
flyte run lib/workflows/workflow1.py process_workflow
```

However, for deployment and remote execution, still use `--root-dir` for consistency:

```bash
flyte run --root-dir . lib/workflows/workflow1.py process_workflow
flyte deploy --root-dir . lib/workflows/workflow1.py
```

### When to use

- Multiple related workflows in one project
- Shared task environments and utilities
- Team projects with multiple contributors
- Applications requiring organized code structure
- Projects that benefit from proper Python packaging

## Full build deployment

When you need complete reproducibility and want to embed all code directly in the container image, use the full build pattern. This disables Flyte's fast deployment system in favor of traditional container builds.

### Overview

By default, Flyte uses a fast deployment system that:
- Creates a tar archive of your files
- Skips the full image build and push process
- Provides faster iteration during development

However, sometimes you need to **completely embed your code into the container image** for:
- Full reproducibility with immutable container images
- Environments where fast deployment isn't available
- Production deployments with all dependencies baked in
- Air-gapped or restricted deployment environments

### Key configuration

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/full_build/main.py" lang="python" >}}

### Local dependency example

The main.py file imports from a local dependency that gets included in the build:

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/full_build/dep.py" lang="python" >}}

### Critical configuration components

1. **Set `copy_style` to `"none"`**:
   ```python
   flyte.with_runcontext(copy_style="none", version="x").run(main, n=10)
   ```
   This disables Flyte's fast deployment system and forces a full container build.

2. **Set a custom version**:
   ```python
   flyte.with_runcontext(copy_style="none", version="x").run(main, n=10)
   ```
   The `version` parameter should be set to a desired value (not auto-generated) for consistent image tagging.

3. **Configure image source copying**:
   ```python
   image=flyte.Image.from_debian_base().with_source_folder(
       pathlib.Path(__file__).parent,
       copy_contents_only=True
   )
   ```
   Use `.with_source_folder()` to specify what code to copy into the container.

4. **Set `root_dir` correctly**:
   ```python
   flyte.init_from_config(root_dir=pathlib.Path(__file__).parent)
   ```
   - If `copy_contents_only=True`: Set `root_dir` to the source folder (contents are copied)
   - If `copy_contents_only=False`: Set `root_dir` to parent directory (folder is copied)

### Configuration options

#### Option A: Copy Folder Structure
```python
# Copies the entire folder structure into the container
image=flyte.Image.from_debian_base().with_source_folder(
    pathlib.Path(__file__).parent,
    copy_contents_only=False  # Default
)

# When copy_contents_only=False, set root_dir to parent.parent
flyte.init_from_config(root_dir=pathlib.Path(__file__).parent.parent)
```

#### Option B: Copy Contents Only (Recommended)
```python
# Copies only the contents of the folder (flattens structure)
# This is useful when you want to avoid nested folders - for example all your code is in the root of the repo
image=flyte.Image.from_debian_base().with_source_folder(
    pathlib.Path(__file__).parent,
    copy_contents_only=True
)

# When copy_contents_only=True, set root_dir to parent
flyte.init_from_config(root_dir=pathlib.Path(__file__).parent)
```

### Version management best practices

When using `copy_style="none"`, always specify an explicit version:
- Use semantic versioning: `"v1.0.0"`, `"v1.1.0"`
- Use build numbers: `"build-123"`
- Use git commits: `"abc123"`

Avoid auto-generated versions to ensure reproducible deployments.

### Performance considerations

- **Full builds take longer** than fast deployment
- **Container images will be larger** as they include all source code
- **Better for production** where immutability is important
- **Use during development** when testing the full deployment pipeline

### When to use

✅ **Use full build when:**
- Deploying to production environments
- Need immutable, reproducible container images
- Working with complex dependency structures
- Deploying to air-gapped or restricted environments
- Building CI/CD pipelines

❌ **Don't use full build when:**
- Rapid development and iteration
- Working with frequently changing code
- Development environments where speed matters
- Simple workflows without complex dependencies

### Troubleshooting

**Common issues:**
1. **Import errors**: Check your `root_dir` configuration matches `copy_contents_only`
2. **Missing files**: Ensure all dependencies are in the source folder
3. **Version conflicts**: Use explicit, unique version strings
4. **Build failures**: Check that the base image has all required system dependencies

**Debug tips:**
- Add print statements to verify file paths in containers
- Use `docker run -it <image> /bin/bash` to inspect built images
- Check Flyte logs for build errors and warnings
- Verify that relative imports work correctly in the container context

## Python path deployment

For projects where workflows are separated from business logic across multiple directories, use the Python path pattern with proper `root_dir` configuration.

### Example structure

```
pythonpath/
├── workflows/
│   └── workflow.py      # Flyte workflow definitions
├── src/
│   └── my_module.py     # Business logic modules
├── run.sh               # Execute from project root
└── run_inside_folder.sh # Execute from workflows/ directory
```

### Implementation

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pythonpath/workflows/workflow.py" lang="python" >}}

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pythonpath/src/my_module.py" lang="python" >}}

### Task environment dependencies

Note how the workflow imports both the task environment and the task function:

```python
from src.my_module import env, say_hello

env = flyte.TaskEnvironment(
    name="workflow_env",
    depends_on=[env],  # Depends on the imported environment
)
```

This pattern allows sharing task environments across modules while maintaining proper dependency relationships.

### Key considerations

- **Import resolution**: `root_dir` enables proper module imports across directories
- **File packaging**: Flyte packages all files starting from `root_dir`
- **Execution flexibility**: Works regardless of where you execute the script
- **PYTHONPATH handling**: Different behavior for CLI vs direct Python execution

### CLI vs Direct Python execution

#### Using Flyte CLI with `--root-dir` (Recommended)

When using `flyte run` with `--root-dir`, you don't need to export PYTHONPATH:

```bash
flyte run --root-dir . workflows/workflow.py greet --name "World"
```

The CLI automatically:
- Adds the `--root-dir` location to `sys.path`
- Resolves all imports correctly
- Packages files from the root directory for remote execution

#### Using Python directly

When running Python scripts directly, you must set PYTHONPATH manually:

```bash
PYTHONPATH=.:$PYTHONPATH python workflows/workflow.py
```

This is because:
- Python doesn't automatically know about your project structure
- You need to explicitly tell Python where to find your modules
- The `root_dir` parameter handles remote packaging, not local path resolution

### Best practices

1. **Always set `root_dir`** when workflows import from multiple directories
2. **Use pathlib** for cross-platform path handling
3. **Set `root_dir` to your project root** to ensure all dependencies are captured
4. **Test both execution patterns** to ensure deployment works from any directory

### Common pitfalls

- **Forgetting `root_dir`**: Results in import errors during remote execution
- **Wrong `root_dir` path**: May package too many or too few files
- **Not setting PYTHONPATH when using Python directly**: Use `flyte run --root-dir .` instead
- **Mixing execution methods**: If you use `flyte run --root-dir .`, you don't need PYTHONPATH

### When to use

- Legacy projects with established directory structures
- Separation of concerns between workflows and business logic
- Multiple workflow definitions sharing common modules
- Projects with complex import hierarchies

**Note:** This pattern is an escape hatch for larger projects where code organization requires separating workflows from business logic. Ideally, structure projects with `pyproject.toml` for cleaner dependency management.

## Dynamic environment deployment

For environments that need to change based on deployment context (development vs production), use dynamic environment selection based on Flyte domains.

### Domain-based environment selection

Use `flyte.current_domain()` to deterministically create different task environments based on the deployment domain:

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/dynamic_environments/environment_picker.py" lang="python" >}}

### Why this pattern works

**Environment reproducibility in local and remote clusters is critical.** Flyte re-instantiates modules in remote clusters, so `current_domain()` will be set correctly based on where the code executes.

✅ **Do use `flyte.current_domain()`** - Flyte automatically sets this based on the execution context

❌ **Don't use environment variables directly** - They won't yield correct results unless manually passed to the downstream system

### How it works

1. Flyte sets the domain context when initializing
2. `current_domain()` returns the domain string (e.g., "development", "staging", "production")
3. Your code deterministically configures resources based on this domain
4. When Flyte executes remotely, it re-instantiates modules with the correct domain context
5. The same environment configuration logic runs consistently everywhere

### Important constraints

`flyte.current_domain()` only works **after** `flyte.init()` is called:

- ✅ Works with `flyte run` and `flyte deploy` CLI commands (they init automatically)
- ✅ Works when called from `if __name__ == "__main__"` after explicit `flyte.init()`
- ❌ Does NOT work at module level without initialization

**Critical:** `flyte.init()` invocation at the module level is **strictly discouraged**. The reason is that at runtime, Flyte controls the initialization and configuration files are not present at runtime.

### Alternative: Environment variable approach

For cases where you need to pass domain information as environment variables to the container runtime, use this approach:

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/dynamic_environments_with_envvars/environment_picker.py" lang="python" >}}

#### Key differences from domain-based approach

- **Environment variable access**: The domain name is available inside tasks via `os.environ['DOMAIN_NAME']`
- **External control**: Can be controlled via system environment variables before execution
- **Runtime visibility**: Tasks can inspect which environment they're running in during execution
- **Default fallback**: Uses `"development"` as default when `DOMAIN_NAME` is not set

#### Usage with environment variables

```bash
# Set environment and run
export DOMAIN_NAME=production
flyte run environment_picker.py entrypoint --n 5

# Or set inline
DOMAIN_NAME=development flyte run environment_picker.py entrypoint --n 5
```

#### When to use environment variables vs domain-based

**Use environment variables when:**
- Tasks need runtime access to environment information
- External systems set environment configuration
- You need flexibility to override environment externally
- Debugging requires visibility into environment selection

**Use domain-based approach when:**
- Environment selection should be automatic based on Flyte domain
- You want tighter integration with Flyte's domain system
- No need for runtime environment inspection within tasks

You can vary multiple aspects based on context:

- **Base images**: Different images for dev vs prod
- **Environment variables**: Configuration per environment
- **Resource requirements**: Different CPU/memory per domain
- **Dependencies**: Different package versions
- **Registry settings**: Different container registries

### Usage patterns

```bash
# CLI usage (recommended)
flyte run environment_picker.py entrypoint --n 5
flyte deploy environment_picker.py
```

For programmatic usage, ensure proper initialization:

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/dynamic_environments/main.py" lang="python" >}}

### When to use dynamic environments

**General use cases:**
- Multi-environment deployments (dev/staging/prod)
- Different resource requirements per environment
- Environment-specific dependencies or settings
- Context-sensitive configuration needs

**Domain-based approach for:**
- Automatic environment selection tied to Flyte domains
- Simpler configuration without external environment variables
- Integration with Flyte's built-in domain system

**Environment variable approach for:**
- Runtime visibility into environment selection within tasks
- External control over environment configuration
- Debugging and logging environment-specific behavior
- Integration with external deployment systems that set environment variables

## Best practices

### Project organization

1. **Separate concerns**: Keep business logic separate from Flyte task definitions
2. **Use proper imports**: Structure projects for clean import patterns
3. **Version control**: Include all necessary files in version control
4. **Documentation**: Document deployment requirements and patterns

### Image management

1. **Registry configuration**: Use consistent registry settings across environments
2. **Image tagging**: Use meaningful tags for production deployments
3. **Base image selection**: Choose appropriate base images for your needs
4. **Dependency management**: Keep container images lightweight but complete

### Configuration management

1. **Root directory**: Set `root_dir` appropriately for your project structure
2. **Path handling**: Use `pathlib.Path` for cross-platform compatibility
3. **Environment variables**: Use environment-specific configurations
4. **Secrets management**: Handle sensitive data appropriately

### Development workflow

1. **Local testing**: Test tasks locally before deployment
2. **Incremental development**: Use `flyte run` for quick iterations
3. **Production deployment**: Use `flyte deploy` for permanent deployments
4. **Monitoring**: Monitor deployed tasks and environments

## Choosing the right pattern

| Pattern | Use Case | Complexity | Best For |
|---------|----------|------------|----------|
| Simple file | Quick prototypes, learning | Low | Single tasks, experiments |
| Custom Dockerfile | System dependencies, custom environments | Medium | Complex dependencies |
| PyProject package | Professional projects, async pipelines | Medium-High | Production applications |
| Package structure | Multiple workflows, shared utilities | Medium | Organized team projects |
| Full build | Production, reproducibility | High | Immutable deployments |
| Python path | Legacy structures, separated concerns | Medium | Existing codebases |
| Dynamic environment | Multi-environment, domain-aware deployments | Medium | Context-aware deployments |

Start with simpler patterns and evolve to more complex ones as your requirements grow. Many projects will combine multiple patterns as they scale and mature.