---
title: Compute plane components reference
weight: 12
variants: -flyte +byoc +selfmanaged
---

# Compute plane components reference

This section provides a detailed reference for each security-relevant component running on the customer’s compute plane.
Understanding these components is essential for enterprise security teams conducting architecture reviews.

## Executor

The Executor is a Kubernetes controller that runs on the customer’s compute plane.
It is the core component responsible for translating orchestration instructions into actual workload execution.
The Executor watches for TaskAction custom resources created by the Queue Service, reconciles each TaskAction through its lifecycle (Queued, Initializing, Running, Succeeded/Failed), reports state transitions back to the control plane’s State Service via ConnectRPC through the Cloudflare tunnel, and creates and manages Kubernetes pods for task execution.

The Executor runs entirely within the customer’s cluster.
It accesses the customer’s object store and secrets using IAM roles bound to its Kubernetes service account via workload identity federation.
At no point does the Executor communicate directly with external services outside the customer’s cloud account (except through the Cloudflare tunnel to the control plane).

## Apps and serving

Apps and Serving enables customers to deploy long-running web applications — Streamlit dashboards, FastAPI services, notebooks, and inference endpoints — directly on the customer's compute plane.
Apps run as Knative Services within tenant-scoped Kubernetes namespaces, with the Union Operator managing the full lifecycle including autoscaling and scale-to-zero.
No application code, data, or serving traffic passes through the Union.ai control plane.
Inbound traffic routes through Cloudflare for DDoS protection to a Kourier gateway (Union's Envoy fork) running on the customer's cluster, which enforces authentication against the control plane before forwarding to the app container.
Browser access uses SSO; programmatic access requires a Union API key.
All endpoints require authentication by default, with optional per-app anonymous access.
Union's RBAC controls which users can deploy and access apps per project, and resource quotas constrain consumption.
The load balancer, serving infrastructure, and app containers all run within the customer's cluster, maintaining the same data residency guarantees as workflow execution.

## Object store service

The Object Store Service runs on the compute plane and provides the signing capabilities that enable the presigned URL security model.
Its key operations include CreateSignedURL (generates presigned URLs using the customer’s IAM credentials via the admin role), CreateUploadLocation (generates presigned PUT URLs for fast registration with Content-MD5 integrity verification), Presign (generic presigning for arbitrary object store keys), and Get/Put (direct object store read/write used internally by platform services).

Two object store buckets are provisioned per compute plane cluster: a metadata bucket for task inputs, outputs, reports, and intermediate data, and a fast-registration bucket for code bundles uploaded during task registration.
Object layout follows a hierarchical pattern: org/project/domain/run-name/action-name, providing natural namespace isolation.

## Log provider

The Log Provider runs on the compute plane and serves task logs from two sources.
For live tasks, logs are streamed directly from the Kubernetes API (pod stdout/stderr) in real time.
For completed tasks, logs are read from the cloud log aggregator (CloudWatch, Cloud Logging, or Azure Monitor) after pod termination.
Log lines include structured metadata: timestamp, message content, and originator classification (user vs. system).
This structured approach enables security teams to distinguish between application-generated logs and platform-generated logs for audit purposes.

## Image builder

When enabled, the Image Builder runs on the compute plane and uses Buildkit to construct container images without exposing source code or built artifacts outside the customer’s infrastructure.
The build process pulls the base image from a customer-approved registry (public or private), accesses user code via a presigned URL with a limited time-to-live, builds the container image with specified layers (pip packages, apt packages, custom commands, UV/Poetry projects), and pushes the built image to the customer’s container registry (ECR, GCR, or ACR).
Source code and built images never leave the customer’s infrastructure during the build process.

## Tunnel service

The Tunnel Service maintains the Cloudflare Tunnel connection between the compute plane and control plane.
It is responsible for initiating and maintaining the outbound-only encrypted connection, performing periodic health checks and heartbeats, and reconnecting automatically in case of network disruption.
The Cluster Service on the control plane performs periodic reconciliation to ensure tunnel health and DNS records are current.
