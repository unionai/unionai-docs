---
title: Control plane
weight: 2
variants: -flyte +union
---

The control plane is the Union.ai-hosted component that orchestrates workflow execution, manages user access, and provides the web interface. It runs on AWS infrastructure managed by Union.ai and is covered by Union.ai's SOC 2 Type II certification.

## What it stores

The control plane stores only the metadata required for orchestration. This includes task definitions (container image references, resource requirements, and typed interfaces), run and action metadata (identifiers, phase transitions, timestamps, and error information), user identity and RBAC records, cluster configuration and health records, and trigger and schedule definitions.

The control plane does **not** store customer data payloads. When it needs to reference data, it stores URIs pointing to objects in the customer's object store (for example, `s3://customer-bucket/org/project/domain/run/action/output.pb`). The data itself never transits through or resides in the control plane.

This metadata-only design limits the blast radius of any control plane security incident. Even with full access to the control plane database, an attacker would obtain only workflow structure and scheduling information -- not the data those workflows process.

## Infrastructure

The control plane runs on AWS with multi-AZ redundancy to ensure high availability. Its primary data store is managed PostgreSQL (AWS RDS) with AES-256 encryption at rest and automated failover across availability zones. The database is isolated within a VPC with restricted security groups that permit access only from control plane application services.

TLS terminates at the edge, and all internal communication occurs over encrypted channels. Automated backups run on a defined schedule with point-in-time recovery capability. Union.ai maintains disaster recovery procedures and applies security patches on a regular cadence. The SOC 2 Type II report covers the availability, security, and operational controls of this infrastructure.

## Components

The control plane consists of several services, each responsible for a specific aspect of orchestration:

**Admin** serves as the UI and API gateway. It handles user-facing requests from both the web console and CLI tools, enforces authentication and authorization, and exposes the ConnectRPC (gRPC-Web) API.

**Queue Service** is responsible for scheduling TaskActions. When a workflow execution reaches a point where a task must run, the Queue Service determines the target data plane cluster and creates the appropriate TaskAction custom resource.

**State Service** receives state transitions from data plane Executors. As tasks start, succeed, fail, or retry, the State Service records these transitions and updates the execution graph.

**Cluster Service** maintains cluster health information and handles DNS reconciliation. It monitors the status of registered data plane clusters and ensures that routing information remains current.

**DataProxy** provides a streaming relay for logs and metrics. When a user views live logs in the UI, DataProxy streams them from the data plane without persisting the content. It also handles presigned URL signing requests, brokering access to data in the customer's object store.

## Verification

### What it stores (Critical)

**Reviewer focus:** Confirm that the control plane database contains only orchestration metadata and no customer data payloads.

**How to verify:**

1. The metadata schema is derived from the open-source Flyte protobuf definitions in the [flyte-sdk repository](https://github.com/flyteorg/flyte-sdk). Review the protobuf schemas to confirm that execution and task metadata messages contain only identifiers, phase enums, timestamps, URIs, and typed interface definitions -- no arbitrary data payload fields.

2. Query the control plane API for a completed execution:

   ```bash
   uctl get execution <execution-id> -o json
   ```

   Inspect the full JSON response. Fields should include `id`, `spec`, `closure` (containing `phase`, `startedAt`, `duration`, `outputs` as a URI reference), and similar metadata. No field should contain inline data content.

3. For additional confidence, run a workflow that processes sensitive test data and repeat the above query. Confirm that the sensitive content does not appear anywhere in the API response.

### Infrastructure (Medium)

**Reviewer focus:** Confirm that the control plane infrastructure meets stated security and availability properties.

**How to verify:**

- Request the current SOC 2 Type II report from Union.ai, which covers control plane infrastructure controls including encryption, access management, availability, and change management.
- Review the [Union.ai Trust Center](https://trust.union.ai) for current compliance certifications and security documentation.
