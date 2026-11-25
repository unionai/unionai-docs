---
title: Role-based access control
description: The built-in roles, custom policies, and how permissions are enforced.
icon: shield-lock-fill
weight: 2
variants: -flyte +union
---

# Role-based access control

## Built-in roles

Union.ai provides three user-assignable roles with progressively broader permissions.

| Role | Capabilities |
|---|---|
| Admin | Full access: manage users, clusters, secrets, projects, all runs |
| Contributor | Create/abort runs, deploy tasks, manage secrets within assigned projects |
| Viewer | Read-only: runs, actions, logs, reports |

Additional internal system roles exist for platform operations but are not user-visible or user-assignable.

## Custom policies

Roles (built-in or custom) define sets of permitted **actions**; custom **policies** then bind those roles to resources — scoped org-wide, by domain, or by project+domain — using composable YAML **bindings**. Both are managed with the `flyte` CLI (`flyte create role` / `flyte create policy`). This allows organizations to define fine-grained access policies that match their team structure and security requirements.

## Enforcement

Every request is authenticated and authorized against the user's role assignments before any data access occurs. Enforcement happens at two points: the control plane API gates orchestration metadata operations (run lifecycle, task definitions, RBAC management, project/domain queries), and the data plane's `dataproxy` service gates every customer-data request (signed URLs, structured I/O retrieval, log fetching, auxiliary UI proxying, secret writes) after the Envoy router inside the customer's cluster has authenticated it. For each decision, `dataproxy` asks the control plane's authorizer, sending the caller's identity and the requested action, not customer data. Both enforcement points evaluate the same Union.ai identity against the same RBAC policy.

## Least privilege

Union.ai enforces least privilege across all components. IAM roles on the data plane are scoped to minimum required permissions. Each data plane has two IAM roles: an admin role for platform services and a user role for task pods. IAM roles are bound via cloud-native workload identity federation, eliminating static credentials entirely. Presigned URLs grant single-object, operation-specific, time-limited access. Service accounts receive only the permissions needed for their specific function.

## Verification

### RBAC enforcement

**Reviewer focus:** Confirm that each role enforces the expected permissions and that custom policies correctly scope access to specific projects and domains.

**How to verify:**

1. Create three test users with Admin, Contributor, and Viewer roles.

2. Log in as Viewer and confirm restricted operations are denied:

   ```bash
   flyte run ...          # Expect denied
   flyte create secret ... # Expect denied
   flyte get run          # Expect success
   ```

3. Log in as Contributor scoped to project A:

   ```bash
   flyte run --project B ... # Expect denied
   flyte run --project A ... # Expect success
   ```

4. Create a custom policy scoping a user to project X, development domain only. Attempt to access the production domain. Expect denied.

5. Display all active policy bindings:

   ```bash
   flyte -of json get policy
   ```

6. For Union.ai employee access, get the subjects of the staff identities in your tenant from Union.ai (`flyte get member` and `flyte get user` don't list support staff). Look up the policies assigned to each identity with `flyte get assignment --user-subject <subject>`, inspect those policies with `flyte get policy <name>`, then inspect the roles those policies bind with `flyte get role <name>`. The role carries the action list, so the last step is the one that shows the effective access. See [Human access controls](./human-access).

Steps 1–5 are fully self-service. Step 6 also needs the staff subjects from Union.ai, and assignment output shows only customer-visible policies, not internal system policies.
