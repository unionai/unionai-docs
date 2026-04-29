---
title: Two-plane separation
weight: 1
variants: -flyte +union
---

# Two-plane separation

Union.ai's architecture is divided into two distinct planes: a **control plane** hosted by Union.ai on AWS, and a **data plane** that runs on the customer's own Kubernetes cluster within their cloud account.

## Control plane

The control plane handles workflow orchestration, user management, and the web interface. It stores only the metadata required for these functions; bulk customer data payloads are stored as URI references rather than inline. See [Control plane](./control-plane) for components and infrastructure.

## Data plane

The data plane is where all computation and data handling occurs. It runs entirely within the customer's cloud account, on infrastructure the customer controls (or, in the BYOC model, infrastructure that Union.ai manages on the customer's behalf within the customer's account). It is protected by the customer's IAM policies. See [Data plane](./data-plane) for components, Kubernetes security, and IAM.

## Blast radius

This separation limits the blast radius of a control plane security incident. A compromised control plane would only expose what is stored or proxied through it: task metadata in its databases, inline data transiting memory during active requests, and log stream content. It could not expose bulk customer data, which is signed and accessed directly on the data plane.

For the full classification of what data lives in each plane, what transits control plane memory, and how each pathway is protected, see [Data classification and residency](../data-protection/classification-and-residency). For network paths between the planes, see [Network architecture](./network).

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

5. Enable VPC Flow Logs in the customer's cloud account and analyze traffic during workflow execution. Bulk data transfers (files, DataFrames, code bundles) should flow directly between task pods and the customer's object store via presigned URLs. Structured task I/O and log streams will transit the Cloudflare Tunnel to the control plane.

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
