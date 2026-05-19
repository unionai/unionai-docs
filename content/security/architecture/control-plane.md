---
title: Control plane
weight: 2
variants: -flyte +union
---

# Control plane

The control plane is the Union.ai-hosted component that orchestrates task execution, manages user access, and provides the API surface. It runs on AWS infrastructure managed by Union.ai and is covered by Union.ai's SOC 2 Type II certification.

Under Zero Trust, the control plane handles only orchestration metadata. Customer data -- workflow inputs and outputs, code bundles, secret values, logs, reports, and auxiliary UI traffic -- never transits the control plane in any form, not even transiently in memory. Those requests are served directly from the data plane through the [Direct-to-DataPlane tunnel](./network).

## What it stores

The control plane stores the information required for orchestration. All of it is metadata; none of it is customer data payload.

- **Orchestration metadata**: identifiers, action state (phase, timestamps, cluster assignment), user profiles, scheduling configuration, and the RBAC graph.
- **Task and run definitions**: each run submission includes a full TaskSpec (container image, typed interface, resource requirements, security context) and a RunSpec (environment variables, labels, annotations). Trigger specs carry default input values for scheduled runs.
- **Error and event information**: error messages from task executions (which may contain customer data from Python tracebacks), Kubernetes event messages, and per-attempt plugin state.

It stores only **URIs** pointing into the customer's object store for any payload reference (for example, `s3://customer-bucket/org/project/domain/run/action/output.pb`); the payloads themselves stay in the customer's object store.

For the full classification of what is and isn't stored in the control plane and the sensitive fields that may appear in task definitions, see [Data classification and residency](../data-protection/classification-and-residency).

## Infrastructure

The control plane runs on AWS with multi-AZ redundancy to ensure high availability. It uses managed cloud database services for orchestration metadata, task/run definitions, execution events, and error messages. All backends are encrypted at rest and isolated within a VPC with restricted security groups that permit access only from control plane application services. See [Encryption](../data-protection/encryption) for at-rest encryption details by data type.

TLS terminates at the edge, and all internal communication occurs over encrypted channels. Automated backups run on a defined schedule with point-in-time recovery capability. Union.ai maintains disaster recovery procedures and applies security patches on a regular cadence. The SOC 2 Type II report covers the availability, security, and operational controls of this infrastructure.

## Capabilities

The control plane exposes the following capabilities:

- **API and UI gateway** -- an authenticated HTTPS API and web console for users, the SDK, and the CLI. All requests are subject to authentication and RBAC enforcement before any orchestration logic runs.
- **Scheduling and execution tracking** -- schedules TaskActions across registered data plane clusters and records execution state (phase transitions, timestamps, errors) reported back from the data plane.
- **Cluster registry** -- maintains the inventory of registered data plane clusters and their health.
- **Cluster selection** -- exposes the `SelectCluster` RPC that clients (SDK / UI) call to resolve which data plane cluster handles a given customer-data request. The control plane returns the per-cluster tunnel domain (or, under Sovereign Data Plane, internal LB hostname); the client then dispatches the data-path request directly to that cluster. The control plane does not participate in the data path itself.

The control plane has no data-gateway role under Zero Trust. The pre-ZT `dataproxy` service that handled signed URLs, log streaming, structured I/O, and auxiliary UI proxying has been relocated to the data plane (see [Data plane](./data-plane#components)). See [Data flow](../data-protection/data-flow) for the new request path.

