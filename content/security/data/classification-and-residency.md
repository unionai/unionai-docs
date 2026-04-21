---
title: Data classification and residency
weight: 1
variants: -flyte +union
---

# Data classification and residency

## Data classification

Every data type in the Union.ai platform is classified by its residency and access pattern. This classification determines where data is stored and how it is accessed.

| Classification | Data types | At rest | In transit | Enters CP memory? |
|---|---|---|---|---|
| Bulk Customer Data | Files, directories, DataFrames, code bundles, container images, reports | Customer infrastructure (S3 SSE / GCS / Azure SSE) | HTTPS via presigned URL | **No** -- never enters control plane |
| Inline Customer Data | Structured task inputs/outputs, secret values (during creation), execution log streams | Customer infrastructure (S3 SSE / GCS / Azure SSE; cloud secret managers) | TLS (client→CP) + TLS+mTLS+tunnel (CP→DP) | **Yes** -- plaintext in memory, not persisted/cached/logged |
| Orchestration Metadata | Task definitions (including env vars, default values, SQL, pod specs), run/action state, error messages, trigger specs | Control plane databases (PostgreSQL AES-256/KMS; Cassandra) | TLS (API) + TLS+mTLS+tunnel (events) | **Yes** -- read from DB into memory for API responses |
| Platform Metadata | User identity/RBAC records, cluster records | Control plane databases (PostgreSQL AES-256/KMS) | TLS (API) | **Yes** -- read from DB into memory for API responses |

**Bulk customer data** -- files, directories, DataFrames, code bundles, container images, and reports -- is stored exclusively in the customer's infrastructure and never enters the control plane. These objects are accessed via presigned URLs.

**Inline customer data** -- structured task inputs and outputs, secret values during creation/update, and execution log streams -- is stored at rest in the customer's infrastructure but transits control plane memory during request processing. This data is encrypted in transit (TLS + Cloudflare Tunnel), exists as plaintext in control plane memory only for the duration of each request, and is not persisted, cached, or logged in the control plane.

**Orchestration metadata** is stored in the control plane databases (encrypted at rest). This includes task definitions, which contain structural information (container image references, typed interfaces) and fields that may be customer-sensitive: environment variables, default input literal values, SQL query statements, Kubernetes pod specs, plugin configuration, and config key-value pairs. Error messages from task executions (which may contain data from Python tracebacks) are also stored. A full task definition (TaskSpec) is stored on every run submission.

## Data residency

All customer data resides in the customer's own cloud account and region. The customer chooses the region for their data plane deployment, and all data plane resources -- object storage, container registry, secrets backend, log aggregator, and compute -- are provisioned within that region.

The control plane is available in the following regions: US West (us-west-2), US East (us-east-2), EU West-1 (Ireland), EU West-2 (London), and EU Central (eu-central-1). No bulk customer data is replicated to or cached in Union.ai infrastructure. Inline data (structured task I/O, secret values during creation, log streams) transits control plane memory during request processing but is not persisted. This transit occurs through the control plane region, so customers should select a control plane region consistent with their data residency requirements. For EU-deployed data planes using an EU control plane region, all data -- both at rest and in transit -- stays within the EU, supporting GDPR data residency requirements.

For details on the architectural separation that enforces these residency guarantees, see [Two-plane separation](../architecture/two-plane-separation).

## Verification

### Data classification (Critical)

**Reviewer focus:** Confirm that each data type resides where the classification table claims, and that no customer data payloads appear in the control plane.

**How to verify:**

Run a workflow with recognizable data (e.g., a known string or file), then verify the location of each data type:

1. **Inputs/outputs** -- confirm they are in the customer's object store:

   ```bash
   aws s3 ls s3://<customer-bucket>/org/project/domain/run-name/action-name/
   ```

2. **Code bundle** -- confirm it is in the customer's object store:

   ```bash
   aws s3 ls s3://<customer-bucket>/org/project/domain/code-bundles/
   ```

3. **Container image** -- confirm it is in the customer's container registry:

   ```bash
   aws ecr describe-images --repository-name <repo> --region <region>
   ```

4. **Logs** -- confirm they are in the customer's log aggregator:

   ```bash
   aws logs get-log-events --log-group-name <group> --log-stream-name <stream>
   ```

5. **Secrets** -- confirm they are in the customer's secrets backend:

   ```bash
   aws secretsmanager list-secrets --region <region>
   ```

6. **Task spec metadata** -- confirm it contains only metadata, stored in the control plane:

   ```bash
   uctl get task <task-name> -o json
   ```

   The response should contain resource requirements, typed interfaces, and container image references -- no data content.

7. **Run metadata** -- confirm it contains only metadata, stored in the control plane:

   ```bash
   uctl get execution <execution-id> -o json
   ```

   The response should contain phase, timestamps, URIs, and error messages -- no data content.

### Data residency (Critical -- especially for EU/regulated deployments)

**Reviewer focus:** Confirm that all data plane resources reside in the customer's chosen region and that no customer data is stored outside that region.

**How to verify:**

1. Confirm the object store region:

   ```bash
   aws s3api get-bucket-location --bucket <customer-bucket>
   ```

   The output should match the customer's chosen deployment region.

2. Verify all data plane resources in the cloud console -- compute, storage, registry, secrets, and log aggregator should all be in the same region.

3. Confirm the cluster region via the Union.ai API:

   ```bash
   uctl get cluster
   ```

   The cluster region should match the customer's chosen deployment region.
