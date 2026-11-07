---
title: Control plane
description: What the Union-hosted control plane orchestrates, what it stores, and when it handles customer data.
icon: building
weight: 2
variants: -flyte +union
---

# Control plane

The control plane is the Union.ai-hosted component that orchestrates task execution, manages user access, and provides the API surface. It runs on AWS infrastructure managed by Union.ai and is covered by Union.ai's SOC 2 Type II certification.

Where customer-data requests -- workflow inputs and outputs, code bundles, secret writes, logs, reports, and auxiliary UI traffic -- are served depends on the organization's clusters. If at least one cluster in the organization has a data-plane ingress endpoint that is enabled and ready, clients send these requests directly to that cluster's data plane. If no cluster does, they go to a `dataproxy` service running in the control plane, which forwards them to the cluster.

## What it stores

The control plane stores **orchestration metadata** -- the operational scaffolding plus the task definitions and execution records that drive it. Concretely:

- **Action state**: run and action identifiers, phase, timestamps, cluster assignment, and scheduling configuration.
- **Task and run definitions**: each run submission includes a full TaskSpec (container image, typed interface, resource requirements, security context) and a RunSpec (environment variables, labels, annotations). Trigger specs carry default input values for scheduled runs.
- **Error and event information**: error messages from task executions (which may contain customer data from Python tracebacks), Kubernetes event messages, and per-attempt plugin state.
- **Platform metadata**: user identity records, the RBAC graph, and data plane cluster registrations.

For payloads, it generally stores **URIs** pointing into the customer's object store (for example, `s3://customer-bucket/org/project/domain/run/action/output.pb`), with these exceptions:

- **Tracked runs**: in an organization where not every cluster has a data-plane ingress endpoint enabled and ready, the inputs, outputs, and reports of [tracked runs](../../user-guide/get-started/run-modes/running-locally#track-local-runs-in-the-console) can be stored in the control plane's own bucket. Today this happens when no cluster in the organization has such an endpoint. Tracked-run data stored there stays there and is read from there, even if the organization later enables data-plane ingress.
- **Trigger inputs**: trigger input values are stored inline in the trigger spec when no cluster in the organization has a data-plane ingress endpoint enabled and ready, or when the trigger is registered with an SDK older than 2.5.0.

For the full classification of what is and isn't stored in the control plane, see [Data classification and residency](../data-protection/classification-and-residency). That page does not yet reflect the tracked-run and trigger-input exceptions above.

## Infrastructure

The control plane runs on AWS with multi-AZ redundancy to ensure high availability. It uses managed cloud database services for orchestration metadata, task/run definitions, execution events, and error messages, and an object-store bucket for tracked-run data. The databases are encrypted at rest using AES-256 / cloud-KMS, and isolated within a VPC with restricted security groups that permit access only from control plane application services.

TLS terminates at the edge, and all internal communication occurs over encrypted channels. Automated backups run on a defined schedule with point-in-time recovery capability. Union.ai maintains disaster recovery procedures and applies security patches on a regular cadence. The SOC 2 Type II report covers the availability, security, and operational controls of this infrastructure.

## Capabilities

The control plane exposes the following capabilities:

- **API and UI gateway** -- an authenticated HTTPS API and web console for users, the SDK, and the CLI. All requests are subject to authentication and RBAC enforcement before any orchestration logic runs.
- **Scheduling and execution tracking** -- schedules TaskActions across registered data plane clusters and records execution state (phase transitions, timestamps, errors) reported back from the data plane.
- **Cluster registry** -- maintains the inventory of registered data plane clusters and their health.
- **Cluster selection** -- exposes the `SelectCluster` RPC that clients (SDK / UI) call to resolve which data plane cluster handles a given customer-data request. When at least one cluster in the organization has a data-plane ingress endpoint enabled and ready, the control plane returns that cluster's ingress endpoint, and the client dispatches the data-path request directly to that cluster. In that case, a request fails, rather than falling back to the control plane, when it is tied to a specific cluster that has no such endpoint, or when its cluster pool has no healthy cluster with such an endpoint and an online tunnel (`Unavailable`). The control plane returns its own endpoint only when no cluster in the organization has a data-plane ingress endpoint enabled and ready; even then, it rejects trigger-input uploads with `UNIMPLEMENTED`.

Signed URLs, log streaming, structured I/O retrieval, and auxiliary UI proxying are handled by the `dataproxy` service that runs in the data plane (see [Data plane](./data-plane#components)). The control plane also runs a `dataproxy` service, which serves these requests for organizations where no cluster has a data-plane ingress endpoint enabled and ready, and serves tracked-run data from the control plane's own bucket. For the customer-data request path, see [Network architecture](./network).
