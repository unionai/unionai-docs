---
title: Human access controls
description: What access Union personnel have to a customer data plane, which in self-managed deployments is none.
icon: person-badge
weight: 4
variants: -flyte +union
---

# Human access controls

## Self-managed

In self-managed deployments, Union.ai personnel have no infrastructure access to the customer's data plane: no IAM roles, no VPN, and no SSH keys. They operate only the Union.ai-hosted control plane. Application-level access to the tenant is a separate matter, covered under [Customer-side support access](#customer-side-support-access) below.

## BYOC

In BYOC deployments, Union.ai personnel additionally have authenticated Kubernetes cluster access for operational purposes: upgrades, node pool provisioning, Helm chart updates, health monitoring, and troubleshooting. This access uses cloud-native private connectivity (PrivateLink/PSC) and is scoped to Kubernetes cluster management. All cluster management actions are logged.

## Customer-side support access

Separately from BYOC Kubernetes cluster management, Union.ai support staff hold an identity in the customer's tenant so that they can troubleshoot. This applies to both self-managed and BYOC deployments.

Support staff are granted access through the same RBAC framework that governs the customer's own users: an identity in the tenant, bound to a policy that determines what they can do. The access is subject to the same authentication (OIDC/SSO), authorization (RBAC policies), and audit logging as any other user in the customer's organization. Customers can list every identity-to-policy assignment in their organization, including any held by Union.ai staff, with `flyte get assignment`.

This is distinct from BYOC Kubernetes cluster management access (described above), which is infrastructure-level access for platform operations. Customer-side support access operates at the application level: viewing runs, inspecting logs, diagnosing task failures, and reviewing configuration. It does not grant Kubernetes cluster access, IAM role access, or direct access to the customer's cloud account.

## Access scope

When Union.ai personnel hold a role in a customer's tenant (in BYOC, or through support access in self-managed), that role lets them: view orchestration metadata, view whatever it authorizes in the console and CLI (including run inputs and outputs, logs, code bundles, and reports), and perform administrative operations as authorized by the customer's RBAC policy.

In BYOC, Union.ai personnel also manage the Kubernetes cluster. That capability comes from the separate private-connectivity management path described above, not from any tenant role.

They *cannot*: read secret values (the API is write-only), or reach the customer's cloud account, IAM roles, object stores, secrets backends, container registries, or log aggregators directly. Every request for run data follows the same authenticated, RBAC-gated path as any other user's, and the path depends on what is being fetched: bulk artifacts (files, directories, DataFrames, code bundles, and reports) are read through a per-request presigned URL that is not retained, while structured inputs and outputs and log streams are served back through the data plane's `dataproxy` service. Customer data never transits Union.ai's control plane in any form, so personnel with control plane infrastructure access cannot observe customer data even in flight; every customer-data request is served from the data plane through the Direct-to-Data-Plane tunnel, with authentication and RBAC enforced inside the customer's cluster.

All access by Union.ai personnel is authenticated and logged with caller identity, operation performed, and timestamp.

## Verification

### Human access controls

**Reviewer focus:** Confirm that Union.ai personnel access is appropriately scoped for each deployment model, that every grant is visible and auditable, and that no path exists to read secret values or to reach the customer's cloud account directly.

**How to verify:**

Self-managed: Union.ai has no IAM roles, no VPN, and no SSH keys for the customer's cluster. Every channel between Union.ai and the customer is initiated *from* the customer's data plane. Union.ai cannot initiate connections *to* the customer's infrastructure under any tier.

BYOC:

1. Inspect the operator service account permissions:

   ```bash
   kubectl auth can-i --list --as=<union-operator-sa>
   ```

   This shows exactly what Union.ai can do on the cluster.

2. Review the Kubernetes audit log and CloudTrail for Union.ai personnel access history.

3. Write-only secrets: even when logged into the customer's tenant, personnel cannot read secret values.

4. Presigned URLs are per-request and ephemeral. The underlying data is fetched from the customer's S3/GCS/Azure Blob, not from any Union.ai storage.

Customer-side support access:

1. List every identity-to-policy assignment in the organization, which is where any Union.ai staff access appears:

   ```bash
   flyte get assignment
   ```

2. Inspect the policy each assignment names. A policy binds roles to resources, so this shows which role applies to which projects and domains:

   ```bash
   flyte get policy <name>
   ```

3. Inspect every role those policies bind. The role carries the action list, so this is the step that shows the effective access:

   ```bash
   flyte get role <name>
   ```

4. Review the audit log for requests made by those identities. Every request is logged with caller identity, operation performed, and timestamp.
