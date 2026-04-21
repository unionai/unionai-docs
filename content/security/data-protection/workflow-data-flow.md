---
title: Workflow data flow
weight: 5
variants: -flyte +union
---

# Workflow data flow

This page traces the security-relevant data movements at each stage of the workflow lifecycle: registration, execution, and result retrieval. Bulk data (files, DataFrames, code bundles, container images) stays in the customer's infrastructure at every stage. Smaller inline data (structured task inputs/outputs, secret values during creation, log streams) transits control plane memory during request processing but is not persisted there.

## Task deployment and run creation

When a run is created, the SDK serializes the full task specification (container image, resource requirements, typed interface, and all configuration) and sends it inline to the control plane along with the structured task inputs. The code bundle is uploaded directly to the customer's object store via a presigned PUT URL. Code never touches the control plane. The task specification is stored in the control plane databases (see [Control plane](../architecture/control-plane) for the full field enumeration).

The SDK sends structured task inputs to the control plane via `UploadInputs` (up to 10 MB). The control plane proxies the full input payload through its memory (encrypted in transit, plaintext in memory, not persisted) to the data plane object store via the Cloudflare Tunnel. Binary input artifacts (files, directories, DataFrames) are uploaded directly to the customer's object store via presigned URLs, bypassing the control plane. The control plane stores only the input URI, then enqueues the action to the data plane.

The Executor on the data plane creates a pod that reads inputs from and writes outputs back to the customer's object store. During workflow execution, inter-task I/O flows directly between task pods and the object store via IAM, with no control plane involvement. Secrets required by the task are injected into pods from the customer's secrets backend at runtime. Secret values do not traverse the control plane during execution. (Secret values do traverse the control plane during initial secret creation and updates, when the value is relayed through DataProxy to the data plane's secrets backend. See [Secrets management](./secrets).) The control plane receives phase transitions, status updates, and error messages from the Executor. Error messages may contain customer data from Python tracebacks.

For details on secrets injection, see [Secrets management](./secrets).

## Result retrieval

Once a run completes, its results are accessible through three channels, each with different data flow characteristics:

**Binary outputs, reports, and code bundles** are accessed via presigned URLs. The data flows directly from the customer's object store to the client and does not pass through the control plane.

**Structured outputs** (protobuf literals) are retrieved via `GetActionData`, which fetches the full output payload from the data plane object store through the control plane (encrypted in transit, plaintext in control plane memory during the request, not persisted). Both structured inputs and outputs are returned together, up to 20 MiB total.

**Logs** are streamed from the data plane through the Cloudflare Tunnel as a stateless relay. The control plane forwards the stream as plaintext in memory (encrypted in transit) without persisting or filtering the content.

**Metadata** (run status, phase transitions, timestamps, and error messages) is served directly from the control plane database.

For details on the two data flow patterns, see [Data flow](./data-flow).

## Verification

### End-to-end data flow

**Reviewer focus:** Confirm the data separation model at every stage: bulk data stays in the customer's infrastructure (presigned URLs), inline data transits the control plane transiently (not persisted), and task definitions stored in the control plane contain only expected fields.

**How to verify:**

**Step 1: Deployment and code bundle**

Run a workflow and observe where the code bundle is stored:

```bash
union run --remote my_task.py main
```

Verify that the code bundle is in the customer's bucket:

```bash
aws s3 ls s3://<customer-bucket>/org/project/domain/code-bundles/
```

The code bundle `.tgz` file should appear in the customer's own object store.

**Step 2: Execution**

Inspect the task pod to confirm it reads from customer infrastructure:

```bash
kubectl describe pod <task-pod> -n <workspace-namespace>
```

The pod description should show volumes mounted from customer S3, secrets from the customer's backend, and a non-root security context.

**Step 3: Retrieval**

Open browser developer tools (Network tab) and view the task's outputs in the Union.ai UI. Binary output artifacts (files, DataFrames) should be fetched via presigned URLs pointing to the customer's S3/GCS/Azure Blob endpoint. Structured outputs (protobuf literals) are fetched via the inline proxy through the control plane. Separately, confirm that the control plane API returns metadata and URI references:

```bash
uctl get execution <execution-id> -o json
```

The response should contain phase, timestamps, URIs, and task definition fields. Bulk data content should not appear inline.

**Step 4: Negative proof**

Search control plane audit logs for the recognizable data string used in the workflow. It should not appear. If VPC Flow Logs are enabled, bulk data transfers should flow directly between task pods and the customer's object store. Structured task I/O (up to 10-20 MiB) and log streams will transit the Cloudflare Tunnel as documented in [Data flow](./data-flow).
