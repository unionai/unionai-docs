---
title: Deployment models
weight: 6
variants: -flyte +union
---

# Deployment models

Union.ai supports two deployment models: **BYOC** (Bring Your Own Cloud) and **Self-managed**. Both models share the same fundamental [two-plane separation](./two-plane-separation): the control plane is hosted by Union.ai, and the data plane runs in the customer's cloud account. They differ in who operates the data plane's Kubernetes cluster.

## Common properties

Regardless of deployment model, both BYOC and Self-managed share the same core security properties:

- The same control plane / data plane architecture described in [Two-plane separation](./two-plane-separation)
- Encryption in transit (TLS 1.2+) and cloud-provider native encryption at rest (see [Encryption](../data-protection/encryption))
- RBAC for user and service account authorization
- Tenant isolation via Kubernetes namespaces and IAM scoping
- Audit logging of administrative and user actions
- Outbound-only [network connectivity](./network) (Cloudflare Tunnel and direct gRPC)

The key difference is operational: in BYOC, Union.ai manages the Kubernetes cluster within the customer's cloud account. In Self-managed, the customer operates the cluster entirely on their own.

## BYOC

In the BYOC model, Union.ai manages the Kubernetes cluster within the customer's cloud account. The cluster runs in the customer's VPC, uses the customer's IAM roles, and stores data in the customer's object store, but Union.ai handles the operational burden of running the cluster.

The Kubernetes API endpoint is private-only, accessible through [PrivateLink, Private Service Connect, or Azure Private Link](./private-connectivity). Union.ai accesses the cluster exclusively through this private connection for management operations.

Union.ai manages:

- Kubernetes cluster provisioning and lifecycle
- Kubernetes version upgrades
- Node pool configuration and scaling
- Helm chart deployments and updates for Union.ai components
- The monitoring stack (Prometheus, Grafana, Fluent Bit)
- Serving infrastructure (Kourier, Knative, Union Operator)
- Data plane component patching and updates

The customer retains ownership and control of:

- The cloud account and its IAM policies
- VPC configuration and network architecture
- Object storage buckets and their access policies
- Any additional infrastructure outside the managed cluster

Union.ai is responsible for the availability and security of the managed Kubernetes cluster. The customer is responsible for the availability and security of the surrounding cloud account infrastructure (VPC, IAM, object storage). Union.ai assumes the cluster-level third-party dependency risk: if a Kubernetes vulnerability requires patching, Union.ai handles it.

## Self-managed

In the Self-managed model, the customer operates the data plane independently. Union.ai has zero access to the data plane infrastructure. The only connections between the control plane and the data plane are two outbound-only channels initiated by the data plane: a Cloudflare Tunnel and a direct gRPC connection. See [Network architecture](./network) for details.

The customer provisions all IAM roles, configures network policies, manages Kubernetes versions and upgrades, and handles all patching of data plane components. The customer is solely responsible for data plane availability, security hardening, and compliance of the data plane infrastructure.

This model provides maximum isolation and control. It is appropriate for organizations that have the Kubernetes operational expertise to manage the cluster and prefer to eliminate any third-party access to their data plane infrastructure.

## Availability and resilience

The control plane runs on AWS with multi-AZ redundancy and automated failover. Availability is covered by Union.ai's SOC 2 Type II certification, and specific SLA commitments are defined in customer contracts.

A critical resilience property of the architecture is that **in-flight workflows continue running during control plane outages**. The Executor is a Kubernetes controller: once a task pod is created, it runs independently of the control plane. If either outbound channel drops or the control plane becomes unavailable, running task pods are unaffected. When connectivity is restored, the Executor reconciles state with the control plane, and the execution history is updated. New workflow submissions require control plane availability, but existing work is not interrupted.

For data plane availability, the responsibility depends on the deployment model. In the self-managed model, the customer is solely responsible for data plane availability. In the BYOC model, Union.ai is responsible for the availability of the managed Kubernetes cluster, while the customer remains responsible for the underlying cloud account resources.

## Verification

### Availability and resilience

**Reviewer focus:** Confirm that in-flight workflows survive control plane connectivity loss and that state reconciles upon reconnection.

**How to verify:**

1. Start a long-running workflow (e.g., a task with a `sleep` of several minutes).

2. Simulate a connectivity disruption to the control plane by scaling down the Tunnel Service:

   ```bash
   kubectl scale deployment <tunnel-deployment> -n union --replicas=0
   ```

3. Verify that task pods continue running:

   ```bash
   kubectl get pods -n <execution-namespace>
   ```

   The task pods should remain in `Running` state and continue their work.

4. Restore connectivity:

   ```bash
   kubectl scale deployment <tunnel-deployment> -n union --replicas=1
   ```

5. Check the Union.ai UI or query the API to confirm that the execution state reconciled correctly. The execution should show as completed (or progressed) with accurate timestamps, not as failed or lost.
