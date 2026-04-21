---
title: Two-plane separation
weight: 1
variants: -flyte +union
---

# Two-plane separation

Union.ai's architecture is divided into two distinct planes: a **control plane** hosted by Union.ai on AWS, and a **data plane** that runs on the customer's own Kubernetes cluster within their cloud account. This separation is the foundational security property of the system.

The control plane handles workflow orchestration, user management, and the web interface. It stores only the metadata required for these functions -- task definitions, execution state, scheduling information, and user records. The control plane never stores customer data payloads. When it references data, it stores only URIs pointing to objects in the customer's object store, never the data itself.

> [!WARNING]
> **Audit finding (ref #7, #11):** "The control plane never stores customer data payloads" needs qualification. The v2 control plane databases store task/run/action/trigger identifiers (including task function names, run names), user identity, and execution state as explicit columns. TaskSpec blobs stored across three databases (PostgreSQL + 2x Cassandra) contain environment variables, default input literal values, SQL query statements, K8s pod specs, arbitrary plugin configuration, and config key-value pairs. RunSpec blobs contain additional env vars and security context. Trigger specs contain default literal values (replacing v1 launch plans). Error messages from task executions and Kubernetes event messages are persisted via the events system. In v2, the full TaskSpec is sent inline on every run — these fields transit and are stored on every run submission. PostgreSQL data is encrypted at rest (AWS RDS AES-256/KMS); Cassandra encryption depends on the managed service configuration.

The data plane is where all computation and data handling occurs. It runs entirely within the customer's cloud account on infrastructure the customer controls (or, in the BYOC model, infrastructure that Union.ai manages on the customer's behalf within the customer's account). All customer data -- inputs, outputs, intermediate artifacts, logs, and model weights -- resides in the data plane.

> [!WARNING]
> **Audit finding (ref #3, #4, #5):** "All customer data resides in the data plane" is true for data at rest but incomplete. Structured task inputs transit control plane memory on every run submission via `UploadInputs` (up to 10 MB). Structured task inputs AND outputs transit control plane memory on every retrieval via `GetActionData` (up to 20 MiB). Secret values transit control plane memory during Create/Update operations. Execution log streams pass through control plane memory unredacted. In all these cases the data is transient (not persisted, not logged, not cached) and encrypted in transit, but it does exist in Union.ai process memory during request processing.

When data must be surfaced to a client (for example, when a user views task outputs in the UI), the control plane either proxies a signing request to generate a presigned URL or relays a data stream without persisting it. In both cases, the actual data travels directly between the client and the customer's object store. The control plane acts as a broker, not a data store.

> [!NOTE]
> **Audit finding (ref #3):** "The actual data travels directly between the client and the customer's object store" is true for binary artifacts (files, directories, DataFrames, code bundles) which use the signed URL path. However, structured task I/O (protobuf literals) is proxied through control plane memory via `UploadInputs` and `GetActionData` -- the data does not travel directly in those cases. The distinction is by data type, not by size.

This separation means that even in the event of a full control plane compromise, customer data payloads remain in the customer's cloud account, protected by the customer's own IAM policies and network controls. The control plane simply does not have the data to leak.

> [!WARNING]
> **Audit finding (ref #3, #7):** "The control plane simply does not have the data to leak" overstates the separation. A compromised control plane could intercept structured task I/O during `UploadInputs`/`GetActionData` processing, secret values during Create/Update relay, and log streams during streaming. Additionally, the control plane databases contain TaskSpec and RunSpec blobs with potentially sensitive fields (env vars, default values, SQL statements, K8s pod specs, plugin configuration). In v2, the full TaskSpec is stored on every run submission. A full CP compromise would expose this data. The blast radius is limited by: transient residence (no persistence of I/O data), size caps (10-20 MiB), and the fact that binary artifacts (files, DataFrames, code bundles) genuinely bypass the CP via signed URLs.

For details on what each plane contains and how they communicate, see [Control plane](./control-plane), [Data plane](./data-plane), and [Network architecture](./network).

## Verification

### Data residency (Critical)

**Reviewer focus:** Confirm that customer data resides exclusively in the customer's cloud account and that the control plane holds only metadata references.

> [!NOTE]
> **Audit finding (ref #3, #7):** This verification step should also check for data that transits the control plane transiently (structured I/O via `UploadInputs`/`GetActionData`) and for potentially sensitive content in TaskSpec blobs stored in the control plane databases (environment variables, default values, SQL statements, K8s pod specs).

**How to verify:**

1. Run a workflow that produces known output data (e.g., a task that writes a DataFrame or file).

2. Confirm data is in the customer's bucket:

   ```bash
   aws s3 ls s3://<customer-bucket>/org/project/domain/run-name/action-name/
   ```

   The output artifacts should appear here, in the customer's own object store.

3. Query the control plane API and confirm it returns only metadata:

   ```bash
   uctl get execution <execution-id> -o json
   ```

   The response should contain URIs, phase information, timestamps, and error messages -- but no data content. Look for `s3://` or `gs://` references rather than inline data.

4. Open the Union.ai UI, navigate to the execution, and use browser developer tools (Network tab) to inspect requests when viewing outputs. Presigned URL requests should resolve to the customer's S3/GCS/Azure Blob endpoint, not to a Union.ai domain.

5. (Advanced) Enable VPC Flow Logs in the customer's cloud account and analyze traffic during workflow execution. Data-sized transfers should flow between task pods and the customer's object store. There should be no data-sized transfers to Union.ai IP ranges -- only small metadata-sized traffic over the Cloudflare Tunnel.
