---
title: Data plane
weight: 3
variants: -flyte +union
mermaid: true
---

# Data plane

The data plane runs entirely within the customer's cloud account on a Kubernetes cluster. It is where all computation occurs and where customer data is stored at rest (see [Data classification and residency](../data-protection/classification-and-residency)). In the self-managed model, the customer operates the data plane independently. In the BYOC model, Union.ai manages the Kubernetes cluster on the customer's behalf, but it still runs in the customer's cloud account. See [Deployment models](./deployment-models) for the differences.

## Components

The data plane consists of several components, each handling a specific aspect of task execution and data management.

**Envoy router** is the AuthN/AuthZ enforcement point that fronts every customer-data request entering the cluster. Under the default tier, it sits at the egress of the Direct-to-DataPlane tunnel; under the [Sovereign Data Plane](./sovereign-data-plane) tier, it sits behind the customer-managed internal load balancer. In either case, every request is authenticated against the requester's Union.ai identity and evaluated against the RBAC policy *inside the customer's cluster* before forwarding to the dataproxy service. The Union.ai control plane is not on the path.

**Dataproxy service** is the single endpoint for every customer-data request. It handles:

- **Signed URL generation** for bulk artifacts (files, directories, DataFrames, code bundles, reports) -- the dataproxy issues short-lived signed URLs via the tunnel so clients can read or write directly to the customer's object store. The data bytes themselves do not flow through dataproxy.
- **Structured I/O retrieval** -- inputs and outputs of actions (small protobuf literals) are served back through the dataproxy.
- **Log fetching** -- live logs from the Kubernetes API, persisted logs from the cloud log aggregator (CloudWatch, Cloud Logging, or Azure Monitor). There is no content filtering or redaction; any sensitive data (secrets, PII, stack traces) that user code writes to stdout/stderr is served unmodified.
- **Auxiliary UI proxying** -- Ray dashboards, Spark history servers, in-task debuggers, and other per-action UIs are served back through the dataproxy via the same authenticated path.
- **Secret writes** -- secret values from the SDK or UI are routed to the data-plane secrets backend (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, or K8s Secrets) without traversing the control plane.

**Executor** is a Kubernetes controller that watches for TaskAction custom resources created by the control plane. When a TaskAction appears, the Executor reconciles its lifecycle: creating task pods, monitoring their status, and reporting state transitions back to the control plane. If connectivity to the control plane is lost, in-flight pods continue running and state reconciles when the connection is restored.

**Image Builder** uses Buildkit running on the customer's Kubernetes cluster to build container images from user-submitted `Image` specifications. Source code and built images never leave the customer's infrastructure. Base images are pulled from customer-configured registries, and built images are pushed to the customer's container registry (ECR, GCR, or ACR).

**Tunnel Service** maintains the outbound-only encrypted Direct-to-DataPlane tunnel (a Cloudflare Tunnel under the hood) from the data plane to the Cloudflare edge under the default tier. This service initiates the tunnel (no inbound ports required), performs health checks and heartbeats, and automatically reconnects if the connection drops. Under the [Sovereign Data Plane](./sovereign-data-plane) tier, the Tunnel Service is replaced by a customer-managed internal load balancer that fronts the Envoy router; the rest of the data-plane components are identical.

In addition to the client-to-data-plane path, the data plane operator establishes a separate outbound gRPC connection (TLS) to the regional control plane endpoint for orchestration RPCs (cluster registration, action lifecycle, event reporting, catalog and artifact lookups, admin RPCs). This channel is outbound-initiated under both tiers and carries no customer data. See [Network architecture](./network) for the channel details.

**Metrics Reporter** ships operational metrics (resource utilization, GPU utilization, queue depth) from the data plane to the control plane on its own schedule. The push model means the control plane needs no network route into the data plane at all -- a prerequisite for the Sovereign Data Plane tier.

**Apps & Serving** provides model and application serving capabilities using Knative with a Kourier gateway. All serving infrastructure runs within the customer's cluster. Authentication is enforced on all endpoints by default (SSO for browser access, API keys for programmatic access), with an option to allow anonymous access on specific endpoints. See [Apps & Serving security](#apps--serving-security) below for details.

### Multi-cluster routing

When a tenant spans multiple data-plane clusters, customer-data requests need to reach the correct one. The control plane exposes a `SelectCluster` RPC that resolves an action ID, project/domain, or queue/org reference to the per-cluster tunnel domain (or, under Sovereign Data Plane, the per-cluster internal LB hostname). The SDK and UI call `SelectCluster` first, then dispatch the data-path request directly to the resolved cluster -- no aggregator or fan-out hop in front of the dataproxy. Org-level secrets are scoped through a `--cluster-pool` parameter so that creation, listing, and deletion target the right cluster pool.

For how each of these pathways handles data in transit, see [Data flow](../data-protection/data-flow).

## Object store layout

Each data plane cluster uses two object store buckets: a **metadata bucket** for execution metadata and a **fast-registration bucket** for rapid code deployment artifacts. Within these buckets, objects are organized by namespace: `org/project/domain/run-name/action-name/`. This layout provides isolation: IAM policies and bucket policies can scope access to specific organizational boundaries.

## Kubernetes security

The data plane enforces several layers of Kubernetes security to protect workloads and limit blast radius.

**Workload identity federation** eliminates the need for static cloud credentials on the data plane. See [IAM and workload identity](#iam-and-workload-identity) below for details.

**Kubernetes RBAC** restricts what each service account can do within the cluster. Platform components have scoped permissions for their specific functions, and task pods run under service accounts with minimal privileges.

**Network policies** control pod-to-pod communication within the cluster, limiting lateral movement in the event of a container compromise.

**Resource quotas and limit ranges** prevent any single workload from consuming all cluster resources, providing both stability and a degree of isolation between tenants and projects.

**Pod security contexts** enforce non-root execution for platform components, reducing the impact of container escape vulnerabilities.

## Container security

When a user defines an `Image` specification, source code is uploaded to the customer's object store via presigned URL and fetched by the builder; it never transits through the control plane.

Base images are pulled from registries configured by the customer, allowing the use of hardened or pre-approved base images. Customers can apply their own image tagging conventions, vulnerability scanning policies, and registry access controls.

Task pods mount code bundles via presigned URLs with limited time-to-live (TTL). These URLs expire after a short window, limiting the exposure if a URL is intercepted.

## IAM and workload identity

The data plane uses two IAM roles to separate platform-level and user-level access:

**`adminflyterole`** is used by platform services (Executor, Dataproxy). It has read/write access to the object store buckets, access to the secrets manager for retrieving user-defined secrets, and read access to persisted logs. This role is bound to platform service accounts via workload identity federation.

**`userflyterole`** is used by task pods (the containers running user code). It has read/write access to the object store buckets for reading inputs and writing outputs. It does not have access to the secrets manager or platform-level resources.

Both roles use cloud-native workload identity federation: IRSA (IAM Roles for Service Accounts) on AWS, Workload Identity on GCP, and Azure Workload Identity on Azure. No static credentials are created, stored, or rotated. The Kubernetes service account annotations bind each pod to the appropriate IAM role automatically.

## Apps & Serving security

App and serving traffic flows entirely within the customer's infrastructure. No application code, data, or serving requests pass through the control plane.

Under the default tier, inbound traffic reaches the serving endpoints through Cloudflare, which provides DDoS protection, before routing to the Kourier ingress gateway running in the customer's cluster. Under the [Sovereign Data Plane](./sovereign-data-plane) tier, serving endpoints sit behind the same customer-managed internal load balancer and are reachable only from the customer's corporate network. Authentication is enforced by default on all endpoints under either tier: browser-based access uses SSO, and programmatic access uses API keys. Individual endpoints can be configured for anonymous access when required (for example, public-facing model endpoints on the default tier).

RBAC controls govern which users and service accounts can deploy applications and access specific endpoints, scoped per project. All serving infrastructure (Knative, Kourier, and the Union Operator) runs within the customer's Kubernetes cluster. In the BYOC model, Union.ai manages the lifecycle of this serving infrastructure (upgrades, scaling, configuration), but the infrastructure itself resides in the customer's account.

## Verification

### Components

**Reviewer focus:** Confirm that the described components are running in the customer's cluster and match the documented architecture.

**How to verify:**

1. List data plane pods and deployments:

   ```bash
   kubectl get pods -n union
   kubectl get deployments -n union -o wide
   ```

   Confirm that the Executor, Envoy router, Dataproxy, Tunnel Service (default tier only), Metrics Reporter, and other components are present.

2. Inspect a specific component:

   ```bash
   kubectl describe pod <executor-pod> -n union
   ```

   Verify the container image, service account, and resource configuration match expectations.

### Kubernetes security

**Reviewer focus:** Confirm that Kubernetes RBAC, network policies, resource quotas, and pod security contexts are in place and correctly scoped.

**How to verify:**

1. Review cluster role bindings for Union components:

   ```bash
   kubectl get clusterrolebindings | grep union
   ```

2. Check network policies across namespaces:

   ```bash
   kubectl get networkpolicies -A
   ```

3. Verify resource quotas:

   ```bash
   kubectl get resourcequotas -A
   ```

4. Inspect pod security contexts:

   ```bash
   kubectl get pods -n <namespace> -o jsonpath='{.items[0].spec.securityContext}'
   ```

   Confirm `runAsNonRoot: true` or equivalent non-root settings on platform pods.

### Container security

**Reviewer focus:** Confirm that image builds execute entirely within the customer's infrastructure and that built images never leave the customer's registry.

**How to verify:**

1. Trigger an image build by submitting a workflow with an `Image` specification.

2. Observe the build pod:

   ```bash
   kubectl get pods -n union | grep build
   kubectl logs <buildkit-pod> -n union
   ```

   Confirm that the build pulls base images from the customer's configured registry and pushes the result to the customer's container registry.

3. Verify the image in the customer's registry:

   ```bash
   aws ecr describe-images --repository-name <repo> --image-ids imageTag=<tag>
   ```

   (Or the equivalent `gcloud` / `az` command for GCP/Azure.)

### IAM and workload identity

**Reviewer focus:** Confirm that the two IAM roles exist with the documented permissions, that workload identity federation is in use, and that no static credentials are present.

**How to verify:**

1. Inspect the IAM roles and their policies:

   ```bash
   aws iam get-role --role-name adminflyterole
   aws iam list-role-policies --role-name adminflyterole
   aws iam list-attached-role-policies --role-name adminflyterole

   aws iam get-role --role-name userflyterole
   aws iam list-role-policies --role-name userflyterole
   aws iam list-attached-role-policies --role-name userflyterole
   ```

   Confirm that `adminflyterole` has object store, secrets manager, and log access. Confirm that `userflyterole` has only object store access.

2. Verify workload identity annotations on service accounts:

   ```bash
   kubectl get sa -n union -o yaml | grep role-arn
   ```

   Each service account should have an annotation binding it to the appropriate IAM role via IRSA (or the equivalent for GCP/Azure).

3. Confirm no static credentials exist:

   ```bash
   kubectl get secrets -n union -o name | grep -i aws
   ```

   There should be no secrets containing static AWS access keys. Workload identity federation eliminates the need for them.
