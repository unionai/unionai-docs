---
title: Control plane
weight: 2
variants: -flyte +union
---

# Control plane

The control plane is the Union.ai-hosted component that orchestrates task execution, manages user access, and provides the web interface. It runs on AWS infrastructure managed by Union.ai and is covered by Union.ai's SOC 2 Type II certification.

## What it stores

The control plane uses three databases (PostgreSQL + 2x Cassandra/Scylla) to store the information required for orchestration. This information falls into three categories:

**Orchestration metadata** (stored as database columns): task, run, action, and trigger identifiers (including task function names and run names), action state (phase, timestamps, cluster assignment), user identity (who created and deployed each run), and scheduling configuration. This is pure operational data.

**Task and run definitions** (stored as serialized protobuf blobs): each run submission includes a full TaskSpec containing the task's container image, command, typed interface, resource requirements, and security context. A full TaskSpec is stored on every run submission, content-addressed by digest. RunSpec blobs carry environment variables, security context, labels, and annotations. Trigger specs carry default input values for scheduled runs. All data in PostgreSQL is encrypted at rest (AWS RDS AES-256/KMS).

The following table enumerates the fields inside TaskSpec blobs. Reviewers can verify these against the open-source protobuf definitions in the [flyte-sdk repository](https://github.com/flyteorg/flyte-sdk).

| Field | Classification |
|-------|----------------|
| Input/output parameter names and types | Structural metadata |
| Container image URL, command, args | Structural metadata |
| Secret group/key references (not values) | Structural metadata |
| IAM role ARNs, K8s service account names | Structural metadata |
| **Environment variables** | **Potentially sensitive** |
| **Default input literal values** | **Potentially sensitive** |
| **SQL query statements** | **Potentially sensitive** |
| **Full Kubernetes pod spec** (arbitrary JSON) | **Potentially sensitive** |
| **Plugin configuration** (arbitrary JSON) | **Potentially sensitive** |
| **Config key-value pairs** | **Potentially sensitive** |
| **OAuth2 client IDs and IDP endpoints** | **Potentially sensitive** |

**Error and event information**: error messages from task executions (which may contain customer data from Python tracebacks) and Kubernetes event messages are persisted via the events system. Plugin state (opaque bytes specific to the executor plugin) is stored per action attempt.

The control plane does **not** store bulk customer data payloads (files, directories, DataFrames, code bundles, container images, or inter-task artifacts). When it references such data, it stores only URIs pointing to objects in the customer's object store (for example, `s3://customer-bucket/org/project/domain/run/action/output.pb`).

Certain inline data does transit control plane memory during request processing: structured task inputs on every run submission (`UploadInputs`, up to 10 MB), structured task inputs and outputs on every retrieval (`GetActionData`, up to 20 MiB), secret values during create/update, and execution log streams. This data is encrypted in transit, exists in memory only for the request duration, and is not persisted, cached, or logged.

With full access to the control plane databases, an attacker would obtain task definitions (including the potentially sensitive fields listed above), error messages, and execution metadata. They would not obtain bulk data payloads, which reside in the customer's object store. The blast radius is further limited by the transient nature of inline data (not persisted) and the write-only design of the secrets API (values cannot be read back).

## Infrastructure

The control plane runs on AWS with multi-AZ redundancy to ensure high availability. Its primary data store is managed PostgreSQL (AWS RDS) with AES-256 encryption at rest and automated failover across availability zones. The database is isolated within a VPC with restricted security groups that permit access only from control plane application services.

TLS terminates at the edge, and all internal communication occurs over encrypted channels. Automated backups run on a defined schedule with point-in-time recovery capability. Union.ai maintains disaster recovery procedures and applies security patches on a regular cadence. The SOC 2 Type II report covers the availability, security, and operational controls of this infrastructure.

## Components

The control plane consists of several services, each responsible for a specific aspect of orchestration:

**Admin** serves as the UI and API gateway. It handles user-facing requests from both the web console and CLI tools, enforces authentication and authorization, and exposes the ConnectRPC (gRPC-Web) API.

**Queue Service** is responsible for scheduling TaskActions. When a run requires a task to execute, the Queue Service determines the target data plane cluster and creates the appropriate TaskAction.

**Actions Service** receives state transitions from data plane Executors. As tasks start, succeed, fail, or retry, the Actions Service records these transitions and updates the run state.

**Cluster Service** maintains cluster health information and handles DNS reconciliation. It monitors the status of registered data plane clusters and ensures that routing information remains current.

**DataProxy** is the control plane's data-handling gateway. It serves several functions: proxying structured task inputs to the data plane object store on run submission (`UploadInputs`), fetching structured task inputs and outputs on retrieval (`GetActionData`), streaming execution logs from the data plane to clients, and brokering presigned URL signing requests for bulk data access. For `UploadInputs` and `GetActionData`, the full data payload (up to 10-20 MiB) transits DataProxy's memory as plaintext, encrypted in transit on both sides. Log streams pass through without content filtering or redaction. In all cases, the data is not persisted, cached, or logged by DataProxy.

## Verification

### What it stores

**Reviewer focus:** Confirm that the control plane databases contain orchestration metadata and task definitions as described above, but no bulk customer data payloads. Verify that task definitions do not contain unintended sensitive content beyond the fields documented here.

**How to verify:**

1. The task definition schema is derived from the open-source Flyte protobuf definitions in the [flyte-sdk repository](https://github.com/flyteorg/flyte-sdk). Review the `TaskTemplate` and `RunSpec` protobuf schemas and compare them to the field enumeration table above to confirm that the fields stored match the documented classifications.

2. Query the control plane API for a completed execution:

   ```bash
   uctl get execution <execution-id> -o json
   ```

   The response should contain identifiers, phase, timestamps, URIs, and error information. Bulk data content (file contents, DataFrame payloads) should not appear inline -- only URI references to the customer's object store.

3. Query a task definition and inspect the fields present:

   ```bash
   uctl get task <task-name> -o json
   ```

   The response will include task definition fields (container spec, typed interface, resource requirements). Check whether environment variables, default input values, or other potentially sensitive fields from the table above are present, and confirm they match what you expect for that task.

### Infrastructure

**Reviewer focus:** Confirm that the control plane infrastructure meets stated security and availability properties.

**How to verify:**

- Request the current SOC 2 Type II report from Union.ai, which covers control plane infrastructure controls including encryption, access management, availability, and change management.
- Review the [Union.ai Trust Center](https://trust.union.ai) for current compliance certifications and security documentation.
