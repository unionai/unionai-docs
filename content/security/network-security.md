---
title: Network security and connectivity
weight: 14
variants: -flyte +union
---

# Network security and connectivity

This page provides a detailed reference for Union.ai's network security architecture, covering all tunnels, communication paths, and connectivity options.

## Network architecture overview

Union.ai uses two separate outbound-only tunnels to connect the customer's data plane to the outside world:

1. **Control plane tunnel** -- carries orchestration commands between the control plane and data plane. No customer data flows through this tunnel.
2. **Direct-to-DataPlane tunnel** -- carries all data access (logs, inputs/outputs, metrics, presigned URLs, apps, auxiliary UIs) directly between clients and the data plane. The control plane is never in this path.

Both tunnels are outbound-only from the customer's cluster, meaning no inbound firewall rules are required on the customer's network.

![Network security](../_static/images/security/network-security.png)

> [!NOTE]
> This diagram needs updating to reflect the current Direct-to-DataPlane architecture.

## Control plane tunnel

The control plane tunnel carries orchestration traffic between the Union.ai control plane and the customer's data plane. This includes:

* TaskAction delivery (scheduling commands)
* State transitions (phase updates, completions, failures)
* Health checks
* DNS reconciliation

This tunnel is outbound-only from the customer's cluster, initiated by the Tunnel Service running on the data plane. All traffic uses mutual TLS (mTLS) encryption via Cloudflare's edge network. No customer data flows through this tunnel -- only orchestration metadata.

### Regional endpoints

Union.ai operates regional control plane endpoints:

| Area | Region | Endpoint |
| --- | --- | --- |
| US | us-east-2 | hosted.unionai.cloud |
| US | us-west-2 | us-west-2.unionai.cloud |
| Europe | eu-west-1 | eu-west-1.unionai.cloud |
| Europe | eu-west-2 | eu-west-2.unionai.cloud |
| Europe | eu-central-1 | eu-central-1.unionai.cloud |

In locked-down environments, networking teams can limit egress to published Cloudflare CIDR blocks, and further restrict to specific regions in coordination with the Union.ai networking team.

## Direct-to-DataPlane tunnel

The Direct-to-DataPlane tunnel provides a dedicated path for all data access between clients and the data plane. This tunnel serves:

* Task logs (live and persisted)
* Task inputs and outputs (via presigned URLs)
* Observability metrics
* Presigned URL generation
* App Serving endpoints
* Auxiliary UIs (Ray dashboard, Spark UI, etc.)

This tunnel is also outbound-only from the customer's cluster and terminates at Cloudflare's edge network. Traffic is routed to an Envoy router (Kourier gateway) running on the customer's cluster.

### Envoy router responsibilities

The Envoy router on the data plane performs:

* **Interception** -- all incoming traffic through the tunnel is intercepted by the Envoy router
* **Authentication and RBAC verification** -- each request is authenticated and checked against Union.ai RBAC policies before proceeding
* **Forwarding** -- approved traffic is forwarded to the appropriate service (DataProxy for presigned URLs, app containers for App Serving, etc.)
* **Backpressure management** -- manages backpressure for scale-from-zero scenarios, holding requests while containers start up

### Subdomain pattern

The Direct-to-DataPlane tunnel uses the subdomain pattern:

```
*.apps.<org>.hosted.unionai.cloud
```

where `<org>` is the customer's organization identifier.

### DDoS protection

Because the tunnel terminates at Cloudflare's edge network, all traffic benefits from Cloudflare's DDoS protection before reaching the customer's infrastructure.

### Shared infrastructure with App Serving

The Direct-to-DataPlane tunnel is the same infrastructure used for Union.ai's App Serving feature. Apps, data visualization, and all data retrieval share this tunnel.

## Enterprise: VPN-routable access

For organizations requiring maximum network security, the Direct-to-DataPlane tunnel can be replaced with a customer-managed load balancer within their VPC. In this configuration:

* The load balancer is routable only from the customer's corporate VPN
* Union.ai RBAC and SSO enforcement remain fully active on the data plane
* No Union.ai employee can access customer data (the same guarantee as the default tier)
* The Cloudflare dependency for data access is eliminated

This is Union.ai's Enterprise deployment tier and is available for organizations with strict network perimeter requirements.

> [!NOTE] Information needed
> Exact load balancer configuration requirements for the Enterprise tier need to be documented.

> [!NOTE] Information needed
> Supported load balancer types (ALB, NLB, etc.) and any cloud-specific requirements need to be confirmed.

> [!NOTE] Information needed
> DNS configuration steps for pointing the Direct-to-DataPlane subdomain to the customer's load balancer need to be documented.

> [!NOTE] Information needed
> Whether the Enterprise tier introduces different egress requirements compared to the default Cloudflare-based setup needs to be clarified.

## BYOC management connection

In BYOC deployments, Union.ai maintains a private management connection to the customer's Kubernetes cluster. This connection is separate from both the control plane tunnel and the Direct-to-DataPlane tunnel.

| Cloud Provider | Technology |
| --- | --- |
| AWS | AWS PrivateLink |
| GCP | GCP Private Service Connect |
| Azure | Azure Private Link |

This connection is used exclusively for cluster management operations:

* Kubernetes version upgrades
* Node pool provisioning
* Helm chart updates
* Health monitoring and troubleshooting

The Kubernetes API endpoint is never exposed to the public Internet. No customer data flows through this connection.

See [BYOC deployment differences: Network architecture](./byoc-differences#network-architecture) for full details.

## Communication paths

The following table lists all communication paths in a Union.ai deployment:

| Communication Path | Protocol | Encryption |
| --- | --- | --- |
| Client to Control Plane | ConnectRPC (gRPC-Web) over HTTPS | TLS 1.2+ |
| Client to Data Plane (Direct-to-DataPlane) | HTTPS via Cloudflare Tunnel | TLS 1.2+ (Envoy-terminated) |
| Control Plane to Data Plane (control tunnel) | Cloudflare Tunnel (outbound-initiated) | mTLS |
| Client to Object Store (presigned URL) | HTTPS | TLS 1.2+ (cloud provider enforced) |
| Fluent Bit to Log Aggregator | Cloud provider SDK | TLS (cloud-native) |
| Task Pods to Object Store | Cloud provider SDK | TLS (cloud-native) |
| Union.ai to Customer K8s API (BYOC only) | PrivateLink / PSC | mTLS |

## Firewall and egress requirements

Both the control plane tunnel and the Direct-to-DataPlane tunnel require the customer to allow outbound HTTPS traffic to Cloudflare's edge network. No inbound firewall rules are required.

In locked-down environments, egress can be restricted to:

* Published Cloudflare CIDR blocks
* Specific Cloudflare regions (in coordination with the Union.ai networking team)

> [!NOTE] Information needed
> Detailed Cloudflare CIDR blocks and region-specific restrictions should be obtained from the Union.ai networking team.
