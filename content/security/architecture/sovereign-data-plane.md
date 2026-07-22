---
title: Sovereign Data Plane
weight: 5
variants: -flyte +union
---

# Sovereign Data Plane

The Sovereign Data Plane is an Enterprise-tier deployment option that replaces the Direct-to-Data-Plane tunnel with a customer-managed load balancer inside the customer's VPC, reachable only from inside the customer's corporate network. In this mode, **the data plane is unreachable from any third-party network (including Cloudflare's), and Union.ai employees cannot reach customer data even with full Union.ai credentials.**

This is a strictly stronger network perimeter than the default tier. The identity perimeter (Union RBAC and SSO) is unchanged, and every visualization feature (input/output inspection, log streaming, auxiliary UIs) continues to work for users who are connected to the corporate network.

## When to use it

The Sovereign Data Plane is intended for organizations whose threat model assumes the vendor itself may be compromised, or whose security policy is "no third-party network can ever reach our data plane." Typical drivers:

- **Regulated industries** (finance, healthcare, defense, life sciences) where the data trust boundary must terminate at the customer's network perimeter.
- **Organizations that do not trust Cloudflare** for the data path. Under the default tier, Cloudflare terminates TLS at the tunnel edge; under the Sovereign Data Plane tier this hop is removed entirely.
- **High-scale model serving** where the serving endpoints must remain entirely inside the customer's cloud and reachable only by internal applications.

The Sovereign Data Plane is available on the Enterprise tier on customer request. The default tier is the only option on Starter and Team.

## How it differs from the default

| | Default (Direct-to-Data-Plane) | Sovereign Data Plane |
|---|---|---|
| Client → data plane path | Direct-to-Data-Plane tunnel terminating at the Envoy router inside the customer's cluster | Customer-managed load balancer inside the customer's VPC, terminating at the same Envoy router |
| Reachable from | Public internet, gated by Cloudflare + Envoy AuthN/RBAC | Only from inside the customer's corporate network (VPN) |
| TLS termination | Cloudflare edge, then mTLS to the data plane | Customer-controlled, end-to-end inside the VPC |
| Who can reach the data plane network | Any authenticated, RBAC-authorized user | Only users on the customer's VPN |
| Union.ai employee access to data | Possible only if granted access by customer for support purposes and authenticated by RBAC with full audit trails | **Not possible** without being on the customer's VPN |
| Setup ownership | Provisioned and managed by Union.ai | Customer's SRE/DevOps team stands up the load balancer; Union.ai deploys the data plane behind it |

## What stays the same

Switching to the Sovereign Data Plane changes the **network** perimeter only. Everything else carries over from the default architecture:

- **Identity and access control.** Union RBAC and SSO continue to authenticate and authorize every request. The Envoy router inside the customer's cluster enforces RBAC on every data-path request, just as in the default tier.
- **Visualization features.** Workflow inputs and outputs, live and persisted logs, reports, Ray and Spark dashboards, and the in-task debugger all continue to work, served directly from the data plane.
- **Two-plane separation.** The control plane still orchestrates runs and holds metadata; the data plane still holds and serves all customer data.
- **Data residency.** All customer data continues to reside in the customer's chosen cloud account and region. No customer data ever transits Union infrastructure under either tier.
- **`dataproxy` service.** The data plane `dataproxy` service that handles signed URL generation, log fetching, I/O retrieval, and auxiliary UI proxying is the same component under both tiers.

## Topology

The Sovereign Data Plane request flow mirrors the default tier with one substitution: the Direct-to-Data-Plane tunnel is replaced by a customer-managed load balancer.

```
[Authenticated client on corporate VPN]
        │
        ▼
[Customer-managed load balancer]      ─ inside the customer's VPC,
        │                               reachable only from the corporate VPN
        ▼
[Envoy router (data plane)]           ★ AuthN against Union identity,
        │                               RBAC enforced on every request
        ▼
[Dataproxy service (data plane)]
        │
        ▼
[Object store · KMS · logs ·          ─ customer IAM / Workload Identity /
 k8s API · auxiliary UIs]               customer-managed KMS
```

The data plane never accepts a connection from any third-party network. The load balancer is configured as internal-only, so only hosts inside the customer's corporate network can reach it. Union.ai's control plane continues to communicate with the data plane only over the outbound-only direct gRPC channel for orchestration metadata; no customer data flows on that channel.

## Setup

The Sovereign Data Plane is a deployment-time configuration. The customer's SRE/DevOps team provisions a load balancer inside their VPC that is reachable only from the corporate VPN, and the Union.ai data plane is deployed behind it instead of behind the Direct-to-Data-Plane tunnel. The exact form of the load balancer (cloud-native, ingress controller, internal ALB/NLB/ILB, route reflector, etc.) depends on the customer's existing infrastructure conventions; Union.ai supports the common patterns.

Existing Union RBAC and SSO continue to apply: the network perimeter changes, but the identity perimeter does not. Engagement is through Union Solutions Engineering as part of an Enterprise deployment.

## Trade-offs

The Sovereign Data Plane is strictly stronger than the default tier on network reachability, but comes with operational responsibilities the default tier does not have:

- **Customer owns the load balancer.** Provisioning, scaling, TLS certificate rotation, and high availability are the customer's responsibility, the same as for any other internal service in their VPC.
- **VPN coverage drives user reach.** Users who need to inspect runs from outside the corporate network (for example, working from a personal device, or after a VPN outage) cannot reach the data plane. The default tier's Cloudflare path is reachable from anywhere with internet access.
- **No emergency Union.ai access.** Under the default tier, Union.ai support personnel who have been granted access to specific projects can help diagnose customer issues by inspecting the same surfaces that the customer sees. Under the Sovereign Data Plane, that path is closed: Union.ai support can no longer see the data plane. Operations teams should know that emergency Union.ai access is unavailable before adopting the Sovereign Data Plane.

## Verification

### Network reachability

**Reviewer focus:** Confirm that the data plane is reachable only from inside the customer's corporate network and not from the public internet or any third-party network.

**How to verify:**

1. From a host outside the corporate VPN, attempt to resolve the data plane's load balancer hostname. The resolution should return a private RFC 1918 address (or fail entirely), and any connection attempt should fail.

2. From a host inside the corporate VPN, the same resolution and connection should succeed, subject to Union RBAC at the Envoy router.

3. Inspect the load balancer configuration in the customer's cloud console to confirm it is provisioned as internal-only:

   ```bash
   # AWS example
   aws elbv2 describe-load-balancers --names <lb-name> \
     --query 'LoadBalancers[].Scheme'
   ```

   The scheme should be `internal`, not `internet-facing`.

4. Inspect VPC Flow Logs to confirm there is no inbound traffic to the data plane cluster from Cloudflare IP ranges, Union IP ranges, or the public internet.

### Identity continues to gate access

**Reviewer focus:** Confirm that being on the corporate VPN is necessary but not sufficient: Union identity and RBAC still gate every data-path request.

**How to verify:**

1. From a host inside the corporate VPN with no Union credentials, attempt to access a data-path endpoint. The request should be denied at the Envoy router (HTTP 401 or 403).

2. With valid Union credentials but an RBAC role that does not authorize the target resource, attempt the same request. It should be denied (HTTP 403).

3. With valid Union credentials and an authorized RBAC role, the request should succeed.

4. Inspect Union's authorization-service logs (or equivalent) to confirm that every data-path request through the load balancer was authenticated against a Union identity and evaluated against the RBAC policy.
