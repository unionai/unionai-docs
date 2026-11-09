---
title: Private connectivity (BYOC)
description: How Union.ai reaches a BYOC customer cluster, and the optional private endpoint over AWS PrivateLink or GCP Private Service Connect.
icon: reception-4
weight: 6
variants: -flyte +union
---

# Private connectivity (BYOC)

In the BYOC deployment model, Union.ai maintains a management connection to the customer's Kubernetes cluster. By default, this connection reaches the cluster's public Kubernetes API endpoint. A private endpoint is optional and available only for EKS and GKE clusters: when it is configured, the connection uses AWS PrivateLink (EKS) or GCP Private Service Connect (GKE). Azure (AKS) clusters have no private-endpoint option and are managed over their public API endpoint.

With a private endpoint, this connection is used exclusively for cluster management operations: Kubernetes version upgrades, node pool provisioning and scaling, Helm chart deployments and updates, and health monitoring. It provides Union.ai with the access needed to manage the Kubernetes cluster without exposing the Kubernetes API to the public internet.

With a private endpoint, the management connection does **not** carry customer data or orchestration traffic. Customer data and orchestration RPCs flow through the outbound channels described in [Network architecture](./network). The management connection over the private endpoint handles only infrastructure management operations.

When the private endpoint is configured, the Kubernetes API isn't reachable from the public internet. This aligns with several compliance controls: ISO 27001 A.5.15 (Access control), A.8.20 (Networks security), A.8.22 (Segregation of networks), and CIS Controls v8 Control 12 (Network infrastructure management). Without a private endpoint, the cluster's Kubernetes API endpoint is public.

In the self-managed alternative, no management connection exists because the customer operates the data plane independently. See the [security overview](../_index) for the deployment-model summary.

## Verification

### Private management connection

**Reviewer focus:** For an EKS or GKE cluster configured with a private endpoint, confirm that the Kubernetes API endpoint is accessible only via the private connectivity service and is not exposed to the public internet.

**How to verify:**

1. In the AWS console, navigate to VPC > Endpoint services and confirm that an endpoint service exists in front of the Network Load Balancer that forwards to the customer's Kubernetes API:

   ```bash
   # AWS example
   aws ec2 describe-vpc-endpoint-service-configurations
   ```

   For GCP, use `gcloud compute service-attachments list` and `gcloud compute forwarding-rules list`.

2. Verify that the Kubernetes API resolves to a private IP or hostname:

   ```bash
   kubectl cluster-info
   ```

   The server address should be a private IP (e.g., `10.x.x.x`) or a private DNS name, not a public endpoint.

3. Attempt to reach the Kubernetes API from outside the VPC to confirm it is unreachable:

   ```bash
   curl -k https://<k8s-api-endpoint>/healthz
   ```

   This should time out or be refused when run from a host outside the customer's VPC or private connectivity path.
