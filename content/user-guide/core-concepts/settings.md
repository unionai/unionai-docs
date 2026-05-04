---
title: Settings
weight: 7
variants: -flyte +union
---

# Settings

{{< key product_name >}} provides a hierarchical settings system for configuring default behavior at each level of your [org → domain → project hierarchy](./projects-and-domains). Settings defined at a broader scope are inherited by narrower scopes, and any scope can override an inherited value.

Settings are **defaults only** — they apply when a task or workflow does not specify a value directly. Per-task configuration (such as `Resources` or `TaskEnvironment`) always takes precedence over scope-level settings.

## Scope hierarchy

Settings are stored at three scope levels:

| Scope | Who manages it | Inherits from |
|-------|---------------|---------------|
| **Org** | Org admins | — |
| **Domain** | Org admins | Org |
| **Project** | Project owners, org admins | Domain, then org |

When a setting has no value at the current scope, the next broader scope is consulted automatically.

## Editing settings

Use `flyte edit settings` to view and modify settings interactively. The command opens your `$EDITOR` with a structured YAML file showing the current state of that scope.

```shell
# Edit org-level settings
flyte edit settings

# Edit domain-level settings (inherits from org)
flyte edit settings --domain production

# Edit project-level settings (inherits from domain, then org)
flyte edit settings --domain production --project ml-pipeline
```

The editor file has three sections:

- **Local overrides** — values explicitly set at this scope.
- **Inherited settings** — values resolved from a parent scope, shown as comments with their origin.
- **Available settings** — all remaining keys, shown as commented placeholders with descriptions.

Example editor file for a domain that has one local override and one inherited setting:

```yaml
### Settings for scope: DOMAIN(production)
## Remove or comment out a line to inherit that setting from the parent scope.
## Set a value to ~unset to explicitly clear it, blocking parent inheritance.

### Local overrides
## Default queue for task runs
run.default_queue: fast-queue

### Inherited settings (uncomment to override at this scope)
## Kubernetes service account for task pods
# security.service_account: default  ## inherited from ORG

### Available settings (uncomment and edit to set at this scope)
## Base path for raw data storage (e.g. s3://my-bucket/prefix)
# storage.raw_data_path: ''
## CPU resource quantity (e.g. "500m", "2")
# task_resource.min.cpu: ''
## Memory resource quantity (e.g. "256Mi", "4Gi")
# task_resource.min.memory: ''
...
```

The three comment prefixes have distinct roles:

| Prefix | Meaning |
|--------|---------|
| `###` | Section header |
| `##` | Field description or metadata |
| `#` | Inactive setting — remove the leading `#` to activate |

To set or change a value, uncomment the relevant line and edit it. To stop overriding a setting and revert to inheriting from the parent scope, comment out or delete the line entirely.

When you save and close the editor, the CLI prints a summary of your changes and asks for confirmation before applying them:

```
Changes to apply:
  + run.default_queue: fast-queue
  ~ task_resource.min.cpu: 500m → 2

Apply these changes? [Y/n]:
```

> [!NOTE]
> If your YAML fails to parse after saving, the editor reopens with an error header above your content so you can correct the syntax without losing your work. If you decline to reopen, your edits are saved automatically to `~/.flyte/settings-edit-<timestamp>.yaml`.

### Apply settings from a file

For CI pipelines or scripted setup, use `--from-file` to skip the interactive editor entirely:

```shell
flyte edit settings --domain production --from-file settings.yaml
```

The file should be a plain YAML mapping of dot-notation keys to values. Changes are printed and applied immediately without a confirmation prompt.

## Available settings

| Key | Type | Description |
|-----|------|-------------|
| `run.default_queue` | string | Default queue for task runs |
| `security.service_account` | string | Kubernetes service account for task pods |
| `storage.raw_data_path` | string | Base path for raw data storage (e.g. `s3://my-bucket/prefix`) |
| `task_resource.min.cpu` | quantity | Minimum CPU request applied to task pods (e.g. `500m`, `2`) |
| `task_resource.min.gpu` | quantity | Minimum GPU request applied to task pods (e.g. `1`) |
| `task_resource.min.memory` | quantity | Minimum memory request applied to task pods (e.g. `256Mi`, `4Gi`) |
| `task_resource.min.storage` | quantity | Minimum ephemeral storage request applied to task pods (e.g. `10Gi`) |
| `task_resource.max.cpu` | quantity | Maximum CPU limit applied to task pods |
| `task_resource.max.gpu` | quantity | Maximum GPU limit applied to task pods |
| `task_resource.max.memory` | quantity | Maximum memory limit applied to task pods |
| `task_resource.max.storage` | quantity | Maximum ephemeral storage limit applied to task pods |
| `task_resource.mirror_limits_request` | bool | When `true`, resource limits are set equal to requests |
| `labels` | list | Kubernetes labels applied to task pods |
| `annotations` | map | Kubernetes annotations applied to task pods |
| `environment_variables` | map | Environment variables injected into task pods |

Quantity values use Kubernetes resource quantity format. Examples: `500m` (0.5 CPU), `2` (2 CPU), `256Mi` (256 mebibytes), `4Gi` (4 gibibytes).

## Inheritance rules

**Scalar settings** — `run`, `security`, `storage`, and `task_resource` fields: the most specific scope with a value wins. If the project sets `run.default_queue`, that value is used. If not, the domain's value is checked, then the org's.

**Map settings** — `annotations` and `environment_variables`: entries merge across scopes, with parent entries applied first and child entries overriding on key conflict. For example, if the org sets `LOG_LEVEL=info` and the project sets `LOG_LEVEL=debug`, the project's value wins.

**List settings** — `labels`: items accumulate across scopes, with parent items listed first and child items appended.

### Explicitly clearing a value

Set a value to `~unset` to stop inheritance at that scope without providing a value of its own. Child scopes can still define their own value. For map and list settings, `~unset` clears all accumulated entries from parent scopes.

```yaml
# This domain has no service account — child projects are free to set their own.
security.service_account: ~unset

# Clear all environment variables inherited from org at this domain level.
environment_variables: ~unset
```

## Relationship to task configuration

Settings provide defaults only. Any value set directly on a task — through `Resources`, `TaskEnvironment`, task decorator arguments, or a per-invocation override — takes precedence over the scope-level setting for that task, regardless of which scope the setting was defined at.

For example, if the org sets `task_resource.min.cpu: "500m"` as a default, a task with `@task(resources=Resources(cpu="2"))` will still use `2` CPUs.

## Permissions

Settings operations require the following actions, scoped to the org, domain, or project being accessed:

| Operation | Required action |
|-----------|----------------|
| View settings (open the editor) | `view_flyte_inventory` |
| Create or update settings | `register_flyte_inventory` |

The **Contributor** built-in role includes both actions. The **Viewer** role includes `view_flyte_inventory` only. See [User management](../user-management) for details on roles and how to assign them.
