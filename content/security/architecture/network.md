---
title: Network architecture
weight: 4
variants: -flyte +union
---

# Network architecture

The network architecture reinforces the [two-plane separation](./two-plane-separation) with an outbound-only connectivity model between the data plane and the control plane. The data plane initiates an outbound-only direct gRPC connection to the control plane for orchestration metadata. Client-to-data-plane traffic uses a separate channel: by default, an outbound-initiated Direct-to-DataPlane tunnel terminating at an Envoy router inside the customer's cluster; under the [Sovereign Data Plane](./sovereign-data-plane) tier, a customer-managed load balancer inside the customer's VPC instead. Under either tier, no inbound firewall rules are required on the customer's external perimeter.

## Outbound-only model

All network connections between the data plane and Union are initiated by the data plane. Under the default tier, the customer's network requires only standard outbound HTTPS access to Cloudflare edge nodes. No inbound firewall rules, port forwarding, or VPN configuration are needed at the customer's external perimeter.

At the external perimeter, this model eliminates the inbound attack surface entirely. There are no externally-listening services on the customer's network for an attacker to discover through port scanning or exploit through service vulnerabilities. The customer's external network perimeter remains unaffected by the Union.ai integration. Firewall management at the perimeter is simplified to a single rule: permit outbound HTTPS, which most enterprise networks already allow.

The trust model is customer-initiated: the data plane decides when and whether to connect, and the customer can sever either channel at any time by blocking outbound traffic or shutting down the data plane operator.

Under the [Sovereign Data Plane](./sovereign-data-plane) tier, the client-to-data-plane path runs through a customer-managed internal load balancer inside the customer's VPC instead of the Cloudflare-backed tunnel; the data-plane-to-control-plane gRPC channel remains outbound-only. The external perimeter still requires no inbound rules; the internal load balancer is reachable only from inside the customer's corporate network.

The Zero Trust client-to-data-plane path is **one network hop shorter** than the prior architecture, in which customer-data requests were proxied through the control plane before reaching the data plane. Log streaming, structured I/O retrieval, and large input uploads consequently complete with lower first-byte and end-to-end latency than they did pre-Zero-Trust; there is no performance trade-off in adopting the new architecture.

## Direct-to-DataPlane tunnel

The Direct-to-DataPlane tunnel is an outbound-only encrypted Cloudflare Tunnel from the customer's cluster to the Cloudflare edge network. It is initiated by a `cloudflared` daemon in the data plane and carries client-to-data-plane traffic in -- not control-plane-to-data-plane traffic. The tunnel **terminates inside the customer's cluster** at an Envoy router that authenticates each request against Union identity and enforces RBAC before forwarding to the data-plane `dataproxy` service. The Union control plane is not on this path. For background on the underlying connector, see Cloudflare's [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) documentation.

All traffic through the tunnel is encrypted using a layered transport: TLS 1.3 from the client to the Cloudflare edge, mTLS plus Cloudflare Tunnel encryption from the edge to the data plane, and Cloudflare Access service tokens for application-layer authentication. Tunnel tokens are rotated automatically: the data plane operator periodically polls Union and picks up updated tokens when issued.

The tunnel maintains health checks and heartbeats, and automatically reconnects if the connection drops. State reconciliation occurs upon reconnection, so no requests are lost during brief connectivity interruptions.

The tunnel carries every kind of customer-data request: structured task input uploads via signed URLs, log streams (live and persisted), secret writes, auxiliary UI traffic (Ray dashboard, Spark history server, in-task debugger), Apps & Serving ingress, and dataproxy RPCs generally. Bulk artifacts (files, directories, DataFrames, code bundles, reports) transit signed URLs issued by the dataproxy, so the bytes themselves flow directly between the client and the customer's object store. Container images also bypass the tunnel: they are pulled by Kubernetes from the customer's container registry over standard HTTPS. For end-to-end request flow, see [Data flow](../data-protection/data-flow).

### Per-cluster routing

In multi-cluster deployments, each data-plane cluster has its own dedicated tunnel domain (e.g. `<cluster-id>.<base-domain>`). The SDK and UI resolve the right cluster for a given request via the `SelectCluster` RPC and dispatch directly to that cluster's tunnel domain. This keeps log streaming, I/O retrieval, and metrics requests terminating at the correct cluster without round-tripping through any shared aggregator.

### Sovereign Data Plane

Enterprise customers can replace the Cloudflare-mediated tunnel entirely with a customer-managed load balancer inside their own VPC, reachable only from the corporate VPN. This makes the data plane unreachable from any third-party network -- including Cloudflare's -- and unreachable to Union employees. See [Sovereign Data Plane](./sovereign-data-plane) for the topology and trade-offs.

## Direct gRPC connection

In addition to the Direct-to-DataPlane tunnel, the data plane maintains a separate outbound gRPC connection over TLS to the regional control plane endpoint. The data plane operator multiplexes orchestration RPCs over this connection. It is outbound-initiated by the data plane and requires no inbound firewall rules. No customer data flows on this channel -- only orchestration metadata.

This channel carries:

- **Cluster registration**: the data plane registers itself with the control plane on startup and keeps the registration current.
- **Action lifecycle**: TaskAction polling, scheduling decisions, and reconciliation.
- **Event reporting**: execution events, phase transitions, and status updates from the data plane to the control plane.
- **Catalog and artifact lookups**: artifact registry, run metadata, and task definition reads.
- **Admin RPCs**: project, domain, and identity queries.

The connection terminates at the Cloudflare edge for the regional `*.unionai.cloud` / `*.union.ai` hostname, which then routes to the hosted control plane. All traffic is encrypted with TLS 1.2+.

## Regional endpoints

Union.ai provides control plane endpoints in multiple regions. Customers select the region closest to their data plane deployment to minimize latency. Region selection also has data residency implications -- see [Data classification and residency](../data-protection/classification-and-residency#data-residency).

| Region | Location |
|---|---|
| US East | us-east-2 |
| US West | us-west-2 |
| Europe West 1 | eu-west-1 |
| Europe West 2 | eu-west-2 |
| Europe Central | eu-central-1 |

Each region has its own dedicated control plane endpoint hostname.

## Egress configuration

For customers with strict egress controls, outbound traffic can be limited to Cloudflare's published CIDR blocks. These blocks can be further restricted to specific Cloudflare regions to minimize the allowed egress surface. Cloudflare publishes its IP ranges at [cloudflare.com/ips](https://www.cloudflare.com/ips/).

For firewall rules that permit `cloudflared` egress while blocking all ingress, see Cloudflare's [Tunnel with firewall](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/) guide.

## Communication paths

All communication paths in the system use encryption. No unencrypted communication paths exist.

| Path | Protocol | Encryption |
|---|---|---|
| Client to Control Plane (orchestration API, UI metadata) | HTTPS | TLS 1.2+ |
| Client to Data Plane (customer-data requests) | Direct-to-DataPlane tunnel | TLS 1.3 + mTLS |
| Data Plane → Control Plane (orchestration metadata, outbound-initiated) | gRPC over TLS | TLS 1.2+ |
| Client to Object Store | HTTPS (presigned URL) | TLS 1.2+ (cloud provider enforced) |
| Fluent Bit to Log Aggregator | Cloud provider SDK | TLS (cloud-native) |
| Task Pods to Object Store | Cloud provider SDK | TLS (cloud-native) |
| Union.ai to Customer Kubernetes API (BYOC only) | PrivateLink / PSC | TLS (private connectivity) |

For details on the BYOC private management connection, see [Private connectivity (BYOC)](./private-connectivity).

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

### Direct-to-DataPlane tunnel and direct gRPC

**Reviewer focus:** Confirm that bulk data (files, DataFrames, code bundles) transfers directly between clients and the customer's object store via presigned URLs, and that structured task I/O and log streams flow through the Direct-to-DataPlane tunnel directly to the data plane (no Union control plane on the path). Confirm that the direct gRPC connection from the data plane operator to the regional control plane endpoint is outbound-initiated and carries no customer data.

**How to verify:**

1. Inspect tunnel pod logs:

   ```bash
   kubectl logs <tunnel-pod> -n union
   ```

   Logs should show health checks, connection establishment, and message exchanges.

2. Analyze VPC Flow Logs for traffic patterns. Bulk data transfers (files, DataFrames, code bundles) should flow directly between task pods and the customer's object store endpoints (S3/GCS/Azure Blob), not through Cloudflare IPs. Structured task I/O and log streams will flow through the tunnel as documented.

3. Use browser developer tools (Network tab) in the Union.ai UI to confirm that binary output artifacts are fetched via presigned URLs (resolving to the customer's storage domain), while structured outputs are fetched via the control plane API.

### Egress configuration

**Reviewer focus:** Confirm that egress can be restricted to Cloudflare CIDR blocks without breaking functionality.

**How to verify:**

1. Apply egress rules that allow outbound traffic only to Cloudflare CIDR blocks (and the customer's cloud provider endpoints for object store and logging).

2. Verify that the tunnel connection establishes successfully and workflows execute normally.

3. Attempt to reach an endpoint outside the allowed egress list from a task pod to confirm the restriction is effective.
