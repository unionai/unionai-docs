---
title: Projects and domains
weight: 6
variants: -flyte +byoc +selfmanaged
---

# Projects and domains

{{< key product_name >}} organizes work into a hierarchy of **organization**, **projects**, and **domains**.

- **Organization**: Your {{< key product_name >}} instance, typically representing a company or department. Set up during onboarding and mapped to your endpoint URL (e.g., `my-org.my-company.com`). You do not create or manage organizations directly.
- **Project**: A logical grouping of related workflows, tasks, launch plans, and executions. Projects are the primary unit you create and manage.
- **Domain**: An environment classification within each project. Three fixed domains exist: `development`, `staging`, and `production`. Domains cannot be created or deleted.

Every project contains all three domains, creating **project-domain pairs** like `my-project/development`, `my-project/staging`, and `my-project/production`. Workflows, executions, and data are scoped to a specific project-domain pair.

## How projects and domains are used

When you run or deploy workflows, you target a project and domain:

- **CLI**: Use `--project` and `--domain` flags with `flyte run` or `flyte deploy`, or set defaults in your [configuration file](./connecting-to-a-cluster).
- **Python SDK**: Specify `project` and `domain` in [`flyte.init`](../api-reference/flyte-sdk/packages/flyte/_index#init) or [`flyte.init_from_config`](../api-reference/flyte-sdk/packages/flyte/_index#init_from_config).

Projects and domains also determine:

- **Access control**: RBAC policies scope permissions to an organization, project, domain, or project-domain pair. See [User management](./user-management).
- **Data isolation**: Storage and cache are isolated per project-domain pair.

## Managing projects via CLI

> [!NOTE]
> Project management currently uses the `uctl` CLI. This will move to the `flyte` CLI in a future release.

### Create a project

```shell
uctl create project \
    --name my-project \
    --id my-project \
    --description "My project description"
```

The `--id` is a unique identifier used in CLI commands and configuration. The `--name` is a human-readable label. The project name must not contain whitespace.

You can also create a project from a YAML file:

```yaml
:name: project.yaml

id: "my-project"
name: "my-project"
description: "My project description"
labels:
  values:
    team: ml-platform
```

```shell
uctl create project --file project.yaml
```

See [`uctl create project`](../api-reference/uctl-cli/uctl-create/uctl-create-project) for all options.

### List projects

List all projects:

```shell
uctl get project
```

Get a specific project:

```shell
uctl get project my-project
```

Filter and sort results:

```shell
uctl get project --filter.sortBy=created_at --filter.limit=10 --filter.asc
```

See [`uctl get project`](../api-reference/uctl-cli/uctl-get/uctl-get-project) for all options.

### Update a project

Update the description or labels of a project:

```shell
uctl update project -p my-project --description "Updated description" --labels team=ml-platform
```

See [`uctl update project`](../api-reference/uctl-cli/uctl-update/uctl-update-project) for all options.

### Archive a project

Archiving a project hides it from default listings but does not delete its data:

```shell
uctl update project -p my-project --archive
```

### Activate an archived project

Restore an archived project to active status:

```shell
uctl update project -p my-project --activate
```

## Listing projects programmatically

You can list and retrieve projects from Python using [`flyte.remote.Project`](../api-reference/flyte-sdk/packages/flyte.remote/project/_index):

```python
import flyte

flyte.init_from_config()

# Get a specific project
project = flyte.remote.Project.get(name="my-project", org="my-org")

# List all projects
for project in flyte.remote.Project.listall():
    print(project.to_dict())

# List with filtering and sorting
for project in flyte.remote.Project.listall(sort_by=("created_at", "desc")):
    print(project.to_dict())
```

Both `get()` and `listall()` support async execution via `.aio()`:

```python
project = await flyte.remote.Project.get.aio(name="my-project", org="my-org")
```

> [!NOTE]
> The Python SDK provides read-only access to projects. To create or modify projects, use the `uctl` CLI or the UI.

## Managing projects via the UI

When you log in to your {{< key product_name >}} instance, you land on the **Projects** page, which lists all projects in your organization. By default, the domain is set to `development`. You can change the active domain using the selector in the top left.

From the project list you can:

* **Open a project**: Select a project from the list to navigate to it.
* **Create a project**: Click **+ New project** in the top right. In the dialog, specify a name and description. The project will be created across all three domains.
* **Archive a project**: Click the three-dot menu on a project's entry and select **Archive project**.

## Domains

Domains provide environment separation within each project. The three domains are:

| Domain | Purpose |
|--------|---------|
| `development` | For iterating on workflows during active development. |
| `staging` | For testing workflows before promoting to production. |
| `production` | For production workloads. |

Domains are predefined and cannot be created, renamed, or deleted.

### Targeting a domain

Set the default domain in your configuration file:

```yaml
task:
  domain: development
```

Or override per command:

```shell
flyte run --domain staging hello.py main
```

When using `flyte deploy`, the domain determines where the deployed workflows will execute:

```shell
flyte deploy --project my-project --domain production workflows
```
