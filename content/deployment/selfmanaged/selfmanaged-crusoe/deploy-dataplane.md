---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required Crusoe resources (CMK cluster, Cloud Storage bucket, access keys, access policy), see [Prepare infrastructure](../selfmanaged-crusoe/prepare-infra) first.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have a CMK cluster running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have a Crusoe Cloud Storage bucket, access keys, and access policy as described in [Prepare infrastructure](../selfmanaged-crusoe/prepare-infra).

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).
* Install the [`flyte` CLI](../../../api-reference/flyte-cli) (used later to run a sample workflow).

## Deploy the {{< key product_name >}} operator

1. Set your `KUBECONFIG` to the CMK cluster where you want to deploy the data plane:

   ```bash
   export KUBECONFIG=<PATH_TO_KUBECONFIG>
   ```

2. Configure the Union CLI and provision data plane resources:

   ```bash
   uctl config init --host=<ORG_NAME>.union.ai
   uctl selfserve provision-dataplane-resources --clusterName <CLUSTER_NAME> --provider metal
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML values file specific to the `metal` provider.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

   We use `--provider metal` for Crusoe because the Union operator treats Crusoe as a generic S3-compatible / Kubernetes environment rather than a first-class cloud provider integration (like AWS/GCP/Azure).

3. Update the generated values file with your Crusoe-specific storage configuration. Replace the placeholders with your actual credentials and settings.

   ```yaml
   host: <ORG_NAME>.union.ai
   clusterName: <CLUSTER_NAME>
   orgName: <ORG_NAME>
   provider: metal

   storage:
     provider: custom
     bucketName: <BUCKET_NAME>
     fastRegistrationBucketName: <BUCKET_NAME>
     custom:
       type: stow
       container: <BUCKET_NAME>
       stow:
         kind: s3
         config:
           region: <CRUSOE_REGION>
           auth_type: accesskey
           access_key_id: <ACCESS_KEY_ID>
           secret_key: <SECRET_ACCESS_KEY>
           endpoint: https://object.crusoecloud.com    # [VERIFY endpoint]
           disable_ssl: false
           disable_force_path_style: false             # [VERIFY: set true if Crusoe requires virtual-hosted style]

   executor:
     extraEnvVars:
       - name: FLYTE_AWS_ENDPOINT
         value: "https://object.crusoecloud.com"      # [VERIFY]
       - name: AWS_ACCESS_KEY_ID
         value: <ACCESS_KEY_ID>
       - name: AWS_SECRET_ACCESS_KEY
         value: <SECRET_ACCESS_KEY>
       - name: AWS_DEFAULT_REGION
         value: <CRUSOE_REGION>

   config:
     k8s:
       plugins:
         k8s:
           default-env-vars:
             - FLYTE_AWS_ENDPOINT: https://object.crusoecloud.com   # [VERIFY]
             - AWS_ACCESS_KEY_ID: <ACCESS_KEY_ID>
             - AWS_SECRET_ACCESS_KEY: <SECRET_ACCESS_KEY>
             - AWS_DEFAULT_REGION: <CRUSOE_REGION>

   operator:
     enableTunnelService: true

   secrets:
     admin:
       create: true
       clientId: <CLIENT_ID>
       clientSecret: <CLIENT_SECRET>

   fluentbit:
     enabled: true
     env:
       - name: AWS_ACCESS_KEY_ID
         value: <ACCESS_KEY_ID>
       - name: AWS_SECRET_ACCESS_KEY
         value: <SECRET_ACCESS_KEY>
   ```

   > [!NOTE]
   > The `uctl selfserve provision-dataplane-resources` command in step 2 generates the `<CLIENT_ID>` and `<CLIENT_SECRET>` values. Use the values from that command's output.

4. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

5. Install the Custom Resource Definitions (CRDs) via server-side apply. The CRDs are vendored in [unionai/helm-charts](https://github.com/unionai/helm-charts) under `crds/`:

   ```bash
   git clone https://github.com/unionai/helm-charts.git
   cd helm-charts

   # Required — FlyteWorkflow CRD consumed by propeller.
   kubectl apply --server-side --force-conflicts -f crds/flyte-v1/

   # Required when monitoring.enabled=true (chart default).
   kubectl apply --server-side --force-conflicts -f crds/kube-prometheus-stack/
   ```

   Server-side apply avoids the 256 KiB `last-applied-configuration` annotation overflow on larger CRDs. `--force-conflicts` is needed only on first install.

6. Install the data plane. Replace `<PATH_TO_VALUES_FILE>` with the path to the Helm values file you customized in step 3.

   ```bash
   helm upgrade --install unionai-dataplane unionai/dataplane \
     --namespace union --create-namespace \
     --values <PATH_TO_VALUES_FILE> \
     --skip-crds \
     --timeout 10m
   ```

7. Verify the pods are running:

   ```bash
   kubectl get pods -n union
   ```

   When the deployment succeeds, all pods show a `Running` status, including `union-operator-proxy`, `union-operator-buildkit`, `flytepropeller`, and `executor`.

8. Verify the cluster is registered with the control plane:

   ```bash
   uctl get cluster
   ```

   The output is similar to the following:

   ```text
   NAME              ORG       STATE          HEALTH
   union-crusoe      my-org    STATE_ENABLED  HEALTHY
   ```

9. **Required for helm charts on a version <= 2026.5.8.** Create an API key for your organization. This is required for v2 workflow executions on the data plane. If you have already created one, rerun the same command to propagate the key to the new cluster:

   ```bash
   uctl create apikey --keyName EAGER_API_KEY --org <ORG_NAME>
   ```

   > [!NOTE]
   > If you receive a `PermissionDenied` error, contact [Union.ai support](https://www.union.ai/) to have the permission enabled for your organization.

## Test a workflow

To run a sample workflow, complete the following steps:

1. Create a Flyte CLI configuration file at the path `.flyte/config.yaml` in your project directory. Replace `<ORG_NAME>` and `<PROJECT_NAME>` with your organization and project identifiers.

   ```yaml
   admin:
     endpoint: dns:///<ORG_NAME>.union.ai
   image:
     builder: remote
   task:
     domain: development
     org: <ORG_NAME>
     project: <PROJECT_NAME>
   ```

2. Run a sample workflow:

   ```bash
   flyte run --image ghcr.io/flyteorg/flyte:py3.13-v2.0.2 \
     hello_world.py main --n 5
   ```

   > [!NOTE]
   > If the remote image builder isn't enabled for your organization, use the `--image` flag with a pre-built container image as in the preceding `flyte run` example.

3. Check the run status. Replace `<RUN_NAME>` with the workflow run identifier.

   ```bash
   flyte get run <RUN_NAME>
   ```

   Look for `ACTION_PHASE_SUCCEEDED` in the output to confirm the workflow completed successfully.

> [!NOTE] Crusoe-specific tip
> To land tasks on Crusoe GPU nodes, add a task-level resource request and a node selector matching Crusoe's GPU node pool labels.
> <!-- [VERIFY label keys — e.g., crusoe.ai/gpu-type=h100] -->

## Troubleshooting

| Symptom                                      | Cause                                                  | Fix                                                                                                                       |
| -------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `PathStyleRequestNotAllowed 400`             | Control plane generates path-style URLs but Crusoe requires virtual-hosted. | Set `storage.custom.stow.config.disable_force_path_style: true`.                                  |
| `403 Forbidden` on S3 operations             | No access policy attached to the storage key.          | Create/attach an object storage access policy in the Crusoe Cloud Console.                                                |
| Task pods reach `s3.us-east-1.amazonaws.com` | Task pods missing the Crusoe endpoint.                 | Add `FLYTE_AWS_ENDPOINT` to `config.k8s.plugins.k8s.default-env-vars`.                                                    |
| "All enabled clusters are unhealthy"         | Control plane can't reach the data plane.              | Verify the tunnel service: `kubectl get pods -n union \| grep proxy`.                                                     |
| "Remote image builder is not enabled"        | Remote builder not enabled on the control plane.       | Contact Union.ai or use `--image` with a pre-built image.                                                                 |
| `invalid keys: collectbillableresourceusage` | Chart/operator version mismatch.                       | Use matching chart and operator image versions.                                                                           |
| Helm "another operation in progress"         | Interrupted Helm upgrade.                              | Run `helm rollback unionai-dataplane <LAST_GOOD_REVISION> -n union`.                                                      |
| "Provided Tunnel token is not valid"         | Control plane not configured for this cluster.         | Complete cluster registration first.                                                                                      |

## Additional resources

For more information, see the following resources:

- [Crusoe Managed Kubernetes overview](https://docs.crusoecloud.com/kubernetes/overview/)
- [Crusoe Cloud Storage overview](https://docs.crusoecloud.com/storage/object-storage/overview)

<!--
Open items to confirm before publishing (carried over from draft):
1. S3 endpoint URL — object.crusoecloud.com, storage.crusoecloud.com, region-scoped, or other?
2. Addressing style — does Crusoe require virtual-hosted style or support path-style?
3. Region naming — canonical region/AZ format (e.g., us-northcentral1-a)?
4. IAM policy schema — AWS-style JSON or custom?
5. Console navigation paths — exact menu paths for buckets, keys, policies.
6. Kubernetes service name — CMK, CKE, or other branding?
7. GPU node pool labels & taints — canonical labels (e.g., crusoe.ai/gpu-type=h100)?
8. Supported Kubernetes versions — confirm the "most recent three minor" claim.
9. Networking / egress — special config for outbound tunnel to *.union.ai on 443?
10. Default StorageClass on CMK for PVCs (BuildKit cache, fluent-bit)?
11. Image registry pull-through cache to reduce GHCR pull latency?
12. Logging sink — back to the same bucket, or a managed logging service?
-->
