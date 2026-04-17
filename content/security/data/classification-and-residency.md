---
title: Data classification and residency
weight: 1
variants: -flyte +union
---

# Data classification and residency

## Data classification

Every data type in the Union.ai platform is classified by its residency and access pattern. This classification determines where data is stored and how it is accessed.

| Classification | Data types | Residency |
|---|---|---|
| Customer Data | Task inputs/outputs, code bundles, container images, reports, task logs, secrets, observability metrics | Customer infrastructure |
| Orchestration Metadata | Task definitions (specs), run/action metadata (phase, timestamps, errors) | Control plane DB |
| Platform Metadata | User identity/RBAC records, cluster records | Control plane DB |

Customer data -- the artifacts produced and consumed by workflows -- resides exclusively in the customer's own infrastructure. This includes everything a task reads, writes, or depends on at runtime: inputs and outputs in object storage, code bundles, container images in the customer's registry, log output, secrets, and observability metrics. The control plane never stores customer data payloads. Orchestration metadata and platform metadata are stored in the control plane database, but these contain only the structural and operational information needed to coordinate workflow execution -- task specifications, phase transitions, timestamps, error messages, user records, and cluster configuration. No customer data content appears in either metadata category.

## Data residency

All customer data resides in the customer's own cloud account and region. The customer chooses the region for their data plane deployment, and all data plane resources -- object storage, container registry, secrets backend, log aggregator, and compute -- are provisioned within that region.

The control plane is available in the following regions: US West (us-west-2), US East (us-east-2), EU West-1 (Ireland), EU West-2 (London), and EU Central (eu-central-1). No customer data is replicated to or cached in Union.ai infrastructure at any point during the workflow lifecycle. For customers deploying in EU regions, this architecture ensures that all customer data remains within the EU, supporting GDPR data residency requirements.

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
