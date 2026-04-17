---
title: Two-plane separation
weight: 1
variants: -flyte +union
---

# Two-plane separation

Union.ai's architecture is divided into two distinct planes: a **control plane** hosted by Union.ai on AWS, and a **data plane** that runs on the customer's own Kubernetes cluster within their cloud account. This separation is the foundational security property of the system.

The control plane handles workflow orchestration, user management, and the web interface. It stores only the metadata required for these functions -- task definitions, execution state, scheduling information, and user records. The control plane never stores customer data payloads. When it references data, it stores only URIs pointing to objects in the customer's object store, never the data itself.

The data plane is where all computation and data handling occurs. It runs entirely within the customer's cloud account on infrastructure the customer controls (or, in the BYOC model, infrastructure that Union.ai manages on the customer's behalf within the customer's account). All customer data -- inputs, outputs, intermediate artifacts, logs, and model weights -- resides in the data plane.

When data must be surfaced to a client (for example, when a user views task outputs in the UI), the control plane either proxies a signing request to generate a presigned URL or relays a data stream without persisting it. In both cases, the actual data travels directly between the client and the customer's object store. The control plane acts as a broker, not a data store.

This separation means that even in the event of a full control plane compromise, customer data payloads remain in the customer's cloud account, protected by the customer's own IAM policies and network controls. The control plane simply does not have the data to leak.

For details on what each plane contains and how they communicate, see [Control plane](./control-plane), [Data plane](./data-plane), and [Network architecture](./network).

## Verification

### Data residency (Critical)

**Reviewer focus:** Confirm that customer data resides exclusively in the customer's cloud account and that the control plane holds only metadata references.

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
