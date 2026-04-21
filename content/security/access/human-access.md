---
title: Human access controls
weight: 4
variants: -flyte +union
---

# Human access controls

## Self-managed

In self-managed deployments, Union.ai personnel access only the control plane tenant. They have zero access to data plane infrastructure. This access uses the same OIDC/SSO mechanisms and RBAC policies as customer users.

## BYOC

In BYOC deployments, Union.ai personnel additionally have authenticated Kubernetes cluster access for operational purposes: upgrades, node pool provisioning, helm chart updates, health monitoring, and troubleshooting. This access uses cloud-native private connectivity (PrivateLink/PSC) and is scoped to Kubernetes cluster management. All cluster management actions are logged.

Union.ai is implementing just-in-time (JIT) access controls to replace persistent support access with time-bound, customer-authorized grants.

## Access scope

When accessing a customer's tenant, Union.ai personnel CAN: view orchestration metadata, view logs relayed through the tunnel, perform administrative operations as authorized by the customer's RBAC policy, and (in BYOC) manage the Kubernetes cluster.

Personnel CANNOT: read secret values (the API is write-only), access raw data in customer object stores (presigned URLs are per-request and not retained), access the customer's cloud account or IAM roles, or access customer object stores, secrets backends, container registries, or log aggregators.

> [!NOTE]
> **Audit finding (ref #3, #5):** These access restrictions are validated for data at rest. However, Union.ai personnel with control plane infrastructure access could potentially observe data that transits control plane memory during request processing (structured task I/O, log streams, secret values during create/update). This is inherent to any pass-through proxy architecture and is mitigated by the transient nature of the data (not persisted, not logged, not cached).

All access by Union.ai personnel is authenticated and logged with caller identity, operation performed, and timestamp.

## Verification

### Human access controls (Critical)

**Reviewer focus:** Confirm that Union.ai personnel access is appropriately scoped for each deployment model and that no path exists to access customer data or secrets.

**How to verify:**

Self-managed: Union.ai has no IAM roles, no VPN, no SSH keys, and no kubectl access to the customer's cluster. The tunnel is outbound-only FROM the customer -- Union.ai cannot initiate connections TO the customer's infrastructure.

BYOC:

1. Inspect the operator service account permissions:

   ```bash
   kubectl auth can-i --list --as=<union-operator-sa>
   ```

   This shows exactly what Union.ai can do on the cluster.

2. Review the Kubernetes audit log and CloudTrail for Union.ai personnel access history.

3. Write-only secrets: even when logged into the customer's tenant, personnel cannot read secret values.

4. Presigned URLs are per-request and ephemeral -- the underlying data is fetched from the customer's S3/GCS/Azure Blob, not from any Union.ai storage.
