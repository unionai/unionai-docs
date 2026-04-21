---
title: Workflow data flow
weight: 5
variants: -flyte +union
---

# Workflow data flow

This page traces the security-relevant data movements at each stage of the workflow lifecycle: registration, execution, and result retrieval. At every stage, customer data remains in the customer's infrastructure while only metadata passes through the control plane.

> [!WARNING]
> **Audit finding (ref #3, #4, #5):** "Only metadata passes through the control plane" is not accurate. Structured task inputs pass through control plane memory on run submission. Structured task inputs and outputs pass through on retrieval. Secret values pass through on create/update. Execution logs stream through unredacted. See the detailed findings below for each stage.

## Task registration

The SDK serializes the task specification -- container image reference, resource requirements, and typed interface -- into a protobuf message and sends it to the control plane. The code bundle is uploaded directly to the customer's object store via a presigned PUT URL. The code never touches the control plane. Only the specification metadata, including the object store URI pointing to the code bundle, is stored in the control plane database.

For details on the presigned URL mechanism, see [Data flow](./data-flow).

## Run creation and execution

When a run is created, the SDK serializes input data and uploads it to the customer's object store. Only the input URI is stored in the control plane. The control plane then enqueues the action to the data plane via the Cloudflare Tunnel.

> [!WARNING]
> **Audit finding (ref #3):** "The SDK serializes input data and uploads it to the customer's object store" is incorrect. The SDK sends structured task inputs to the control plane via `UploadInputs`. The control plane then proxies the full input payload through its memory to the data plane object store via the Cloudflare Tunnel. The inputs do not go directly from the SDK to the object store. Only binary artifacts (files, directories, DataFrames) are uploaded directly via presigned URLs. In-cluster inter-task I/O during workflow execution does go directly to the object store via IAM, bypassing the control plane.

The Executor on the data plane creates a pod that reads inputs from and writes outputs back to the customer's object store. Secrets required by the task are injected into pods from the customer's secrets backend -- they never traverse the control plane during runtime. The control plane receives only phase transitions and status updates (started, succeeded, failed, retrying) from the Executor, not the data being processed.

> [!NOTE]
> **Audit finding (ref #4):** "Secrets never traverse the control plane during runtime" is correct -- secret consumption at runtime is entirely within the data plane. However, secret values do traverse the control plane during initial secret creation and updates, when the value is relayed through DataProxy to the data plane's secrets backend. The control plane also receives error messages (up to 4KB) from the Executor, which can contain customer data from Python tracebacks.

For details on secrets injection, see [Secrets management](./secrets).

## Result retrieval

Once a run completes, its results are accessible through three channels, each with different data flow characteristics:

**Outputs, reports, and code bundles** are accessed via presigned URLs. The data flows directly from the customer's object store to the client -- it does not pass through the control plane.

> [!WARNING]
> **Audit finding (ref #3):** This is true for reports, code bundles, and binary output artifacts (files, directories, DataFrames) which use presigned URLs. However, structured task outputs (protobuf literals) are retrieved via `GetActionData`, where the full output payload passes through control plane memory before being returned to the client.

**Logs** are streamed from the data plane through the Cloudflare Tunnel as a stateless relay. The control plane forwards the stream without persisting any content.

**Metadata** -- run status, phase transitions, timestamps, and error messages -- is served directly from the control plane database.

For details on the two data flow patterns, see [Data flow](./data-flow).

## Verification

### End-to-end data flow (Critical)

**Reviewer focus:** Confirm that customer data stays in the customer's infrastructure at every stage of the workflow lifecycle. This is the most important verification in this section -- it demonstrates the entire data separation model in action.

**How to verify:**

**Step 1 -- Registration:**

Run a workflow and observe where the code bundle is stored:

```bash
union run --remote my_task.py main
```

Verify that the code bundle is in the customer's bucket:

```bash
aws s3 ls s3://<customer-bucket>/org/project/domain/code-bundles/
```

The code bundle `.tgz` file should appear in the customer's own object store.

**Step 2 -- Execution:**

Inspect the task pod to confirm it reads from customer infrastructure:

```bash
kubectl describe pod <task-pod> -n <workspace-namespace>
```

The pod description should show volumes mounted from customer S3, secrets from the customer's backend, and a non-root security context.

**Step 3 -- Retrieval:**

Open browser developer tools (Network tab) and view the task's outputs in the Union.ai UI. Output requests should use presigned URLs pointing to the customer's S3/GCS/Azure Blob endpoint. Separately, confirm that the control plane returns only metadata:

```bash
uctl get execution <execution-id> -o json
```

The response should contain phase, timestamps, and URIs -- no inline data content.

**Step 4 -- Negative proof:**

Search control plane audit logs for the recognizable data string used in the workflow -- it should not appear. If VPC Flow Logs are enabled, data-sized transfers should flow only to/from the customer's object store, not to Union.ai IP ranges.
