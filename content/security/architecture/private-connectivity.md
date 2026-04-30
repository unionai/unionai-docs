---
title: Private connectivity (BYOC)
weight: 5
variants: -flyte +union
---

# Private connectivity (BYOC)

In the BYOC deployment model, Union.ai maintains a private management connection to the customer's Kubernetes cluster. This connection uses the cloud provider's native private connectivity service: AWS PrivateLink, GCP Private Service Connect, or Azure Private Link, depending on the customer's cloud platform.

This private connection is used exclusively for cluster management operations: Kubernetes version upgrades, node pool provisioning and scaling, Helm chart deployments and updates, and health monitoring. It provides Union.ai with the access needed to manage the Kubernetes cluster without exposing the Kubernetes API to the public internet.

The private management connection does **not** carry customer data or orchestration traffic. Customer data and orchestration RPCs flow through the outbound channels described in [Network architecture](./network). The private connectivity path handles only infrastructure management operations.

By keeping the Kubernetes API endpoint private, this design aligns with several compliance controls, including ISO 27001 A.5.15 (Access control), A.8.20 (Networks security), A.8.22 (Segregation of networks), and CIS Controls v8 Control 12 (Network infrastructure management). The Kubernetes API is never reachable from the public internet.

For details on the self-managed alternative (where no private management connection exists because the customer operates the data plane independently), see [Deployment models](./deployment-models).

## Verification

### Private management connection

**Reviewer focus:** Confirm that the Kubernetes API endpoint is accessible only via the private connectivity service and is not exposed to the public internet.

**How to verify:**

1. In the AWS console (or equivalent for GCP/Azure), navigate to VPC > Endpoints and confirm that a PrivateLink (or Private Service Connect / Azure Private Link) endpoint exists connecting to the customer's Kubernetes API:

   ```bash
   # AWS example
   aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=*eks*
   ```

   For GCP, use `gcloud compute service-attachments list` and `gcloud compute forwarding-rules list`. For Azure, use `az network private-endpoint list` and `az network private-link-service list`.

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
