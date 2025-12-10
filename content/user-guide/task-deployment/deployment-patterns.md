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
3. **[PyProject package deployment](#pyproject-package-deployment)** - Structured Python packages with dependencies
4. **[Full build deployment](#full-build-deployment)** - Complete code embedding in containers
5. **[Python path deployment](#python-path-deployment)** - Multi-directory project structures
6. **[Dynamic environment deployment](#dynamic-environment-deployment)** - Environment selection based on context

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

### Key considerations

- **Path handling**: Use `Path(__file__).parent` for relative Dockerfile paths
- **Registry configuration**: Specify a registry for image storage
- **Build context**: The directory containing the Dockerfile becomes the build context
- **Dependencies**: Include all requirements in the Dockerfile or requirements.txt

### When to use

- Need specific system packages or tools
- Custom base image requirements
- Complex installation procedures
- Multi-stage build optimization

## PyProject package deployment

For structured Python projects with proper package management, use the PyProject pattern. This approach provides:

- Proper dependency management with `pyproject.toml`
- Clean separation of business logic and Flyte tasks
- Professional project structure with `src/` layout
- Support for async task execution

### Example structure

```
pyproject_package/
├── pyproject.toml          # Project metadata and dependencies
├── .python-version         # Python version specification
└── src/
    └── pyproject_package/
        ├── __init__.py     # Package initialization
        ├── main.py         # Entrypoint with Flyte tasks
        ├── data/
        │   ├── __init__.py
        │   ├── loader.py   # Data utilities (no Flyte)
        │   └── processor.py # Processing utilities (no Flyte)
        ├── models/
        │   ├── __init__.py
        │   └── analyzer.py # Analysis utilities (no Flyte)
        └── tasks/
            ├── __init__.py
            └── tasks.py    # Flyte task definitions
```

### Key components

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pyproject_package/src/pyproject_package/tasks/tasks.py" lang="python" >}}

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pyproject_package/src/pyproject_package/main.py" lang="python" >}}

### Configuration

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/pyproject_package/pyproject.toml" lang="toml" >}}

### When to use

- Professional, maintainable projects
- Clear separation between business logic and orchestration
- Complex dependency management
- Team development with proper package structure

## Full build deployment

When you need complete reproducibility and want to embed all code directly in the container image, use the full build pattern. This disables Flyte's fast deployment system in favor of traditional container builds.

### Key configuration

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/full_build/main.py" lang="python" >}}

### Configuration options

- **`copy_style="none"`**: Disables Flyte's fast deployment system
- **`version="v1.0"`**: Sets explicit version for reproducible image tagging
- **`copy_contents_only=True`**: Copies folder contents without creating nested directories
- **`root_dir`**: Must match the source folder configuration

### When to use

- Production deployments requiring full reproducibility
- Environments where fast deployment isn't available
- Immutable container image requirements
- Air-gapped or restricted deployment environments

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

### Key considerations

- **Import resolution**: `root_dir` enables proper module imports across directories
- **File packaging**: Flyte packages all files starting from `root_dir`
- **Execution flexibility**: Works regardless of where you execute the script
- **PYTHONPATH**: May need to set `PYTHONPATH` for local development

### When to use

- Legacy projects with established directory structures
- Separation of concerns between workflows and business logic
- Multiple workflow definitions sharing common modules
- Projects with complex import hierarchies

## Dynamic environment deployment

For environments that need to change based on deployment context (development vs production), use dynamic environment selection.

### Implementation

{{< code file="/external/unionai-examples/v2/user-guide/task-deployment/deployment-patterns/dynamic_environments/environment_picker.py" lang="python" >}}

### Environment variations

You can vary multiple aspects based on context:

- **Base images**: Different images for dev vs prod
- **Environment variables**: Configuration per environment
- **Resource requirements**: Different CPU/memory per domain
- **Dependencies**: Different package versions

### When to use

- Multi-environment deployments (dev/staging/prod)
- Context-sensitive configuration
- Different resource requirements per environment
- Environment-specific dependencies or settings

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
| PyProject package | Professional projects, team development | Medium-High | Structured applications |
| Full build | Production, reproducibility | High | Immutable deployments |
| Python path | Legacy structures, separated concerns | Medium | Existing codebases |
| Dynamic environment | Multi-environment deployments | Medium | Context-aware deployments |

Start with simpler patterns and evolve to more complex ones as your requirements grow. Many projects will combine multiple patterns as they scale and mature.