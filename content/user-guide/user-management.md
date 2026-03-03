---
title: User management
weight: 18
variants: -flyte +byoc +selfmanaged
---

# User management

{{< key product_name >}} includes role-based access control (RBAC) for managing user and application permissions.
The authorization system is based on the following concepts:

* **Action**: An operation that can be performed by a **user** or **application**.
  For example, `register_flyte_inventory` is the action of registering tasks and workflows.
* **Role**: A set of **actions**.
  The system includes built-in roles (see below) and also enables administrators to define custom roles.
* **Policy**: A set of bindings between a **role** and an **organization**, **project**, **domain**, or **project-domain** pair.
* **User** or **application**: An actor to which **policies** can be assigned.
  Through the assigned policies, the user or application acquires permission to perform the specified **actions** on the designated resources.
  A user is a person, registered and identified by **email address**.
  An application is an automated process (a bot, service, or other type of program), registered and identified by **application ID**.
* **Organization**: A set of projects associated with a company, department, or other organization.
* **Project**: A set of associated workflows, tasks, launch plans, and other {{< key product_name >}} entities.
* **Domain**: Categories representing the standard environments used in the development process: **development**, **staging**, and **production**.
* **Project-domain pair**: The set of projects is divided orthogonally by the three **domains**.
  The result is a set of project-domain pairs.
  For example: `{{< key default_project >}}/development`, `{{< key default_project >}}/staging`, and `{{< key default_project >}}/production`.

## Actions

The following is the full list of actions available in the {{< key product_name >}} system:

* `administer_project`: Permission to archive and update a project and manage customizable resources.
* `manage_permissions`: Permission to manage user and machine applications and their policy assignments.
* `create_flyte_executions`: Permission to launch new executions.
* `register_flyte_inventory`: Permission to register workflows, tasks, and launch plans.
* `view_flyte_executions`: Permission to view historical execution data.
* `view_flyte_inventory`: Permission to view registered workflows, tasks, and launch plans.

## Built-in policies

{{< key product_name >}} ships with three built-in policies: **Admin**, **Contributor**, and **Viewer**.

* An **Admin** has permission to perform all actions (`administer_project`, `manage_permissions`, `create_flyte_executions`, `register_flyte_inventory`, `view_flyte_executions`, `view_flyte_inventory`) across the organization (in all projects and domains).
  In other words:
  * Invite users and assign roles.
  * View the **Monitoring** and **Billing** dashboards.
  * Do everything a **Contributor** can do.
* A **Contributor** has permission to perform the actions `create_flyte_executions`, `register_flyte_inventory`, `view_flyte_executions`, and `view_flyte_inventory` across the organization (in all projects and domains).
  In other words:
  * Register and execute workflows, tasks, and launch plans.
  * Do everything a **Viewer** can do.
* A **Viewer** has permission to perform the actions `view_flyte_executions` and `view_flyte_inventory` across the organization (in all projects and domains).
  In other words:
  * View workflows, tasks, launch plans, and executions.

## Multiple policies

Users and applications can be assigned to zero or more policies.
A user or application with no policies will have no permissions but will not be removed from the system (they will still appear on the list of users).
A user or application with multiple policies will have the logical union of the permission sets of those policies.

> [!NOTE]
> The default policies that come out of the box are hierarchical.
> The **Admin** permission set is a superset of the **Contributor** permission set, and the **Contributor** permission set is a superset of the **Viewer** permission set.
> This means, for example, that if you make a user an **Admin**, then additionally assigning them **Contributor** or **Viewer** will make no difference.
> But this is only the case due to how these particular roles are defined.
> In general, it is possible to create roles where assigning multiple ones is meaningful.

## Custom roles and policies

You can create custom roles and policies to mix and match permissions at the organization, project, or domain level.

Roles and policies are managed using the [`uctl` CLI](../api-reference/uctl-cli/_index).

### Create a role

Create a role spec file `my_role.yaml` that defines a set of actions:

```yaml
:name: my_role.yaml

name: Workflow Runner
actions:
- view_flyte_inventory
- view_flyte_executions
- create_flyte_executions
```

Create the role from the command line:

```shell
$ uctl create role --roleFile my_role.yaml
```

See [`uctl create role`](../api-reference/uctl-cli/uctl-create/uctl-create-role) for full details.

### List and view roles

To list all roles:

```shell
$ uctl get role
```

To view a specific role:

```shell
$ uctl get role --name "Workflow Runner"
```

See [`uctl get role`](../api-reference/uctl-cli/uctl-get/uctl-get-role) for full details.

### Delete a role

```shell
$ uctl delete role --name "Workflow Runner"
```

See [`uctl delete role`](../api-reference/uctl-cli/uctl-delete/uctl-delete-role) for full details.

### Create a policy

Create a policy spec file `my_policy.yaml` that binds roles to project/domain pairs.
Here we create a policy that binds the **Contributor** role to `{{< key default_project >}}/development` and binds the **Workflow Runner** role (defined above) to `{{< key default_project >}}/production`:

```yaml
:name: my_policy.yaml

name: Workflow Developer Policy
bindings:
- role: Workflow Runner
  resource:
    project: {{< key default_project >}}
    domain: production
- role: contributor # Built-in system role
  resource:
    project: {{< key default_project >}}
    domain: development
```

Create the policy from the command line:

```shell
$ uctl create policy --policyFile my_policy.yaml
```

Any user or application to which this policy is assigned will be granted **Contributor** permissions to `{{< key default_project >}}/development` while being granted the more restrictive **Workflow Runner** permission to `{{< key default_project >}}/production`.

See [`uctl create policy`](../api-reference/uctl-cli/uctl-create/uctl-create-policy) for full details.

### List and view policies

To list all policies:

```shell
$ uctl get policy
```

To view a specific policy:

```shell
$ uctl get policy --name "Workflow Developer Policy"
```

See [`uctl get policy`](../api-reference/uctl-cli/uctl-get/uctl-get-policy) for full details.

### Delete a policy

```shell
$ uctl delete policy --name "Workflow Developer Policy"
```

See [`uctl delete policy`](../api-reference/uctl-cli/uctl-delete/uctl-delete-policy) for full details.

### Assign a policy to a user or application

Once a policy is created, you can assign it to a user or application using the command line:

```shell
$ uctl append identityassignments \
       --user "bob@contoso.com" \
       --policy "Workflow Developer Policy"
```

Similarly, you can assign the policy to an application:

```shell
$ uctl append identityassignments \
       --application "contoso-operator" \
       --policy "Workflow Developer Policy"
```

See [`uctl append identityassignments`](../api-reference/uctl-cli/uctl-append/uctl-append-identityassignments) for full details.

### View identity assignments

To list all identity assignments:

```shell
$ uctl get identityassignment
```

See [`uctl get identityassignment`](../api-reference/uctl-cli/uctl-get/uctl-get-identityassignment) for full details.

### Remove identity assignments

```shell
$ uctl delete identityassignments \
       --user "bob@contoso.com" \
       --policy "Workflow Developer Policy"
```

See [`uctl delete identityassignments`](../api-reference/uctl-cli/uctl-delete/uctl-delete-identityassignments) for full details.

## Initial onboarding

The initial {{< key product_name >}} onboarding process sets up your organization with at least one **Admin** user who has permission to invite teammates and manage their roles.

## Managing users in the UI

You can also manage users and their policy assignments through the {{< key product_name >}} UI.
Navigate to **Settings > User Management** to access the user management interface.

To manage users you must have the **Admin** policy (or a custom policy that includes the `manage_permissions` action).

From the user management interface you can:

* **View users**: See the list of all users and their assigned policies. You can search the list and filter by policy.
* **Add a user**: Add a new user by specifying their name, email, and the policies to assign. The new user will receive an email invite from Okta. They should accept the invite and set up a password, at which point they can access the {{< key product_name >}} UI.
* **Change assigned policies**: Select a user to edit their assigned policies.
* **Remove a user**: Select a user and choose the option to remove them.

You can also assign policies to users from the command line using `uctl append identityassignments` (see [Assign a policy to a user or application](#assign-a-policy-to-a-user-or-application) above).
