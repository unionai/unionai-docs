---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required Crusoe resources (CMK cluster, Cloud Storage bucket, access keys, access policy), see [Prepare infrastructure](../selfmanaged-crusoe/prepare-infra) first.

> [!NOTE] Planning more than one cluster?
> This page covers the single-cluster path: one cluster in the `default` cluster pool, as created by the `flyte create cluster ... --pool default` command below. If you plan to connect several clusters to the same control plane, read [Multiple clusters](../configuration/multi-cluster) first. Pool membership governs metadata sharing: clusters in the same pool share one metadata bucket, and clusters in different pools must use different ones, so it affects the metadata bucket you configure below.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have a CMK cluster running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have a Crusoe Cloud Storage bucket, access keys, and access policy as described in [Prepare infrastructure](../selfmanaged-crusoe/prepare-infra).

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).
* Install the [`flyte` CLI](../../../api-reference/flyte-cli) (used later to run a sample workflow).
* Install the [`flyteplugins-union` plugin](../../../api-reference/flyte-cli#plugin-commands), which provides the `flyte get cluster` command: `pip install flyteplugins-union`.

## Deploy the {{< key product_name >}} operator

1. Set your `KUBECONFIG` to the CMK cluster where you want to deploy the data plane:

   ```bash
   export KUBECONFIG=<PATH_TO_KUBECONFIG>
   ```

2. Configure the `flyte` CLI to talk to your control plane, then register the cluster name:

   ```bash
   flyte create config --endpoint <YOUR_UNION_CONTROLPLANE_URL> --org <ORG_NAME>
   flyte create cluster <CLUSTER_NAME> --pool default
   ```

   `flyte create config` writes `.flyte/config.yaml`. The first command that contacts the control plane opens a browser to authenticate you.

   Register the cluster before you install the chart: the data plane binds to this record when it starts. Every organization is provisioned with a `default` pool, so `--pool default` needs no extra setup.

3. Configure the Union CLI and provision data plane resources:

   ```bash
   uctl config init --host=<ORG_NAME>.union.ai
   uctl selfserve provision-dataplane-resources --clusterName <CLUSTER_NAME> --provider custom
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     You will pass the client ID and client secret to the Helm chart in step 7.

   * Save the secret that is displayed. Union does not store it, and it cannot be retrieved later.

   We use `--provider custom` for Crusoe because the Union operator treats Crusoe as a generic S3-compatible / Kubernetes environment rather than a first-class cloud provider integration (like AWS/GCP/Azure).

4. Create a values file for the data plane chart. Start from the base values file and layer your Crusoe-specific storage configuration on top, replacing the placeholders with your actual credentials and settings:

   ```bash
   curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.yaml
   ```

   Rather than putting your access keys in the values file, store them in a Kubernetes Secret and reference it from the chart. Create the namespace and the secret first; the chart reads the secret while rendering, so it must exist before you install:

   ```bash
   kubectl create namespace union
   kubectl create secret generic storage-credentials -n union \
     --from-literal=access_key_id=<ACCESS_KEY_ID> \
     --from-literal=secret_key=<SECRET_ACCESS_KEY>
   ```

   Then write the values file:

   ```yaml
   host: <ORG_NAME>.union.ai
   clusterName: <CLUSTER_NAME>
   orgName: <ORG_NAME>
   provider: custom

   storage:
     provider: compat
     authType: accesskey
     bucketName: <BUCKET_NAME>
     fastRegistrationBucketName: <BUCKET_NAME>
     endpoint: <YOUR_STORAGE_ENDPOINT>
     region: <CRUSOE_REGION>
     disableSSL: false
     credentialsSecretRef:
       name: storage-credentials

   config:
     k8s:
       plugins:
         k8s:
           default-env-vars:
             - AWS_DEFAULT_REGION: <CRUSOE_REGION>

   operator:
     enableTunnelService: true

   fluentbit:
     enabled: true
     env:
       - name: AWS_ACCESS_KEY_ID
         valueFrom:
           secretKeyRef:
             name: storage-credentials
             key: access_key_id
       - name: AWS_SECRET_ACCESS_KEY
         valueFrom:
           secretKeyRef:
             name: storage-credentials
             key: secret_key
   ```

   With `storage.provider: compat` and `authType: accesskey`, the chart builds the stow config itself and injects `FLYTE_AWS_ENDPOINT`, `FLYTE_AWS_ACCESS_KEY_ID`, and `FLYTE_AWS_SECRET_ACCESS_KEY` into task pods from `storage.endpoint` and the secret, so those no longer need to be listed by hand.

   > [!NOTE]
   > The chart resolves the secret with a Helm `lookup`, which returns nothing during `helm template` or `--dry-run`. Those commands render the storage config without credentials; only a real install picks them up. If your secret uses different field names, set `credentialsSecretRef.accessKeyIdKey` and `credentialsSecretRef.secretKeyKey` to match.

   > [!NOTE]
   > The `uctl selfserve provision-dataplane-resources` command in step 3 generates the `<CLIENT_ID>` and `<CLIENT_SECRET>` values. Use the values from that command's output.

5. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

6. Install the Custom Resource Definitions (CRDs):

   ```bash
   helm upgrade --install unionai-dataplane-crds unionai/dataplane-crds
   ```

7. Install the data plane. Replace `<PATH_TO_VALUES_FILE>` with the path to the Helm values file you customized in step 4, and `<CLIENT_ID>` / `<CLIENT_SECRET>` with the credentials printed in step 3.

   ```bash
   helm upgrade --install unionai-dataplane unionai/dataplane \
     --namespace union --create-namespace \
     --values <PATH_TO_VALUES_FILE> \
     --set global.AUTH_CLIENT_ID=<CLIENT_ID> \
     --set-string secrets.admin.clientId=<CLIENT_ID> \
     --set secrets.admin.clientSecret=<CLIENT_SECRET> \
     --timeout 10m
   ```

8. Verify the pods are running:

   ```bash
   kubectl get pods -n union
   ```

   When the deployment succeeds, all pods show a `Running` status, including `union-operator-proxy`, `union-operator-buildkit`, `flytepropeller`, and `executor`.

9. Verify the cluster is registered with the control plane:

   ```bash
   flyte get cluster
   ```

   The output is similar to the following:

   ```text
   Enabled Clusters
   NAME            ORG       STATE     HEALTH
   union-crusoe    my-org    enabled   healthy
   ```

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

## Troubleshooting

| Symptom                                      | Cause                                                  | Fix                                                                                                                       |
| -------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `PathStyleRequestNotAllowed 400`             | Control plane generates path-style URLs but Crusoe requires virtual-hosted. | `compat` cannot express this setting. Switch `storage` to `provider: custom` with an explicit `stow` block setting `disable_force_path_style: true`. Keep `credentialsSecretRef`: the chart still injects the task-pod variables and also merges the stow credentials into the `custom` stow config automatically, as the [CoreWeave page](../selfmanaged-coreweave/deploy-dataplane) shows. |
| `403 Forbidden` on S3 operations             | No access policy attached to the storage key.          | Create/attach an object storage access policy in the Crusoe Cloud Console.                                                |
| Task pods reach `s3.us-east-1.amazonaws.com` | Task pods missing the Crusoe endpoint.                 | The chart injects `FLYTE_AWS_ENDPOINT` from `storage.endpoint` when `injectPodEnvVars` is enabled (the default); confirm that value is set.                     |
| "All enabled clusters are unhealthy"         | Control plane can't reach the data plane.              | Verify the tunnel service: `kubectl get pods -n union \| grep proxy`.                                                     |
| "Remote image builder is not enabled"        | Remote builder not enabled on the control plane.       | Contact Union.ai or use `--image` with a pre-built image.                                                                 |
| `invalid keys: collectbillableresourceusage` | Chart/operator version mismatch.                       | Use matching chart and operator image versions.                                                                           |
| Helm "another operation in progress"         | Interrupted Helm upgrade.                              | Run `helm rollback unionai-dataplane <LAST_GOOD_REVISION> -n union`.                                                      |
| "Provided Tunnel token is not valid"         | Control plane not configured for this cluster.         | Complete cluster registration first.                                                                                      |

## Next: manage your cluster and pools

`uctl selfserve provision-dataplane-resources` provisions the data plane and
registers this cluster with the control plane. Once it is connected, you manage
the **cluster pool** it belongs to (and route work to it with queues) from the
[Cluster and workload management](../../../user-guide/cluster-workload-management/_index)
user guide:

- [Cluster pools](../../../user-guide/cluster-workload-management/cluster-pools): group clusters that share one data plane (object store, secrets, registry).
- [Clusters](../../../user-guide/cluster-workload-management/clusters): inspect and manage the cluster records registered with the control plane.
- [Managing queues](../../../user-guide/cluster-workload-management/queues): route workloads to a pool and enforce concurrency, priority, and fairness.

Each cluster is assigned exactly one pool. If no custom pool is specified when the
cluster is created, it joins the `default` pool that every organization is
provisioned with, so a single-cluster deployment needs no extra pool setup.

## Additional resources

For more information, see the following resources:

- [Crusoe Managed Kubernetes overview](https://docs.crusoecloud.com/kubernetes/overview/)
- [Crusoe Cloud Storage overview](https://docs.crusoecloud.com/storage/object-storage/overview)

