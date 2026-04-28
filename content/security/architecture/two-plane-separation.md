---
title: Two-plane separation
weight: 1
variants: -flyte +union
---

# Two-plane separation

Union.ai's architecture is divided into two distinct planes: a **control plane** hosted by Union.ai on AWS, and a **data plane** that runs on the customer's own Kubernetes cluster within their cloud account.

The control plane handles workflow orchestration, user management, and the web interface.
It stores task metadata, execution state and scheduling information, along with user profiles (name and email pulled from the configured identity provider) and authentication credentials. All of these are encrypted at rest in its databases.

Task metadata includes the task function name, input and output parameter types, plug-in configuration, and default input values. It also stores one of three execution targets per task: a container image reference (with environment variables), a Kubernetes pod specification, or a SQL query string.

When the control plane references bulk data (inputs, outputs, artifacts), it stores only URIs pointing to objects in the customer's object store.

The data plane is where all computation and data handling occurs. It runs entirely within the customer's cloud account on infrastructure the customer controls (or, in the BYOC model, infrastructure that Union.ai manages on the customer's behalf within the customer's account). All bulk customer data like files, directories, DataFrames, code bundles, container images, and inter-task artifacts are stored exclusively in the data plane and never enter the control plane. These objects are uploaded and downloaded directly via presigned URLs and are not visible to the control plane or to Union employees.

Certain smaller inline data transits control plane memory during request processing: structured task inputs and outputs (protobuf literals, up to 10-20 MiB), secret values during creation and update, and execution log streams. This data is encrypted in transit (TLS + Cloudflare Tunnel), exists in control plane memory only for the duration of each request, and is not persisted, cached, or logged there. The control plane acts as a pass-through proxy for this data, not a store.

This separation limits the blast radius of a control plane security incident. Bulk data (files, DataFrames, code bundles, container images) is inaccessible from the control plane. It resides entirely in the customer's cloud account, protected by the customer's IAM policies. A compromised control plane would only expose: task metadata stored in its databases, inline data transiting memory during active requests, and log stream content. It could not expose bulk data, since presigned URLs are generated on the data plane.

For details on what each plane contains and how they communicate, see [Control plane](./control-plane), [Data plane](./data-plane), and [Network architecture](./network).

## Verification

### Data residency

**Reviewer focus:** Confirm that bulk customer data resides in the customer's cloud account, that inline data transiting the control plane is not persisted, and that task definitions stored in the control plane databases do not contain unintended sensitive content.

**How to verify:**

1. Run a workflow that produces known output data (e.g., a task that writes a DataFrame or file).

2. Confirm data is in the customer's bucket:

   ```bash
   aws s3 ls s3://<customer-bucket>/org/project/domain/run-name/action-name/
   ```

   The output artifacts should appear here, in the customer's own object store.

3. Query the control plane API and confirm that execution responses contain metadata and URI references, not inline data payloads:

   ```bash
   uctl get execution <execution-id> -o json
   ```

   The response should contain URIs (`s3://` or `gs://` references), phase information, timestamps, and error messages. Task definition fields (env vars, default values, resource specs) will be present, as these are stored in the control plane as documented in [Control plane](./control-plane).

4. Open the Union.ai UI, navigate to the execution, and use browser developer tools (Network tab) to inspect requests when viewing outputs. Binary output artifacts (files, DataFrames) should be fetched via presigned URLs resolving to the customer's S3/GCS/Azure Blob endpoint. Structured outputs (protobuf literals) are fetched via the inline proxy pattern through the control plane.

5. Enable VPC Flow Logs in the customer's cloud account and analyze traffic during workflow execution. Bulk data transfers (files, DataFrames, code bundles) should flow directly between task pods and the customer's object store via presigned URLs. Structured task I/O (up to 10-20 MiB per request) and log streams will transit the Cloudflare Tunnel to the control plane.

### Customer authority over data

**Reviewer focus:** Confirm that bulk data is unreadable without the customer's encryption keys, regardless of who holds a presigned URL.

**How to verify:**

1. From a successful workflow run, capture a presigned URL for an output artifact (Union.ai UI, browser developer tools → Network tab, or via `uctl`).

2. Confirm the URL fetches the artifact:

   ```bash
   curl -o /tmp/output "<presigned-url>"
   ```

3. Disable the customer-managed key that encrypts the bucket:

   ```bash
   aws kms disable-key --key-id <bucket-kms-key-id>
   ```

   On GCP, disable the CMEK key version protecting the bucket. On Azure, disable the customer-managed key in Key Vault.

4. Re-fetch the same URL (or issue a fresh one). The request should fail with `KMS.DisabledException` (AWS) or the equivalent. Re-enable the key to restore access.

The presigned URL itself is unchanged and still authentic. The data behind it is opaque without the customer's key — proof that customer-controlled keys are the final gate on bulk data access, independent of who can issue URLs.
