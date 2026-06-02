---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required resources (Kubernetes cluster, object storage, container registry, credentials), see [Prepare infrastructure](../selfmanaged-generic/prepare-infra) first.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization (e.g. `https://your-org-name.us-east-2.unionai.cloud`).
* You have a cluster name provided by or coordinated with Union.
* You have a Kubernetes cluster, running one of the most recent three minor Kubernetes versions. [Learn more](https://kubernetes.io/releases/version-skew-policy/).
* Object storage provided by a vendor or an S3-compatible platform (such as [MinIO](https://min.io)), with CORS configured as described in [Prepare infrastructure](../selfmanaged-generic/prepare-infra).
* A container registry accessible from your cluster.

## Prerequisites

* Install [Helm 3](https://helm.sh/docs/intro/install/).
* Install [uctl](../../../api-reference/uctl-cli/_index).

## Deploy the {{< key product_name >}} operator

1. Add the {{< key product_name >}} Helm repo:

   ```bash
   helm repo add unionai https://unionai.github.io/helm-charts/
   helm repo update
   ```

2. Provision an OAuth client and register the cluster with your control plane:

   ```bash
   uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME> --provider metal
   ```

   * The command outputs a client ID and secret that Union services use to communicate with your control plane. Save the secret — Union does not store credentials; rerunning the same command retrieves it.

3. Start from the base dataplane values in [unionai/helm-charts](https://github.com/unionai/helm-charts):

   ```bash
   curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.yaml
   ```

   Fill in your infrastructure details:

   - Set `storage.endpoint` to your S3-compatible storage endpoint (e.g. your MinIO URL).
   - Set `storage.accessKey` and `storage.secretKey` to your storage credentials.
   - Set `storage.bucketName` and `storage.fastRegistrationBucketName` to your bucket name(s).
   - Set `storage.region` to the region of your storage provider.
   - The same credentials are also needed in `fluentbit.env` for log shipping.
   - Plug in the `CLIENT_ID` and `CLIENT_SECRET` from step 2 wherever the chart expects them.

4. Install the data plane CRDs via server-side apply. The CRDs are vendored in [unionai/helm-charts](https://github.com/unionai/helm-charts) under `crds/`:

   ```bash
   git clone https://github.com/unionai/helm-charts.git
   cd helm-charts

   # Required — FlyteWorkflow CRD consumed by propeller.
   kubectl apply --server-side --force-conflicts -f crds/flyte-v1/

   # Required when monitoring.enabled=true. Skip if monitoring is disabled (the chart default)
   kubectl apply --server-side --force-conflicts -f crds/kube-prometheus-stack/
   ```

   Server-side apply avoids the 256 KiB `last-applied-configuration` annotation overflow on larger CRDs. `--force-conflicts` is needed only on first install.

5. Install the data plane Helm chart with `--skip-crds` so Helm doesn't re-manage the CRDs you just applied:

   ```bash
   helm upgrade --install union unionai/dataplane \
     -f values.yaml \
     --namespace union \
     --create-namespace \
     --skip-crds \
     --force-conflicts
   ```

6. **Required for helm charts on a version <= 2026.5.8.** Create an API key for your organization. This is required for v2 workflow executions on the data plane. If you have already created one, rerun the same command to propagate the key to the new cluster:

   ```bash
   uctl create apikey --keyName EAGER_API_KEY --org <YOUR_ORG_NAME>
   ```

7. Once deployed you can check to see if the cluster has been successfully registered to the control plane:

   ```bash
   uctl get cluster
    ----------- ------- --------------- -----------
   | NAME      | ORG   | STATE         | HEALTH    |
    ----------- ------- --------------- -----------
   | <cluster> | <org> | STATE_ENABLED | HEALTHY   |
    ----------- ------- --------------- -----------
   1 rows
   ```

8. Follow the [Quickstart](../../../user-guide/quickstart) to run your first workflow and verify your cluster is working correctly.
