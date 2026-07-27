---
title: Deploy the data plane
weight: 3
variants: -flyte +union
---

# Deploy the data plane

This walkthrough installs the {{< key product_name >}} data plane operator on AWS, GCP, Azure, OCI, or a generic (on-premise / S3-compatible) Kubernetes cluster. The steps are the same across providers; only the Helm values file differs, and each provider's values are documented on its infrastructure page.

Before you start, provision your cloud infrastructure using the matching page and note its **Deploy configuration** section:

| Provider | Infrastructure page | `--provider` | Values file |
| --- | --- | --- | --- |
| AWS | [AWS](../infrastructure-recommendations/aws) | `aws` | `values.aws.yaml` |
| GCP | [GCP](../infrastructure-recommendations/gcp) | `gcp` | `values.gcp.yaml` |
| Azure | [Azure](../infrastructure-recommendations/azure) | `azure` | `values.azure.yaml` |
| OCI | [OCI](../infrastructure-recommendations/oci) | `oci` | `values.yaml` (base) |
| Generic | [Generic Kubernetes](../infrastructure-recommendations/generic) | `custom` | `values.yaml` (base) |

> [!NOTE] GPU-optimized providers
> CoreWeave, Crusoe, and Nebius have their own deployment guides with provider-specific GPU, storage, and registry steps: [CoreWeave](./coreweave) · [Crusoe](./crusoe) · [Nebius](./nebius).

> [!NOTE] Planning more than one cluster?
> This page covers the single-cluster path: one cluster in the `default` cluster pool, as created by the `flyte create cluster ... --pool default` command below. If you plan to connect several clusters to the same control plane, read [Multiple clusters](../configuration/multi-cluster) first. Pool membership governs metadata sharing: clusters in the same pool share one metadata bucket, and clusters in different pools must use different ones, so it affects the metadata bucket you configure.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization (e.g. `https://your-org-name.us-east-2.unionai.cloud`).
* You have a cluster name provided by or coordinated with Union.
* You have a Kubernetes cluster with workload identity (IRSA / GKE Workload Identity / Entra Workload Identity) or the equivalent credentials enabled, running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have provisioned object storage, a container registry, and identity bindings as described on your provider's [infrastructure recommendations](../infrastructure-recommendations/_index) page.

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).
* Install the [`flyte` CLI](../../../api-reference/flyte-cli).
* Install the [`flyteplugins-union` plugin](../../../api-reference/flyte-cli#plugin-commands), which provides the `flyte create cluster` and `flyte get cluster` commands: `pip install flyteplugins-union`.

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

   Register the cluster before you install the chart: the data plane binds to this record when it starts. Every organization is provisioned with a `default` pool, so `--pool default` needs no extra setup.

3. Use the `uctl selfserve provision-dataplane-resources` command to generate a new client and client secret for communicating with your control plane, provision authorization permissions for the app to operate on the cluster name you selected, and provide follow-up instructions. Pass the `--provider` value for your cloud (see the table above):

   ```bash
   uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME> --provider <PROVIDER>
   ```

   * The command outputs the ID, name, and a secret that the {{< key product_name >}} services use to communicate with your control plane. You pass the client ID and client secret to the Helm chart in step 5.
   * Save the secret that is displayed. Union does not store it, and it cannot be retrieved later.

4. Download the values file for your provider (see the table above) and fill in your infrastructure details. The exact keys — object storage, service-account/identity bindings, and any provider-specific settings — are documented in the **Deploy configuration** section of your provider's infrastructure page ([AWS](../infrastructure-recommendations/aws#deploy-configuration) · [GCP](../infrastructure-recommendations/gcp#deploy-configuration) · [Azure](../infrastructure-recommendations/azure#deploy-configuration) · [OCI](../infrastructure-recommendations/oci#deploy-configuration) · [Generic](../infrastructure-recommendations/generic#deploy-configuration)):

   ```bash
   curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/<VALUES_FILE>
   ```

   Every provider needs these shared `global` keys set:

   - Set `global.UNION_CONTROL_PLANE_HOST` and `global.CONTROLPLANE_HOST` to your control plane hostname (no scheme, no port).
   - Set `global.CLUSTER_NAME` to the cluster name you registered in step 2.
   - Set `global.ORG_NAME` to your organization name.

   Set the remaining provider-specific keys as described on your infrastructure page.

5. Install the data plane Helm chart, passing the client ID and client secret from step 3:

   ```bash
   helm upgrade --install union unionai/dataplane \
     -f <VALUES_FILE> \
     --set global.AUTH_CLIENT_ID=<CLIENT_ID> \
     --set-string secrets.admin.clientId=<CLIENT_ID> \
     --set secrets.admin.clientSecret=<CLIENT_SECRET> \
     --namespace union \
     --create-namespace
   ```

6. Once deployed, check that the cluster registered with the control plane:

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
- [Managing queues](../../../user-guide/cluster-workload-management/queues): route workloads to a pool and enforce concurrency, priority, and fairness.

Every organization is provisioned with a `default` pool that new clusters join
automatically, so a single-cluster deployment needs no extra pool setup.
