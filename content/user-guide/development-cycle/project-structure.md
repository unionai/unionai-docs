---
title: Project structure
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Project structure

Organizing a workflow project repository effectively is key for ensuring scalability, collaboration, and easy maintenance.
Here are best practices for structuring a {{< key product_name >}} workflow project repo, covering task organization, workflow management, dependency handling, and documentation.

## Recommended Directory Structure

A typical {{< key product_name >}} workflow project structure could look like this:

```shell
├── .github/workflows/
├── .gitignore
├── docs/
│   └── README.md
├── src/
│   ├── core/                    # Core logic specific to the use case
│   │   ├── __init__.py
│   │   ├── model.py
│   │   ├── data.py
│   │   └── structs.py
│   ├── tasks/                   # Contains individual tasks
│   │   ├── __init__.py
│   │   ├── preprocess.py
│   │   ├── fit.py
│   │   ├── test.py
│   │   └── plot.py
│   ├── workflows/               # Contains workflow definitions
│   │   ├── __init__.py
│   │   ├── inference.py
│   │   └── train.py
│   └── orchestration/           # For helper constructs (e.g., secrets, images)
│       ├── __init__.py
│       └── constants.py
├── uv.lock
└── pyproject.toml

```

This structure is designed to ensure each project component has a clear, logical home, making it easy for team members to find and modify files.

## Organizing Tasks and Workflows

In {{< key product_name >}}, tasks are the building blocks of workflows, so it’s important to structure them intuitively:

* **Tasks**: Store each task in its own file within the `tasks/` directory. If multiple tasks are closely related, consider grouping them within a module. Alternatively, each task can have its own module to allow more granular organization and sub-directories could be used to group similar tasks.

* **Workflows**: Store workflows, which combine tasks into end-to-end processes, in the `workflows/` directory. This separation ensures workflows are organized independently from core task logic, promoting modularity and reuse.

## Orchestration Directory for Helper Constructs

Include a directory, such as `orchestration/` or `union_utils/`, for constructs that facilitate workflow orchestration. This can house helper files like:

* **Secrets**: Definitions for accessing secrets (e.g., API keys) in {{< key product_name >}}.

* **ImageSpec**: A tool that simplifies container management, allowing you to avoid writing Dockerfiles directly.

## Core Logic for Workflow-Specific Functionality

Use a `core/` directory for business logic specific to your workflows. This keeps the core application code separate from workflow orchestration code, improving maintainability and making it easier for new team members to understand core functionality.

## Importance of `__init__.py`

Adding `__init__.py` files within each directory is essential:

* **For Imports**: These files make the directory a Python package, enabling proper imports across modules.

* **For {{< key product_name >}}'s Fast Registration**: When performing fast registration, {{< key product_name >}} considers the first directory without an `__init__.py` as the root. {{< key product_name >}} will then package the root and its contents into a tarball, streamlining the registration process and avoiding the need to rebuild the container image every time you make code changes.

## Monorepo vs Multi-repo: Choosing a structure

When working with multiple teams, you have two main options:

* **Monorepo**: A single repository shared across all teams, which can simplify dependency management and allow for shared constructs. However, it can introduce complexity in permissions and version control for different teams.

* **Multi-repo**: Separate repositories for each team or project can improve isolation and control. In this case, consider creating shared, installable packages for constructs that multiple teams use, ensuring consistency without merging codebases.

## CI/CD

The GitHub action should:
* Register (and promote if needed) on merge to domain branch.
* Execute on merge of input YAML.
* Inject git SHA as entity version.

## Documentation and Docstrings

Writing clear docstrings is encouraged, as they are automatically propagated to the {{< key product_name >}} UI. This provides useful context for anyone viewing the workflows and tasks in the UI, reducing the need to consult source code for explanations.
