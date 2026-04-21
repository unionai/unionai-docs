---
title: Two-plane separation
weight: 1
variants: -flyte +union
---

# Two-plane separation

Union.ai's architecture is divided into two distinct planes: a **control plane** hosted by Union.ai on AWS, and a **data plane** that runs on the customer's own Kubernetes cluster within their cloud account. This separation is the foundational security property of the system.

The control plane handles workflow orchestration, user management, and the web interface. It stores orchestration metadata -- task definitions, execution state, scheduling information, and user records -- encrypted at rest in its databases. Task definitions include structural information (container image references, typed interfaces) and fields that may be customer-sensitive (environment variables, default input values, SQL statements, Kubernetes pod specs, and plugin configuration). When the control plane references bulk data (inputs, outputs, artifacts), it stores only URIs pointing to objects in the customer's object store.

The data plane is where all computation and data handling occurs. It runs entirely within the customer's cloud account on infrastructure the customer controls (or, in the BYOC model, infrastructure that Union.ai manages on the customer's behalf within the customer's account). All bulk customer data -- files, directories, DataFrames, code bundles, container images, and inter-task artifacts -- is stored exclusively in the data plane and never enters the control plane. These objects are uploaded and downloaded directly via presigned URLs.

Certain smaller inline data transits control plane memory during request processing: structured task inputs and outputs (protobuf literals, up to 10-20 MiB), secret values during creation and update, and execution log streams. This data is encrypted in transit (TLS + Cloudflare Tunnel), exists in control plane memory only for the duration of each request, and is not persisted, cached, or logged there. The control plane acts as a pass-through proxy for this data, not a store.

This separation limits the blast radius of a control plane security incident. Bulk data (files, DataFrames, code bundles, container images) is inaccessible from the control plane -- it resides entirely in the customer's cloud account, protected by the customer's IAM policies. A compromised control plane could expose: task definitions stored in its databases (including the potentially sensitive fields listed above), inline data transiting memory during active requests (bounded by size caps and request duration), and log stream content. It could not access bulk data, since presigned URLs are generated on the data plane.

For details on what each plane contains and how they communicate, see [Control plane](./control-plane), [Data plane](./data-plane), and [Network architecture](./network).

## Verification

### Data residency (Critical)

**Reviewer focus:** Confirm that bulk customer data resides in the customer's cloud account, that inline data transiting the control plane is not persisted, and that task definitions stored in the control plane databases do not contain unintended sensitive content.

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
