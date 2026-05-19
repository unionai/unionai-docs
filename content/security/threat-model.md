---
title: Threat model
weight: 4
variants: -flyte +union
---

# Threat model

This page enumerates the realistic adversaries against a Union.ai deployment and, for each, what they can and cannot reach. The analysis assumes Zero Trust is in effect: the `dataproxy` service runs in the customer's data plane behind the Envoy router, customer data never transits the control plane, and operational metrics flow data-plane-to-control-plane via a push model.

## A topological, not behavioral, property

> **No customer data, metadata, code, or logs ever touch Union.ai's control plane. Not in flight. Not at rest. Not ever.**

This central guarantee under Zero Trust is a property of the **deployment topology**, not of Union's operational behavior. It is verifiable by inspecting:

- The Helm chart that deploys the data plane.
- The tunnel configuration (`operator/tunnels`) and Envoy filter chain that authenticate and authorize every data-path request inside the customer's cluster.
- The `dataproxy` deployment manifest, which runs in the customer's namespace under workload identity scoped to the customer's cloud account.
- The Terraform module (`infra/terraform/modules/dataplane/`) that provisions the customer-side resources.

The property does **not** depend on Union employees behaving correctly, Union's incident response procedures, a future audit catching a regression, or cryptographic primitives remaining unbroken. Each of those is a defense-in-depth layer; none of them is the load-bearing claim. The data path the property describes does not exist, so the question of whether it can be misused does not arise.

## Trust boundaries

```
[Public internet]
        │
        ▼
[Cloudflare edge]                  ─ TLS 1.3 termination,
        │                            service-token policy
        ▼                            (default tier; absent under Sovereign DP)
[Customer VPC]                     ─ no inbound port at the external perimeter
        │
        ▼
[Customer K8s cluster]
        │
        ▼
[Direct-to-DataPlane tunnel  ──or──  customer-managed internal LB]
        │
        ▼
[Envoy router]                     ★ AuthN against Union identity,
        │                            RBAC enforced on every request
        ▼
[Dataproxy service]                ─ in-cluster, single-tenant, customer-owned
        │
        ▼
[Object store · KMS · logs ·       ─ customer IAM / Workload Identity /
 K8s API · auxiliary UIs]            customer-managed KMS

[Union Control Plane]  ───  metadata only  ──────▶   [Customer Data Plane]
   (multi-tenant)        (run IDs, status,                (single-tenant,
                          scheduling refs)                 customer-owned)
```

## Assets

The analysis below references these asset classes:

- **A1** Workflow inputs and outputs -- the largest surface, most sensitive.
- **A2** Code bundles.
- **A3** Live and persisted execution logs.
- **A4** Custom user-rendered reports and auxiliary UIs (Ray dashboards, Spark history servers, in-task debuggers).
- **A5** Workflow metadata: run IDs, action status, scheduling, dependency references, RBAC graph.
- **A6** User identity, auth tokens, RBAC policy.
- **A7** Secrets (org-wide and cluster-pool scoped), tunnel credentials.

## Adversaries

### T1 — External attacker on the public internet

**Capability.** Network probing, credential stuffing, vulnerability exploits against any internet-reachable surface.

**Reach.** No inbound port is open on the customer's data plane at the external perimeter. The cluster does not accept connections from anywhere; under the default tier, the Direct-to-DataPlane tunnel is initiated outbound from inside the cluster, and under the [Sovereign Data Plane](./architecture/sovereign-data-plane) tier, the data plane is reachable only from the customer's corporate VPN. The only Union surface reachable from the public internet is the control plane API, which holds only A5 (metadata) and A6 (identity); both are gated by RBAC. Reaching A1–A4 requires breaching the customer's own cloud perimeter (IAM, KMS, network policy).

**Reachable**: portions of A5 gated by RBAC. **Not reachable**: A1–A4, A7 plaintext.

### T2 — Compromised Union control plane

**Capability.** Full code execution on any control plane service; can read control plane databases and credentials.

**Reach.** This is the adversary Zero Trust is specifically designed against. Full code execution on the control plane yields A5 (workflow metadata) and A6 (identity records, RBAC graph). It does **not** yield A1–A4: those payloads never enter the control plane in any form under Zero Trust, so there is no in-memory or on-disk copy to extract. The control plane also cannot inject itself into the data path -- in default mode it can only initiate the same outbound-authenticated calls a normal client could (subject to Envoy AuthN/AuthZ at the tunnel egress inside the customer's cluster); under Sovereign DP it has no network route to the data plane at all. Lateral movement to A1–A4 requires *also* compromising the customer's own IAM/KMS, which sit inside the customer's cloud account, not Union's.

**Reachable**: A5, A6. **Not reachable**: A1–A4, A7 plaintext.

### T3 — Malicious or coerced Union employee

**Capability.** Full operator access to control plane and Union-managed infrastructure.

**Reach.** Same blast radius as T2. Operator access to Union infrastructure does not include access to the customer's cloud account; the data lives there, not at Union. Under Sovereign DP, the employee additionally cannot reach the data plane's *network* -- the data plane is reachable only on the customer's corporate VPN, and Union employees are not on it.

**Reachable**: A5, A6. **Not reachable**: A1–A4. Under Sovereign DP, not even the data plane network.

### T4 — Compromised transport intermediary

**Capability.** Read or modify traffic at the tunnel termination point.

**Reach.** This is the most important *residual* risk under the default tier. Cloudflare terminates TLS at the tunnel edge, so a compromised Cloudflare edge would see plaintext for default-tier customer-data traffic in flight (though never at rest -- nothing persists there). Three mitigations apply:

1. Cloudflare's own threat model and operational controls are stronger than most alternatives a customer could self-deploy.
2. Authentication and authorization are enforced *after* the edge, in the Envoy router inside the customer's cluster -- so a compromised edge cannot impersonate a Union user or escalate beyond the user-level RBAC of whatever request it is observing.
3. For customers who reject this residual risk entirely, the [Sovereign Data Plane](./architecture/sovereign-data-plane) tier removes Cloudflare from the path -- traffic runs over the customer's own VPN/PrivateLink and never touches a third party.

**Reachable (default)**: A1–A4 in flight only, no persistence. **Sovereign DP**: nothing.

### T5 — Compromised customer data-plane node

**Capability.** Root on a data-plane worker pod.

**Reach.** Worst case for the *customer*, but not a Union-trust-boundary problem. The customer's existing controls apply: Workload Identity Federation (per-pod, no static keys), least-privilege node service accounts, Calico network policy that blocks IMDS (`169.254.169.252/32`, `169.254.169.254/32`) and RFC-1918 egress, customer-managed KMS on etcd, and node hardening (Secure Boot, Integrity Monitoring, container-optimized OS). Union does not gain additional access from a node compromise; the blast radius stays inside the customer's cluster.

**Reachable**: A1–A4 within the compromised node's RBAC scope.

### T6 — Authorized customer user, malicious

**Capability.** Holds valid Union credentials and an RBAC role.

**Reach.** Reach is bounded by the assigned RBAC role. RBAC is enforced at **both** the control plane API (for orchestration metadata operations) **and** the data-plane Envoy router (for data-path operations) -- the same identity is checked at both enforcement points, so a Viewer cannot escalate by hitting the data plane directly. Presigned URLs are scoped to a single object, a single operation (GET or PUT), and a short TTL, so a stolen URL or replay does not yield broader access.

**Reachable**: scoped to RBAC role.

### T7 — Passive network observer

**Capability.** Observes encrypted traffic on the wire.

**Reach.** Every hop is encrypted: TLS 1.3 between the client and the Cloudflare edge (default tier) or directly to the customer-managed LB (Sovereign DP); mTLS on the tunnel; cloud-native TLS between dataproxy and the object store; signed-URL HTTPS for direct object-store access. A passive observer cannot read traffic in transit.

**Reachable**: ciphertext only.

### T8 — Future cryptanalysis

**Capability.** Recovers plaintext from recorded ciphertext at some later date.

**Reach.** This is where the absence-of-path property structurally beats the encryption-of-path property. Recorded ciphertext from data that flowed through the control plane could one day be decrypted; recorded ciphertext from data *that never flowed through the control plane* cannot be, because the bytes were never on a Union wire to record. Customer data only ever traverses customer-controlled networks (or the Cloudflare tunnel inbound to the customer's cluster); whatever future cryptanalysis discovers about Union's TLS termination has nothing to apply to.

**Reachable post-Zero-Trust**: nothing that was ever on a Union wire, because nothing customer-sensitive was ever there.

## Auditability

The Zero Trust property is independently auditable from outside Union. A customer security team can verify each of the claims above using sources they already have or can enable:

- **Network topology.** GKE / EKS / AKS audit logs confirm the tunnel pod's outbound-only connection pattern. Cloud Audit Logs show no inbound traffic to the data plane cluster API from Union IP ranges.
- **Application path.** Union's authorization-service logs record every data-plane request, the resolved Union identity, and the RBAC decision. Control plane logs over the same window show no payload-bearing requests for customer-data operations -- by inspection, the API surfaces that used to proxy customer data have no corresponding endpoints.
- **Object store.** Cloud-native audit logs (CloudTrail, Cloud Audit Logs, Azure Storage logs) record every read and write to the bucket. The principal on every payload-bearing access is a customer-controlled identity, never Union.
- **Tunnel.** Cloudflare Access logs record every authenticated request through the tunnel, including the resolved Union identity, the destination service inside the cluster, and the response status. (Under Sovereign DP, the equivalent logs are produced by the customer-managed LB.)

Customers can ingest all of the above into their own SIEM and assert on it independently of Union.

## Residual risks

Five risks are not eliminated by the architecture and are stated explicitly so customer security teams can decide how to address them.

1. **Default-mode TLS termination at Cloudflare** (T4). For customers whose threat model treats Cloudflare as untrusted, the Sovereign Data Plane tier removes Cloudflare from the path. Otherwise it is a deliberate trade.

2. **Metadata leakage on control plane compromise** (T2/T3). Run IDs, schedules, action status, error messages, and the RBAC graph are visible on a compromised control plane. Customers who consider workflow *topology* sensitive should be aware that an orchestrator necessarily knows the topology to orchestrate it.

3. **Customer-side IAM is the floor.** Zero Trust does not protect against the customer's own IAM misconfiguration. Union ships correct defaults (least-privilege node service accounts, Workload Identity Federation, IMDS blocking, customer-managed KMS, private nodes); customers retain the ability to loosen them.

4. **Compromised customer cluster** (T5) sees its own data. Defense in depth at the customer's IAM and network layer is still required.

5. **`EAGER_API_KEY`** is broadly scoped today and provisioned via internal fanout. It is on the deprecation backlog; once replaced, the residual risk associated with that token disappears.

## Verification

### Topological property by inspection

**Reviewer focus:** Confirm that the Zero Trust property is verifiable from the deployment artifacts without relying on Union's testimony.

**How to verify:**

1. Read the Helm chart for the data plane. Confirm that the `dataproxy` deployment manifest is present, that it runs in the customer's namespace, and that its service account is bound to the customer's cloud identity via Workload Identity Federation.
2. Read the Envoy filter chain in the data plane configuration. Confirm that every customer-data route is gated by an AuthN filter against Union identity and an RBAC filter against the Union RBAC policy.
3. Read the tunnel configuration (`operator/tunnels`). Confirm that the tunnel terminates inside the customer's cluster, not at the control plane.
4. Read the Terraform module that provisions the data plane. Confirm that the IAM roles and KMS keys live in the customer's cloud account.

### Adversary-by-adversary

**Reviewer focus:** Confirm that each adversary's reach matches the analysis above.

**How to verify:**

- **T1 (external).** Run an external port scan against the data plane cluster's public IP ranges; confirm no Union-related service responds. Inspect VPC Flow Logs for inbound traffic from Cloudflare or Union IP ranges; confirm none.
- **T2/T3 (compromised CP / malicious employee).** Inspect control plane API endpoints. Confirm that no endpoint returns workflow input or output payloads, log content, or secret values. The `GetSecret` RPC by design returns only metadata.
- **T4 (transport intermediary).** Inspect the encryption-at-each-phase table in [Data flow](./data-protection/data-flow) for default tier; note the Cloudflare edge hop. For Sovereign DP, inspect the same table; note that the Cloudflare hop is absent.
- **T5 (compromised node).** Inspect the node service account's IAM policy; confirm scoping (no `iam:PassRole` to admin roles, no broad storage admin, no project editor). Inspect Calico network policies; confirm IMDS and RFC-1918 egress blocks.
- **T6 (malicious user).** Create a Viewer-role user. Attempt to call data-path endpoints (log streaming, I/O retrieval) via the tunnel. Confirm denial at the Envoy router, not just at the control plane API.
- **T7 (passive observer).** Inspect [Encryption](./data-protection/encryption) for the encryption status of every hop. Confirm no plaintext hop exists.

### Auditability

**Reviewer focus:** Confirm that the customer's own SIEM can produce evidence sufficient to verify the Zero Trust property without Union's cooperation.

**How to verify:**

1. Ingest cluster audit logs, Cloud Audit / CloudTrail logs, Cloudflare Access logs (or the equivalent for the customer-managed LB under Sovereign DP), and Union's authorization-service log export.
2. Query for any customer-data-shaped request reaching the control plane region; assert zero results.
3. Query for the principal on every object-store access; assert that none are Union-controlled.
4. Run this query continuously as part of the customer's normal security monitoring; any future drift will produce immediate evidence.
