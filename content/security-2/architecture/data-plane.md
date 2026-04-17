---
title: Data plane
weight: 3
variants: -flyte +union
mermaid: true
---

The data plane runs entirely within the customer's cloud account on a Kubernetes cluster. It is where all computation occurs and where all customer data resides. In the self-managed model, the customer operates the data plane independently. In the BYOC model, Union.ai manages the Kubernetes cluster on the customer's behalf, but it still runs in the customer's cloud account. See [Deployment models](./deployment-models) for the differences.

## Components

The data plane consists of several components, each handling a specific aspect of workflow execution and data management.

**Executor** is a Kubernetes controller that watches for TaskAction custom resources created by the control plane's Queue Service. When a TaskAction appears, the Executor reconciles its lifecycle: creating task pods, monitoring their status, and reporting state transitions back to the control plane via ConnectRPC. The Executor operates as a standard Kubernetes controller -- if connectivity to the control plane is lost, in-flight pods continue running and state reconciles when the connection is restored.

**Object Store Service** handles presigned URL signing for secure data access. It supports several operations: `CreateSignedURL` for generating time-limited download URLs, `CreateUploadLocation` for generating upload URLs with Content-MD5 integrity verification, `Presign` for general-purpose URL signing, and `Get`/`Put` for direct object operations. All data access from clients goes through presigned URLs, ensuring the control plane never handles data payloads directly.

**Log Provider** serves task logs through two channels. For running tasks, it streams live logs from the Kubernetes API. For completed tasks, it retrieves logs from the cloud provider's log aggregator (CloudWatch, Cloud Logging, or Azure Monitor). Logs include structured metadata (task identifiers, timestamps, log levels) and are streamed through the DataProxy relay without being persisted in the control plane.

**Image Builder** uses Buildkit running on the customer's Kubernetes cluster to build container images from user-submitted `Image` specifications. Source code and built images never leave the customer's infrastructure. Base images are pulled from customer-configured registries, and built images are pushed to the customer's container registry (ECR, GCR, or ACR).

**Tunnel Service** maintains the outbound-only encrypted connection from the data plane to the control plane via Cloudflare. This service initiates the connection (no inbound ports required), performs health checks and heartbeats, and automatically reconnects if the connection drops. See [Network architecture](./network) for details on what traffic traverses this tunnel.

**Apps & Serving** provides model and application serving capabilities using Knative with a Kourier gateway. All serving infrastructure runs within the customer's cluster. Authentication is enforced on all endpoints by default (SSO for browser access, API keys for programmatic access), with an option to allow anonymous access on specific endpoints. See [Apps & Serving security](#apps--serving-security) below for details.

## Object store layout

Each data plane cluster uses two object store buckets: a **metadata bucket** for execution metadata and a **fast-registration bucket** for rapid code deployment artifacts. Within these buckets, objects are organized by namespace: `org/project/domain/run-name/action-name/`. This layout provides natural namespace isolation -- IAM policies and bucket policies can scope access to specific organizational boundaries.

## Kubernetes security

The data plane enforces several layers of Kubernetes security to protect workloads and limit blast radius.

**Workload identity federation** eliminates the need for static cloud credentials. Task pods and platform services authenticate to cloud APIs using cloud-native identity mechanisms (IRSA on AWS, Workload Identity on GCP, Azure Workload Identity on Azure). No long-lived access keys are stored as Kubernetes secrets.

**Kubernetes RBAC** restricts what each service account can do within the cluster. Platform components have scoped permissions for their specific functions, and task pods run under service accounts with minimal privileges.

**Network policies** control pod-to-pod communication within the cluster, limiting lateral movement in the event of a container compromise.

**Resource quotas and limit ranges** prevent any single workload from consuming all cluster resources, providing both stability and a degree of isolation between tenants and projects.

**Pod security contexts** enforce non-root execution for platform components, reducing the impact of container escape vulnerabilities.

## Container security

The Image Builder runs Buildkit on the customer's Kubernetes cluster. When a user defines an `Image` specification, the build executes entirely within the customer's infrastructure. Source code is uploaded to the customer's object store via presigned URL and fetched by the builder -- it never transits through the control plane. Built images are pushed directly to the customer's container registry (ECR, GCR, or ACR).

Base images are pulled from registries configured by the customer, allowing the use of hardened or pre-approved base images. Customers can apply their own image tagging conventions, vulnerability scanning policies, and registry access controls.

Task pods mount code bundles via presigned URLs with limited time-to-live (TTL). These URLs expire after a short window, limiting the exposure if a URL is intercepted.

## IAM and workload identity

The data plane uses two IAM roles to separate platform-level and user-level access:

**adminflyterole** is used by platform services (Executor, Object Store Service, Log Provider). It has read/write access to the object store buckets, access to the secrets manager for retrieving user-defined secrets, and read access to persisted logs. This role is bound to platform service accounts via workload identity federation.

**userflyterole** is used by task pods -- the containers running user code. It has read/write access to the object store buckets for reading inputs and writing outputs. It does not have access to the secrets manager or platform-level resources.

Both roles use cloud-native workload identity federation: IRSA (IAM Roles for Service Accounts) on AWS, Workload Identity on GCP, and Azure Workload Identity on Azure. No static credentials are created, stored, or rotated. The Kubernetes service account annotations bind each pod to the appropriate IAM role automatically.

## Apps & Serving security

App and serving traffic flows entirely within the customer's infrastructure -- no application code, data, or serving requests pass through the control plane.

Inbound traffic reaches the serving endpoints through Cloudflare, which provides DDoS protection, before routing to the Kourier ingress gateway running in the customer's cluster. Authentication is enforced by default on all endpoints: browser-based access uses SSO, and programmatic access uses API keys. Individual endpoints can be configured for anonymous access when required (for example, public-facing model endpoints).

RBAC controls govern which users and service accounts can deploy applications and access specific endpoints, scoped per project. All serving infrastructure -- Knative, Kourier, and the Union Operator -- runs within the customer's Kubernetes cluster. In the BYOC model, Union.ai manages the lifecycle of this serving infrastructure (upgrades, scaling, configuration), but the infrastructure itself resides in the customer's account.

## Verification

### Components (Medium-High)

**Reviewer focus:** Confirm that the described components are running in the customer's cluster and match the documented architecture.

**How to verify:**

1. List data plane pods and deployments:

   ```bash
   kubectl get pods -n union
   kubectl get deployments -n union -o wide
   ```

   Confirm that the Executor, Object Store Service, Tunnel Service, and other components are present.

2. Inspect a specific component:

   ```bash
   kubectl describe pod <executor-pod> -n union
   ```

   Verify the container image, service account, and resource configuration match expectations.

### Kubernetes security (High)

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

### Container security (High)

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

### IAM and workload identity (Critical)

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
