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

2. Use the `uctl selfserve provision-dataplane-resources` command to generate a new client and client secret for communicating with your Union control plane, provision authorization permissions for the app to operate on the Union cluster name you have selected, generate values file to install dataplane in your Kubernetes cluster and provide follow-up instructions:

   ```bash
   uctl config init --host=<YOUR_UNION_CONTROL_PLANE_URL>
   uctl selfserve provision-dataplane-resources --clusterName <YOUR_SELECTED_CLUSTERNAME>  --provider gcp
   ```

   * The command will output the ID, name, and a secret that will be used by the Union services to communicate with your control plane.
     It will also generate a YAML file specific to the provider that you specify, in this case `gcp`.

   * Save the secret that is displayed. Union does not store the credentials; rerunning the same command can be used to retrieve the secret later.

3. Update the generated values file with your infrastructure details:

   Using the [environment variables](../selfmanaged-gcp/prepare-infra#environment-variables) from the prepare infrastructure step:

   - Set `global.METADATA_BUCKET` to `${BUCKET_PREFIX}-metadata`.
   - Set `global.FAST_REGISTRATION_BUCKET` to `${BUCKET_PREFIX}-fast-reg`.
   - Set `global.BACKEND_IAM_ROLE_ARN` to `${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com`.
   - Set `global.WORKER_IAM_ROLE_ARN` to the same value (or a separate GSA if you use distinct worker permissions).
   - Set `storage.region` to `${REGION}`.
   - Set `storage.gcp.projectId` to `${PROJECT_ID}`.
   - Set `imageBuilder.registryName` to `${AR_REPOSITORY}` (defaults to `union-dataplane`; the chart auto-generates the full Artifact Registry URL from the project ID and region).

4. Install the data plane Helm chart:

   ```bash
   helm upgrade --install union unionai/dataplane \
     -f <GENERATED_VALUES_FILE> \
     --namespace union \
     --create-namespace
   ```

5. Create an API key for your organization. This is required for v2 workflow executions on the data plane. If you have already created one, rerun the same command to propagate the key to the new cluster:

   ```bash
   uctl create apikey --keyName EAGER_API_KEY --org <YOUR_ORG_NAME>
   ```

6. Once deployed you can check to see if the cluster has been successfully registered to the control plane:

   ```bash
   uctl get cluster
    ----------- ------- --------------- -----------
   | NAME      | ORG   | STATE         | HEALTH    |
    ----------- ------- --------------- -----------
   | <cluster> | <org> | STATE_ENABLED | HEALTHY   |
    ----------- ------- --------------- -----------
   1 rows
   ```

7. Follow the [Quickstart](../../../user-guide/quickstart) to run your first workflow and verify your cluster is working correctly.
