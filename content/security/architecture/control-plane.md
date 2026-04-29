---
title: Control plane
weight: 2
variants: -flyte +union
---

# Control plane

The control plane is the Union.ai-hosted component that orchestrates task execution, manages user access, and provides the web interface. It runs on AWS infrastructure managed by Union.ai and is covered by Union.ai's SOC 2 Type II certification.

## What it stores

The control plane uses databases to store the information required for orchestration:

- **Orchestration metadata**: identifiers, action state (phase, timestamps, cluster assignment), user profiles, and scheduling configuration.
- **Task and run definitions**: each run submission includes a full TaskSpec (container image, typed interface, resource requirements, security context) and a RunSpec (environment variables, labels, annotations). Trigger specs carry default input values for scheduled runs.
- **Error and event information**: error messages from task executions (which may contain customer data from Python tracebacks), Kubernetes event messages, and per-attempt plugin state.

The control plane does not store bulk customer data payloads. When it references such data it stores only URIs pointing to objects in the customer's object store (for example, `s3://customer-bucket/org/project/domain/run/action/output.pb`).

For the full classification of what is and isn't stored in the control plane, the sensitive fields that may appear in task definitions, and how inline data (structured I/O, secret values during creation, log streams) transits control plane memory without being persisted, see [Data classification and residency](../data-protection/classification-and-residency).

## Infrastructure

The control plane runs on AWS with multi-AZ redundancy to ensure high availability. It uses managed cloud database services for orchestration metadata, task/run definitions, execution events, and error messages. All backends are encrypted at rest and isolated within a VPC with restricted security groups that permit access only from control plane application services. See [Encryption](../data-protection/encryption) for at-rest encryption details by data type.

TLS terminates at the edge, and all internal communication occurs over encrypted channels. Automated backups run on a defined schedule with point-in-time recovery capability. Union.ai maintains disaster recovery procedures and applies security patches on a regular cadence. The SOC 2 Type II report covers the availability, security, and operational controls of this infrastructure.

## Components

The control plane consists of several services, each responsible for a specific aspect of orchestration:

**Admin** serves as the UI and API gateway. It handles user-facing requests from both the web console and CLI tools, enforces authentication and authorization, and exposes the HTTPS API.

**Queue Service** is responsible for scheduling TaskActions. When a run requires a task to execute, the Queue Service determines the target data plane cluster and creates the appropriate TaskAction.

**Actions Service** receives state transitions from data plane Executors. As tasks start, succeed, fail, or retry, the Actions Service records these transitions and updates the run state.

**Cluster Service** maintains cluster health information and handles DNS reconciliation. It monitors the status of registered data plane clusters and ensures that routing information remains current.

**DataProxy** is the control plane's data-handling gateway. It proxies structured task inputs and outputs between clients and the data plane object store, streams execution logs from the data plane to clients, and brokers presigned URL signing requests for bulk data access. See [Data flow](../data-protection/data-flow) for what these pathways carry and how data is handled in transit.

## Verification

### What it stores

**Reviewer focus:** Confirm that the control plane databases contain orchestration metadata and task definitions as described above, but no bulk customer data payloads. Verify that task definitions do not contain unintended sensitive content beyond the fields documented here.

**How to verify:**

1. The task definition schema is derived from the open-source Flyte protobuf definitions in the [flyte-sdk repository](https://github.com/flyteorg/flyte-sdk). Review the `TaskTemplate` and `RunSpec` protobuf schemas and compare them to the field enumeration in [Data classification and residency](../data-protection/classification-and-residency) to confirm that the fields stored match the documented classifications.

2. Query the control plane API for a completed execution:

   ```bash
   uctl get execution <execution-id> -o json
   ```

   The response should contain identifiers, phase, timestamps, URIs, and error information. Bulk data content (file contents, DataFrame payloads) should not appear inline; only URI references to the customer's object store should be present.

3. Query a task definition and inspect the fields present:

   ```bash
   uctl get task <task-name> -o json
   ```

   The response will include task definition fields (container spec, typed interface, resource requirements). Check whether environment variables, default input values, or other potentially sensitive fields documented in [Data classification and residency](../data-protection/classification-and-residency) are present, and confirm they match what you expect for that task.

### Infrastructure

**Reviewer focus:** Confirm that the control plane infrastructure meets stated security and availability properties.

**How to verify:**

- Request the current SOC 2 Type II report from Union.ai, which covers control plane infrastructure controls including encryption, access management, availability, and change management.
- Review the [Union.ai Trust Center](https://trust.union.ai) for current compliance certifications and security documentation.
