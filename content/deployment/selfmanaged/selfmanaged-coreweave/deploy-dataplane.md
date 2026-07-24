---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required CoreWeave resources (CKS cluster, AI Object Storage bucket, access keys, access policy), see [Prepare infrastructure](../selfmanaged-coreweave/prepare-infra) first.

> [!NOTE] Planning more than one cluster?
> This page covers the single-cluster path: one cluster in the `default` cluster pool, as created by the `flyte create cluster ... --pool default` command below. If you plan to connect several clusters to the same control plane, read [Multiple clusters](../configuration/multi-cluster) first. Pool membership governs metadata sharing: clusters in the same pool share one metadata bucket, and clusters in different pools must use different ones, so it affects the metadata bucket you configure below.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have a CKS cluster running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have a CoreWeave AI Object Storage bucket, access keys, and access policy as described in [Prepare infrastructure](../selfmanaged-coreweave/prepare-infra).

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).
* Install the [`flyte` CLI](../../../api-reference/flyte-cli) (used later to run a sample workflow).
* Install the [`flyteplugins-union` plugin](../../../api-reference/flyte-cli#plugin-commands), which provides the `flyte get cluster` command: `pip install flyteplugins-union`.

## Deploy the {{< key product_name >}} operator

1. Set your `KUBECONFIG` to the CKS cluster where you want to deploy the data plane:

   ```bash
   export KUBECONFIG=<PATH_TO_KUBECONFIG>
   ```

2. Configure the `flyte` CLI to talk to your control plane, then register the cluster name:

   ```bash
   flyte create config --endpoint <ORG_NAME>.union.ai --org <ORG_NAME>
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

4. Create a values file for the data plane chart. Start from the base values file and layer your CoreWeave-specific storage configuration on top. AI Object Storage requires virtual-hosted style S3 URLs, so you must override the default storage configuration. Replace the placeholders with your actual credentials and settings.

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
     provider: custom
     authType: accesskey
     bucketName: <BUCKET_NAME>
     fastRegistrationBucketName: <BUCKET_NAME>
     credentialsSecretRef:
       name: storage-credentials
     custom:
       type: stow
       container: <BUCKET_NAME>
       stow:
         kind: s3
         config:
           region: <AVAILABILITY_ZONE>
           auth_type: accesskey
           endpoint: https://cwobject.com
           disable_ssl: false
           disable_force_path_style: true

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

   Two separate mechanisms read that secret:

   - `storage.credentialsSecretRef` makes the chart inject `FLYTE_AWS_ACCESS_KEY_ID` and `FLYTE_AWS_SECRET_ACCESS_KEY` into task pods. This path is independent of `storage.provider`, so it works with `custom`, and it is why no per-executor environment variables are needed.
   - The chart renders the `storage.custom` block as a Helm template. When `credentialsSecretRef` is set, the chart looks up that secret and merges its `access_key_id` and `secret_key` into the stow configuration the control plane components use, so you do not add credentials to the `custom` block yourself.

   > [!NOTE]
   > The `uctl selfserve provision-dataplane-resources` command in step 3 generates the `<CLIENT_ID>` and `<CLIENT_SECRET>` values. Use the values from that command's output.

   > [!NOTE]
   > The chart resolves the secret with a Helm `lookup`, which returns nothing during `helm template` or `--dry-run`. Those commands render the storage config without credentials; only a real install picks them up. If your secret uses different field names, set `credentialsSecretRef.accessKeyIdKey` and `credentialsSecretRef.secretKeyKey` to match.
   >
   > This page keeps `storage.provider: custom` because CoreWeave AI Object Storage requires virtual-hosted style URLs, and `disable_force_path_style` is only reachable through a `custom` stow block.

   The settings below are required for AI Object Storage compatibility:

   | Setting                                                                 | Value                                | Purpose                                                         |
   | ----------------------------------------------------------------------- | ------------------------------------ | --------------------------------------------------------------- |
   | `storage.custom.stow.config.disable_force_path_style`                   | `true`                               | Enables virtual-hosted style S3 URLs.                           |
   | `storage.custom.stow.config.endpoint`                                   | `https://cwobject.com`               | AI Object Storage endpoint for the control plane.               |
  
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
     --set-string global.AUTH_CLIENT_ID=<CLIENT_ID> \
     --set secrets.admin.clientId=<CLIENT_ID> \
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
   union-coreweave my-org    enabled   healthy
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

## Troubleshooting

| Symptom                                      | Cause                                                  | Fix                                                                                                                                                                 |
| -------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PathStyleRequestNotAllowed 400`             | The control plane generates path-style S3 URLs.        | Set `storage.custom.stow.config.disable_force_path_style` to `true` in the Helm values file.                                                                        |
| `403 Forbidden` on S3 operations             | No access policy for the storage key.                  | Create an object storage access policy in the [Cloud Console](https://docs.coreweave.com/products/storage/object-storage/auth-access/organization-policies/manage). |
| Task pods reach `s3.us-east-1.amazonaws.com` | Task pods are missing the CoreWeave endpoint.          | Add `FLYTE_AWS_ENDPOINT` to `config.k8s.plugins.k8s.default-env-vars` with the value `https://<BUCKET_NAME>.cwobject.com`.                                          |
| "All enabled clusters are unhealthy"         | The control plane can't reach the data plane.          | Verify the tunnel service is running: `kubectl get pods -n union \| grep proxy`.                                                                                    |
| "Remote image builder is not enabled"        | The remote builder isn't enabled on the control plane. | Contact Union.ai to enable the remote builder, or use `--image` with a pre-built image.                                                                             |
| `invalid keys: collectbillableresourceusage` | Chart version mismatch with the operator.              | Use matching chart and operator image versions.                                                                                                                     |
| Helm "another operation in progress"         | An interrupted Helm upgrade.                           | Run `helm rollback unionai-dataplane <LAST_GOOD_REVISION> -n union`.                                                                                                |
| "Provided Tunnel token is not valid"         | The control plane isn't configured for this cluster.   | Complete cluster registration first.                                                                                                                                |

## Next: manage your cluster and pools

`uctl selfserve provision-dataplane-resources` provisions the data plane and
registers this cluster with the control plane. Once it is connected, you manage
the **cluster pool** it belongs to, and route work to it with queues, from the
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

- [CoreWeave AI Object Storage](https://docs.coreweave.com/products/storage/object-storage)
- [Create a CKS cluster](https://docs.coreweave.com/products/cks/clusters/create)
