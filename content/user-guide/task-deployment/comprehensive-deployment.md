---
title: How Task Deployment Works
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# How task deployment works

In this section, we will take a deep dive into how the `flyte deploy` command and the `flyte.deploy()` SDK function work under the hood to deploy tasks to your Flyte backend.

## Overview of the deployment process

When you run perform a deployment here's what happens:

### 1. Module loading and task environment discovery

In the first step, Flyte determines which files to load in order to search for task environments, based on the command line options provided:

**Single file (default):**

```bash
flyte deploy my_example.py env
```

- The file `my_example.py` is executed,
- All declared `TaskEnvironment` objects in the file are instantiated,
  but only the one assigned to the variable `env` is selected for deployment.

**`--all` Option:**

```bash
flyte deploy --all my_app.py
```
- The file `my_example.py` is executed,
- All declared `TaskEnvironment` objects in the file are instantiated and selected for deployment.
- No specific variable name is required.

**`--recursive` Option:**
```bash
flyte deploy --recursive ./directory
```

- The directory is recursively traveresed and all Python files are executed and all `TaskEnvironment` objects are isntantiated.
- All `TaskEnvironment` objects across all files are selected for deployment.

### 2. Task Analysis and Serialization

- For every task environment selected for deployment, all of its tasks are identified.
- Task metadata is extracted: parameter types, return types, and resource requirements.
- Each task is serialized into a Flyte `TaskTemplate`.
- Dependency graphs between environments are built (see below).

### 3. Task Environment Dependency Resolution

In many cases, a task in one task environment may invoke a task in another environment, establishing a dependency between the two environments. For example, if `env_a` has a task that calls a task in `env_b`, then `env_a` depends on `env_b`. This means that when deploying `env_a`, `env_b` must also be deployed to ensure that all tasks can be executed correctly.

To handle this, `TaskEnvironment`s can declare dependencies on other `TaskEnvironment`s using the `depends_on` parameter. During deployment, the system performs the following steps to resolve these dependencies:

1. Starting with specified environment(s)
2. Recursively discovering all transitive dependencies
3. Including all dependencies in the deployment plan
4. Processing dependencies depth-first to ensure correct order

```python
# Define environments with dependencies
prep_env = flyte.TaskEnvironment(name="preprocessing")
ml_env = flyte.TaskEnvironment(name="ml_training", depends_on=[prep_env])
viz_env = flyte.TaskEnvironment(name="visualization", depends_on=[ml_env])

# Deploy only viz_env - automatically includes ml_env and prep_env
deployment = flyte.deploy(viz_env, version="v2.0.0")

# Or deploy multiple environments explicitly
deployment = flyte.deploy(data_env, ml_env, viz_env, version="v2.0.0")
```

For detailed information about working with multiple environments, see [Multiple Environments](../task-configuration/multiple-environments).

### 4. Code bundle creation AND Upload

Once the task environments and their dependencies are resolved, Flyte proceeds to package your code into a bundle based on the `copy_style` option:

**`"loaded_modules"` (default):**
This is the smart bundling approach that analyzes which Python modules were actually imported during the task environment discovery phase.
It examines the runtime module registry (`sys.modules`) and includes only those modules that meet specific criteria: they must have source files located within your project directory (not in system locations like `site-packages`), and they must not be part of the Flyte SDK itself.
This selective approach results in smaller, faster-to-upload bundles that contain exactly the code needed to run your tasks, making it ideal for most development and production scenarios.

**`"all"`:**
This comprehensive bundling strategy takes a directory-walking approach, recursively traversing your entire project directory and including every file it encounters.
Unlike the smart bundling that only includes imported Python modules, this method captures all project files regardless of whether they were imported during discovery.
This is particularly useful for projects that use dynamic imports, load configuration files or data assets at runtime, or have dependencies that aren't captured through normal Python import mechanisms.

**`"none"`:**
This option completely skips code bundle creation, meaning no source code is packaged or uploaded to cloud storage.
When using this approach, you must provide an explicit version parameter since there's no code bundle to generate a version from.
This strategy is designed for scenarios where your code is already baked into custom container images, eliminating the need for separate code injection during task execution.
It results in the fastest deployment times but requires more complex image management workflows.

After the code bundle is created (if applicable), it is uploaded to a cloud storage location (like S3 or GCS) accessible by your Flyte backend.

### 5. Image Building (if needed)

If your `TaskEnvironment` specifies [custom images](../task-configuration/container-images), Flyte builds and pushes container images before deploying tasks. The build process varies based on your configuration and backend type:

**Local Image Building:**
When `image.builder` is set to `local` in [your `config.yaml`](../getting-started/local-setup), images are built on your local machine using Docker. This approach:
- Requires Docker to be installed and running on your development machine
- Uses Docker BuildKit to build images from generated Dockerfiles or your custom Dockerfile
- Pushes built images to the container registry specified in your `Image` configuration
- Is the only option available for Flyte OSS instances

**Remote Image Building:**
When `image.builder` is set to `remote` in [your `config.yaml`](../getting-started/local-setup), images are built on cloud infrastructure. This approach:
- Builds images using Union's ImageBuilder service (currently only available for Union backends, not OSS Flyte)
- Requires no local Docker installation or configuration
- Can push to Union's internal registry or external registries you specify
- Provides faster, more consistent builds by leveraging cloud resources

> [!NOTE]
> Remote building is currently exclusive to Union backends - OSS Flyte installations must use `local`

## Deployment options and configuration

### Command Line Options

The `flyte deploy` command provides extensive configuration options:

```bash
flyte deploy [OPTIONS] <PATH> [ENVIRONMENT_VARIABLE]
```

### Core Options

**Project and Domain:**
```bash
# Specify target project and domain
flyte deploy --project my-project --domain development my_app.py env

# Use defaults from configuration
flyte deploy my_app.py env
```

**Versioning:**
```bash
# Explicit version
flyte deploy --version v1.0.0 my_app.py env

# Auto-generated version (default)
flyte deploy my_app.py env
```

**Dry Run:**
```bash
# Preview what would be deployed
flyte deploy --dry-run my_app.py env
```

### Code Bundling Options

The `--copy-style` option controls what gets packaged:

**Smart Bundling (Default):**
```bash
flyte deploy --copy-style loaded_modules my_app.py env
```
- **Includes**: Only imported Python modules from your project
- **Excludes**: Site-packages, system modules, Flyte SDK
- **Best for**: Most projects (optimal size and speed)

**Comprehensive Bundling:**
```bash
flyte deploy --copy-style all my_app.py env
```
- **Includes**: All files in project directory
- **Best for**: Projects with dynamic imports or data files

**No Bundling:**
```bash
flyte deploy --copy-style none --version v1.0.0 my_app.py env
```
- **Requires**: Explicit version parameter
- **Best for**: Pre-built container images with baked-in code

### Environment Discovery Options

Control which environments get discovered and deployed:

**Single Environment (Default):**
```bash
# Deploy specific environment variable
flyte deploy my_app.py env
```

**All Environments in File:**
```bash
# Deploy all TaskEnvironment objects in file
flyte deploy --all my_app.py
```

**Recursive Directory Deployment:**
```bash
# Deploy all environments in directory tree
flyte deploy --recursive ./src

# Combine with comprehensive bundling
flyte deploy --recursive --copy-style all ./project
```

### Image Management Options

**Custom Image Mappings:**
```bash
# Map image references to specific URIs
flyte deploy --image base=ghcr.io/org/base:v1.0 my_app.py env

# Multiple image mappings
flyte deploy \
  --image base=ghcr.io/org/base:v1.0 \
  --image gpu=ghcr.io/org/gpu:v2.0 \
  my_app.py env
```

**Root Directory Override:**
```bash
# Useful for monorepos
flyte deploy --root-dir ./services/ml ./services/ml/app.py env
```

### Error Handling Options

**Ignore Load Errors:**
```bash
# Continue deployment despite module failures
flyte deploy --recursive --ignore-load-errors ./large-project
```

**Path Synchronization:**
```bash
# Disable local sys.path sync (advanced use case)
flyte deploy --no-sync-local-sys-paths my_app.py env
```

## SDK Deployment Options

The core deployment functionality is available programmatically through the `flyte.deploy()` function, though some CLI-specific options are not applicable:

### Basic SDK Deployment

```python
import flyte

env = flyte.TaskEnvironment(name="my_env")

@env.task
async def process_data(data: str) -> str:
    return f"Processed: {data}"

if __name__ == "__main__":
    flyte.init_from_config()

    # Basic deployment
    deployment = flyte.deploy(env)
```

### SDK Deployment with Options

```python
# Comprehensive deployment configuration
deployment = flyte.deploy(
    env,                          # Environment to deploy
    dryrun=False,                # Set to True for dry run
    version="v1.2.0",            # Explicit version tag
    copy_style="loaded_modules"   # Code bundling strategy
)

print(f"Deployment successful: {deployment[0].summary_repr()}")
```

[DONE TO HERE]()

## Option Interactions and Best Practices

### Understanding Option Relationships

**Environment Discovery vs. Code Bundling:**
- `--recursive`/`--all` control **which files are loaded** to find environments
- `--copy-style` controls **what code gets packaged** for deployment
- These operate independently and can be combined freely

**Single Bundle for Multiple Environments:**
```bash
# All discovered environments share the same code bundle
flyte deploy --recursive --copy-style loaded_modules ./project
```

**Version Requirements:**
```bash
# copy-style none requires explicit version
flyte deploy --copy-style none --version v1.0.0 my_app.py env
```

### Deployment Strategies by Use Case

**Development Workflow:**
```bash
# Quick iteration with optimal bundling
flyte deploy my_workflow.py env

# Test without deploying
flyte deploy --dry-run my_workflow.py env
```

**Project-Wide Deployment:**
```bash
# Deploy all environments in project
flyte deploy --recursive ./src

# Include all project files
flyte deploy --recursive --copy-style all ./src
```

**Production Deployment:**
```bash
# Versioned deployment with pre-built images
flyte deploy --copy-style none --version v1.2.0 app.py env

# Custom image deployment
flyte deploy \
  --version v1.2.0 \
  --image prod=ghcr.io/org/prod:v1.2.0 \
  app.py env
```

**Monorepo Management:**
```bash
# Service-specific deployment
flyte deploy --root-dir ./services/ml ./services/ml/main.py env

# Robust deployment ignoring errors
flyte deploy --recursive --ignore-load-errors ./services
```

## Fast Registration Architecture

Flyte v2 uses "fast registration" to enable rapid development cycles:

### How It Works

1. **Container Images** contain the runtime environment and dependencies
2. **Code Bundles** contain your Python source code (stored separately)
3. **At Runtime**: Code bundles are downloaded and injected into running containers

### Benefits

- **Rapid Iteration**: Update code without rebuilding images
- **Resource Efficiency**: Share images across multiple deployments
- **Version Flexibility**: Run different code versions with same base image
- **Caching Optimization**: Separate caching for images vs. code

### When Code Gets Injected

```python
# At task execution time:
# 1. Container starts with base image
# 2. Flyte agent downloads code bundle from storage
# 3. Code is extracted into container
# 4. Your task function executes
```

## Advanced Deployment Patterns

### Multi-Environment Workflows

```python
# Environment dependencies
prep_env = flyte.TaskEnvironment(name="preprocessing")
ml_env = flyte.TaskEnvironment(
    name="ml_training",
    depends_on=[prep_env],
    resources=flyte.Resources(memory="8Gi", cpu="4")
)

# Deploy with dependency resolution
flyte.deploy(ml_env)  # Automatically deploys prep_env too
```

### Dynamic Environment Selection

```python
def create_environment():
    if flyte.current_domain() == "development":
        return flyte.TaskEnvironment(
            name="dev_env",
            image=flyte.Image.from_debian_base()
        )
    else:
        return flyte.TaskEnvironment(
            name="prod_env",
            image=flyte.Image.from_registry("prod-image:latest"),
            resources=flyte.Resources(memory="4Gi", cpu="2")
        )

env = create_environment()
```

### Custom Image Workflows

```python
# Custom Dockerfile
env = flyte.TaskEnvironment(
    name="custom_env",
    image=flyte.Image.from_dockerfile(
        "Dockerfile",
        registry="ghcr.io/myorg",
        name="my_custom_image"
    )
)

# Extended base image
ml_env = flyte.TaskEnvironment(
    name="ml_env",
    image=flyte.Image.from_registry("pytorch/pytorch:2.0")
        .with_pip_packages("transformers", "datasets")
        .with_apt_packages("git", "curl")
)
```

## Troubleshooting Deployment

### Common Issues and Solutions

**Module Load Errors:**
```bash
# Use ignore-load-errors for large codebases
flyte deploy --recursive --ignore-load-errors ./project
```

**Missing Dependencies:**
```bash
# Use comprehensive bundling
flyte deploy --copy-style all my_app.py env
```

**Image Build Failures:**
```bash
# Check image configuration and registry access
flyte deploy --dry-run my_app.py env  # Preview without building
```

**Version Conflicts:**
```bash
# Use explicit versions
flyte deploy --version $(git rev-parse HEAD) my_app.py env
```

### Debugging Deployment

```python
# SDK debugging with detailed output
import logging
logging.basicConfig(level=logging.DEBUG)

deployment = flyte.deploy(env, dryrun=True)  # Test without deploying
print(deployment[0].summary_repr())
```

## Summary

Task Environment deployment in Flyte v2 provides a flexible and powerful system for moving your code to production. Key concepts to remember:

- **Deploy environments, not individual tasks** - TaskEnvironments are the unit of deployment
- **Fast registration** separates code from container images for rapid iteration
- **Flexible bundling** with `copy_style` options for different project needs
- **Comprehensive discovery** with `--recursive` and `--all` for complex projects
- **Rich configuration** options for production and development workflows

The deployment system is designed to scale from simple single-task experiments to complex multi-environment production workflows while maintaining developer productivity and operational efficiency.