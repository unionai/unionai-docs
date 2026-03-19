---
title: User management
weight: 8
variants: -flyte +byoc +selfmanaged
---

# User management

Union includes role-based access control (RBAC) for managing user and application permissions.
The system has four core concepts:

* **Role**: A named set of actions (e.g. view inventory, create executions).
* **Policy**: Binds one or more roles to specific projects, domains, or the entire organization.
* **User / Application**: An actor assigned to policies. Users are identified by email; applications by ID.
* **Action**: An operation like `view_flyte_inventory` or `create_flyte_executions`.

## Built-in policies

Union ships with three built-in policies:

| Policy | Actions | Summary |
|---|---|---|
| **Admin** | All actions | Full control including user management and billing |
| **Contributor** | `create_flyte_executions`, `register_flyte_inventory`, `view_flyte_executions`, `view_flyte_inventory` | Register and run workflows |
| **Viewer** | `view_flyte_executions`, `view_flyte_inventory` | Read-only access |

Users can hold multiple policies — permissions are the union of all assigned policies.

## Custom roles and policies

For fine-grained control, create custom roles and policies using the CLI or programmatically.

### Prerequisites

Install the Union CLI plugin:

```bash
pip install flyteplugins-union
```

This adds `role`, `policy`, `assignment`, `user`, and `member` subcommands to the `flyte` CLI.

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
**Step 1 — Create the role**

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

Save and close — the role is created.

**Step 2 — Create the policy**

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

**Step 3 — Assign the policy to a user**

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

* **View users** — see all users and their assigned policies.
* **Add a user** — specify name, email, and policies. The user receives an email invite.
* **Change policies** — select a user and edit their assignments.
* **Remove a user** — select a user and remove them.

## Available actions

| Action | Description |
|---|---|
| `administer_project` | Archive/update projects, manage customizable resources |
| `manage_permissions` | Manage users, applications, and policy assignments |
| `create_flyte_executions` | Launch executions |
| `register_flyte_inventory` | Register workflows, tasks, and launch plans |
| `view_flyte_executions` | View execution history |
| `view_flyte_inventory` | View registered workflows, tasks, and launch plans |

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
