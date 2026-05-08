---
title: Human access controls
weight: 4
variants: -flyte +union
---

# Human access controls

## Self-managed

In self-managed deployments, Union.ai personnel access only the Union.ai-hosted control plane infrastructure. They have zero access to the customer's data plane. This access uses standard OIDC/SSO and RBAC.

## BYOC

In BYOC deployments, Union.ai personnel additionally have authenticated Kubernetes cluster access for operational purposes: upgrades, node pool provisioning, Helm chart updates, health monitoring, and troubleshooting. This access uses cloud-native private connectivity (PrivateLink/PSC) and is scoped to Kubernetes cluster management. All cluster management actions are logged.

## Customer-side support access (optional)

Separately from BYOC Kubernetes cluster management, Union.ai offers an optional support service where customers can grant Union.ai staff access to the customer's tenant for troubleshooting. This is available for both self-managed and BYOC deployments.

When requested, Union.ai support personnel are granted access through the same RBAC framework used by the customer's own users. The customer creates a role binding for Union.ai staff, scoped to the specific projects, domains, and permission level appropriate for the troubleshooting engagement. This access can be time-limited so that it expires automatically after the support engagement concludes.

This service is entirely optional. Customers must explicitly request it and configure the RBAC grants themselves. Union.ai staff cannot self-provision this access. The access is subject to the same authentication (OIDC/SSO), authorization (RBAC policies), and audit logging as any other user in the customer's organization.

This is distinct from BYOC Kubernetes cluster management access (described above), which is infrastructure-level access for platform operations. Customer-side support access operates at the application level: viewing runs, inspecting logs, diagnosing task failures, and reviewing configuration. It does not grant Kubernetes cluster access, IAM role access, or direct access to the customer's cloud account.

## Access scope

When Union.ai personnel are granted access to a customer's tenant (in BYOC, or via the optional support service in self-managed), they CAN: view orchestration metadata, view logs relayed through the tunnel, perform administrative operations as authorized by the customer's RBAC policy, and (in BYOC) manage the Kubernetes cluster.

Personnel CANNOT: read secret values (the API is write-only), access bulk data in customer object stores (presigned URLs are per-request and not retained), or access the customer's cloud account, IAM roles, object stores, secrets backends, container registries, or log aggregators. Personnel with control plane infrastructure access could in principle observe inline data transiting control plane memory during request processing (structured task I/O, log streams, secret values during create/update), but this data is transient (not persisted, not logged, not cached) and is inherent to any pass-through proxy architecture.

All access by Union.ai personnel is authenticated and logged with caller identity, operation performed, and timestamp.

## Verification

### Human access controls

**Reviewer focus:** Confirm that Union.ai personnel access is appropriately scoped for each deployment model and that no path exists to access customer data or secrets.

**How to verify:**

Self-managed: Union.ai has no IAM roles, no VPN, no SSH keys, and no kubectl access to the customer's cluster. Both outbound channels (Cloudflare Tunnel and direct gRPC) are initiated FROM the customer's data plane. Union.ai cannot initiate connections TO the customer's infrastructure.

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

1. Confirm that no Union.ai support user exists in the customer's tenant unless explicitly provisioned by the customer.

2. If support access has been granted, verify the RBAC binding:

   ```bash
   uctl get policy
   ```

   The Union.ai support user should appear with the scoped role and time limit configured by the customer.

3. After the time limit expires, repeat the query. The binding should no longer be active.
