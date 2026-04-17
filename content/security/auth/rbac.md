---
title: Role-based access control
weight: 3
variants: -flyte +union
---

# Role-based access control

Union.ai implements a policy-based Role-Based Access Control (RBAC) system with three built-in role types.

| Role | Capabilities | Typical Assignment |
| --- | --- | --- |
| Admin | Full access: manage users, clusters, secrets, projects, and all runs | Platform administrators, security team leads |
| Contributor | Create/abort runs, register tasks, manage secrets within assigned projects | ML engineers, data scientists, DevOps |
| Viewer | Read-only access to runs, actions, logs, reports | Stakeholders, auditors, read-only consumers |
| Custom Policies | Custom policies bind roles (built-in or custom) to resources scoped at org-wide, domain, or project+domain level using composable YAML bindings via `uctl` | Giving contributor access to a specific project's development and staging domains, but only viewer access in production |

RBAC policies are enforced at the service layer.
Every API request is authenticated and authorized against the user's role assignments before any data access occurs.
Users have the ability to create custom policies to further refine access control.

## Least privilege principle

Union.ai enforces the principle of least privilege across all system components:

* IAM roles on the data plane are scoped to minimum required permissions
* Two IAM roles per data plane: admin role (for platform services) and user role (for task pods)
* IAM roles are bound to Kubernetes service accounts via cloud-native workload identity federation
* Presigned URLs grant single-object, operation-specific, time-limited access
* Service accounts receive only the permissions needed for their specific function
