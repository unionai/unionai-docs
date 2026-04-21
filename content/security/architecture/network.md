---
title: Network architecture
weight: 4
variants: -flyte +union
---

# Network architecture

The network architecture reinforces the [two-plane separation](./two-plane-separation) with an outbound-only connectivity model. The data plane initiates all connections to the control plane -- there are no inbound firewall rules, no VPN tunnels, and no listening services on the customer's network that Union.ai can reach.

## Outbound-only model

All network connections between the data plane and the control plane are initiated by the data plane. The customer's network requires only standard outbound HTTPS access to Cloudflare edge nodes. No inbound firewall rules, port forwarding, or VPN configuration is needed.

This model eliminates the inbound attack surface entirely. There are no listening services on the customer's network for an attacker to discover through port scanning or exploit through service vulnerabilities. The customer's network perimeter remains unaffected by the Union.ai integration. Firewall management is simplified to permitting outbound HTTPS -- a rule that most enterprise networks already allow.

The trust model is customer-initiated: the data plane decides when and whether to connect, and the customer can sever the connection at any time by blocking outbound traffic or shutting down the Tunnel Service.

## Cloudflare Tunnel

The connection between the data plane and the control plane uses a Cloudflare Tunnel -- an outbound-only encrypted connection from the customer's cluster to the Cloudflare edge network, which then routes to the Union.ai control plane.

All traffic through the tunnel is encrypted using a layered transport: TLS with mutual authentication (X.509 client certificates), Cloudflare Access service tokens for application-layer authentication, and Cloudflare Tunnel encryption for the network path. Tunnel tokens are managed via operator polling and rotate implicitly when the control plane issues updated values.

The Tunnel Service in the data plane maintains this connection with health checks and heartbeats, and automatically reconnects if the connection drops. State reconciliation occurs upon reconnection, so no data is lost during brief connectivity interruptions.

The tunnel carries the following traffic, all encrypted in transit:

- **Orchestration instructions** -- TaskAction definitions from the control plane to the data plane
- **State transitions** -- execution phase updates from the data plane to the control plane
- **Structured task inputs** -- serialized protobuf task inputs proxied to the data plane object store on run submission (up to 10 MB per request, plaintext in DataProxy memory during transit, not persisted)
- **Structured task inputs and outputs** -- fetched from the data plane object store on result retrieval (up to 20 MiB per request, plaintext in DataProxy memory, not persisted)
- **Log streams** -- execution log content streamed through the DataProxy relay as plaintext in memory, not persisted or filtered
- **Secret values** -- secret values during create/update operations, relayed through DataProxy as plaintext in memory to the data plane secret manager, not persisted in the control plane
- **Presigned URL signing requests** -- metadata-only requests brokered to generate time-limited data access URLs
- **Health checks** -- bidirectional health and liveness signals

Bulk customer data -- files, directories, DataFrames, code bundles, and container images -- does **not** traverse the tunnel. These objects are transferred directly between clients and the customer's object store via presigned URLs, bypassing the control plane entirely.

## Regional endpoints

Union.ai provides control plane endpoints in multiple regions. Customers select the region closest to their data plane deployment to minimize latency.

| Region | Location | Domain |
|---|---|---|
| US East | us-east-2 | `hosted.unionai.cloud` |
| US West | us-west-2 | (region-specific subdomain) |
| Europe West 1 | eu-west-1 | (region-specific subdomain) |
| Europe West 2 | eu-west-2 | (region-specific subdomain) |
| Europe Central | eu-central-1 | (region-specific subdomain) |

## Egress configuration

For customers with strict egress controls, outbound traffic can be limited to Cloudflare's published CIDR blocks. These blocks can be further restricted to specific Cloudflare regions to minimize the allowed egress surface. Cloudflare publishes its IP ranges at [cloudflare.com/ips](https://www.cloudflare.com/ips/).

## Communication paths

All communication paths in the system use encryption. No unencrypted communication paths exist.

| Path | Protocol | Encryption |
|---|---|---|
| Client to Control Plane | ConnectRPC (gRPC-Web) over HTTPS | TLS 1.2+ |
| Control Plane to Data Plane | Cloudflare Tunnel (outbound-initiated) | mTLS |
| Client to Object Store | HTTPS (presigned URL) | TLS 1.2+ (cloud provider enforced) |
| Fluent Bit to Log Aggregator | Cloud provider SDK | TLS (cloud-native) |
| Task Pods to Object Store | Cloud provider SDK | TLS (cloud-native) |
| Union.ai to Customer K8s API (BYOC only) | PrivateLink / PSC | TLS (private connectivity) |

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

   Services should be `ClusterIP` type or, if `LoadBalancer`, should serve only Apps & Serving endpoints -- not control plane connectivity.

3. Review VPC Flow Logs to confirm that connections to Cloudflare are outbound-initiated. All flows to Cloudflare IP ranges should show the data plane node as the source.

4. (Optional) Run a port scan from an external host against the data plane nodes to confirm no Union.ai-related services are reachable.

### Cloudflare Tunnel

**Reviewer focus:** Confirm that bulk data (files, DataFrames, code bundles) bypasses the tunnel via presigned URLs, and that structured task I/O and log streams transit the tunnel as documented above (encrypted in transit, not persisted).

**How to verify:**

1. Inspect tunnel pod logs:

   ```bash
   kubectl logs <tunnel-pod> -n union
   ```

   Logs should show health checks, connection establishment, and message exchanges.

2. Analyze VPC Flow Logs for traffic patterns. Bulk data transfers (files, DataFrames, code bundles) should flow directly between task pods and the customer's object store endpoints (S3/GCS/Azure Blob), not through Cloudflare IPs. Structured task I/O (up to 10-20 MiB per request) and log streams will flow through the tunnel as documented.

3. Use browser developer tools (Network tab) in the Union.ai UI to confirm that binary output artifacts are fetched via presigned URLs (resolving to the customer's storage domain), while structured outputs are fetched via the control plane API.

4. (Advanced) Request or build a tunnel audit mode that logs all messages crossing the tunnel with their sizes and types. This would provide definitive evidence of the traffic composition documented above.

### Egress configuration

**Reviewer focus:** Confirm that egress can be restricted to Cloudflare CIDR blocks without breaking functionality.

**How to verify:**

1. Apply egress rules that allow outbound traffic only to Cloudflare CIDR blocks (and the customer's cloud provider endpoints for object store and logging).

2. Verify that the tunnel connection establishes successfully and workflows execute normally.

3. Attempt to reach an endpoint outside the allowed egress list from a task pod to confirm the restriction is effective.
