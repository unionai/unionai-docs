---
title: Deploy the dataplane
weight: 2
variants: -flyte +union
---

# Deploy the dataplane

If you have not yet set up the required GCP resources (GKE cluster, GCS, Artifact Registry, Workload Identity), see [Prepare infrastructure](../selfmanaged-gcp/prepare-infra) first.

## Assumptions

* You have a {{< key product_name >}} organization, and you know the control plane URL for your organization (e.g. `https://your-org-name.us-east-2.unionai.cloud`).
* You have a cluster name provided by or coordinated with Union.
* You have a GKE cluster with Workload Identity enabled, running one of the most recent three minor Kubernetes versions.
  [Learn more](https://kubernetes.io/releases/version-skew-policy/)
* You have configured GCS bucket(s), Artifact Registry, and Workload Identity as described in [Prepare infrastructure](../selfmanaged-gcp/prepare-infra).

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
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME> --provider gcp
   ```

   * The command outputs a client ID and secret that Union services use to communicate with your control plane. Save the secret — Union does not store credentials; rerunning the same command retrieves it.

3. Start from the canonical GCP dataplane values overlay in [unionai/helm-charts](https://github.com/unionai/helm-charts):

   ```bash
   curl -O https://raw.githubusercontent.com/unionai/helm-charts/main/charts/dataplane/values.gcp.yaml
   ```

   Fill in your infrastructure details (use the [environment variables](../selfmanaged-gcp/prepare-infra#environment-variables) from the prepare infrastructure step):

   - Set `global.METADATA_BUCKET` to `${BUCKET_PREFIX}-metadata`.
   - Set `global.FAST_REGISTRATION_BUCKET` to `${BUCKET_PREFIX}-fast-reg`.
   - Set `global.BACKEND_IAM_ROLE_ARN` to `${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com`.
   - Set `global.WORKER_IAM_ROLE_ARN` to the same value (or a separate GSA if you use distinct worker permissions).
   - Set `storage.bucketName` to `${BUCKET_PREFIX}-metadata`.
   - Set `storage.fastRegistrationBucketName` to `${BUCKET_PREFIX}-fast-reg`.
   - Set `storage.region` to `${REGION}`.
   - Set `storage.gcp.projectId` to `${PROJECT_ID}`.
   - Set `commonServiceAccount.annotations."iam.gke.io/gcp-service-account"` to `${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com`.
   - Set `imageBuilder.registryName` to `${AR_REPOSITORY}` (defaults to `union-dataplane`; the chart auto-generates the full Artifact Registry URL from the project ID and region).
   - Plug in the `CLIENT_ID` and `CLIENT_SECRET` from step 2 wherever the overlay expects them.

4. Install the data plane CRDs via server-side apply. The CRDs are vendored in [unionai/helm-charts](https://github.com/unionai/helm-charts) under `crds/`:

   ```bash
   git clone https://github.com/unionai/helm-charts.git
   cd helm-charts

   # Mandatory in all modes — FlyteWorkflow CRD + Knative Serving CRDs
   # consumed by propeller and the dataplane chart's serving stack.
   kubectl apply --server-side --force-conflicts -f crds/dataplane/

   # Required when knative-operator.enabled=true (the chart default). The
   # post-install hook creates a KnativeServing resource and will fail
   # without these CRDs in place. Skip in zero-trust mode
   # (knative-operator.enabled=false), which vendors Knative Serving
   # directly via the dataplane chart's gateway templates instead of the
   # operator subchart.
   kubectl apply --server-side --force-conflicts -f crds/knative-operator/

   # Required when monitoring.enabled=true. Skip if monitoring is disabled (the chart default)
   kubectl apply --server-side --force-conflicts -f crds/kube-prometheus-stack/
   ```

   Server-side apply avoids the 256 KiB `last-applied-configuration` annotation overflow on larger CRDs. `--force-conflicts` is needed only on first install.

5. Install the data plane Helm chart with `--skip-crds` so Helm doesn't re-manage the CRDs you just applied:

   ```bash
   helm upgrade --install union unionai/dataplane \
     -f values.gcp.yaml \
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
