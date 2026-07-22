---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required OCI resources (OKE cluster, Object Storage, Container Registry, IAM access), see [Prepare infrastructure](../selfmanaged-oci/prepare-infra) first.

> [!NOTE] Planning more than one cluster?
> This page covers the single-cluster path: one cluster in the `default` cluster pool, as created by the `flyte create cluster ... --pool default` command below. If you plan to connect several clusters to the same control plane, read [Multiple clusters](../configuration/multi-cluster) first. Pool membership governs metadata sharing -- clusters in the same pool share one metadata bucket, and clusters in different pools must use different ones -- so it affects the metadata bucket you configure below.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization.
* You have a cluster name provided by or coordinated with Union.
* You have an OKE cluster running one of the most recent three minor Kubernetes versions.
  [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have configured Object Storage bucket(s), Container Registry, and IAM access as described in [Prepare infrastructure](../selfmanaged-oci/prepare-infra).

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).
* Install the [`flyte` CLI](../../../api-reference/flyte-cli).
* Install the [`flyteplugins-union` plugin](../../../api-reference/flyte-cli#plugin-commands), which provides the `flyte get cluster` command: `pip install flyteplugins-union`.

## Deploy the {{< key product_name >}} operator

1. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

2. Configure the `flyte` CLI to talk to your control plane, then register the cluster name:

   ```bash
   flyte create config --endpoint <YOUR_UNION_CONTROL_PLANE_URL> --org <YOUR_ORG_NAME>
   flyte create cluster <YOUR_SELECTED_CLUSTERNAME> --pool default
   ```

   `flyte create config` writes `.flyte/config.yaml`. The first command that contacts the control plane opens a browser to authenticate you.

   Register the cluster before you install the chart -- the data plane binds to this record when it starts. Every organization is provisioned with a `default` pool, so `--pool default` needs no extra setup.

3. Use the `uctl selfserve provision-dataplane-resources` command to generate a new client and client secret for communicating with your Union control plane, provision authorization permissions for the app to operate on the union cluster name you have selected, and provide follow-up instructions:

   ```bash
   uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider oci
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     You will pass the client ID and client secret to the Helm chart in step 5.

   * Save the secret that is displayed. Union does not store it, and it cannot be retrieved later.

4. Download the base values file for the data plane chart and fill in your infrastructure details:

   ```bash
   curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.yaml
   ```

   There is no published OCI overlay, so start from the base values file and set the OCI-specific keys on top of it:

   - Set `global.UNION_CONTROL_PLANE_HOST` and `global.CONTROLPLANE_HOST` to your control plane hostname (no scheme, no port).
   - Set `global.CLUSTER_NAME` to the cluster name you registered in step 2.
   - Set `global.ORG_NAME` to your organization name.
   - Set `storage.bucketName` and `storage.fastRegistrationBucketName` to your Object Storage bucket name(s).
   - Set `storage.region` to your OCI region.
   - If using static credentials (Option B), set `storage.accessKey` and `storage.secretKey` to your S3 Compatibility API credentials.

5. Install the data plane Helm chart, passing the client ID and client secret from step 3:

   ```bash
   helm upgrade --install union unionai/dataplane \
     -f values.yaml \
     --set global.AUTH_CLIENT_ID=<CLIENT_ID> \
     --set-string secrets.admin.clientId=<CLIENT_ID> \
     --set secrets.admin.clientSecret=<CLIENT_SECRET> \
     --namespace union \
     --create-namespace 
     --force-conflicts
   ```

6. Once deployed you can check to see if the cluster has been successfully registered to the control plane:

   ```bash
   flyte get cluster
   ```

   The command groups clusters by state. A successfully registered cluster appears under **Enabled Clusters**:

   ```text
   Enabled Clusters
   NAME        ORG     STATE     HEALTH
   <cluster>   <org>   enabled   healthy
   ```

7. Follow the [Quickstart](../../../user-guide/quickstart) to run your first workflow and verify your cluster is working correctly.

## Next: manage your cluster and pools

`uctl selfserve provision-dataplane-resources` provisions the data plane and
registers this cluster with the control plane. Once it is connected, you manage
the **cluster pool** it belongs to, and route work to it with queues, from the
[Cluster and workload management](../../../user-guide/cluster-workload-management/_index)
user guide:

- [Cluster pools](../../../user-guide/cluster-workload-management/cluster-pools): group clusters that share one data plane (object store, secrets, registry).
- [Clusters](../../../user-guide/cluster-workload-management/clusters): inspect and manage the cluster records registered with the control plane.
- [Queues](../../../user-guide/cluster-workload-management/queues): route workloads to a pool and enforce concurrency, priority, and fairness.

Every organization is provisioned with a `default` pool that new clusters join
automatically, so a single-cluster deployment needs no extra pool setup.
