---
title: Role-based access control
weight: 2
variants: -flyte +union
---

# Role-based access control

## Built-in roles

Union.ai provides three user-assignable roles with progressively broader permissions.

| Role | Capabilities |
|---|---|
| Admin | Full access: manage users, clusters, secrets, projects, all runs |
| Contributor | Create/abort runs, register tasks, manage secrets within assigned projects |
| Viewer | Read-only: runs, actions, logs, reports |

Additional internal system roles exist for platform operations but are not user-visible or user-assignable.

## Custom policies

Custom policies bind roles (built-in or custom) to resources scoped at org-wide, domain, or project+domain level using composable YAML bindings via `uctl`. This allows organizations to define fine-grained access policies that match their team structure and security requirements.

## Enforcement

Every API request is authenticated and authorized against the user's role assignments before any data access occurs. Enforcement happens at the service layer. Internal-only services (data plane object store proxy, data plane logs proxy) rely on network-level isolation rather than per-request authorization checks, on the basis that they are reachable only from within the service mesh.

## Least privilege

Union.ai enforces least privilege across all components. IAM roles on the data plane are scoped to minimum required permissions. Each data plane has two IAM roles: an admin role for platform services and a user role for task pods. IAM roles are bound via cloud-native workload identity federation, eliminating static credentials entirely. Presigned URLs grant single-object, operation-specific, time-limited access. Service accounts receive only the permissions needed for their specific function.

## Verification

### RBAC enforcement

**Reviewer focus:** Confirm that each role enforces the expected permissions and that custom policies correctly scope access to specific projects and domains.

**How to verify:**

1. Create three test users with Admin, Contributor, and Viewer roles.

2. Log in as Viewer and confirm restricted operations are denied:

   ```bash
   uctl create run ...   # Expect 403 denied
   uctl create secret ...  # Expect denied
   uctl get executions   # Expect success
   ```

3. Log in as Contributor scoped to project A:

   ```bash
   uctl create run --project B ...  # Expect denied
   uctl create run --project A ...  # Expect success
   ```

4. Create a custom policy scoping a user to project X, development domain only. Attempt to access the production domain -- expect denied.

5. Display all active policy bindings:

   ```bash
   uctl get policy
   ```

6. For Union.ai employee access: the customer creates a RBAC policy for Union.ai support -- scoped, viewer only, and time-limited.

All verification steps are self-service using existing features.
