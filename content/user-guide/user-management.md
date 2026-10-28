---
title: User management
description: Manage users, roles, and policies for your Union cluster.
icon: person
weight: 8
variants: -flyte +union
---

# User management

Union includes role-based access control (RBAC) for managing user and application permissions.
The system has four core concepts:

* **Role**: A named set of actions (e.g. view inventory, create executions).
* **Policy**: Binds one or more roles to specific projects, domains, or the entire organization.
* **User / Application**: An actor assigned to policies. Users are identified by email; applications by ID.
* **Action**: An operation like `view_flyte_inventory`, `create_flyte_executions` or `manage_secrets`. See [Available actions](#available-actions).

## Built-in policies

Union ships with three built-in policies:

| Policy | Actions | Summary |
|---|---|---|
| **Admin** | All actions | Full control including user management and billing |
| **Contributor** | `create_flyte_executions`, `register_flyte_inventory`, `view_flyte_executions`, `view_flyte_inventory`, `edit_execution_related_attributes`, `edit_cluster_related_attributes`, `view_llm_gateway`, `manage_llm_gateway_keys`, `view_secrets`, `manage_secrets`, `view_apps`, `manage_apps`, `view_triggers`, `manage_triggers`, `view_workspaces`, `manage_workspaces`, `view_artifacts`, `manage_artifacts`, `view_settings`, `edit_settings`, `manage_api_keys`, `view_clusters`, `view_usage`, `view_identities` | Register and run workflows |
| **Viewer** | `view_flyte_executions`, `view_flyte_inventory`, `view_llm_gateway`, `view_apps`, `view_triggers`, `view_workspaces`, `view_artifacts`, `view_settings`, `view_clusters`, `view_usage`, `view_identities` | Read-only access |

Built-in policies are managed by Union. Custom roles only hold the actions you give them.

Users can hold multiple policies: permissions are the union of all assigned policies.

## Custom roles and policies

For fine-grained control, create custom roles and policies using the CLI or programmatically.

### Prerequisites

Install the Union CLI plugin:

```bash
pip install 'flyteplugins-union>=0.20.1'
```

This adds `role`, `policy`, `assignment`, `user`, and `member` subcommands to the `flyte` CLI.

> [!WARNING]
> Use `flyteplugins-union` 0.20.1 or later.
> Older versions don't support every action in [Available actions](#available-actions).
> They fail to read a role that holds one (`flyte get role`, `flyte update role`, `Role.get`),
> and `Role.update` silently removes them.

### Walkthrough: restrict a team to run workflows in production only

The goal: create a role that can view and execute workflows but not register new ones,
bind it to the production domain of a specific project, and assign it to a user.

{{< tabs "walkthrough-create" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Role, Policy, Assignment

# Step 1 — Create the role
Role.create(
    "Production Runner",
    description="Can view and execute workflows",
    actions=[
        "view_flyte_inventory",
        "view_flyte_executions",
        "create_flyte_executions",
    ],
)

# Step 2 — Create the policy
Policy.create(
    "Team Prod Access",
    description="Production execution access for the team",
    bindings=[
        {
            "role": "Production Runner",
            "resource": {
                "project": "my-project",
                "domain": "production",
            },
        },
    ],
)

# Step 3 — Assign the policy to a user
Assignment.create(email="jane@example.com", policy="Team Prod Access")
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
**Step 1: Create the role**

Use `--edit` to open an interactive editor (no YAML file needed):

```bash
flyte create role "Production Runner" --edit
```

Your `$EDITOR` opens with a template. Set the actions:

```yaml
name: Production Runner
description: Can view and execute workflows
actions:
  - view_flyte_inventory
  - view_flyte_executions
  - create_flyte_executions
```

Save and close. The role is created.

**Step 2: Create the policy**

```bash
flyte create policy "Team Prod Access" --edit
```

Bind the role to a specific project and domain:

```yaml
name: Team Prod Access
description: Production execution access for the team
bindings:
  - role: Production Runner
    resource:
      project: my-project
      domain: production
```

**Step 3: Assign the policy to a user**

```bash
flyte create assignment --email jane@example.com --policy "Team Prod Access"
```

You can also assign by user subject or application credentials subject:

```bash
flyte create assignment --user-subject user-123 --policy "Team Prod Access"
flyte create assignment --creds-subject app-456 --policy "Team Prod Access"
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Updating roles and policies

{{< tabs "walkthrough-update" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}

```python
from flyteplugins.union.remote import Role, Policy

# Add an action to an existing role
Role.update(
    "Production Runner",
    actions=[
        "view_flyte_inventory",
        "view_flyte_executions",
        "create_flyte_executions",
        "register_flyte_inventory",  # newly added
    ],
)

# Update policy bindings
policy = Policy.get("Team Prod Access")
new_bindings = policy.bindings + [
    {
        "role": "Production Runner",
        "resource": {"project": "my-project", "domain": "staging"},
    },
]
Policy.update("Team Prod Access", old_bindings=policy.bindings, new_bindings=new_bindings)
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
`update` opens the existing definition in your editor so you can modify it in place:

```bash
flyte update role "Production Runner"
flyte update policy "Team Prod Access"
```

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Managing users in the UI

Navigate to **Settings > User Management** to:

* **View users**: see all users and their assigned policies.
* **Add a user**: specify name, email, and policies. The user receives an email invite.
* **Change policies**: select a user and edit their assignments.
* **Remove a user**: select a user and remove them.

## Available actions

| Action | Description |
|---|---|
| `administer_project` | Archive/update projects, manage customizable resources |
| `manage_permissions` | Manage users, applications, and policy assignments |
| `view_permissions` | View roles, policies, and assignments |
| `create_flyte_executions` | Launch runs and upload inputs |
| `register_flyte_inventory` | Register and deploy workflows, tasks, and launch plans |
| `view_flyte_executions` | View runs and actions |
| `view_flyte_inventory` | View registered workflows, tasks, and launch plans |
| `view_secrets` | View secrets (get, list) |
| `manage_secrets` | Create, update, and delete secrets |
| `view_apps` | View apps, replicas, app logs, and app metrics |
| `manage_apps` | Deploy, update, and delete apps |
| `view_triggers` | View triggers and their revision history |
| `manage_triggers` | Activate and deactivate triggers (creating and deleting triggers requires `register_flyte_inventory`) |
| `view_workspaces` | View workspace definitions and instances |
| `manage_workspaces` | Create and update workspace definitions; start and stop workspace instances |
| `view_artifacts` | View artifacts, cards, and artifact usage |
| `manage_artifacts` | Create, declare, tag, and delete artifacts |
| `view_settings` | View settings |
| `edit_settings` | Create and update settings |
| `manage_api_keys` | Create and delete API keys |
| `view_clusters` | View clusters, cluster pools, node groups, and cluster usage |
| `view_usage` | View usage, metrics, quotas, and credits |
| `view_identities` | View users and members |
| `administer_account` | Manage billing and account-wide settings |
| `manage_cluster` | Manage clusters |
| `manage_queue` | Manage cluster queues |
| `view_cluster_config` | View the component configuration of a cluster |
| `edit_execution_related_attributes` | Edit execution-related attributes (task resources, workflow execution config, external resources) |
| `edit_cluster_related_attributes` | Edit cluster-related attributes (cluster resources, cluster assignment) |
| `edit_unused_attributes` | Edit execution queue, execution cluster label, quality of service, and plugin override attributes |
| `support_system_logs` | View system logs |
| `view_llm_gateway` | View the LLM gateway, its providers, virtual keys, and usage |
| `manage_llm_gateway` | Deploy and delete the LLM gateway and manage its upstream providers |
| `manage_llm_gateway_keys` | Issue and revoke LLM gateway virtual keys |

## CLI command reference

| Command | Description |
|---|---|
| `flyte create role <name> --edit \| --file <path>` | Create a role interactively or from YAML |
| `flyte get role [<name>]` | List all roles or view a specific one |
| `flyte update role <name>` | Edit a role in `$EDITOR` |
| `flyte delete role <name>` | Delete a role |
| `flyte create policy <name> --edit \| --file <path>` | Create a policy interactively or from YAML |
| `flyte get policy [<name>]` | List all policies or view a specific one |
| `flyte update policy <name>` | Edit a policy in `$EDITOR` |
| `flyte delete policy <name>` | Delete a policy |
| `flyte create assignment --email <email> \| --user-subject <id> \| --creds-subject <id> --policy <name>` | Assign a policy to a user or application |
| `flyte get assignment [--user-subject <id> \| --creds-subject <id>]` | List all assignments or view a specific one |
| `flyte delete assignment --user-subject <id> \| --creds-subject <id> --policy <name>` | Unassign a policy from a user or application |
| `flyte get user [<subject>]` | List all users or view a specific one |
| `flyte delete user <subject>` | Delete a user |
| `flyte get member` | List all members (users and applications) |
