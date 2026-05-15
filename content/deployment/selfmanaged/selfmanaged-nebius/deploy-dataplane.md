---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required Nebius resources (MK8s cluster, Object Storage bucket, service account, access key), see [Prepare infrastructure](../selfmanaged-nebius/prepare-infra) first.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have a Nebius Managed Kubernetes cluster running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have a Nebius Object Storage bucket, service account, and access key as described in [Prepare infrastructure](../selfmanaged-nebius/prepare-infra).

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).
* Install the [`flyte` CLI](../../../api-reference/flyte-cli) (used later to run a sample workflow).
* Install the [Nebius CLI](https://docs.nebius.com/cli) and authenticate with `nebius profile create`.

## Deploy the {{< key product_name >}} operator

1. Set your `KUBECONFIG` to the Nebius MK8s cluster where you want to deploy the data plane:

   ```bash
   nebius mk8s cluster get-credentials --id <CLUSTER_ID> --external
   export KUBECONFIG=<PATH_TO_KUBECONFIG>
   ```

2. Configure the Union CLI and provision data plane resources:

   ```bash
   uctl config init --host=<ORG_NAME>.union.ai
   uctl selfserve provision-dataplane-resources --clusterName <CLUSTER_NAME> --provider metal
   ```

   * The command outputs the ID, name, and a secret used by the Union services to communicate with your control plane. It also generates a YAML values file specific to the `metal` provider.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

   We use `--provider metal` because Nebius is treated as a generic Kubernetes target rather than a first-class hyperscaler integration (no native IAM-for-Pods equivalent today). <!-- [VERIFY: Nebius Workload Identity GA status] -->

3. Update the generated values file with your Nebius-specific storage configuration. Replace the placeholders with your actual credentials and settings.

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
           region: <NEBIUS_REGION>           # e.g., eu-north1
           auth_type: accesskey
           access_key_id: <ACCESS_KEY_ID>
           secret_key: <SECRET_ACCESS_KEY>
           endpoint: https://storage.<NEBIUS_REGION>.nebius.cloud
           disable_ssl: false
           disable_force_path_style: false   # Nebius supports path-style; [VERIFY]

   executor:
     extraEnvVars:
       - name: FLYTE_AWS_ENDPOINT
         value: "https://storage.<NEBIUS_REGION>.nebius.cloud"
       - name: AWS_ACCESS_KEY_ID
         value: <ACCESS_KEY_ID>
       - name: AWS_SECRET_ACCESS_KEY
         value: <SECRET_ACCESS_KEY>
       - name: AWS_DEFAULT_REGION
         value: <NEBIUS_REGION>

   config:
     k8s:
       plugins:
         k8s:
           default-env-vars:
             - FLYTE_AWS_ENDPOINT: https://storage.<NEBIUS_REGION>.nebius.cloud
             - AWS_ACCESS_KEY_ID: <ACCESS_KEY_ID>
             - AWS_SECRET_ACCESS_KEY: <SECRET_ACCESS_KEY>
             - AWS_DEFAULT_REGION: <NEBIUS_REGION>

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

   The settings below are required for Nebius Object Storage compatibility:

   | Setting                                                                 | Value                                                | Purpose                                                            |
   | ----------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------ |
   | `storage.custom.stow.config.endpoint`                                   | `https://storage.<NEBIUS_REGION>.nebius.cloud`       | Nebius Object Storage S3-compatible endpoint.                      |
   | `storage.custom.stow.config.region`                                     | e.g., `eu-north1`                                    | Region of the bucket. Must match the bucket's region.              |
   | `storage.custom.stow.config.auth_type`                                  | `accesskey`                                          | Use static access key authentication.                              |
   | `config.k8s.plugins.k8s.default-env-vars` (entry: `FLYTE_AWS_ENDPOINT`) | `https://storage.<NEBIUS_REGION>.nebius.cloud`       | Endpoint injected into task pods so they target Nebius, not AWS.   |
   | `executor.extraEnvVars.AWS_DEFAULT_REGION`                              | `<NEBIUS_REGION>`                                    | Ensures the S3 SDK signs requests with the correct region.        |

4. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

5. Install the Custom Resource Definitions (CRDs):

   ```bash
   helm upgrade --install unionai-dataplane-crds unionai/dataplane-crds
   ```

6. Install the data plane. Replace `<PATH_TO_VALUES_FILE>` with the path to the Helm values file you customized in step 3.

   ```bash
   helm upgrade --install unionai-dataplane unionai/dataplane \
     --namespace union --create-namespace \
     --values <PATH_TO_VALUES_FILE> \
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
   NAME            ORG       STATE          HEALTH
   union-nebius    my-org    STATE_ENABLED  HEALTHY
   ```

9. Create an API key for your organization. This is required for v2 workflow executions on the data plane. If you have already created one, rerun the same command to propagate the key to the new cluster:

   ```bash
   uctl create apikey --keyName EAGER_API_KEY --org <ORG_NAME>
   ```

   > [!NOTE]
   > If you receive a `PermissionDenied` error, contact [Union.ai support](https://www.union.ai/) to have the permission enabled for your organization.

## GPU node configuration

To run GPU workloads on Nebius, ensure the NVIDIA device plugin is installed and your task definitions request GPU resources. Nebius MK8s pre-installs the NVIDIA GPU operator on GPU node groups, so no additional setup is typically required. <!-- [VERIFY: confirm NVIDIA operator is installed by default vs. add-on] -->

Example task resource request:

```python
from flyte import Resources

@env.task(resources=Resources(gpu="H100:1", memory="64Gi"))
def train_model(...):
    ...
```

Nebius node selectors / tolerations may be required depending on how your GPU node groups are tainted. Add them via `pod_template` on the task or globally in the Helm values under `config.k8s.plugins.k8s.default-tolerations`.

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

## Troubleshooting

| Symptom                                              | Cause                                                                   | Fix                                                                                                                                            |
| ---------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `403 Forbidden` on S3 operations                     | Service account lacks the `storage.editor` role on the bucket.          | Bind the role in **IAM > Service Accounts**, or scope a custom role to the bucket ARN.                                                         |
| `SignatureDoesNotMatch`                              | Region mismatch between bucket and `AWS_DEFAULT_REGION` / region in Helm values. | Ensure `region`, `AWS_DEFAULT_REGION`, and the endpoint subdomain (`storage.<region>.nebius.cloud`) all reference the same Nebius region.   |
| Task pods reach `s3.us-east-1.amazonaws.com`         | Task pods are missing the Nebius endpoint.                              | Add `FLYTE_AWS_ENDPOINT` to `config.k8s.plugins.k8s.default-env-vars` with the value `https://storage.<NEBIUS_REGION>.nebius.cloud`.           |
| `PathStyleRequestNotAllowed 400`                     | Nebius rejected path-style URLs for this bucket.                        | Set `storage.custom.stow.config.disable_force_path_style: true` to switch to virtual-hosted style. <!-- [VERIFY default] -->                   |
| `dial tcp: lookup storage.<region>.nebius.cloud: no such host` | Egress restricted by Nebius VPC network policy.                   | Ensure the MK8s node subnet has egress to the Nebius Object Storage endpoint, or use a VPC endpoint if available.                              |
| "All enabled clusters are unhealthy"                 | The control plane can't reach the data plane.                           | Verify the tunnel service is running: `kubectl get pods -n union \| grep proxy`. Confirm `operator.enableTunnelService: true` in the Helm values. |
| "Remote image builder is not enabled"                | The remote builder isn't enabled on the control plane.                  | Contact Union.ai to enable the remote builder, or use `--image` with a pre-built image.                                                        |
| GPU pods stuck in `Pending` with `Insufficient nvidia.com/gpu` | GPU node group not provisioned, or taints not tolerated.       | Confirm GPU node group exists in the Nebius Console; add matching tolerations to the task's `pod_template`.                                    |
| `invalid keys: collectbillableresourceusage`         | Chart version mismatch with the operator.                               | Use matching chart and operator image versions.                                                                                                |
| Helm "another operation in progress"                 | An interrupted Helm upgrade.                                            | Run `helm rollback unionai-dataplane <LAST_GOOD_REVISION> -n union`.                                                                           |
| "Provided Tunnel token is not valid"                 | The control plane isn't configured for this cluster.                    | Complete cluster registration first via `uctl selfserve provision-dataplane-resources`.                                                        |

## Additional resources

For more information, see the following resources:

- [Nebius Managed Kubernetes documentation](https://docs.nebius.com/kubernetes)
- [Nebius Object Storage documentation](https://docs.nebius.com/object-storage)
- [Nebius IAM and service accounts](https://docs.nebius.com/iam)

<!--
Open items to confirm before publishing (carried over from draft):
1. Object Storage endpoint format — storage.<region>.nebius.cloud or different?
2. Path-style vs. virtual-hosted style — does Nebius support both?
3. Available regions — confirm slugs (eu-north1, eu-west1, us-central1).
4. NVIDIA GPU operator — pre-installed on GPU node groups, or opt-in add-on?
5. Workload Identity — Nebius equivalent of IRSA / Workload Identity Federation?
6. Service account role name — storage.editor, storage.admin, or custom?
-->
