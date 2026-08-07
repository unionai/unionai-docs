---
title: Network architecture
weight: 4
variants: -flyte +union
---

# Network architecture

The network architecture reinforces the [two-plane separation](./two-plane-separation) with an outbound-only connectivity model between the data plane and the control plane. The data plane initiates an outbound-only direct gRPC connection to the control plane for orchestration metadata. Client-to-data-plane traffic uses a separate channel: by default, an outbound-initiated Direct-to-Data-Plane tunnel terminating at an Envoy router inside the customer's cluster; under the [Sovereign Data Plane](./sovereign-data-plane) tier, a customer-managed load balancer inside the customer's VPC instead. Under either tier, no inbound firewall rules are required on the customer's external perimeter.

## Outbound-only model

All network connections between the data plane and Union.ai are initiated by the data plane. Under the default tier, the customer's network requires only standard outbound HTTPS access to Cloudflare edge nodes. No inbound firewall rules, port forwarding, or VPN configuration are needed at the customer's external perimeter.

At the external perimeter, this model eliminates the inbound attack surface entirely. There are no externally-listening services on the customer's network for an attacker to discover through port scanning or exploit through service vulnerabilities. The customer's external network perimeter remains unaffected by the Union.ai integration. Firewall management at the perimeter is simplified to a single rule: permit outbound HTTPS, which most enterprise networks already allow.

The trust model is customer-initiated: the data plane decides when and whether to connect, and the customer can sever either channel at any time by blocking outbound traffic or shutting down the data plane operator.

Under the [Sovereign Data Plane](./sovereign-data-plane) tier, the client-to-data-plane path runs through a customer-managed internal load balancer inside the customer's VPC instead of the Cloudflare-backed tunnel; the data-plane-to-control-plane gRPC channel remains outbound-only. The external perimeter still requires no inbound rules; the internal load balancer is reachable only from inside the customer's corporate network.

The client-to-data-plane path is direct: client → tunnel (or internal load balancer under the Sovereign Data Plane tier) → Envoy router → `dataproxy` → customer storage. Log streaming, structured I/O retrieval, and large input uploads complete with low first-byte and end-to-end latency.

## Direct-to-Data-Plane tunnel

The Direct-to-Data-Plane tunnel is an outbound-only encrypted Cloudflare Tunnel from the customer's cluster to the Cloudflare edge network. It is initiated by a `cloudflared` daemon in the data plane and carries only client-to-data-plane traffic; the data-plane-to-control-plane channel is the separate direct gRPC connection described below. The tunnel **terminates inside the customer's cluster** at an Envoy router that authenticates each request against Union identity and enforces RBAC before forwarding to the data-plane `dataproxy` service. The Union.ai control plane is not on this path. For background on the underlying connector, see Cloudflare's [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) documentation.

Under the default tier, all traffic through the tunnel is encrypted using a layered transport: TLS 1.3 from the client to the Cloudflare edge, mTLS plus Cloudflare Tunnel encryption from the edge to the data plane, and Cloudflare Access service tokens for application-layer authentication. Tunnel tokens are rotated automatically: the data plane operator periodically polls Union.ai and picks up updated tokens when issued.

The tunnel maintains health checks and heartbeats, and automatically reconnects if the connection drops. State reconciliation occurs upon reconnection, so no requests are lost during brief connectivity interruptions.

The tunnel carries every kind of customer-data request: structured task input uploads via signed URLs, log streams (live and persisted), secret writes, auxiliary UI traffic (Ray dashboard, Spark history server, in-task debugger), Apps & Serving ingress, and `dataproxy` RPCs generally. Bulk artifacts (files, directories, DataFrames, code bundles, reports) transit signed URLs issued by the dataproxy, so the bytes themselves flow directly between the client and the customer's object store. Container images also bypass the tunnel: they are pulled by Kubernetes from the customer's container registry over standard HTTPS.

### Per-cluster routing

In multi-cluster deployments, each data plane cluster has its own dedicated tunnel domain (e.g. `<cluster-id>.<base-domain>`). The SDK and UI resolve the right cluster for a given request via the `SelectCluster` RPC and dispatch directly to that cluster's tunnel domain. This keeps log streaming, I/O retrieval, and metrics requests terminating at the correct cluster without round-tripping through any shared aggregator.

### Sovereign Data Plane

Enterprise customers can replace the Direct-to-Data-Plane tunnel entirely with a customer-managed load balancer inside their own VPC, reachable only from the corporate VPN. This makes the data plane unreachable from any third-party network -- including Cloudflare's -- and unreachable to Union.ai employees. See [Sovereign Data Plane](./sovereign-data-plane) for the topology and trade-offs.

## Communication paths

All communication paths in the system use encryption. No unencrypted communication paths exist.

| Path | Protocol | Encryption |
|---|---|---|
| Client to control plane (orchestration API) | HTTPS | TLS 1.2+ |
| Client to data plane (customer-data requests, default tier) | Direct-to-Data-Plane tunnel | TLS 1.3 + mTLS |
| Client to data plane (customer-data requests, Sovereign Data Plane tier) | Customer-managed internal LB (corporate VPN) | TLS (customer-managed) |
| Data plane → control plane (orchestration metadata, outbound-initiated) | gRPC over TLS (TCP 443) | TLS 1.2+ |
| Client to Object Store | HTTPS (presigned URL) | TLS 1.2+ (cloud provider enforced) |
| Fluent Bit to Log Aggregator | Cloud provider SDK | TLS (cloud-native) |
| Task Pods to Object Store | Cloud provider SDK | TLS (cloud-native) |
| Union.ai to Customer Kubernetes API (BYOC only) | PrivateLink / PSC | TLS (private connectivity) |

For details on the BYOC private management connection, see [Private connectivity (BYOC)](./private-connectivity). For the concrete outbound ports and endpoints the data plane connects to, see [Egress requirements](#egress-requirements) below.

## Egress requirements

Because every connection is [outbound-only](#outbound-only-model), configuring network access for the data plane is a matter of permitting a small set of outbound destinations -- there are no inbound firewall rules, port forwarding, or listening services to open. This section makes that model concrete: the specific destinations, ports, and protocols the data plane initiates connections to.

| Source (data plane) | Destination | Port / protocol | Purpose |
|---|---|---|---|
| Data plane operator (all components) | Union.ai control plane, at your tenant endpoint (`<tenant>.hosted.unionai.cloud`) | TCP 443 (TLS) | Outbound gRPC-over-TLS orchestration RPCs: cluster registration, action lifecycle, event reporting, catalog and artifact lookups, admin RPCs, and metrics. This is the same tenant DNS the UI and CLI use, and every data plane component authenticates to the control plane over it. See [Data plane](./data-plane) for the components that use this channel. |
| `cloudflared` (Tunnel Service) | Cloudflare edge network | TCP 7844 | Establishes the outbound [Direct-to-Data-Plane tunnel](#direct-to-data-plane-tunnel) (default tier only). See Cloudflare's [firewall configuration guidance](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/) for the exact ports and hostnames the `cloudflared` daemon needs. |

Both destinations are reached over the customer's existing outbound path (typically a NAT gateway). No inbound rules are required on the customer's external perimeter.

Your tenant's Direct-to-Data-Plane tunnel is published at a tunnel domain of the form `<tenant>-<tenant>-tunnel.unionai.cloud` — the hostname clients and the UI resolve to reach the data plane through the tunnel. This is a client-side resolution target, not an additional data plane egress destination: the `cloudflared` daemon's own outbound connection is to the Cloudflare edge network on TCP 7844, as in the table above.

### Resolving control plane IP addresses

Some environments must allowlist egress by IP address rather than by hostname. The control plane endpoints sit behind regional network load balancers whose IP addresses **can change over time**, so resolve them dynamically wherever your egress policy allows rather than pinning a fixed table.

**Once your tenant is provisioned**, resolve its endpoint and re-resolve it on a schedule rather than pinning fixed addresses:

```bash
dig <tenant>.hosted.unionai.cloud
```

Allowlist the addresses returned, and refresh the allowlist periodically. Where your egress policy supports it, prefer an FQDN- or DNS-based rule over static IPs so that load-balancer changes are picked up automatically.

**Before your tenant is provisioned** — or wherever you must stage egress rules ahead of time — allowlist the current production regional control plane load balancers below, or resolve their DNS names for the latest addresses. Your tenant endpoint resolves to the load balancer in its region, so the addresses returned by `dig` match the corresponding row.

| Region | Control plane load balancer (DNS) | Current IP addresses |
|---|---|---|
| `us-east-2` | `opta-production-lb-f6b2dc1ac0c5d1b3.elb.us-east-2.amazonaws.com` | `3.137.115.239`, `3.129.166.66`, `3.19.82.116` |
| `us-west-2` | `opta-production-us-west-2-lb-eed1102869e8e87d.elb.us-west-2.amazonaws.com` | `44.242.13.239`, `54.202.254.106`, `34.218.20.123` |
| `eu-west-1` | `opta-production-eu-west-1-lb-4f0b7b3ab565ae1b.elb.eu-west-1.amazonaws.com` | `52.30.110.77`, `52.51.69.225`, `54.220.70.146` |
| `eu-west-2` | `opta-production-eu-west-2-lb-8e072fd05bfb19ae.elb.eu-west-2.amazonaws.com` | `18.169.71.70`, `3.11.48.43`, `18.134.175.75` |
| `eu-central-1` | `opta-production-eu-central--lb-5d94314b0baac0c8.elb.eu-central-1.amazonaws.com` | `3.78.52.222`, `3.127.122.108`, `3.68.3.26` |

These addresses are current as of July 2026 and can change; where possible allowlist by DNS (re-resolving the names above) rather than pinning the IPs, and re-verify with your Union account team.

### VPN alternative to the tunnel

> [!NOTE]
> A forthcoming VPN-based option will let the data plane connect without the Cloudflare Tunnel, making the `cloudflared` egress on TCP 7844 optional. This is not yet available: under the default tier today, the Direct-to-Data-Plane tunnel requires outbound TCP 7844 to the Cloudflare edge. Enterprise customers who need to eliminate the third-party tunnel path now can use the [Sovereign Data Plane](./sovereign-data-plane) tier, which replaces it with a customer-managed internal load balancer reachable only from the corporate VPN.

## Verification

### Outbound-only model

**Reviewer focus:** Confirm that no inbound firewall rules or listening services exist on the customer's network for Union.ai traffic, and that all connections are outbound-initiated.

**How to verify:**

1. Review the security group or firewall rules attached to the data plane cluster's nodes. Confirm that no inbound rules reference Union.ai IP ranges or allow inbound traffic from external sources for orchestration purposes:

   ```bash
   # AWS example
   aws ec2 describe-security-groups --group-ids <node-sg-id> \
     --query 'SecurityGroups[].IpPermissions'
   ```

2. Confirm that no Kubernetes services in the `union` namespace expose inbound LoadBalancer or NodePort services to the control plane:

   ```bash
   kubectl get svc -n union
   ```

   Services should be `ClusterIP` type or, if `LoadBalancer`, should serve only Apps & Serving endpoints, not control plane connectivity.

3. Review VPC Flow Logs to confirm that connections to Cloudflare are outbound-initiated. All flows to Cloudflare IP ranges should show the data plane node as the source.

4. (Optional) Run a port scan from an external host against the data plane nodes to confirm no Union.ai-related services are reachable.

### Direct-to-Data-Plane tunnel

**Reviewer focus:** Confirm that bulk data (files, DataFrames, code bundles) transfers directly between clients and the customer's object store via presigned URLs, and that structured task I/O and log streams flow through the Direct-to-Data-Plane tunnel directly to the data plane (no Union.ai control plane on the path).

**How to verify:**

1. Inspect tunnel pod logs:

   ```bash
   kubectl logs <tunnel-pod> -n union
   ```

   Logs should show health checks, connection establishment, and message exchanges.

2. Analyze VPC Flow Logs for traffic patterns. Bulk data transfers (files, DataFrames, code bundles) should flow directly between task pods and the customer's object store endpoints (S3/GCS/Azure Blob), not through Cloudflare IPs. Structured task I/O and log streams will flow through the tunnel as documented.

3. Use browser developer tools (Network tab) in the Union.ai UI to confirm that binary output artifacts are fetched via presigned URLs (resolving to the customer's storage domain), while structured outputs are fetched via the data plane through the Direct-to-Data-Plane tunnel (resolving to a per-cluster tunnel domain, not a control plane endpoint).
